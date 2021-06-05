FROM python:3.8.0

# Copying the requirements for installation to take
# advantage of the caching.
WORKDIR usr/src/app
COPY requirements.txt .
RUN pip install -r ./requirements.txt
COPY . .
