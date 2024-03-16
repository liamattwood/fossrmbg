FROM python:3.9

COPY u2net.onnx /home/.u2net/u2net.onnx

WORKDIR /app

RUN python -m venv venv

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5100

CMD ["python", "main.py"]
