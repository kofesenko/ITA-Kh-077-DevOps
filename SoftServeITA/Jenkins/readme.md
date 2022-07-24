### Task 1
1. Install Jenkins on the system:
```
#Install java for Jenkins usage
sudo apt update
sudo apt install default-jre
#Add the repository key to your system
wget -q -O - https://pkg.jenkins.io/debian-stable/jenkins.io.key |sudo gpg --dearmor -o /usr/share/keyrings/jenkins.gpg
#Append the Debian package repository address to the server’s sources.list
sudo sh -c 'echo deb [signed-by=/usr/share/keyrings/jenkins.gpg] http://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'
#After both commands have been entered, run apt update so that apt will use the new repository.
sudo apt update
#Install Jenkins and its dependencies:
sudo apt install jenkins
#Now that Jenkins is installed, start it by using systemctl
sudo systemctl start jenkins.service
#Since systemctl doesn’t display status output, we’ll use the status command to verify that Jenkins started successfully:
sudo systemctl status jenkins
#Open firewall rules using **ufw**:
sudo ufw allow 8080 #default jenkins port
sudo ufw allow OpenSSH
sudo ufw enable
#Open Jenkins to continue instalation:
http://<server_ip>:8080
#Unlock Jenkins by providing password from the following file:
sudo cat /var/lib/jenkins/secrets/initialAdminPassword
#Continue instalation and configure user
```

2. Create deploy job which will deploy index.html page on apache server from jenkins server using secure copy:
    * Set up second machine:
        ```
        #First we need to configure passwordless connection to this machine from our jenkins machine
        #On jenkins server machine configure ssh keys fro connection to our second server:
        ssh-keygen
        ssh-copy-id jenkins@192.168.0.209
        ssh jenkins@192.168.0.209
        #Notice that we don't need to enter password for connection

        #Second, install apache server on machine:
        sudo apt update
        sudo apt install apache2
        #Now we can access deafault apache page on 192.168.0.209
        #Set up required permissions for **/var/www/html**
        sudo chgrp -R jenkins /var/www
        sudo chmod -R g+rw /var/www


    * In build execute shell:
        ```
        echo "start"
        cat <<EOF > index.html
        <html>
        <head>
            <title>TEST</title>
        </head>
        <body bgcolor=green>
            <p style = "color: red; text-alighn: center; font-size: 70px;" >Hello World!</p>
        </body>
        </html>
        EOF
        echo "finished"
        ls -la
        echo "Build number: $BUILD_NUMBER"
        echo "-----------deploy------------"
        scp -v -o StrictHostKeyChecking=no index.html jenkins@192.168.0.209:/var/www/html
        ```
    * Run build 
        ```
        + echo start
        start
        + cat
        + echo finished
        finished
        + ls -la
        total 12
        drwxr-xr-x 2 jenkins jenkins 4096 Jul 22 13:51 .
        drwxr-xr-x 4 jenkins jenkins 4096 Jul 22 13:51 ..
        -rw-r--r-- 1 jenkins jenkins  162 Jul 24 13:17 index.html
        + echo Build number: 4
        Build number: 4
        + echo -----------deploy------------
        -----------deploy------------
        + scp -v -o StrictHostKeyChecking=no index.html jenkins@192.168.0.209:/var/www/html
        Executing: program /usr/bin/ssh host 192.168.0.209, user jenkins, command scp -v -t /var/www/html
        OpenSSH_8.2p1 Ubuntu-4ubuntu0.5, OpenSSL 1.1.1f  31 Mar 2020
        debug1: Reading configuration data /etc/ssh/ssh_config
        ---------------------------------
        debug1: Authentication succeeded (publickey).
        Authenticated to 192.168.0.209 ([192.168.0.209]:22).
        ----------------------------------
        Transferred: sent 3532, received 3200 bytes, in 1.4 seconds
        Bytes per second: sent 2458.6, received 2227.5
        debug1: Exit status 0
        Finished: SUCCESS
        ```
3.  Create deploy job which will deploy index.html page on apache server from jenkins server using Publish Over SSH plugin:
    * Install **Publish Over SSH** plugin
    * Configure plugin:
        * Add private key
        * SSH Server name = apache
        * hostname = 192.168.0.209
        * username = jenkins
        * remote directory = /var/ww/html
    * Configure deploy job with publish over ssh:
        * add post-build action **Send build artifacts over SSH**
        * Source files = *
        * exec commnad = echo $BUILD_ID
    * In build execute shell:
        ```
        echo "start"
        cat <<EOF > index.html
        <html>
        <head>
            <title>TEST</title>
        </head>
        <body bgcolor=green>
            <p style = "color: red; text-alighn: center; font-size: 70px;" >Hello World!</p>
            <p style = "color: yellow; text-alighn: center; font-size: 70px;" >Deployed by Publish over SSH!</p>
        </body>
        </html>
        EOF
        echo "finished"
        ls -la
        echo "Build number: $BUILD_NUMBER"
        echo "-----------deploy------------"
        ```
    * Save and build
        ```
        Running as SYSTEM
        Building in workspace /var/lib/jenkins/workspace/jobdeploy1
        [jobdeploy1] $ /bin/sh -xe /tmp/jenkins14216587923490304072.sh
        + echo start
        start
        + cat
        + echo finished
        finished
        + ls -la
        total 12
        drwxr-xr-x 2 jenkins jenkins 4096 Jul 22 13:51 .
        drwxr-xr-x 4 jenkins jenkins 4096 Jul 22 13:51 ..
        -rw-r--r-- 1 jenkins jenkins  264 Jul 24 13:56 index.html
        + echo Build number: 6
        Build number: 6
        + echo -----------deploy------------
        -----------deploy------------
        SSH: Connecting from host [jen-vm]
        SSH: Connecting with configuration [apache] ...
        SSH: EXEC: completed after 201 ms
        SSH: Disconnecting configuration [apache] ...
        SSH: Transferred 1 file(s)
        Finished: SUCCESS
        ```
4. Create deploy job which will deploy grabbed from github index.html page on apache server using jenkins server and Publish Over SSH plugin:    
    * Set up SSH connection to GitHub from Jenkins (copy public key on GitHub and Private on Jenkins)
    * In source code management configure Git
    * In Build section configure Send Files or execute commands over SSH
        * Source files **/*.html to grab only index.html file.
   * Build
5. Adjust deploy job which will deploy index.html page on webserver only when changes were commited to index.html
    * In Build triggers section configure Poll SCM
        ```
        H/2 * * * *
        ```