#!/usr/bin/env bash
set -o errexit  # Exit if any command fails

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt
