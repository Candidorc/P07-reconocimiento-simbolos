FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install streamlit tensorflow==2.20.0 keras==3.13.2 pillow numpy

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]