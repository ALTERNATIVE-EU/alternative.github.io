# AI/ML API

## Prerequisites

Before proceeding with the installation or deployment of the AI/ML API, ensure you have the following prerequisites:

- Python 3.9
- Anaconda
- `PipelineAlternative_clinicaldata` data
- PBPK (Physiologically Based Pharmacokinetic) data
- cddd (Compound Database for Drug Discovery) data

## Installation

### Clone the Repository

```sh
git clone git@github.com:ALTERNATIVE-EU/ai-ml-api.git
```

### Prepare Data Directories

Place the required data directories in their respective locations:

- `PipelineAlternative_clinicaldata` `models` directory
- `cddd` directories inside `PipelineAlternative_clinicaldata`
- `PBPK` directory inside `models`

Copy the contents of the `patches` directory into the `models` directory:

```sh
cp -r patches/* ./models/
```

### Set up Virtual Environments

#### cddd Environment

Create and activate a virtual environment for `cddd`:

```sh
cd cddd
conda env create -f environment.yml
conda activate cddd
pip install --ignore-installed --upgrade https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-1.10.0-cp36-cp36m-linux_x86_64.whl
pip install -e .
conda deactivate
```

#### Alternative Environment

Create and activate the `alternative` virtual environment:

```sh
conda create -n alternative python=3.9
conda activate alternative
```

Install dependencies from the requirements file:

```sh
pip install -f requirements.txt
```

### Start the Server

Launch the API server by running:

```sh
python3 app.py
```

## Installation with Docker

Build and run the AI/ML API container using Docker:

1. Build the image:

    ```sh
    docker build -t ai-ml-api .
    ```

2. Run the container:

    ```sh
    docker run -p 5000:5000 ai-ml-api
    ```

## Deployment in Kubernetes

Update and apply the deployment files located in the `deployment/kubernetes` directory:

```sh
kubectl apply -f deployment/kubernetes
```

For authentication, use Istio with a custom Envoy filter. Follow the instructions provided in the [envoy-filter](./envoy-filter.md) documentation.

## API Usage

### Endpoints

#### ML Evaluation

```sh
curl -X POST -H "Content-Type: application/json" -d '{"smiles": "c1ccccc1O"}' https://ai-ml-api.platform.alternative-project.eu/clinicaldata/ml/evaluate -o results.csv
```

#### AI Evaluation

```sh
curl -X POST -H "Content-Type: application/json" -d '{"smiles": "c1ccccc1O"}' https://ai-ml-api.platform.alternative-project.eu/clinicaldata/ai/evaluate
```

#### AOP (Alternate Operating Procedure) Evaluation

```sh
curl -X POST -H "Content-Type: application/json" -d '{"smiles": "c1ccccc1O"}' https://ai-ml-api.platform.alternative-project.eu/clinicaldata/aop/evaluate
```

#### Doxorubicin PBPK Model

```sh
curl -X POST https://ai-ml-api.platform.alternative-project.eu/pbpk/doxorubicin      -H "Content-Type: application/json"      -d '{"dose_mg": 60, "age": 50, "weight": 70, "height": 190}'
```

#### HTTK (Human Toxicology Toolkit) Model

```sh
curl -X POST https://ai-ml-api.platform.alternative-project.eu/pbpk/httk -H "Content-Type: application/json"      -d '{"chem_name": "Bisphenol A", "species": "human", "daily_dose": 1, "doses_per_day": 1, "days": 15}'
```

#### IsAlive Check

Verify if the server is alive:

```sh
curl https://ai-ml-api.platform.alternative-project.eu/isalive
```

## Testing

To run unit tests, use the following command:

```sh
python -m unittest app_test.py
```
