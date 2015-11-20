import requests

class account:
    def __init__(self,username,password):
        self.username = username
        self.password = password

    def getsessionid(self):
        s = requests.session()
        s.get('https://scratch.mit.edu/')
        print(s.headers)

        headers = {
            'scratchlanguage': 'en',
            'X-CSRFToken': self.csrf,
            'X-Requested-With': 'XMLHttpRequest',
            'referer': 'https://scratch.mit.edu'
        }
        cookies = {
            'scratchcsrftoken': self.csrf,
        }
        payload = {
            'username': self.username,
            'password': self.password
        }

        s.post('https://scratch.mit.edu/login/', data=payload, headers=headers, cookies=cookies)

        print(s.headers)
        for i in s.cookies:
            print(i.name,i.value)

        cookies = s.cookies
