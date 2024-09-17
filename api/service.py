import os
import requests
from dotenv import load_dotenv


load_dotenv()


class Auth:

    def __init__(self):
        self.__base_url = os.environ['BASE_URL']
        self.__auth_url = f'{self.__base_url}api/v1/authentication/token/'

    def get_token(self, username, password):
        auth_payload = {
            'username': username,
            'password': password
        }
        
        # realizar request
        auth_response = requests.post(
            self.__auth_url,
            data=auth_payload
        )
        
        # verificar response
        if auth_response.status_code == 200:
            return auth_response.json()
        return {'error': f'Erro ao atenticar. Status code: {auth_response.status_code}'}