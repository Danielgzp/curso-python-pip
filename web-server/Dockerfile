FROM python:3.10

WORKDIR /countrypopulation
COPY requirements.txt /countrypopulation/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /countrypopulation/requirements.txt

COPY . /countrypopulation/

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]