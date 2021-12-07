from python:3
RUN pip install flask && \
    pip install ibm_db_sa
EXPOSE 8000
COPY . .
CMD ["get_service.py"]
ENTRYPOINT ["python3"]

