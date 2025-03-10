# AudioTubeTG (YouTube Audio Downloader Bot)

## About

This Telegram bot allows users to download YouTube videos and convert them to audio formats (e.g., MP3, WAV). 
Users can send a YouTube video URL to the bot, and the bot will download the audio and send it back as a file.

## Features
Download and convert YouTube videos to audio files.
Simple interaction: send a YouTube URL, and the bot sends the audio file.
Responds to /start and /help commands with a welcome message.

## Installation
Follow these steps to install and set up your bot.

### Requirements
1. Python 3.8+ (for the best experience, use a virtual environment).
2. aiogram 
3. yt-dlp 
4. ffmpeg  
5. Python dependencies (install via requirements.txt).

On Linux you can download python and ffmpeg from your package manager.

On Windows:
- [Python link](https://www.python.org/downloads/)
- [ffmpeg link](https://ffmpeg.org/download.html)

You should also add `ffmpeg` to the PATH. Add path to /bin of `ffmpeg` to PATH variable.
`pip install yt-dlp`
`pip install ffmpeg-python`

To download the program, clone it in the directory that you want.

In case of YouTube download restrictions or cookie issues, this script uses Firefox cookies. 
You must have Firefox browser and sign in with it on YouTube once.