import requests

# making a get requests
# response = requests.get('https://www.dadabhagwan.fm')
response = requests.get('https://www.dadabhagwan.fm') #  internet must needed


# print requests object
print(response.url)

# print status code
print(response.status_code)

'''
otuput :-

E:\PYTHON\Self_Prectice\venv\Scripts\python.exe E:\PYTHON\Self_Prectice\Ethical\request.py 
https://www.dadabhagwan.fm/
200

Process finished with exit code 0


'''