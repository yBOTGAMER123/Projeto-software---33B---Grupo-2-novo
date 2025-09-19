from fastapi import FastAPI
app = FastAPI(title="My API", version="1.0.0")

@app.get("/status")
def health():
    return {"status": "ok"}
