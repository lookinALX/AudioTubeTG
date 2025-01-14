import re
from aiogram import Bot, Dispatcher, Router, types
from aiogram.methods.send_audio import SendAudio
from aiogram.filters import Command
from src.scripts import y2audio


class TelegramBot:
    def __init__(self, token: str):
        """
        Initialize the bot with its token and set up the dispatcher and router.
        """
        self.token = token
        self.bot = Bot(token=self.token)
        self.dp = Dispatcher()
        self.router = Router()

        # Register handlers
        self._register_handlers()

    def _register_handlers(self):
        """
        Register bot command and message handlers.
        """

        @self.router.message(Command(commands=["start", "help"]))
        async def send_welcome(message: types.Message):
            """
            Handler for /start and /help commands.
            """
            await message.reply("Hi! I'm your bot.\nUse /start or /help to see this message.")

        @self.router.message()
        async def download_request_message(message: types.Message):
            """
            Download request message sent to the bot.
            """
            if self.is_youtube_link(message.text):
                url = message.text
                await message.reply("I'll download your video. When the process is complete, "
                                    "I'll send you an audio file")
                converter = y2audio.YouTubeToAudio()
                file_path = converter.download(url)
                print(file_path)
                try:
                    file = types.FSInputFile(file_path)
                    await self.bot.send_audio(message.chat.id, file)
                except Exception as e:
                    await message.reply(f"Failed to send file: {e}")
            else:
                await message.reply("It's not a youtube link. Please send a correct url")

    @staticmethod
    def is_youtube_link(url):
        pattern = (r'(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/('
                   r'watch\?v=|embed\/|v\/|e\/|.+\/videos\/)([A-Za-z0-9_-]{11})')
        return bool(re.match(pattern, url))

    async def run(self):
        """
        Run the bot using asyncio.
        """
        self.dp.include_router(self.router)

        # Delete any pending updates and start polling
        await self.bot.delete_webhook(drop_pending_updates=True)
        await self.dp.start_polling(self.bot)
