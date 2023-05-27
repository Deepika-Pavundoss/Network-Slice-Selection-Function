# Set the base image
FROM python:3.9-slim-buster

# Upgrade pip
RUN pip install --no-cache-dir --upgrade pip

# Install the MySQL client dependencies
RUN apt-get update \
    && apt-get install -y default-libmysqlclient-dev gcc \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code
COPY . .

# Start the request app
CMD [ "python", "requestApp.py" ]