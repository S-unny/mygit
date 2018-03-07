
import requests

resp = requests.get('http://localhost:9999/echo/SYJ')
if resp.status_code == 200 and \
resp.text =='Say hello to my little friend: SYJ!':
	print('It worked')
else:
	print('got this:',resp.text)
