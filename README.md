# Replication package

### for the paper _AI Simulation by Digital Twins: Systematic Survey of the State of the Art and a Reference Framework_.

## Contents

- `/data` - Data file
- `/scripts` - Analysis scripts for the automated analysis of data
- `/output` - Results of the analyses, including charts and numeric results

## How to use

### Install requirements
- Install requirements by executing `pip install -r requirements.txt` from the root folder.

### Run analysis
- For publication trends: execute `python .\scripts\publication_trends.py` from the root folder.
- For the quality report: execute `python .\scripts\quality.py` from the root folder.