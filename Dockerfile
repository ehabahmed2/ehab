FROM python:3.12.3

# Set the working directory
WORKDIR /portfolio_mgmnt

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Run the application
CMD ["gunicorn", "portfolio_mgmnt.wsgi:application", "--bind", "0.0.0.0:8000"]
