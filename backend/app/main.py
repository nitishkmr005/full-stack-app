# cd hello-world-fullstack/backend && pip install -r requirements.txt

# Now let's start the backend server:
# uvicorn app.main:app --reload

# et's start the frontend server. First, we need to install the frontend dependencies and then start the development server:
# cd ../frontend && npm install
# npm run dev

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}