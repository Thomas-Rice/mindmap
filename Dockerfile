FROM python:3.6

# RUN apt-get update -y && \
#     apt-get install -y python-pip python-dev

COPY . /app
WORKDIR /app

RUN  python -m venv venv
CMD  ["source venv/bin/activate"]

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN chmod +x startup.sh

ENTRYPOINT ["/bin/bash", "startup.sh"]

EXPOSE 5000