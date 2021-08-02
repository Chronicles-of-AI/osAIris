FROM python:3.8.7
RUN apt-get update && apt-get upgrade -y
COPY . /app
WORKDIR /app
RUN python -m pip install -r requirements.txt
# RUN python -m pipenv install
# ENTRYPOINT ["bash"]
RUN chmod 777 run.sh
ENTRYPOINT [ "/bin/bash" ]
CMD ["run.sh"]
# CMD ["python3","main.py"]