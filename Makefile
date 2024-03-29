# Directories
SCANS_DIR := ../scans-fresh
PROCESSED_SCANS_DIR := ../scans-processed
WORK_DIR := ../scans-work
OUTPUT_DIR := ../scans-output

# S3 Bucket and other configurations
S3_BUCKET := cantatas-scores
S3_SCANS_DIR := Fresh Scans
S3_PROCESSED_SCANS_DIR := Fresh Scans - Processed

# Default target
all: download contrast-split-crop upload move-s3 move-local

# Run tests
test:
	@python test.py ../tests ../tests-output

# Process all folders
process:
	@python process_scans.py "$(SCANS_DIR)" "$(WORK_DIR)" "$(OUTPUT_DIR)"

# Download images from S3
download:
	aws s3 sync "s3://$(S3_BUCKET)/$(S3_SCANS_DIR)" "$(SCANS_DIR)"

# Upload PDFs to S3
upload:
	aws s3 sync "$(OUTPUT_DIR)" "s3://$(S3_BUCKET)" --metadata-directive REPLACE --content-disposition attachment --exclude "*" --include "*.pdf" --only-show-errors

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
	@rm -rf "$(OUTPUT_DIR)"
