# Replication package

### for the article _AI Simulation by Digital Twins: Systematic Survey, Reference Framework, and Mapping to a Standardized Architecture_.


## About
Insufficient data volume and quality are particularly pressing challenges in the adoption of modern subsymbolic AI. To alleviate these challenges, AI simulation uses virtual training environments in which AI agents can be safely and efficiently developed with simulated, synthetic data. Digital twins open new avenues in AI simulation, as these high-fidelity virtual replicas of physical systems are equipped with state-of-the-art simulators and the ability to further interact with the physical system for additional data collection. In this article, we report on our systematic survey of digital twin-enabled AI simulation. By analyzing 22 primary studies, we identify technological trends and derive a reference framework to situate digital twins and AI components. Based on our findings, we derive a reference framework and provide architectural guidelines by mapping it onto the ISO 23247 reference architecture for digital twins. Finally, we identify challenges and research opportunities for prospective researchers.

**This article is the journal extension of our previous work** _X. Liu and I. David. “AI Simulation by Digital Twins: Systematic Survey of the State of the Art and a Reference Framework“. In: ACM/IEEE International Conference on Model Driven Engineering Languages and Systems Companion, MODELS-C. 1st International Conference on Engineering Digital Twins (EDTConf). ACM, 2024_. The original paper's replication package is available at [here](https://zenodo.org/doi/10.5281/zenodo.13293237).

## Contents

- `/data` - Data extraction sheet of 22 included studies (with fully extrated data); and 16 eventually excluded studies (with quality data that justifies the exclusion).
- `/scripts` - Analysis scripts for the automated analysis of data.
- `/output` - Results of the analyses as used in the article.

## How to use

### Install requirements
- Install requirements by executing `pip install -r requirements.txt` from the root folder.

### Run analysis
- For publication trends: execute `python ./scripts/publication_trends.py` from the root folder.
- For the quality report: execute `python ./scripts/quality.py` from the root folder.
