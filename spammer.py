import sys
import pexpect
from time import sleep
import os
from random import randint

dir = '/data/data/com.termux/files/home/spammer'

video = os.listdir(f'{dir}/video')
image = os.listdir(f'{dir}/image')
sticker = f'{dir}/blinb.tgs'

type_spam = 'image'

chat = 'cubecatinprog'

tg = pexpect.spawn('telegram-cli --json --disable-output')

tg.expect('>')
tg.sendline(f'resolve_username {chat}')
print('Resolve')
tg.expect('id')
tg.sendline(f'channel_join @{chat}')
print('Join')
tg.expect('SUCCESS')
if type_spam == 'sticker':
    line = f'send_document @{chat} {sticker}'
    def spam():
        tg.sendline(line)
elif type_spam == 'video':
    line = f'send_video @{chat} %s'
    def spam():
        tg.sendline(line % f'{dir}/video/{video[randint(0, len(video)-1)]}')
elif type_spam == 'image':
    line = f'send_photo @{chat} %s'
    def spam():
        tg.sendline(line % f'{dir}/image/{video[randint(0, len(video)-1)]}')
for i in range(10000):
    try:
        tg.expect('SUCCESS', timeout=1)
        spam()
        print('OK')
        sleep(0.1)
    except:
        spam()
