from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Language Translator API is running"}
