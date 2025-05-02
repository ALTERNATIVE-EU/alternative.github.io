### Bioconductor

<a href="https://bioconductor.org/install/" target="_blank">Installing and Using Bioconductor</a>. When installing packages with `BiocManager::install()`, add the path to your R package directory, like so (replace `your_R_package_dir` with the directory name):
```
BiocManager::install(lib="/home/jovyan/your_R_package_dir")
```
or
```
BiocManager::install("package_name", lib="/home/jovyan/your_R_package_dir")
```
