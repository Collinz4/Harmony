FROM centos:7

# install system dependencies and update
RUN yum -y install python3
RUN yum -y update && yum -y upgrade
RUN pip3 install --upgrade pip

# create user 'd-user' and set work directory
RUN groupadd harmony-group && \
    adduser harmony-user -G harmony-group
WORKDIR /home/harmony-user/

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH "${PYTHONPATH}:/home/harmony-user/"

# install dependencies
COPY ./requirements.txt /home/harmony-user/requirements.txt
RUN pip3 install -r requirements.txt

# copy project
COPY ./ /home/harmony-user/

USER harmony-user

EXPOSE 8080

CMD ["python3", "./app.py"]
