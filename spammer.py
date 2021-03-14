import pexpect
from time import sleep

sticker = 'blinb.webp'
chat = 'cubecatinprog'

tg = pexpect.spawn('telegram-cli --json --disable-output')

tg.expect('>')
tg.sendline(f'resolve_username {chat}')
tg.expect('>')
tg.sendline(f'channel_join @{chat}')

line = f'send_document @{chat} {sticker}'
tg.expect('>')
tg.sendline(line)
while True:
    try:
        tg.expect('SUCCESS', timeout=1)
        tg.sendline(line)
        print('OK')
    except:
        tg.sendline(line)