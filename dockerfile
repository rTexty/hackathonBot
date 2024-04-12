FROM python:3.12-alpine
WORKDIR /Users/rtexty/Documents/Projects/Hackathon/bot
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "main.py"]
