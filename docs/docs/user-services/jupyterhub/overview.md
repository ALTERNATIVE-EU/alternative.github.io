# JupyterHub

The platform integrates <a href="https://jupyterhub.readthedocs.io/en/stable/" target="_blank">JupyterHub</a> as a way to interact with datasets and virtual environments. To access JupyterHub select the `Jupyterhub` button from the top right corner of any page. Everytime a user visits the JupyterHub page, a <a href="https://jupyterlab.readthedocs.io/en/stable/" target="_blank">JupyterLab</a> server is spawned for them, which enables you to work with documents and activities such as Jupyter notebooks, text editors, files and terminals. <a href="https://jupyter-notebook.readthedocs.io/en/stable/" target="_blank">Jupyter Notebooks</a> (*.ipynb* files) are documents that combine runnable code with narrative text (Markdown), equations (LaTeX), images, interactive visualizations and more. Once your server is ready, you will be redirected to it. After some time of inactivity it will be shutdown.

## JupyterHub

At the top you can find different options and settings. You can get back to JupyterHub by selecting `File` -> `Hub Control Panel` or press `Log Out` to end the session. At the bottom you can see how many terminals and consoles are open and what environment is being used. On the right there are debugging tools.

On the left there's 4 tabs:
- `File Browser` - interact with files or open a `Launcher` tab from the `+` button
- `Running Terminals and Kernels` - see all open tabs and running kernels and terminals, option to close or stop any/all of them
- `Table of Contents` - shows information about the currently open file/notebook
- `Extension Manager` - can be used to install extensions

In the middle, you can see the currently open tabs and interact with them. From the `Launcher` tab (create new one by clicking `+`), you can create notebooks or consoles, open terminals or start new text, markdown and python files. [Example](notebook-example.ipynb) of a notebook file.
