# Central Valley Modeling Documentation

[https://centralvalleymodeling.github.io/](https://centralvalleymodeling.github.io/)  
branch `main` contains the markdown (edit these files when making changes to the documentation)  
branch `deploy` contains the compiled HTML. The content here is built automatically using the command below.  

## Setup
Install the conda from the environment.yml file
`conda env create -f environment.yml`  

## Making Changes
### Step 1: make changes to the the appropriate .md page in `main`  
Don't forget to commit your changes

### Step 2: deploy your docs to the `deploy` branch with the following command
`mkdocs gh-deploy --config-file mkdocs.yml --remote-branch deploy`


> [!NOTE]  
Documentation built with [mkdocs](https://www.mkdocs.org/)  
`pip install mkdocs`
