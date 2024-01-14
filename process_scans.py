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


def process_images(input_dir, work_dir):
    """Process images in a given input directory and place the processed images in a work directory."""
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
            # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
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

                output_path = os.path.join(work_dir, f"{os.path.splitext(filename)[0]}_part_{i}.png")
                cv2.imwrite(output_path, img_part, [cv2.IMWRITE_PNG_COMPRESSION, 3])

def format_output_name(subdir):
    pattern = r'^\d{4}-\d{2}-\d{2}[a-zA-Z]?\s+'
    return re.sub(pattern, '', subdir)

def is_new_pdf_needed(input_files, output_files):
    if not output_files:
        print("No output files found; new PDF needed")
        return True

    # Extract the directory name from the first input file (assuming all input files are in the same directory)
    subdir_name = os.path.basename(os.path.dirname(input_files[0]))
    formatted_subdir_name = format_output_name(subdir_name)

    # Check if there's a corresponding output PDF file
    corresponding_pdf = any(formatted_subdir_name in output_file for output_file in output_files)
    if not corresponding_pdf:
        print(f"No PDF found for directory {subdir_name}; new PDF needed")
        return True

    # Find the newest modification time among the input files
    newest_input_mtime = max(mtime(input_file) for input_file in input_files)

    # Find the newest modification time among the output files
    newest_output_mtime = max(mtime(output_file) for output_file in output_files)

    # Check if any input file is newer than the newest output file
    if newest_input_mtime > newest_output_mtime:
        print("At least one input file is newer than the output files; new PDF needed")
        return True

    print("All input files are up to date with output files")
    return False

def is_image_processing_needed(input_files, work_dir):
    for input_file in input_files:
        input_file_basename = os.path.splitext(os.path.basename(input_file))[0]

        # Check if there's at least one valid work file for each input file
        work_files_for_input = [f for f in os.listdir(work_dir) if f.startswith(input_file_basename) and is_image_file(f)]
        if not work_files_for_input:
            print(f"No valid work files found for input file {input_file} in {work_dir}")
            return True

        # Find the newest modification time among the valid work files for this input
        newest_work_mtime = max(mtime(os.path.join(work_dir, f)) for f in work_files_for_input)

        # Check if the input file is newer than the newest corresponding work file
        input_mtime = mtime(input_file)
        if input_mtime > newest_work_mtime:
            print(f"Input file {input_file} is newer than its work files in {work_dir}")
            return True

    print("All input files are up to date with their corresponding work files in " + work_dir)
    return False


def process_subdir(subdir, input_dir, work_dir, output_dir):
    full_subdir_path = os.path.join(input_dir, subdir)
    subdir_work_path = os.path.join(work_dir, subdir)
    output_name = format_output_name(subdir)
    output_files = glob.glob(os.path.join(output_dir, output_name + '*'))

    if not os.path.exists(subdir_work_path):
        os.makedirs(subdir_work_path)

    input_files = [os.path.join(full_subdir_path, f) for f in os.listdir(full_subdir_path)]

    if is_new_pdf_needed(input_files, output_files):
        if is_image_processing_needed(input_files, subdir_work_path):
            print(f"Processing images for {subdir}")
            process_images(full_subdir_path, subdir_work_path)
        else:
            print(f"Images up to date for {subdir}; skipping")

        print(f"Generating PDF for {subdir_work_path}, {output_dir}, {output_name}")
        images_to_pdf(subdir_work_path, output_dir, output_name)
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
        process_subdir(subdir, args.input_dir, args.work_dir, args.output_dir)