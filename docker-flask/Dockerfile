FROM python:3.10
WORKDIR /app
COPY . /app
RUN pip --no-cache-dir install -r requirements.txt
EXPOSE 9001
CMD ["python3", "main.py"]