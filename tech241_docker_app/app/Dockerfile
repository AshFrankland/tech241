FROM node:12

# Set the working directory in the Docker image
WORKDIR /usr/src/app

# Copy the package.json and package-lock.json files into the Docker image
COPY package*.json ./

# Install the application dependencies inside the Docker image
RUN npm install

# Copy the rest of the application into the Docker image
COPY . .

# Expose port 3000 to have it mapped by Docker daemon
EXPOSE 3000

# The command to run when the container starts
CMD [ "node", "app.js" ]