FROM python:3.7
ENV PYTHONUNBUFFERED 1

RUN apt update && apt upgrade -y
RUN apt install python3-pip libssl-dev curl apt-utils -y --no-install-recommends
RUN apt install gcc python3-dev musl-dev -y --no-install-recommends
RUN rm -rf /var/lib/apt/lists/*

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ADD ./requirements.txt /requirements.txt
RUN pip3 install -U pip
RUN LIBRARY_PATH="/lib:/usr/lib"
RUN /bin/sh -c "pip3 install -r /requirements.txt --no-cache-dir"

WORKDIR /home
COPY . /home

EXPOSE 9091

ENTRYPOINT ["/entrypoint.sh"]

