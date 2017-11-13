#! python3.5
# Password locker - An Insecure password locker program
import sys, pyperclip

PASSWORDS = {
    'email': 'PASSWORD',
    'facebook': 'PASSWORD',
    'twitter': 'PASSWORD'
}

if len(sys.argv) < 2:
    print('Usage: python test.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard')
else:
    print('No account named ' + account)
