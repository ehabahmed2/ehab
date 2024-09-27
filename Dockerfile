FROM python:3.12.3

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire application code
COPY . .

# Set environment variable for Django settings module
ENV DJANGO_SETTINGS_MODULE=portfolio_mgmnt.settings

# Collect static files (if necessary)
RUN python manage.py collectstatic --noinput

# Start the application with gunicorn
CMD ["gunicorn", "portfolio_mgmnt.wsgi:application", "--bind", "0.0.0.0:8000"]
