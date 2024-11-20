
                # Use the official Python image from the Docker Hub
                FROM python:3.11-slim

                # Set the working directory in the container
                WORKDIR /app

                # Copy the requirements file into the container
                COPY requirements.txt .

                # Install the dependencies
                RUN pip install --no-cache-dir -r requirements.txt

                # Copy the rest of the application code into the container
                COPY . .

                # Expose the port that Streamlit will run on
                EXPOSE 8000

                # Add execute permissions to the entrypoint script
                RUN chmod +x entrypoint.sh

                # Specify the entrypoint script
                ENTRYPOINT ["./entrypoint.sh"]
                