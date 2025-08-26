# 1. Start with a solid foundation
FROM python:3.10

# 2. Set up the workspace inside the container
WORKDIR /app

# 3. Copy dependencies list and install them (Optimization)
COPY requirements.txt .
RUN pip install -r requirements.txt

# 4. Copy the application code
COPY . .

# 5. Document the application's port
EXPOSE 5000

# 6. Define the startup command
CMD ["flask", "run", "--host=0.0.0.0"]
