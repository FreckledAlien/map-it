# import pyperclip
import webbrowser, sys
# import webbrowser, sys

sys.argv #['mapit.py', 'location']

# check if cli arguments were passed
if len(sys.argv) > 1:
	address = ' '.join(sys.argv[1:])
# else:
# 	address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)

