import requests

url = 'https://www.lider.cl'    

page = requests.get(url)
#html_bytes = page.read()
#html = html_bytes.decode("utf-8")

print(page.text)
