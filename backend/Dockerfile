FROM python:3.10
WORKDIR /backend
COPY . .
RUN pip install --no-cache-dir --upgrade -r requirements.txt
ENTRYPOINT [ "python" ]
CMD ["main.py"]