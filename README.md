# Automated ILL request workflow. Search LoC site and click on MODS record.
python3.9 ill.py <url to LoC MODS record>

# Automated workflow for processing, converting, and uploading scanned images.

- `make all`: Runs all steps (except tests).
- `make test`: Runs tests.
- `make download`: Syncs folders of images from the S3 "Fresh Scans" folder.
- `make process`: Applies contrast adjustments and other image processing.
- `make upload`: Uploads the final PDFs to a specified S3 bucket.

# Be sure to activate the Python environment first

source venv/bin/activate

# Tests
cd cantatas-tools
python3 test.py ../tests ../tests-output
