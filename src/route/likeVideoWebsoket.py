from fastapi import WebSocket
from typing import List

from main import app, get_db, oauth2_scheme

likes: List[int] = []

@app.websocket("WS/video/{video_id}/like")
async def websocket_endpoint(websocket: WebSocket, video_id: int):
   await websocket.accept()
   while True:
       data = await websocket.receive_text()
       if data == "like":
           likes.append(video_id)
           await websocket.send_text(f"Video {video_id} liked")
       elif data == "unlike":
           likes.remove(video_id)
           await websocket.send_text(f"Like removed from Video {video_id}")