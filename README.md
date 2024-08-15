# Admin Service

This project is a Django-based admin service for managing services, service types, service groups, and service notes.

## Setup

### Prerequisites

- Python >= 3.11

  To set up Python 3.11 using Conda, follow these steps:

  1. Install Miniconda or Anaconda if you haven't already.
  2. Open a terminal or command prompt.
  3. Create a new environment with Python 3.11:
     ```
     conda create -n admin_service python=3.11
     ```
  4. Activate the environment:
     ```
     conda activate admin_service
     ```
  5. Verify the Python version:
     ```
     python --version
     ```
  This should output "Python 3.11.x".

- Poetry

   For detailed instructions on how to install Poetry, please refer to the [official Poetry installation guide](https://python-poetry.org/docs/#installation).

   After installation, verify that Poetry is correctly installed by running:
   ```bash
   poetry --version
   ```

### Environment Setup

1. Install project dependencies:
   ```
   poetry install
   ```

2. Install pre-commit:
   ```
   poetry run pre-commit install
   ```

### Start Project in Dev Mode

1. Run migrations:
   ```
   python manage.py migrate
   ```

2. Create superuser:
   ```
   python manage.py createsuperuser
   ```

3. Start server:
   ```
   python manage.py runserver
   ```
