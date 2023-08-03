# Linux

### Changing file/driectory permissions:

* For universal file permissions:
  * `chmod +rwx <filename>` adds permissions
  * `chmod -rwx <filename>` removes permissions
  * `chmod =rwx <filename>` sets exact permissions
* For the user/owner of the file:
  * `chmod u+rwx <filename>`
  * `chmod u-rwx <filename>`
  * `chmod u=rwx <filename>`
* For the group of the file:
  * `chmod g+rwx <filename>`
  * `chmod g-rwx <filename>`
  * `chmod g=rwx <filename>`
* For others:
  * `chmod o+rwx <filename>`
  * `chmod o-rwx <filename>`
  * `chmod o=rwx <filename>`
* Numerical selection, add up the following numbers for multiple permissions:
  * 0 - No Permission
  * 1 - Execute
  * 2 - Write
  * 4 - Read
  * e.g. Read(4) + Write(2) = 6

### Navigating files/folders:

* `cd` on it's own, or `cd ~` takes you to your home directory
* `cd /` takes you to the root directory
* `cd ..` takes you to the parent dir of your current dir
* `cd .` is a link to your current dir (useful in some commands)
* `ls` show files in current directiory, add `-a` to show hidden files/dirs,
  add `-l` to show details like permissions of files/dirs

### Linux Commands:

* `mkdir <directoryname>` make a new directory
* `touch <filename>` make a new file
* `cp <filename> <copyname>` copy file
* `mv <filename> <destinationname>` move a file
* `rm <filename>` remove file,
  add `-r` to remove a folder **AND IT'S CONTENTS!!!**
* `cat <filename>` display file
* `cat <filename> | grep <str>` search file for <str>
* `nl <filename>` display indexed lines of a file
* `head -<num> <filename>` display the first <num> lines of a file
* `tail -<num> <filename>` display the last <num> lines of a file
* `nano <filename>` basic text editor
* `apt install <packagename>` package installer
* `kill <pid>` to end processes use numerical switches based on severity
  e.g. `-1`, `-9`, `-15`

### System Info:

* `uname`: `uname --help` gives a list of available info
* `whoami`: tells you your username
* `ps` for checking user processes, add `aux` to see all processes in detail
* `history` for kernal input history
* `history !<index>` to run previous command

### Tree (installed program):

* `tree` shows a visual of the files/dir in the current dir

### Shell Scripts:

* `#!/bin/bash` Hash bang bin bash
```sh
#!/bin/bash

# update
sudo apt update -y

# upgrade
sudo apt upgrade -y

# install nginx
sudo apt install nginx -y

# restart nginx
sudo systemctl restart nginx

# enable nginx - like windows startup
sudo systemctl enable nginx
```

### Variables:

* `<VARIABLENAME>=<variablevalue>` to make a standard variable
* `export <VARIABLENAME>=<variablevalue>` to make an environment variable
* `printenv` shows all environment variables
* To make an enviornment variable persistent, it needs to be added to
  the end of the `.bashrc` file. Use `source .bashrc` to use it in the current session

### Bourne Again SHell (BASH):

Unix (command-driven OS) -> Linux (also has a Shell)
/bin/bash

What is a Shell?
* software - provides interface run commands

### Sparta Test App:

* Node js app
* port 3000
* features :
  * a front page (no database)
  * posts - displays data retrieved from the database
* requirements to run Sparta app
  * Linux VM - Ubuntu 18.04 LTS
  * web server - nginx (dependency)
  * right version node js - version 12.x works fine (dependency)
  * get app folder
  * (if posts/connection to db) set DB_HOST env variable
  * app folder, run 2 commands:
    * npm install
    * node app.js OR npm start
* export DB_HOST=mongodb://<DBIp>:27017/posts
* change `try_files $uri $uri/ =404;` to `proxy_pass http://localhost:3000;`
  in the nginx config file `/etc/nginx/sites-available/default` to set up the reverse proxy
* scp -i ~/.ssh/tech241-ash-az-key <filepath> adminuser@<VMIp>:~/

### app provisions:
```sh
#!/bin/bash

# update
sudo apt update -y

# upgrade
sudo apt upgrade -y

# install nginx
sudo apt install nginx -y

# start nginx
# sudo systemctl restart nginx

# make sure sed is installed
sudo apt install sed -y

# set up reverse proxy
sudo sed -i 's|try_files $uri $uri/ =404;|proxy_pass http://localhost:3000;|' /etc/nginx/sites-available/default

# restart nginx
sudo systemctl restart nginx

# enable nginx - like windows startup
sudo systemctl enable nginx

# install node.js and npm
curl -sL https://deb.nodesource.com/setup_12.x | sudo -E bash -
sudo apt install nodejs -y
sudo npm install pm2 -g

# copy app folder from github
git clone https://github.com/AshFrankland/tech241_app.git repo

# set DB_HOST variable
export DB_HOST=mongodb://<DBIP>:27017/posts

# run app
cd repo/app
npm install -y
# node seeds/seed.js
# pm2 kill
pm2 start app.js
# npm start
# nohup node app.js &
```

### user data for a launch template
```sh
#!/bin/bash

export DB_HOST=mongodb://<DBIP>:27017/posts

cd repo/app
npm install -y
node seeds/seed.js

pm2 start app.js
```

### DB VM

* Linux VM - Ubuntu 18.04 LTS
* update and upgrade
* install mongo db - version 3.2.x
  * download key for the right version
  * source list - specify mongo db version
  * apt update again
  * install mongo db
* configure mongo db to accept connnections from the app VM
  * change bindip
  * start mongo db
  * enable mongo db

### DB provisions
```sh
#!/bin/bash

# update
sudo apt update -y

# upgrade
sudo apt upgrade -y

# install mongo db
wget -qO - https://www.mongodb.org/static/pgp/server-3.2.asc | sudo apt-key add -
echo "deb http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.2.list
sudo apt update -y
sudo apt-get install -y mongodb-org=3.2.20 mongodb-org-server=3.2.20 mongodb-org-shell=3.2.20 mongodb-org-mongos=3.2.20 mongodb-org-tools=3.2.20

# make sure sed is installed
sudo apt install sed -y

# configure bindip
sudo sed -i 's/bindIp: 127.0.0.1/bindIp: 0.0.0.0/g' /etc/mongod.conf

# start and enable mongo db
sudo systemctl restart mongod
sudo systemctl enable mongod
```