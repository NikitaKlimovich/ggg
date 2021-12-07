
from python:3
EXPOSE 8000
COPY . .
CMD ["get_service.py"]
ENTRYPOINT["python3"]

