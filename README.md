# This file is pretty simple to run

# Windows

Make sure that you have docker desktop app installed and open.

Make sure that you have git app for Windows installed (No need to open it).

open command prompt and run the following lines of code

git clone ...

cd Garden

Note! your *image_name* can be any name you like 

docker build -t <image_name> ./

docker run <image_name>

Done !!!

# Linux

The following line of code install docker. If you have, don't worry continue to run the code it should update to the latest docker if not updated.

sudo apt-get install docker.io -y


Make sure that your docker daemon service is up. To start your daemon service:

sudo service docker start


git clone ...

cd Garden

Note! your *image_name* can be any name you like 

docker build -t <image_name> ./

docker run <image_name>

Done !!!

