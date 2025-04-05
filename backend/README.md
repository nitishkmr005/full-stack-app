# README for the Backend

This is the backend part of the "Hello World" full-stack web application built using FastAPI.

## Project Structure

- `app/main.py`: The entry point for the FastAPI application.
- `app/api/routes.py`: Defines the API routes for the application.
- `app/__init__.py`: Marks the `app` directory as a Python package.
- `requirements.txt`: Lists the dependencies required for the backend.

## Getting Started

1. **Install Dependencies**: 
   Run the following command to install the required packages:
   ```
   pip install -r requirements.txt
   ```

2. **Run the Application**: 
   Use the following command to start the FastAPI server:
   ```
   uvicorn app.main:app --reload
   ```

3. **Access the API**: 
   Open your browser and navigate to `http://localhost:8000/hello` to see the "Hello, World!" message.

## API Documentation

You can access the interactive API documentation at `http://localhost:8000/docs` after running the application.