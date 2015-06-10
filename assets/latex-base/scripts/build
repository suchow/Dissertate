#!/bin/sh
BASEDIR=$(dirname $0)
cd $BASEDIR
cd ..

# Build the dissertation.
xelatex dissertation
bibtex dissertation
xelatex dissertation
xelatex dissertation

# Hide the log.
mv "dissertation.log" ".logged"

