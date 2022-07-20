### Docker task

1. To use docker we need to install docker engine on our system.
	```
	#Before instalation we have to delete older versions of Docker.
	sudo apt-get remove docker docker-engine docker.io containerd runc
	
	#Update
	sudo apt-get update

	#Install packages to allow apt to use a repository over HTTPS
	sudo apt-get install \
   	ca-certificates \
   	curl \
   	gnupg \
   	lsb-release

	#Add Docker’s official GPG key:
	sudo mkdir -p /etc/apt/keyrings
	curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

	#Use the following command to set up the repository:
	echo \
	"deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
	$(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

	#Update the apt package index, and install the latest version of Docker Engine, containerd, and Docker Compose, or go to the next step to install a specific version:
	sudo apt-get update
	sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin
	```

2. Preparing our **flask-app** by creating recquired files:
	* app.py - with python script
	* requirements.txt - to install all dependencies needed for our application
	* index.html - for web representation 
	* Dockerfile - to build our docker image 
		* Here is our docker file
		```
		# our base image
		FROM alpine:3.5
		# Install python and pip
		RUN apk add --update py2-pip
		# upgrade pip
		RUN pip install --upgrade pip
		# install Python modules needed by the Python app
		COPY requirements.txt /usr/src/app/
		RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt
		# copy files required for the app to run
		COPY app.py /usr/src/app/
		COPY templates/index.html /usr/src/app/templates/
		# tell the port number the container should expose
		EXPOSE 5000
		# run the application
		CMD ["python", "/usr/src/app/app.py"]
		```
3. From our **flask-app** folder we build docker image:
	```
	docker build -t kf/mycatapp .
	```
4. After completion we can run our image: 
	```
	docker run -p 5000:5000 --name mycatapp kf/mycatapp
	```

