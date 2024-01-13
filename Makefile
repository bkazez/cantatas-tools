# Directories
SCANS_DIR := ../scans-fresh
PROCESSED_SCANS_DIR := ../scans-processed
WORK_DIR := ../scans-work
OUTPUT_DIR := ../scans-output

# S3 Bucket and other configurations
S3_BUCKET := cantatas-scores
S3_SCANS_DIR := Fresh Scans
S3_PROCESSED_SCANS_DIR := Fresh Scans - Processed
UPLOAD_SCRIPT := upload_pdfs.sh

# Default target
all: download contrast-split-crop upload move-s3 move-local

# Process all folders
process:
	@echo "Processing images in directory $(SCANS_DIR)"
	@mkdir -p "$(WORK_DIR)"
	@mkdir -p "$(OUTPUT_DIR)"
	@python process_scans.py "$(SCANS_DIR)" "$(WORK_DIR)" "$(OUTPUT_DIR)"
	@echo "Processed directories in $(SCANS_DIR)"

# Download images from S3
download:
	aws s3 sync "s3://$(S3_BUCKET)/$(S3_SCANS_DIR)" "$(SCANS_DIR)"

# Upload PDFs to S3
upload:
	bash "$(UPLOAD_SCRIPT)" "$(OUTPUT_DIR)" "$(S3_BUCKET)"

# Move processed scans to the processed directory on S3
move-s3:
	aws s3 mv "s3://$(S3_BUCKET)/$(S3_SCANS_DIR)" "s3://$(S3_BUCKET)/$(S3_PROCESSED_SCANS_DIR)" --recursive

# Move processed scans to the processed directory locally
move-local:
	mv "$(SCANS_DIR)"/* "$(PROCESSED_SCANS_DIR)/"

# Clean target to remove processed images and PDFs
clean:
	@echo "Cleaning up..."
	@rm -rf "$(WORK_DIR)"
	@rm -rf "$(OUTPUT_DIR)"/*
