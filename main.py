

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()




# Allow all origins, methods, and headers for testing purposes.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/")
def first():
    return {"hello": "world"}
