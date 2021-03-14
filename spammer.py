import sys
import pexpect
from time import sleep

sticker = '/data/data/com.termux/files/home/spammer/blinb.tgs'
chat = 'cubecatinprog'

tg = pexpect.spawn('telegram-cli --json --disable-output')

tg.expect('>')
tg.sendline(f'resolve_username {chat}')
print('Resolve')
tg.expect('>')
tg.sendline(f'channel_join @{chat}')
print('Join')
tg.expect('>')
tg.sendline(f'contact_search {chat}')
tg.expect('>')
tg.sendline('contact_list')
line = f'send_document @{chat} {sticker}'
tg.expect('>')
tg.sendline(line)
while True:
    try:
        tg.expect('>', timeout=1)
        tg.sendline(line)
        print('OK')
        sleep(0.1)
    except:
        tg.interact()
