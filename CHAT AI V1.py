import requests,json,rich,os; from rich import print; from rich.panel import Panel as pa; from rich.prompt import Prompt as NERO;from termcolor import colored; from rich.console import Console
#D4rkCiperX ♕
def NERO_SIN():
	
	co = Console()
	while True:
		print(' [bold red][underline]ChatGpt V1 BY D4rkCipherX ♕')
		print('[blue]⌯'*14)
		nn = NERO.ask(' [bold green]Enter anything ')
		print('\n'*2)
		
		url = "https://api.binjie.fun/api/generateStream"
		
		payload = json.dumps({
		  "prompt": nn,
		  #"userId": "#/ct/172
		  "network": True,
		  "system": "",
		  "withoutContext": False,
		  "stream": False
		})
		
		headers = {
		  'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/26.0 Chrome/122.0.0.0 Mobile Safari/537.36",
		  #'Accept': "apn, */*",
		  'Content-Type': "application/json",
		  'sec-ch-ua': "\"Chromium\";v=\"122\", \"Not(A:Brand\";v=\"24\", \"Samsung Internet\";v=\"26.0\"",
		  'sec-ch-ua-mobile': "?1",
		  'sec-ch-ua-platform': "\"Android\"",
		  'origin': "https://chat18.aichatos8.com",
		  'sec-fetch-site': "cross-site",
		  'sec-fetch-mode': "cors",
		  'sec-fetch-dest': "empty",
		  'referer': "https://chat18.aichatos8.com/",
		  'accept-language': "ar-IQ,ar-AE;q=0.9,ar;q=0.8,en-AU;q=0.7,en;q=0.6,en-US;q=0.5"
		}
		
		response = requests.post(url, data=payload, headers=headers)
		os.system('clear')
		co.print(pa(response.content.decode('utf-8'),title='⌯ ANSWER ⌯',style='bold yellow',border_style='bold cyan'))
		print('\n'*2)

NERO_SIN()