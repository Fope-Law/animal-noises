FROM python:latest
WORKDIR /app
COPY . .
RUN pip3 install flask requests
EXPOSE 5000
ENTRYPOINT ["python", "app.py"]
