from fastapi import FastAPI

app = FastAPI()
user = []

@app.get("/users")
def list_users(): return list_users

