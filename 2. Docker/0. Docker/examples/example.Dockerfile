# Specify image:tag
FROM ubuntu:18.04

# Update OS
RUN apt-get update \
    # Install minimal Python3 version
    && apt-get install -y --no-install-recommends python3 \
    # Remove mirrors making minimal image
    && rm -rf /var/lib/apt/lists/*

# Copy data from docker context
COPY . .

# When we run container this will be the command run
ENTRYPOINT ["python3"]
