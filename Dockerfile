FROM python:3.7-alpine
ADD . /webiste
WORKDIR /webiste
RUN pip install -r requirements.txt
CMD ["python", "app.py"]