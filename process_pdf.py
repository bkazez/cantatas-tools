import os
import sys
import cv2
import numpy as np
import argparse
import tempfile
from pdf2image import convert_from_path
from shutil import rmtree

# Ensure the directory is correctly specified and append it to sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(project_root)

# Attempt to import your custom utilities
try:
    from pdfutils.img import adjust_contrast_peaks, apply_unsharp_mask
    from pdfutils.pdf import images_to_pdf
except ModuleNotFoundError as e:
    print(f"Failed to import modules: {e}")
    sys.exit(1)

def process_pdf(pdf_path):
    temp_dir = tempfile.mkdtemp()
    try:
        images = convert_from_path(pdf_path)
        for i, image in enumerate(images):
            image_np = np.array(image)
            img = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            img = apply_unsharp_mask(img, kernel_size=3, sharpening_factor=1)
            img, debug = adjust_contrast_peaks(img, debug=True)
            output_file = os.path.join(temp_dir, f'image_{i}.png')
            cv2.imwrite(output_file, img)

        # Prepare output paths and names
        output_folder = os.path.dirname(pdf_path)
        output_pdf_name = os.path.splitext(os.path.basename(pdf_path))[0] + '-contrasted'

        # Call the function with the correct directory and parameters
        images_to_pdf(temp_dir, output_folder, output_pdf_name)

        print(f'Output saved to {os.path.join(output_folder, output_pdf_name + ".pdf")}')

    finally:
        rmtree(temp_dir)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process a PDF, convert to grayscale, and adjust its contrast.')
    parser.add_argument('pdf_file', help='The PDF file to process')
    args = parser.parse_args()

    process_pdf(args.pdf_file)
