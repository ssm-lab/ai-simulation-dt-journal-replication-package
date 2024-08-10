# Replication package

### for the paper _AI Simulation by Digital Twins: Systematic Survey of the State of the Art and a Reference Framework_.

## About
Insufficient data volume and quality are particularly pressing challenges in the adoption of modern subsymbolic AI. To alleviate these challenges, AI simulation recommends developing virtual training environments in which AI agents can be safely and efficiently developed. Digital twins open new avenues in AI simulation, as these high-fidelity virtual replicas of physical systems are equipped with state-of-the-art simulators and the ability to further interact with the physical system for additional data collection. In this paper, we report on our systematic survey of digital twin-enabled AI simulation. By analyzing 22 primary studies, we identify technological trends and derive a reference framework to situate digital twins and AI components. Finally, we identify challenges and research opportunities for prospective researchers.

## Contents

- `/data` - Data extraction sheet of 22 included studies (with fully extrated data) and 16 eventually excluded studies (with partially excluded data).
- `/scripts` - Analysis scripts for the automated analysis of data.
- `/output` - Results of the analyses as used in the article.

## How to use

### Install requirements
- Install requirements by executing `pip install -r requirements.txt` from the root folder.

### Run analysis
- For publication trends: execute `python .\scripts\publication_trends.py` from the root folder.
- For the quality report: execute `python .\scripts\quality.py` from the root folder.
