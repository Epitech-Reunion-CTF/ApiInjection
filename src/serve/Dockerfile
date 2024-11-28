FROM python:3.9-slim

# Create and use www-data user

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY . .

# Ensure the app script has the correct permissions
RUN chmod 755 /app/serve.py

# Change ownership of the /app folder to www-data for read-only access
RUN chown -R www-data:www-data /app

RUN touch /home/flag.txt
RUN echo "epictf{Y0u_W1ll_L0v3_CUrL}" > /home/flag.txt

# Expose the port the app runs on
EXPOSE 5000

# Switch to the www-data user
USER www-data

# Define the command to run the application
CMD ["python3", "/app/serve.py"]
