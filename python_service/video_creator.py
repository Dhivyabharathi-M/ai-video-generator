import os
import random
import requests
import edge_tts
import whisper
from moviepy.editor import *
from moviepy.video.fx.all import fadein, fadeout
from moviepy.config import change_settings
from PIL import Image, ImageDraw, ImageFont

# 🔧 Tell MoviePy where ImageMagick is
change_settings({
    "IMAGEMAGICK_BINARY": r"C:\Program Files\ImageMagick-7.1.2-Q16-HDRI\magick.exe"
})

PEXELS_API_KEY = "B59vxcb6PcWkvAsF018w1Y8rzctgTMmqHcND1ekeR5HmwaVySPO5mjf2"
OUTPUT_FOLDER = "outputs"

if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)


# 🔊 TEXT TO SPEECH
async def text_to_speech(text, output_file):
    communicate = edge_tts.Communicate(text, "en-US-AriaNeural")
    await communicate.save(output_file)


# 🎥 FETCH VIDEOS FROM PEXELS
def fetch_videos(query, count=3):
    headers = {"Authorization": PEXELS_API_KEY}
    url = f"https://api.pexels.com/videos/search?query={query}&per_page={count}"

    response = requests.get(url, headers=headers)
    data = response.json()

    video_paths = []

    for i, video in enumerate(data.get("videos", [])):
        video_url = video["video_files"][0]["link"]
        video_file = os.path.join(OUTPUT_FOLDER, f"clip_{i}.mp4")

        video_data = requests.get(video_url)
        with open(video_file, "wb") as f:
            f.write(video_data.content)

        video_paths.append(video_file)

    return video_paths


# 🎬 MAIN VIDEO CREATOR
async def create_video(topic, script):

    audio_path = os.path.join(OUTPUT_FOLDER, "voice.mp3")
    video_path = os.path.join(OUTPUT_FOLDER, f"{topic.replace(' ', '_')}.mp4")

    # 1️⃣ Generate voice
    await text_to_speech(script, audio_path)

    audio = AudioFileClip(audio_path)
    duration = audio.duration

    # 2️⃣ Fetch Pexels Clips
    video_files = fetch_videos(topic, 3)

    if not video_files:
        raise Exception("No videos found from Pexels.")

    clips = []
    clip_duration = duration / len(video_files)

    for file in video_files:
        video = VideoFileClip(file)

        max_start = max(0, video.duration - clip_duration - 1)
        start = random.uniform(0, max_start)

        clip = (
            video
            .subclip(start, start + clip_duration)
            .resize(height=720)
            .fx(fadein, 0.5)
            .fx(fadeout, 0.5)
        )

        clips.append(clip)

    background_video = concatenate_videoclips(clips, method="compose")

    # 3️⃣ Dynamic Sentence Captions
    sentences = script.split(". ")
    caption_clips = []
    start_time = 0
    sentence_duration = duration / len(sentences)

    for sentence in sentences:
        txt_clip = (
            TextClip(
                sentence.strip(),
                fontsize=42,
                color="white",
                stroke_color="black",
                stroke_width=2,
                size=(900, None),
                method="caption",
            )
            .set_position(("center", 620))
            .set_start(start_time)
            .set_duration(sentence_duration)
            .crossfadein(0.3)
            .crossfadeout(0.3)
        )

        caption_clips.append(txt_clip)
        start_time += sentence_duration

    final_video = CompositeVideoClip([background_video] + caption_clips)
    final_video = final_video.set_audio(audio)

    final_video.write_videofile(video_path, fps=24)

    # 4️⃣ Generate Subtitles
    generate_subtitles(audio_path, video_path)

    # 5️⃣ Generate Thumbnail
    generate_thumbnail(topic)

    return video_path


# 📝 SUBTITLE GENERATION (Whisper)
def generate_subtitles(audio_path, video_path):

    os.environ["PATH"] += os.pathsep + r"C:\ffmpeg-8.0.1-essentials_build\bin"

    model = whisper.load_model("base")

    result = model.transcribe(audio_path, fp16=False)

    srt_path = video_path.replace(".mp4", ".srt")

    with open(srt_path, "w", encoding="utf-8") as f:
        f.write(result["text"])


# 🖼 THUMBNAIL GENERATOR
def generate_thumbnail(title):

    img = Image.new("RGB", (1280, 720), color=(20, 20, 20))
    draw = ImageDraw.Draw(img)

    font = ImageFont.load_default()

    w, h = draw.textsize(title, font=font)

    draw.text(
        ((1280 - w) / 2, (720 - h) / 2),
        title,
        fill="yellow",
        font=font,
    )

    thumbnail_path = os.path.join(OUTPUT_FOLDER, "thumbnail.jpg")
    img.save(thumbnail_path)
