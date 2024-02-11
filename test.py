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
            i_values = [True] # np.linspace(3, 7, 3, dtype=int)
            j_values = [True] # np.linspace(3, 7, 5, dtype=int)

            for i in i_values:
                for j in j_values:
                    # Write out original
                    #output_filename = f"{os.path.splitext(filename)[0]}_orig.png"
                    #cv2.imwrite(os.path.join(output_dir, output_filename), img, [cv2.IMWRITE_PNG_COMPRESSION, 3])

                    # Operate on a copy to avoid analyzing `img` multiple times
                    img_copy = img.copy()
                    output_filename = f"{os.path.splitext(filename)[0]}_{i}_{j}.png"
                    output_path = os.path.join(output_dir, output_filename)
                    img_copy = apply_unsharp_mask(img_copy, kernel_size=3, sharpening_factor=1)
                    img_copy, debug_overlay = adjust_contrast_peaks(img_copy, debug=True)

                    # Add debug info
                    if len(img_copy.shape) == 2:  # img_part is grayscale
                        img_copy = cv2.cvtColor(img_copy, cv2.COLOR_GRAY2BGR)
                    h, w, _ = img_copy.shape
                    overlay_start_y = h - debug_overlay.shape[0]
                    overlay_start_x = 0
                    img_copy[overlay_start_y:h, overlay_start_x:overlay_start_x + debug_overlay.shape[1]] = debug_overlay


                    cv2.imwrite(output_path, img_copy, [cv2.IMWRITE_PNG_COMPRESSION, 3])

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Process images in a directory and generate PDFs.")
    parser.add_argument("input_dir", help="Path to the directory containing scans.")
    parser.add_argument("output_dir", help="Path to the directory where processed images will be saved.")
    args = parser.parse_args()

    process_images(args.input_dir, args.output_dir)
