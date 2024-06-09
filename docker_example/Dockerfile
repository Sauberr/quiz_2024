FROM python:3.12

RUN apt update
RUN python --version

RUN mkdir /docker_example

WORKDIR /docker_example

COPY hello_world_from_docker.py ./hello_world_from_docker.py
COPY requirements.txt ./requirements.txt

RUN python -m pip install --upgrade pip
RUN pip install -r ./requirements.txt

CMD ["python", "hello_world_from_docker.py"]
