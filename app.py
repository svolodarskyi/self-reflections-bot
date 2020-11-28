from telethon import TelegramClient, events, sync, Button
from telethon.tl.types import InputPeerChat
import aiocron
from dotenv import load_dotenv
import os

import quotes
import to_dropbox

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN_')
API_ID = os.getenv('API_ID')
API_HASH = os.getenv('API_HASH')

bot = TelegramClient('self_reflect_bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

time = '22 12 * * *'

@bot.on(events.NewMessage(pattern='/start'))
async def start(event):
    """Send a message when the command /start is issued."""
    await event.respond('Right now the reminder is set to 8:00 pm')
    raise events.StopPropagation
 
@bot.on(events.NewMessage(pattern="Yup"))
@bot.on(events.NewMessage(pattern="/doit"))
async def reflect(event):

    questions = [
                    'Lesson of the day?',
                    'One thing I want to change?'
                    'Am I getting closer to my goals?',
                ]

    answers = []

    async with bot.conversation(event.chat_id) as conv:

        for i in range(3):
            await conv.send_message(questions[i])
            answers[i] = (await conv.get_response()).raw_text

        await conv.send_message('Well done!')
        await conv.send_message(f'Quote of the day: \n{quotes.get_quote()}')

        to_dropbox.upload_note(questions, answers)

@aiocron.crontab(time)
async def attime():

    entity = await bot.get_entity(349435141)

    await bot.send_message(entity, 'Hey there! Time for self-reflections.', buttons=[
                Button.text('Yup', resize=True, single_use=True),
                Button.text('Nah', resize=True, single_use=True)
            ])

def main():
    
    """Start the bot."""
    bot.run_until_disconnected()

if __name__ == '__main__':
    main()

