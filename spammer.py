import sys
import pexpect
from time import sleep

sticker = '/data/data/com.termux/files/home/spammer/blinb.tgs'
chat = 'windy31chat'

tg = pexpect.spawn('telegram-cli --json --disable-output')

tg.expect('>')
tg.sendline(f'resolve_username {chat}')
print('Resolve')
tg.expect('id')
tg.sendline(f'channel_join @{chat}')
print('Join')
tg.expect('SUCCESS')
line = f'send_document @{chat} {sticker}'
tg.sendline(line)
for i in range(10000):
    try:
        tg.expect('SUCCESS', timeout=1)
        tg.sendline(line)
        print('OK')
        sleep(0.1)
    except:
        tg.sendline(line)
