# Project Worker Visit

A test task for making simple APIs for mobile app, where the worker can make visits to different units.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Docker setup](#docker-setup)

## Getting Started

These instructions will help you set up and run the project on your local machine.

### Prerequisites

- Python (version 3.10)
- Pip (Python package installer)
- Virtual Environment (recommended)

### Installation(Local setup)

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```

2. Set up a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use: venv\Scripts\activate
    ```

3. Install the project dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run database migrations:
    ```bash
    python manage.py migrate
    ```

5. Create Superuser:
    ```bash
    python manage.py createsuperuser
    ```

6. Run server:
    ```bash
    python manage.py runserver
    ```

### Docker setup

1. Install Docker and Docker engine in local system

2. Run Docker:
    In terminal, navigate to root directory and run the following commands:
    ```bash
    docker-compose up -d
    ```
    Then need to apply all the migartion run following commands:
    ```bash
    docker-compose run web python manage.py makemigrations
    docker-compose run web python manage.py migrate
    docker-compose run web python manage.py createsuperuser
    ```



