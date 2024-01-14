import os
import re
import argparse
import cv2
import sys
import glob
from stat import S_ISDIR, S_ISREG
import logging
import unicodedata

sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from pdfutils.img import adjust_contrast_peaks, rotate, split, autocrop, is_image_file, apply_unsharp_mask
from pdfutils.pdf import images_to_pdf

def exists(file_path):
    return os.path.exists(file_path)

def mtime(file_path):
    return os.stat(file_path).st_mtime if exists(file_path) else -1

def output_image_path(input_file, work_subdir, part_index):
    input_basename = os.path.splitext(os.path.basename(input_file))[0]
    return os.path.join(
        work_subdir,
        f"{input_basename}_part_{part_index}.png")

def output_pdf_path(output_dir, work_subdir):
    pdf_name = output_pdf_name(work_subdir)

    # Put PDFs in directories by composer name: "Bach - Passions" => "Bach/Bach - Passions"
    parts = re.split(r'\s+-\s+', pdf_name, maxsplit=1)
    if len(parts) >= 2:
        composer = parts[0]
        pdf_name = os.path.join(composer, pdf_name)

    return os.path.join(output_dir, pdf_name) + '.pdf'

def output_pdf_name(subdir):
    subdir_basename = os.path.basename(subdir)
    # Remove the date part from the beginning of the string (if it exists)
    name_without_date = re.sub(r'^\d{4}-\d{2}-\d{2}[a-zA-Z]?\s+', '', subdir_basename)

    # Normalize spaces (replace multiple spaces with a single space)
    name_without_date = re.sub(r'\s+', ' ', name_without_date).strip()

    return unicodedata.normalize('NFC', name_without_date)

def process_images(input_dir, work_dir):
    if not os.path.exists(work_dir):
        os.makedirs(work_dir)

    for filename in sorted(os.listdir(input_dir)):
        input_path = os.path.join(input_dir, filename)
        if is_image_file(input_path):
            print(input_path)
            img = cv2.imread(input_path)
            if img is None:
                raise ValueError(f"Unable to open the image file: {input_path}")

            # Image processing steps
            img = img[:, :, 1] # I think green is more contrasted
            img = apply_unsharp_mask(img, kernel_size=3, sharpening_factor=1) # found via testing many values
            img = rotate(img, 180)  # Rotate by 180 degrees
            img_list = split(img)

            # Save processed images
            for i, img_part in enumerate(img_list):
                img_part = adjust_contrast_peaks(
                    img_part,
                    analysis_area_percent=80, # handle pages with just a bit of text in the corner
                    text_black_crop_percent=37, # found via testing many values
                    text_white_crop_percent=11, # found via testing many values
                    )
                img_part = autocrop(
                    img_part,
                    threshold=200,
                    contraction_percent=1,
                    )

                output_path = output_image_path(input_path, work_dir, i)
                print(f"-----{output_path}")
                cv2.imwrite(output_path, img_part, [cv2.IMWRITE_PNG_COMPRESSION, 3])

def is_new_pdf_needed(work_subdir, output_dir):
    pdf_path = output_pdf_path(output_dir, work_subdir)  # Assuming part_index is not used in your case

    # Check if there's a corresponding output PDF file
    if not exists(pdf_path):
        print(f"No PDF found for directory {work_subdir} ({pdf_path}); new PDF needed")
        return True

    # Find the newest modification time among the input files
    input_files = glob.glob(os.path.join(work_subdir, '*'))
    if not input_files:
        print(f"No input files found in {work_subdir}")
        return True  # A new PDF is needed if there are no input files

    newest_input_mtime = max(mtime(file) for file in input_files)

    # Check if any input file is newer than the newest output file
    if newest_input_mtime > mtime(pdf_path):
        print("At least one input file is newer than the output files; new PDF needed")
        return True

    print("All input files are up to date with output files")
    return False

def is_image_processing_needed(input_dir, work_subdir):
    input_files = [os.path.join(input_dir, f) for f in os.listdir(input_dir) if is_image_file(os.path.join(input_dir, f))]

    for input_file in input_files:
        # Generate paths for the expected output parts
        output_paths = [
            output_image_path(input_file, work_subdir, i) for i in range(2)
        ]

        # Check if all output files exist
        output_exists = all(exists(output_path) for output_path in output_paths)
        if not output_exists:
            print(f"No valid work files found for input file {input_file} in {work_subdir}")
            return True  # Processing needed if any output file does not exist

        # Find the newest modification time among the output files
        newest_output_mtime = max(mtime(output_path) for output_path in output_paths)

        # Check if the input file is newer than the newest output file
        if mtime(input_file) > newest_output_mtime:
            print(f"Input file {input_file} is newer than its work files in {work_subdir}")
            return True  # Processing needed if input is newer than outputs

    print(f"All input files are up to date with their corresponding work files in #{work_subdir}")
    return False  # Processing not needed if all outputs are up-to-date

def process_subdir(input_dir, subdir, work_dir, output_dir):
    work_subdir = os.path.join(work_dir, subdir)
    if is_new_pdf_needed(work_subdir, output_dir):
        if is_image_processing_needed(os.path.join(input_dir, subdir), work_subdir):
            print(f"Processing images for {subdir}")
            process_images(os.path.join(input_dir, subdir), work_dir)
        else:
            print(f"Images up to date for {subdir}; skipping")

        pdf_path = output_pdf_path(output_dir, work_subdir)
        pdf_output_dir = os.path.dirname(pdf_path)
        if not os.path.exists(pdf_output_dir):
            os.makedirs(pdf_output_dir)
        pdf_name = os.path.basename(pdf_path)

        print(f"    Generating PDF: {work_subdir} => {pdf_path}")
        images_to_pdf(work_subdir, pdf_output_dir, pdf_name)
    else:
        print(f"Output PDF is up to date for {subdir}; skipping")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Process images in a directory and generate PDFs.")
    parser.add_argument("input_dir", help="Path to the directory containing scans.")
    parser.add_argument("work_dir", help="Path to the directory for processed images.")
    parser.add_argument("output_dir", help="Path to the directory where PDFs will be saved.")
    args = parser.parse_args()

    subdirs = next(os.walk(args.input_dir))[1]
    subdirs.sort()

    for subdir in subdirs:
        process_subdir(args.input_dir, subdir, args.work_dir, args.output_dir)