# ||Base||
# -------------------------------------------------------------------------------------------------------------------- #
# Base Image
FROM python:3.10.4-alpine AS si-base

# Workspace
WORKDIR /home/si

# System Dependencies
RUN apk update && apk upgrade

# ||Manager||
# -------------------------------------------------------------------------------------------------------------------- #
# Base Image
FROM si-base AS si-manager

# Source
COPY ./dependencies /usr/local/lib/python3.10/site-packages/dependencies
COPY ./manager .

# Python Dependencies
RUN pip install --no-cache-dir --upgrade pip -r requirements.txt

# Execute
CMD ["python", "-u", "./manager.py"]

# ||Agent||
# -------------------------------------------------------------------------------------------------------------------- #
# Base Image
FROM si-base AS si-agent

# Source
COPY ./agent .

# Python Dependencies
RUN pip install --no-cache-dir --upgrade pip -r requirements.txt

# Execute
CMD ["python", "-u", "./agent.py"]