# FROM python:3.8.7
# RUN apt-get update && apt-get upgrade -y
# COPY . /app
# WORKDIR /app
# RUN python -m pip install -r requirements.txt
# RUN chmod 777 run.sh
# ENTRYPOINT [ "/bin/bash" ]
# CMD ["run.sh"]

# FROM ubuntu:20.04
# RUN apt-get update && apt-get install python3 python3-pip -y && apt-get upgrade -y
# COPY . /app
# WORKDIR /app
# RUN python3 -m pip install -r requirements.txt
# RUN chmod 777 run.sh
# ENTRYPOINT [ "/bin/bash" ]
# CMD ["run.sh"]

FROM python:3.8.7 as builder
RUN apt-get update && apt-get upgrade -y
RUN python -m venv /venv
ENV PATH="/venv/bin:$PATH"
COPY requirements.txt requirements.txt
RUN python3 -m pip install -r requirements.txt

FROM python:3.8.7-slim-buster
RUN apt-get update && apt-get install python3-pip -y && apt-get upgrade -y
COPY --from=builder /venv /venv
COPY . /app
WORKDIR /app
ENV PATH="/venv/bin:$PATH"
RUN chmod 777 run.sh
ENTRYPOINT [ "/bin/bash" ]
CMD ["run.sh"]