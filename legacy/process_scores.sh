#!/bin/bash

# Define paths
SCANS_DIR=$1
SCORES_DIR=$2
PROCESSING_DIR=$3
ADJUST_CONTRAST_SCRIPT="../../pdfutils/adjust_contrast_peaks.py"
IMAGES_TO_PDF_SCRIPT="../../pdfutils/images_to_pdf.py"

# Regex pattern to strip off the initial date/letter identifier
PREFIX_REGEX='^\d{4}-\d{2}-\d{2}[a-z]? '

# Ensure PROCESSING_DIR and SCORES_DIR exist
mkdir -p "$PROCESSING_DIR"
mkdir -p "$SCORES_DIR"

# Process each subfolder in SCANS_DIR
for SCAN_SUBFOLDER in "$SCANS_DIR"/*; do
    if [ -d "$SCAN_SUBFOLDER" ]; then
        # Extract folder name
        FOLDER_NAME=$(basename "$SCAN_SUBFOLDER")

        # Create a corresponding folder in PROCESSING_DIR
        PROCESSING_SUBFOLDER="$PROCESSING_DIR/$FOLDER_NAME"
        mkdir -p "$PROCESSING_SUBFOLDER"

        # Step 1: Apply contrast adjustment and unsharp mask to images in SCAN_SUBFOLDER
        python3 "$ADJUST_CONTRAST_SCRIPT" \
            --input_folder "$SCAN_SUBFOLDER" \
            --output_folder "$PROCESSING_SUBFOLDER" \
            --analysis_area_percent 50 \
            --text_black_crop_percent 20 \
            --text_white_crop_percent 10 \
            --channel green \
            --sharpening_factor 4 \
            --debug

        # Step 2: Combine images in PROCESSING_SUBFOLDER into a single PDF, save in SCORES_DIR
        PDF_NAME=$(echo "$FOLDER_NAME" | sed -E "s/$PREFIX_REGEX//").pdf
        python3 "$IMAGES_TO_PDF_SCRIPT" \
            --input_folder "$PROCESSING_SUBFOLDER" \
            --output_folder "$SCORES_DIR" \
            --split \
            --remove_prefix

        echo "Processed $FOLDER_NAME"
    fi
done

echo "All folders processed."
