from fastapi import FastAPI, HTTPException, Query
from typing import Optional
import httpx

app = FastAPI()

@app.post("/send_message/{to}/{template_name}/")
async def send_message(to: str,template_name: str):
    access_token = "EAAFtnme63bgBO4dI02BeZBfowFGaSZAcm9sgAVmZA0IarGlnSomZAr2ZARjq3iSFZCnl6AemptVf9918XdAWa1pkuQ8t8ZCA51RrlHYcWSTe4VDF1Y9j6ZBUz7RuL2LXrK8yLdD78FMLQ64vx32ZBF7rZA87BO9tvtQ7ljlTAlqgp386BnzjjTSxwsUxr4R9ZBUPSyd"
    graph_api_url = "https://graph.facebook.com/v18.0/273242249210974/messages"

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    request_body = {
        "messaging_product": "whatsapp",
        "to": to,
        "type": "template",
        "template": {
            "name": template_name,
            "language": {
                "code": "en_US"
            }
        }
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(graph_api_url, headers=headers, json=request_body)

    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Failed to send message")

    return {"message": "Message sent successfully", "result": response.json()}
