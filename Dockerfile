FROM python:3.10-slim

# Install dependencies sistem yang diperlukan matplotlib, seaborn, dsb
RUN apt-get update && apt-get install -y \
    build-essential \
    libglib2.0-0 \
    libxext6 \
    libsm6 \
    libxrender1 \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Salin file ke container
COPY . .

# Install package Python
RUN pip install --no-cache-dir -r requirements.txt

# Jalankan aplikasi Streamlit lewat Python
CMD ["python", "-m", "streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]


