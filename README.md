# Airflow Docker Compose Setup

This directory contains a complete local development setup for Apache Airflow using Docker Compose.

## Prerequisites

- Docker Desktop installed and running.

## Quick Start

1. **Initialize the Environment**:
   The `.env` file and necessary directories (`dags`, `logs`, `plugins`) have already been created for you.

2. **Start Airflow**:
   Run the following command to download images and start the services:
   ```bash
   docker compose up -d
   ```

3. **Access the Web Interface**:
   - Once the services are healthy, open your browser to [http://localhost:8080](http://localhost:8080).
   - **Username**: `airflow`
   - **Password**: `airflow`

4. **Stop Airflow**:
   To stop the services and remove containers:
   ```bash
   docker compose down
   ```

## Directory Structure

- `dags/`: Place your DAG python files here.
- `logs/`: Airflow logs will be persisted here.
- `plugins/`: Custom Airflow plugins.

## Configuration

You can modify environment variables in `docker-compose.yaml` or override them in the `.env` file.
# goouty_airflow
