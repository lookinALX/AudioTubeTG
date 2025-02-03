import yt_dlp
import shutil
import asyncio
import sys
import os


class YouTubeToAudio:
    def __init__(self):
        self.ydl_opts_wav = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'wav',
            }],
            'outtmpl': '%(title)s.%(ext)s',  # Save with the video title as the name
        }

        self.ydl_opts_mp3 = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
            }],
            'outtmpl': '%(title)s.%(ext)s',  # Save with the video title as the name
        }

    async def download(self, url, codec='mp3'):
        """
        Downloads audio from the given YouTube Url and converts it to a mp3 file.
        """
        if codec == 'wav':
            ydl_opts = self.ydl_opts_wav
        else:
            ydl_opts = self.ydl_opts_mp3

        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, self._download, url, ydl_opts, codec)

    def _download(self, url, ydl_opts, codec):
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                file_title = info.get('title', 'output')  # Get video title for naming
                ydl.download([url])

            input_file = f"{file_title}.{codec}"
            if os.path.exists(input_file):
                current_folder = os.getcwd()
                source_path = os.path.join(current_folder, input_file)
                destination_folder = os.path.join(current_folder, "downloads")
                self.move_file(source_path, destination_folder)
                return os.path.join(destination_folder, input_file)

        except Exception as e:
            print(f"An error occurred: {e}")

    async def run(self):
        """
        Entry point for the script. Handles user input.
        """
        args = sys.argv[1:]
        if len(args) > 1:
            print("Too many arguments.")
            print("Usage: python youtubetowav.py <optional link>")
            print("If a link is given, it will automatically convert it to .wav. Otherwise, a prompt will be shown.")
            return

        url = args[0] if args else input("Enter YouTube URL: ")
        await self.download(url)

    @staticmethod
    def move_file(source_path, destination_folder):
        """
            Moves a file to another folder, creating the folder if it doesn't exist.

            :param source_path: Full path of the file to move.
            :param destination_folder: Folder to move the file into.
        """
        try:
            # Check if the source file exists
            if not os.path.exists(source_path):
                print(f"Source file does not exist: {source_path}")
                return

            # Ensure the destination folder exists
            os.makedirs(destination_folder, exist_ok=True)

            # Get the file name from the source path
            file_name = os.path.basename(source_path)

            # Create the destination path
            destination_path = os.path.join(destination_folder, file_name)

            # Move the file
            shutil.move(source_path, destination_path)
            print(f"File successfully moved to: {destination_path}")

        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    converter = YouTubeToAudio()
    asyncio.run(converter.run())
