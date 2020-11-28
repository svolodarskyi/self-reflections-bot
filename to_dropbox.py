import dropbox
import time
from dotenv import load_dotenv
import os

load_dotenv()

DROPBOX_ACCESS_TOKEN = os.getenv('DROPBOX_ACCESS_TOKEN')
dbx = dropbox.Dropbox(DROPBOX_ACCESS_TOKEN)

def upload_note(questions, answers):

    note = ''

    for quest, answ in zip(questions,answers):
        note = note + quest +'\n'+ answ +'\n'+'\n'

    name = time.strftime('%Y-%m-%d-%H-%M-%S')

    dbx.files_upload(note.encode('utf-8'), f'/notes/{name}.txt')

