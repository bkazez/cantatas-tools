The Makefile automates the workflow for processing, converting, and uploading scanned images.

- `make all`: Runs all steps.
- `make download`: Syncs folders of images from the S3 "Fresh Scans" folder.
- `make process`: Applies contrast adjustments and other image processing.
- `make convert`: Splits processed images into pages and compiles them into a single PDF.
- `make upload`: Uploads the final PDFs to a specified S3 bucket.

Be sure to activate the Python environment first:

source venv/bin/activate
. ../../pdfutils/venv/bin/activate