# Use an official Python runtime as a parent image
FROM python:3.10

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE worker_visit_task.settings

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Expose the port the app runs on
EXPOSE 8000

WORKDIR /app/worker_visit_task
RUN python manage.py makemigrations
RUN python manage.py migrate

# Run the command to start the app
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
