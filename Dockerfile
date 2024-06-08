# Pull official Python Docker image
FROM python 3.12.1

# Set environment variables
ENV PYTHONDONTWRITEBYCODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /code

# Install dependencies
RUN pip install --upgrade pip
COPY requirements.txt /code/
RUN pip install -r requirements.txt

# Copy the django project
COPY . /code/