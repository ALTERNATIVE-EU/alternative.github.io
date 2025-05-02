## File System

The `/home/jovyan` and `/home/shared` directories are not being deleted between server stops. `/home/jovyan` is personal for the user - nobody else can see its content; and has 10 GB available space. `/home/shared` is for all users - everybody can see its content; and has 20 GB available space. All other directories are deleted and recreated everytime the server is stopped/started. The folder `/home/jovyan/shared` is a symlink to `/home/shared` and can be used to interact with the files of the shared directory.
