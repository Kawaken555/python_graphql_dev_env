FROM python:3.9

WORKDIR /fastapi

COPY . /fastapi/

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 8000

#CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
