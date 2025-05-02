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

- List Installed Packages:
```
installed.packages()
```

- Exit R Console:
```
q()
```

### Useful R Docs
- <a href="https://www.r-project.org/" target="_blank">The R Project</a>
- <a href="https://cran.r-project.org/doc/contrib/Lemon-kickstart/index.html" target="_blank">Kickstarting R</a>
- <a href="https://datatofish.com/install-package-r/" target="_blank">Installing R Packages</a>

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

