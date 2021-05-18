FROM python:3.7.3

# Copy dependency definitions
ADD linux_packages.txt /tmp/docker_environment/linux_packages.txt
ADD requirements.txt /tmp/docker_environment/requirements.txt

# Install Linux Dependencies
RUN apt-get update; apt-get install -y $(awk '{print $1'} /tmp/docker_environment/linux_packages.txt)

# Install Python Dependencies
RUN pip install -r /tmp/docker_environment/python_packages.txt

# Add controller
ADD controller.py /home/

WORKDIR /home

CMD ["tail","-f","/dev/null"]