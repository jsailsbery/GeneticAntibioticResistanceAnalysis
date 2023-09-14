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
5. notebooks/mcmc.ipynb
* please access these pages via a jupyter notebook server. We suggest to use your own container and run as noted previously.

# Repository SOP

## Branches

### Master

The `master` branch is the main production branch. Code merged into this branch must meet the following criteria:
- A Pull Request (PR) is required.
- Reviews are mandatory, and the author cannot bypass them.
- Pytests must pass before merging.

### Develop

The `develop` branch is for ongoing development and feature integration. Code merged into this branch must meet the following criteria:
- A Pull Request (PR) is required.
- Reviews are mandatory, but the repo owner may force merge.
- Pytests must pass before merging.

## Pull Requests

### Creating a PR

1. Fork this repository.
2. Create a new branch from `master` or `develop` depending on the nature of your changes.
3. Implement your changes on the new branch.
4. Create a Pull Request to merge your branch into the respective target branch (`master` or `develop`).
5. Fill out the PR template with relevant information, including a clear title, description, and any other necessary details.

## Review Process

1. All PRs require at least one review.
2. The author cannot approve their own PR.
3. Reviewers should provide constructive feedback and verify that the code meets coding standards and project requirements.

## Testing

- Ensure that the Pytests suite passes before creating a PR.
- Tests will be automatically run by our continuous integration (CI) system upon creating a PR.

## Merging to Master

1. Create a PR from your feature branch to `master`.
2. Await approval and reviews from other contributors.
3. Once approved, Pytests should pass, and the PR can be merged into `master`.

## Merging to Develop

1. Create a PR from your feature branch to `develop`.
2. Await approval and reviews from other contributors.
3. The repo owner has the option to force merge if necessary.
4. Pytests should pass, and the PR can be merged into `develop`.

