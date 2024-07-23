## Environments

Every JupyterHub server is being spawned with two environments from the start - default python environment and an additional <a href="https://conda.io/projects/conda/en/latest/user-guide/index.html" target="_blank">conda</a> environment. On `Launcher` tab under `Notebook` or `Console` you can choose which environment to use. You can also use the `Terminal`:

### Python Virtual Environments

Each environment has their own independent set of Python packages installed in their `site` directories. A virtual environment is created on top of an existing Python installation, known as the virtual environment’s `base` Python, and may be isolated from the packages in the base environment, so only those explicitly installed in the virtual environment are available. <a href="https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment" target="_blank">Python Virtual Environment Docs</a>.

**Make sure you create these environments in the `/home/jovyan` directory or they will get deleted.**

- Add New Environments:
```
python -m venv /path/to/new/virtual/environment
```

- Activate Different Environment:
```
source environment/bin/activate
```

- Install Packages:
```
pip install packageName
```

- Uninstall Packages:
```
pip uninstall packageName
```

- Show Packages In Environment:
```
pip list
```

- Deactivate Current Environment:
```
deactivate
```

- Delete Environment:
```
rm -rf environment
```

### Conda Environments

Each environment has their own independent set of Python or Conda packages installed. <a href="https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html" target="_blank">Conda Environments Docs</a>. Guide - <a href="https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-pkgs.html#installing-non-conda-packages" target="_blank">using `pip` inside conda environment</a>.

**Make sure you create these environments in the `/home/jovyan` directory or they will get deleted.**

You can check environment names and locations with:
```
bash
conda env list
```

- Add New Environments:
```
conda create --prefix /home/jovyan/Conda2
```

- Activate Different Environment:
```
conda activate /home/jovyan/Conda2
```

- Install Packages:
```
conda install pip
pip install packageName
```

- Uninstall Packages:
```
pip uninstall packageName
```

- Show Packages In Environment:
```
conda list
pip list
```

- Create Kernel From Environment:
```
pip install ipykernel
python -m ipykernel install --user --name=Conda2
```

- Deactivate Current Environment:
```
conda deactivate
```

- Delete Environment:
```
conda activate base
conda remove -p /home/jovyan/Conda2 --all
jupyter kernelspec remove conda2
```