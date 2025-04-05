# Full-Stack Hello World Application

A simple full-stack web application built with React (frontend) and FastAPI (backend) that demonstrates basic client-server communication.

## Prerequisites

Before you begin, ensure you have the following installed:
- Node.js (v16 or higher) - JavaScript runtime environment
  ```bash
  # Check Node.js version
  node --version
  
  # Install Node.js from: https://nodejs.org/
  ```
- Python (v3.8 or higher) - Backend programming language
  ```bash
  # Check Python version
  python --version
  
  # Install Python from: https://www.python.org/downloads/
  ```
- npm (comes with Node.js) - Node.js package manager
  ```bash
  # Check npm version
  npm --version
  ```
- pip (Python package manager)
  ```bash
  # Check pip version
  pip --version
  ```

## Installation Guide

### Installing Node.js

1. **Windows Installation:**
   - Download the Windows Installer (.msi) from https://nodejs.org/
   - Choose LTS (Long Term Support) version
   - Run the installer and follow the installation wizard
   - Verify installation:
     ```bash
     node --version
     npm --version
     ```

2. **macOS Installation:**
   - Using Homebrew:
     ```bash
     brew install node
     ```
   - Or download macOS Installer (.pkg) from https://nodejs.org/
   
3. **Linux Installation:**
   - Ubuntu/Debian:
     ```bash
     curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
     sudo apt-get install -y nodejs
     ```
   - Fedora:
     ```bash
     sudo dnf install nodejs
     ```

## Understanding the Components

### What is Vite?
Vite is a modern frontend build tool that offers:
- Lightning-fast development server
- Hot Module Replacement (HMR)
- Optimized production builds
- Built-in support for React and TypeScript
- No configuration needed to start

### Frontend Architecture
The React frontend is structured as follows:

1. **Entry Point Flow:**
   ```
   index.html → src/main.jsx → src/App.jsx → components/*
   ```
   - `index.html`: Contains the root div where React mounts
   - `main.jsx`: Initializes React and renders the App component
   - `App.jsx`: Main component that structures the application
   - `components/`: Reusable UI components

2. **Key Files Explained:**
   - `package.json`: Project configuration
     - Defines dependencies
     - Contains scripts for development/build
     - Specifies project metadata
   
   - `vite.config.js`: Vite configuration
     - Configures development server
     - Sets up build options
     - Defines plugins and port settings

   - `src/components/HelloWorld.jsx`: Example component
     - Demonstrates component structure
     - Shows API interaction with backend

### Backend Architecture
The FastAPI backend follows this structure:

1. **Entry Point Flow:**
   ```
   uvicorn → app/main.py → app/api/routes.py
   ```
   - `uvicorn`: ASGI server that runs the application
   - `main.py`: Configures and starts FastAPI
   - `routes.py`: Defines API endpoints

2. **Key Files Explained:**
   - `requirements.txt`: Python dependencies
   - `app/__init__.py`: Makes the directory a Python package
   - `app/main.py`: Application configuration and startup
   - `app/api/routes.py`: API endpoint definitions

## Detailed Setup Instructions

### Backend Setup

1. **Create and activate virtual environment:**
   ```bash
   # Windows
   python -m venv venv
   .\venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

2. **Install dependencies:**
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

3. **Start the server:**
   ```bash
   uvicorn app.main:app --reload
   ```

### Frontend Setup

1. **Install dependencies:**
   ```bash
   cd frontend
   npm install
   ```

2. **Start development server:**
   ```bash
   npm run dev
   ```

## Application Flow

1. **Frontend to Backend Communication:**
   ```
   Browser → React Component → API Call → FastAPI Endpoint → Database (if any) → Response
   ```

2. **Development Workflow:**
   - Frontend changes hot-reload automatically
   - Backend changes reload with uvicorn
   - API calls are proxied through Vite's dev server

## File-by-File Execution Flow

### Frontend
1. **index.html**
   ```html
   <!-- Provides the mounting point for React -->
   <div id="root"></div>
   ```

2. **main.jsx**
   ```jsx
   // Initializes React and renders App
   ReactDOM.createRoot(document.getElementById('root')).render(<App />)
   ```

3. **App.jsx**
   ```jsx
   // Main component structure
   function App() {
     return <HelloWorld />
   }
   ```

4. **HelloWorld.jsx**
   ```jsx
   // Example component with API interaction
   function HelloWorld() {
     // API calls and rendering logic
   }
   ```

### Backend
1. **main.py**
   ```python
   # Configures FastAPI application
   app = FastAPI()
   # Sets up CORS, middleware, etc.
   ```

2. **routes.py**
   ```python
   # Defines API endpoints
   @app.get("/hello")
   def hello_world():
       return {"message": "Hello, World!"}
   ```

## Development Tips

1. **Hot Reloading:**
   - Frontend: Changes reflect immediately
   - Backend: Server reloads on file changes

2. **Debugging:**
   - Frontend: Use browser DevTools
   - Backend: FastAPI automatic docs at `/docs`

3. **Common Issues:**
   - Port conflicts: Change in vite.config.js
   - CORS errors: Check backend configuration
   - Module not found: Verify installations

## Production Considerations

1. **Building Frontend:**
   ```bash
   npm run build
   ```
   Creates optimized files in `dist/`

2. **Deploying Backend:**
   ```bash
   uvicorn app.main:app
   ```
   Run without `--reload` in production

## API Documentation
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`
- OpenAPI JSON: `http://localhost:8000/openapi.json`

## Support and Resources
- React Docs: https://react.dev
- FastAPI Docs: https://fastapi.tiangolo.com
- Vite Docs: https://vitejs.dev

## Minimal Project Structure