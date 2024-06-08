#!/usr/bin/bash
REPORT_DIR=$PWD/../"Report"

if [ -d "$REPORT_DIR" ]; then
  # If the directory exists, delete it
  rm -rf "$REPORT_DIR"
fi

# Creating 'Report' directory
mkdir -p $REPORT_DIR

# Running the test and saving results in Report/result.log file
echo "RUNNING TEST..."
make | tee $REPORT_DIR/result.log
echo "FINISH"


# Getting the Assertion Error from the report
grep -e "AssertionError" -e "File ""*\"" $REPORT_DIR/result.log | tee $REPORT_DIR/AssertionError.log
