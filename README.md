#🎬 AI Automated YouTube Video Generator
#🚀 Overview

This project is an end-to-end AI video generation pipeline that automatically creates YouTube-style explainer videos from a topic input.

The system integrates:

n8n (Workflow automation)

FastAPI (Backend API)

Groq/OpenAI (Script generation)

Edge TTS (Voice synthesis)

Pexels API (Stock videos)

MoviePy (Video processing)

Whisper (Subtitle generation)

Pillow (Thumbnail generation)

FFmpeg & ImageMagick (Rendering support)

🔁 Workflow Architecture

Topic → n8n Webhook → AI Script Generation → FastAPI Backend →
Voice Generation → Pexels Video Fetch → Video Rendering →
Subtitle Generation → Thumbnail Creation → Final MP4 Output

🛠 Installation
1️⃣ Clone Repo
git clone https://github.com/your-username/ai-video-generator.git
cd ai-video-generator

2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate

3️⃣ Install Requirements
pip install -r requirements.txt

4️⃣ Install FFmpeg

Download from:
https://www.gyan.dev/ffmpeg/builds/

Add to System PATH.

5️⃣ Install ImageMagick

Download:
ImageMagick-7.x Q16 HDRI

Add to System PATH.

▶ Run Server
uvicorn python_service.app:app --reload

🧪 Test API
curl -X POST http://127.0.0.1:8000/generate-video ^
-H "Content-Type: application/json" ^
-d "{\"topic\":\"AI in Healthcare\",\"script\":\"Artificial Intelligence is transforming healthcare...\"}"

📦 Output

MP4 video

SRT subtitles

Thumbnail image

📈 Future Improvements

Auto YouTube Upload

Background music integration

Multi-language support

Better thumbnail design

GPU acceleration
