FROM python:3.9-slim

# Set environment variables to minimize interactive prompts
ENV DEBIAN_FRONTEND=noninteractive

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update --fix-missing && \
    apt-get install -y --no-install-recommends \
        build-essential \
        flex \
        bison && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy the application code to the container
COPY . /app

# Run the Makefile
RUN make -C translator

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that Streamlit uses
EXPOSE 8501

# Command to run the application
CMD ["streamlit", "run", "deploy.py"]