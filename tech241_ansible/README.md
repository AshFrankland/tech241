# Ansible

### Setting up an Ansible controller

* Set up 3 VMs (controller, app, db)
* SSH into controller VM, update and upgrade
* install anisible: `sudo apt-add-repository ppa:ansible/ansible`
* Add AWS SSH key to .ssh folder on controller VM
* SSH into app and db VMs, update and upgrade both
* Return to controller VM, cd into `/etc/ansible`
* Add SSH paths to `hosts` file: `[web]` `ec2-instance ansible_host=<VMIP> ansible_user=ubuntu ansible_ssh_private_key_file=~/.ssh/tech241.pem`
* Ping the app and db VMs: `sudo ansible <web> -m ping`

### nginx Playbook

```yml
# YAML files start with --- three dashes        
# create a playbook to install nginx in app node

---

# which host?
- hosts: app

  gather_facts: yes

# admin access
  become: true

# add the instructions - install nginx - app    
  tasks:
  - name: Installing Nginx
    apt: pkg=nginx state=present

# ensure nginx is running using an adhoc command
```

### node.js Playbook

```yml
---

# which host?
- hosts: app

  gather_facts: yes

# admin access
  become: true

# add the instructions - install node.js - app
  tasks:
  - name: Update apt package cache
    apt:
      update_cache: yes

  - name: Upgrade packages
    apt:
      upgrade: dist

  - name: Add DB_HOST environment variable to /etc/environment file
    lineinfile:
      path: /etc/environment
      line: 'export DB_HOST="mongodb://3.248.250.113:27017/posts"' 
      state: present
      create: yes

  - name: Clone repository
    git:
      repo: https://github.com/AshFrankland/tech241_app.git
      dest: app

  - name: Install Node.js
    get_url:
      url: https://deb.nodesource.com/setup_12.x
      dest: /tmp/node_setup.sh

  - name: Run Node.js setup script
    command: sudo -E bash /tmp/node_setup.sh

  - name: Install Node.js package
    apt:
      name: nodejs
      state: present

  - name: Install npm packages
    shell: npm install
    args:
      chdir: /home/ubuntu/app/app
      warn: false

  - name: Seed database
    shell: node seeds/seed.js
    args:
      chdir: /home/ubuntu/app/app

  - name: Install sed
    apt:
      name: sed
      state: present

  - name: Configure reverse proxy in Nginx
    shell: sudo sed -i 's#try_files $uri $uri/ =404;#proxy_pass http://localhost:3000;#g' /etc/nginx/sites-available/default

  - name: Restart Nginx
    service:
      name: nginx
      state: restarted

  - name: Install pm2
    npm:
      name: pm2
      global: yes
      state: present

  - name: Stop pm2 processes
    shell: pm2 kill

  - name: Start app with pm2
    shell: pm2 start app.js
    args:
      chdir: /home/ubuntu/app/app
```

### mongodb Playbook

```yml
---

# which host
- hosts: db

# get logs
  gather_facts: yes

# admin access
  become: true

# provide instructions - task     
  tasks:

# install mongodb
  - name: Installing Mongodb      
    apt: pkg=mongodb state=present

# ensure db is running


# change the bindip in mongod.conf
  - name: Update Mongodb config   
    lineinfile:
      path: /etc/mongodb.conf
      regexp: '^bind_ip'
      line: 'bind_ip = 0.0.0.0'

# restart mongodb
  - name: Restart Mongodb
    service:
      name: mongodb
      state: restarted
      enabled: yes
```