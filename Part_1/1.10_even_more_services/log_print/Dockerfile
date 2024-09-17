FROM python:3.12
RUN mkdir -p /usr/src/app/files
WORKDIR /usr/src/app
COPY log_print.py .
RUN pip install flask
ENTRYPOINT ["python3", "./log_print.py"]
CMD ["/usr/src/app/files/timestamp.txt"]