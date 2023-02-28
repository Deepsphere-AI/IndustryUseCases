# Use the official lightweight Python image.
# https://hub.docker.com/_/python
FROM python:3.8


EXPOSE 8080

# Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

# Install production dependencies.
RUN pip install -r requirements.txt


# Timeout is set to 0 to disable the timeouts of the workers to allow Cloud Run to handle instance scaling.
CMD streamlit run --server.port 8080 --server.enableCORS false DSAI_app.py