FROM python:3.12
RUN mkdir -p /usr/src/app/files
WORKDIR /usr/src/app
COPY timestamp_gen.py .
ENTRYPOINT ["python3", "./timestamp_gen.py"]
CMD ["/usr/src/app/files/timestamp.txt"]