from fastapi import FastAPI
import random

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000"
    "https://myrepo-zulyang.vercel.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

messages = [
    "Logic will get you from A to B. Imagination will take you everywhere.",
    "There are 10 kinds of people. Those who know binary and those who don't.",
    "There are two ways of constructing a software design. One way is to make it so simple that there are obviously no deficiencies and the other is to make it so complicated that there are no obvious deficiencies.",
    "It's not that I'm so smart, it's just that I stay with problems longer.",
    "It is pitch dark. You are likely to be eaten by a grue."
]

@app.get("/api/quotes")
def quotes():
    selected_message = random.choice(messages)
    return {"message": selected_message}