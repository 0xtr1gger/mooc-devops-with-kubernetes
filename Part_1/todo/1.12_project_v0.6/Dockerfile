FROM python:3.12-slim
WORKDIR /app
COPY /src /app
RUN pip install -r requirements.txt
ENV PORT=5000
CMD ["python3", "server.py"]