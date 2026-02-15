from fastapi import FastAPI
from pydantic import BaseModel
from python_service.video_creator import create_video

app = FastAPI()

class VideoRequest(BaseModel):
    topic: str
    script: str

@app.post("/generate-video")
async def generate_video(data: VideoRequest):
    output_path = await create_video(data.topic, data.script)
    return {
        "status": "success",
        "video_path": output_path
    }
