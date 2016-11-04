#! python3
# mapIt.py - Launches a map in the browser using an address from the
# command line or clipboard.
import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
	# Get address from command line
	print(sys.argv)
	address = " ".join(sys.argv[1:])
	print(address)
else:
	print("no args given")
	address = pyperclip.paste()

# webbrowser.open("http://inventwithpython.com/")
webbrowser.open("https://www.google.com/maps/place/"+address)
