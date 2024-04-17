from fastapi import FastAPI, HTTPException, Query
from typing import Optional
import httpx
from pywa import WhatsApp
from pywa.types import Message, Button

app = FastAPI()

wa = WhatsApp(
    phone_id='273242249210974',
    token='EAAFtnme63bgBO4dI02BeZBfowFGaSZAcm9sgAVmZA0IarGlnSomZAr2ZARjq3iSFZCnl6AemptVf9918XdAWa1pkuQ8t8ZCA51RrlHYcWSTe4VDF1Y9j6ZBUz7RuL2LXrK8yLdD78FMLQ64vx32ZBF7rZA87BO9tvtQ7ljlTAlqgp386BnzjjTSxwsUxr4R9ZBUPSyd',
    server=app,
    verify_token='hvjchsdjc'

)

@app.post("/send_message/{to}/")
async def send_message(to: str):  
    data = {to:{"Pets":["Tommy","Charlie","Cooper"]}}
    if isinstance(to, str) and len(to) > 0:
        pets = data.get(to, {}).get("Pets", [])
        buttons = [Button(pet, callback_data=pet.lower()) for pet in pets]

        wa.send_message(
            to=to,
            text="Choose a pet to book the service",
            buttons=buttons,
        )
    return {"message": "Message sent successfully"}

@app.post("/slot/{to}/")
async def send_message(to: str): 
    data = {to:{"Pets":["Morning","Afternoon","Evening"]}} 
    if isinstance(to, str) and len(to) > 0:
        pets = data.get(to, {}).get("Pets", [])
        buttons = [Button(pet, callback_data=pet.lower()) for pet in pets]

        wa.send_message(
            to=to,
            text="Choose a slot to book the service",
            buttons=buttons,
        )
    return {"message": "Message sent successfully"}
