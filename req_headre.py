import requests

#  making a get request
response = requests.get('https://www.dadabhagwan.fm/')

#  print response
print(response)

# print headers of response
print(response.headers)

'''
OUTPUT :- 

E:\PYTHON\Self_Prectice\venv\Scripts\python.exe E:\PYTHON\Self_Prectice\Ethical\req_headre.py 
<Response [200]>
{'Date': 'Mon, 07 Aug 2023 14:58:41 GMT', 'Content-Type': 'text/html', 'Transfer-Encoding': 'chunked', 'Connection': 'keep-alive', 'last-modified': 'Wed, 31 May 2023 05:39:11 GMT', 'vary': 'Accept-Encoding', 'x-powered-by': 'ASP.NET', 'access-control-allow-origin': '*', 'CF-Cache-Status': 'DYNAMIC', 'Report-To': '{"endpoints":[{"url":"https:\\/\\/a.nel.cloudflare.com\\/report\\/v3?s=yYhkkPlLpLxDqHBhvj6toXYJJcte5i6hceNUOwWLm22uUkFxQ%2Fbc6TNh7Jcr%2B9CHkYWTFJaO6RmupQSU77NA%2Fvq9PAZpE0VNbS378evDWk8mt2Vh%2FsK769XKVGVk%2FH1HxgDT9YjCMZ5H3658YbJ05J0%3D"}],"group":"cf-nel","max_age":604800}', 'NEL': '{"success_fraction":0,"report_to":"cf-nel","max_age":604800}', 'Server': 'cloudflare', 'CF-RAY': '7f3061117f40076e-MRS', 'Content-Encoding': 'gzip', 'alt-svc': 'h3=":443"; ma=86400'}

Process finished with exit code 0

'''
