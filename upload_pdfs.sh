#!/bin/bash

# Upload to s3 with content-disposition set to force downloads

# Directory containing the PDFs to upload
PDF_DIR=$1
# Base S3 path (bucket name)
S3_BASE_PATH=$2

# Check if PDF_DIR is provided
if [ -z "$PDF_DIR" ]; then
    echo "Error: PDF directory not specified."
    exit 1
fi

# Check if S3_BASE_PATH is provided
if [ -z "$S3_BASE_PATH" ]; then
    echo "Error: S3 base path not specified."
    exit 1
fi

# Iterate through each PDF in PDF_DIR and upload it to S3
for file in "$PDF_DIR"/*.pdf; do
    if [ -f "$file" ]; then
        # Extract the first part of the filename
        filename=$(basename "$file")
        dest_dir=$(echo $filename | cut -d '-' -f 1 | xargs) # Removes trailing spaces
        s3_dest_path="${S3_BASE_PATH}/${dest_dir}"

        # Upload the file
        aws s3 cp "$file" "${s3_dest_path}/${filename}" --metadata-directive REPLACE --content-disposition attachment
        echo "Uploaded: $filename to $s3_dest_path"
    fi
done
