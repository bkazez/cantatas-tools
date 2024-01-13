import os
import cv2
import sys
import argparse
import numpy as np

sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from pdfutils.img import apply_unsharp_mask, rotate, adjust_contrast_peaks, is_image_file

def process_images(input_dir, output_dir):
    """Process images in a given input directory and place the processed images in the output directory."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in sorted(os.listdir(input_dir)):
        input_path = os.path.join(input_dir, filename)
        if is_image_file(input_path):
            print(filename)
            img = cv2.imread(input_path)
            if img is None:
                raise ValueError(f"Unable to open the image file: {input_path}")

            # Image processing steps
            img = img[:, :, 1]  # Use the green channel
            img = rotate(img, 180)  # Rotate by 180 degrees

            # Iterate over different adjustment values
            # I think j = 10, i = 20 is okay
            i_values = [True, False] # np.linspace(3, 7, 3, dtype=int)
            j_values = [True] # np.linspace(3, 7, 5, dtype=int)

            for i in i_values:
                for j in j_values:
                    img_copy = img.copy() # Operate on a copy to avoid analyzing image multiple times
                    if i:
                        img_copy = apply_unsharp_mask(img_copy, kernel_size=3, sharpening_factor=1)
                    img_copy = adjust_contrast_peaks(img_copy, analysis_area_percent=80, text_black_crop_percent=37, text_white_crop_percent=11)

                    output_filename = f"{os.path.splitext(filename)[0]}_{i}_{j}.png"
                    output_path = os.path.join(output_dir, output_filename)
                    cv2.imwrite(output_path, img_copy, [cv2.IMWRITE_PNG_COMPRESSION, 3])

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Process images in a directory and generate PDFs.")
    parser.add_argument("input_dir", help="Path to the directory containing scans.")
    parser.add_argument("output_dir", help="Path to the directory where processed images will be saved.")
    args = parser.parse_args()

    process_images(args.input_dir, args.output_dir)
