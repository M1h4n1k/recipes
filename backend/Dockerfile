FROM python:3.10
WORKDIR /backend
COPY . .
RUN pip install --no-cache-dir --upgrade -r requirements.txt
EXPOSE 84
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "84"]