# 🎬 AI Automated YouTube Video Generator 🚀

## 📖 Overview

This project is an **end-to-end AI video generation pipeline** that automatically creates **YouTube-style explainer videos** from a topic input.

---

## 🔧 Tech Stack & Integrations

The system integrates:

-  **n8n** – Workflow automation  
-  **FastAPI** – Backend API  
-  **Groq / OpenAI** – Script generation  
-  **Edge TTS** – Voice synthesis  
-  **Pexels API** – Stock video fetching  
-  **MoviePy** – Video processing  
-  **Whisper** – Subtitle generation  
-  **Pillow** – Thumbnail creation  
-  **FFmpeg & ImageMagick** – Rendering support  

---

## 🔁 Workflow Architecture

```
Topic
   ↓
n8n Webhook
   ↓
AI Script Generation (Groq / OpenAI)
   ↓
FastAPI Backend
   ↓
Voice Generation (Edge TTS)
   ↓
Pexels Video Fetch
   ↓
MoviePy Video Rendering
   ↓
Whisper Subtitle Generation
   ↓
Thumbnail Creation (Pillow)
   ↓
Final MP4 Output
```

---

## 🛠 Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/ai-video-generator.git
cd ai-video-generator
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install Requirements

```bash
pip install -r requirements.txt
```

### 4️⃣ Install FFmpeg

Download from:  
👉 https://www.gyan.dev/ffmpeg/builds/

Add **FFmpeg** to your **System PATH**.

---

### 5️⃣ Install ImageMagick

Download:  
👉 ImageMagick-7.x Q16 HDRI

Add **ImageMagick** to your **System PATH**

---

## ▶ Run Server

```bash
uvicorn python_service.app:app --reload
```

---

## 🧪 Test API

```bash
curl -X POST http://127.0.0.1:8000/generate-video ^
-H "Content-Type: application/json" ^
-d "{\"topic\":\"AI in Healthcare\",\"script\":\"Artificial Intelligence is transforming healthcare...\"}"
```

---

## 📦 Output

After successful execution, the system generates:

-  **MP4 Video**
-  **SRT Subtitles**
-  **Thumbnail Image**
-  Voice narration audio
-  Stock video clips merged with narration

---

## 📈 Future Improvements

-  Automatic YouTube upload  
-  Background music integration  
-  Multi-language support  
-  AI-powered thumbnail enhancement  
-  GPU acceleration for faster rendering  

---

