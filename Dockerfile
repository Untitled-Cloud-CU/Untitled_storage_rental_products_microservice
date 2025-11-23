# ================================
# 1. Use lightweight base image
# ================================
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# ================================
# 2. Install dependencies
# ================================
# Install system dependencies needed for PyMySQL & Cloud SQL
RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy only requirements first to leverage Docker layer caching
COPY requirements.txt /app

RUN pip install --no-cache-dir -r requirements.txt

# ================================
# 3. Copy project code
# ================================
COPY . /app

# ================================
# 4. Environment variables (Cloud Run injects real ones)
# ================================
ENV DB_USER=root \
    DB_PASS=change_me \
    DB_NAME=storage_rental_products \
    DB_HOST=/cloudsql/storage-rental-products-479116:us-central1:storage-rental-products-db \
    DB_PORT=3306 \
    PYTHONUNBUFFERED=1

# ================================
# 5. Required by Cloud Run
# ================================
EXPOSE 8080

# ================================
# 6. Start FastAPI app
# ================================
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]