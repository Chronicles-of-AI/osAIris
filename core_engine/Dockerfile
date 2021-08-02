FROM python:3.8.7
RUN apt-get update && apt-get upgrade -y
COPY . /app
WORKDIR /app
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
RUN unzip awscliv2.zip \
    && ./aws/install \
    && rm awscliv2.zip \
    && aws --version
RUN python -m pip install -r requirements.txt
RUN chmod 777 run.sh
ENTRYPOINT [ "/bin/bash" ]
CMD ["run.sh"]