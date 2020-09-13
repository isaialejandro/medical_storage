#Base image:
FROM python:3

#create a new directory
RUN mkdir /app
WORKDIR /app

#Add current directory code to workigng directory
ADD . /app/

#Set default environment variables
ENV PYTHONUNBUFFERED 1
ENV LANG C.UTF-8
ENV DEBIAN_FRONTENT=noninteractive

#Set project environment variables
#Grab from Python´s os.environ
ENV PORT=8080

#Install System dependencies
#For OSX/Linux:
#RUN apt-get update && apt-get upgrade && apt-get install -y --no-install-recommends\
#    python3-setuptools \
#    python3-pip \
#    python3-dev \
#    python3-venv \
#    git \
#    && \
#    apt-get clean && \
#    rm -rf /var/lib/apt/lists/*

#For Centos8:
RUN yum update && yum upgrade && dnf install \
    python-setuptools \
    python-pip \
    python-wheel\
    python-dev \
    python-venv \
    git \
    && \
    dnf clean && \
    rm -rf /var/lib/apt/lists/*


#Install environment dependencies
RUN pip install --upgrade pip
RUN pip install pipenv
RUN pip install --no-cache-dir -r requirements.txt

#Install project dependencies
RUN pipenv install --skip-lock --system --dev

#Run collectstatic for load staticfiles project
RUN python3 manage.py collecstatic --noinput

EXPOSE 8080

#CMD python -c "print('CMD from DockerFile!')"
CMD gunicorn djangoOnDocker.wsgi:application --bind 0.0.0.0:$PORT