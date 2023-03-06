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

`/home/jovyan` and `/home/shared` directories are not being deleted between server stops. `/home/jovyan` is personal for the user - nobody else can see its content. `/home/shared` is for all users - everybody can see its content. All other directories are deleted and recreated everytime the server is stopped/started.

## Environments

Every JupyterLab server is being spawned with two environments from the start - default python environment and an additional <a href="https://conda.io/projects/conda/en/latest/user-guide/index.html" target="_blank">conda</a> environment. On `Launcher` tab under `Notebook` or `Console` you can choose which environment to use. You can also use the `Terminal` to:

### Add New Environments:
```
conda create --name Conda2
conda activate Conda2
python -m ipykernel install --user --name=Conda2
```

### Delete Environment:
```
conda activate base
conda remove -n Conda2 --all
jupyter kernelspec remove conda2
```

### Activate Different Environment:
```
conda activate Conda2
```

### Deactivate Current Environment:
```
conda deactivate
```

## Python Library

The python library <a href="https://github.com/ALTERNATIVE-EU/alternative-lib" target="_blank">alternative-lib</a> is designed to help with finding datasets and downloading resources from them, by using <a href="https://github.com/ckan/ckanapi" target="_blank">ckanapi</a>.

It can be installed with:
```
pip install alternative-lib
```

[Example](lib-example.py) of the library being used to get a public dataset and download its resource.