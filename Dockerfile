# ══════════════════════════════════════════════════════════════
# STAGE 1: Builder - Install all dependencies and compile
# ══════════════════════════════════════════════════════════════
FROM python:3.11-slim AS builder

# Set working directory
WORKDIR /app

# Install system dependencies needed to COMPILE Python packages
# libpq-dev: Required for psycopg2 (PostgreSQL driver)
# gcc: C compiler needed to build Python packages
# libjpeg-dev, zlib1g-dev: Required for Pillow (image processing)
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    libjpeg-dev \
    zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first (Docker caches this layer if unchanged)
COPY requirements.txt .

# Install Python packages to /install (will be copied to stage 2)
RUN pip install --prefix=/install --no-cache-dir -r requirements.txt


# ══════════════════════════════════════════════════════════════
# STAGE 2: Production - Lean final image
# ══════════════════════════════════════════════════════════════
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install ONLY runtime libraries (not build tools)
# libpq5: PostgreSQL client library (runtime only)
# libjpeg62-turbo: JPEG library (runtime only)
RUN apt-get update && apt-get install -y \
    libpq5 \
    libjpeg62-turbo \
    && rm -rf /var/lib/apt/lists/*

# Copy installed Python packages from builder stage to system location
COPY --from=builder /install /usr/local

# Create non-root user for security
RUN addgroup --system appgroup && \
    adduser --system --ingroup appgroup appuser

# Copy all application code and set ownership
COPY --chown=appuser:appgroup . .

# Create directories for static and media files
RUN mkdir -p staticfiles media && \
    chown -R appuser:appgroup staticfiles media

# Switch to non-root user
USER appuser

# Prevent Python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE=1

# Ensure Python output is sent straight to terminal (no buffering)
ENV PYTHONUNBUFFERED=1

# Expose port 8000 (Gunicorn listens here)
EXPOSE 8000

# Start Gunicorn with 3 workers
CMD ["gunicorn", "config.wsgi:application", \
     "--bind", "0.0.0.0:8000", \
     "--workers", "3", \
     "--timeout", "120", \
     "--access-logfile", "-", \
     "--error-logfile", "-"]