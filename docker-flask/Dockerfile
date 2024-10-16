FROM python:3.10
WORKDIR /app
COPY . /app
RUN pip --no-cache-dir install -r requirements.txt
EXPOSE 5000
CMD ["python3", "main.py"]