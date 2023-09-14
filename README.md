# GeneticAntibioticResistanceAnalysis
An analysis of Antibiotic resistance via urine test data and genetic markers.

## Jupyter Notebook Container
CLI - commands to run from the base directory of this repo

### BUILD
docker build -t antibiotic_resistance_notebook Dockerfile

### RUN
* please note that ports other than 8888 may be used
docker run -p 8888:8888 -v $(PWD):/app antibiotic_resistance_notebook

## Analysis Documentation
All analysis notes, processes, procedures are documented in the following jupyter notebooks.
1. notebooks/data_visualization.ipynb
2. notebooks/organism_dist_identification.ipynb
3. notebooks/principal_components_analysis.ipynb
4. notebooks/principal_components_analysis_transformed.ipynb
* please access these pages via a jupyter notebook server. We suggest to use your own container and run as noted previously.


