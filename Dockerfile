FROM python:3.9

WORKDIR /bot

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY main.py .

COPY responses.py .

CMD ["python", "main.py"]
