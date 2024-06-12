FROM python:3.12

RUN apt update
RUN mkdir /quizes

WORKDIR /quizes

COPY ./src ./src
COPY ./commands ./commands

COPY ./requirements.txt ./requirements.txt

RUN python -m pip install --upgrade pip
RUN pip install -r ./requirements.txt

CMD ["bash"]