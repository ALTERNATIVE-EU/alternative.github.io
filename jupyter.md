# JupyterHub

The platform integrates <a href="https://jupyterhub.readthedocs.io/en/stable/" target="_blank">JupyterHub</a> as a way to interact with datasets and virtual environments. To access JupyterHub select the `Jupyterhub` button from the top right corner of any page. Everytime a user visits the JupyterHub page, a <a href="https://jupyterlab.readthedocs.io/en/stable/" target="_blank">JupyterLab</a> server is spawned for them, which enables you to work with documents and activities such as Jupyter notebooks, text editors, files and terminals. <a href="https://jupyter-notebook.readthedocs.io/en/stable/" target="_blank">Jupyter Notebooks</a> (*.ipynb* files) are documents that combine runnable code with narrative text (Markdown), equations (LaTeX), images, interactive visualizations and more. Once your server is ready, you will be redirected to it. After some time of inactivity it will be shutdown.

## JupyterLab

At the top you can find different options and settings. You can get back to JupyterHub by selecting `File` -> `Hub Control Panel` or press `Log Out` to end the session. At the bottom you can see how many terminals and consoles are open and what environment is being used. On the right there are debugging tools.

On the left there's 4 tabs:
- `File Browser` - interact with files or open a `Launcher` tab from the `+` button
- `Running Terminals and Kernels` - see all open tabs and running kernels and terminals, option to close or stop any/all of them
- `Table of Contents` - shows information about the currently open file/notebook
- `Extension Manager` - can be used to install extensions

In the middle, you can see the currently open tabs and interact with them. From the `Launcher` tab (create new one by clicking `+`), you can create notebooks or consoles, open terminals or start new text, markdown and python files. [Example](notebook-example.ipynb) of a notebook file.

## File System

Each user has 10 GB available space. `/home/jovyan` and `/home/shared` directories are not being deleted between server stops. `/home/jovyan` is personal for the user - nobody else can see its content. `/home/shared` is for all users - everybody can see its content. All other directories are deleted and recreated everytime the server is stopped/started.

## Environments

Every JupyterLab server is being spawned with two environments from the start - default python environment and an additional <a href="https://conda.io/projects/conda/en/latest/user-guide/index.html" target="_blank">conda</a> environment. On `Launcher` tab under `Notebook` or `Console` you can choose which environment to use. You can also use the `Terminal`:

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

## Python Library

The python library <a href="https://github.com/ALTERNATIVE-EU/alternative-lib" target="_blank">alternative-lib</a> is designed to help with finding datasets and downloading resources from them, by using <a href="https://github.com/ckan/ckanapi" target="_blank">ckanapi</a>.

It can be installed with:
```
pip install alternative-lib
```

[Example](lib-example.py) of the library being used to get a public dataset and download its resource.

## R

You can use R from a `Terminal`. The first time you install a new package you should be asked where to save it. **Make sure any packages you install are in the `/home/jovyan` directory or they will get deleted.**

- Activate R Console:
```
R
```

- Help Command:
```
help()
```

- Install Package:
```
install.packages("package_name")
```

- Exit R Console:
```
q()
```

### Useful R Docs
- <a href="https://www.r-project.org/" target="_blank">The R Project</a>
- <a href="https://cran.r-project.org/doc/contrib/Lemon-kickstart/index.html" target="_blank">Kickstarting R</a>
- <a href="https://datatofish.com/install-package-r/" target="_blank">Installing R Packages</a>
- <a href="https://bioconductor.org/install/" target="_blank">Installing and Using Bioconductor</a>

### Version Update

The R version has been updated from 4.0.4 to 4.3.0. If you have installed any R packages before this update, you will need to add your previous package directory to R's paths, to be able to use those packages.

Commands (should be executed in R console; replace `yourLib` with the path to your R package directory; by default that should have been `~/R/x86_64-pc-linux-gnu-library/4.0`):

To add the directory in paths list:
```
.libPaths( c( .libPaths(), "yourLib") )
```

To make the directory the main library for packages:
```
.libPaths( c( "yourLib" , .libPaths() ) )
```
