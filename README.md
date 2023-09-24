# Weather tracker application for AZ-204 exam practice lab
## How to build the application

### 1. Login into AZ
- `az login`
- `az acr login --name your-acr-name`
### 2. Tag the docker image
- `docker tag your-image-name your-acr-name.azurecr.io/your-image-name:v1`
### 3. Push the Docker Image to Azure Container Registry
- `docker push your-acr-name.azurecr.io/your-image-name:v1`

## Generate dependencies
1. Install pipreqs
2. `pipreqs --encoding=utf8 --use-local`

## How to run
### Development
1. `pip install -r requirements.txt`
2. `flask run --debug`
