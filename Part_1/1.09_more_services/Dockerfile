FROM python
COPY pingpong.py .
RUN pip install Flask
RUN chmod +x pingpong.py
ENTRYPOINT ["python3"]
CMD ["./pingpong.py"]