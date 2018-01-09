import requests
from bs4 import BeautifulSoup

s = requests.session()
response = s.get('https://portal.seniorsolution.com.br/portal/index.php')

soup = BeautifulSoup(response.text)
for n in soup('input'):
    if n['name'] == '_csrf_token':
        token = n['value']
        break


auth = {
    'username': 'bruno.alves'
    , 'passwd': 'S0ngaM0nga'
    , 'ja1e1101d31a28b31246b34a12ee9f157': '1'
    ,'option':'login'
    ,'op2': 'login'
    ,'force_session': '1'
}

s.post('https://portal.seniorsolution.com.br/portal/index.php', data=auth)

response = s.get('https://portal.seniorsolution.com.br/portal/portal.php/rh/ponto/browse')

print(element)


# if __name__ == '__main__':
#     hunt()

<input type="hidden" name="force_session" value="1">