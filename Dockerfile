FROM python:3.12-slim

ENV PATH="/scripts:${PATH}:/app"
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Install system dependencies
RUN apt-get update && apt-get install -y \
    netcat-openbsd \
    gcc \
    libpq-dev \
    postgresql-client \
    libpcre3-dev \
    mime-support \
    && pip install --upgrade pip \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*


# Install python dependencies
COPY ./requirements.txt /requirements.txt
RUN pip install -r requirements.txt


# Create directory structure with correct permissions
# Create directory structure with correct permissions
RUN mkdir -p /app/vol/static /app/vol/media /var/log/uwsgi && \
    adduser --disabled-password --no-create-home user && \
    chown -R user:user /app/vol /var/log/uwsgi && \
    chmod -R 775 /app/vol && \
    chmod -R 777 /var/log/uwsgi

# Copy application files
COPY ./app /app
COPY ./scripts/entrypoint.sh /scripts/entrypoint.sh
RUN chmod +x /scripts/entrypoint.sh

WORKDIR /app

USER user

CMD ["entrypoint.sh"]