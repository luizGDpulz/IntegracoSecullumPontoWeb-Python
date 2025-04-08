import requests
from typing import Dict, Any

class APIToken:
    def __init__(self):
        self.url = "https://autenticador.secullum.com.br/Token"
        self.headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "application/json",
            "charset": "utf-8",
        }
        self.session = requests.Session()
        
    def get(self, username: str, password: str) -> Dict[str, Any]:
        try:
            data = {
                "grant_type": "password",
                "username": username,
                "password": password,
                "client_id": "3"
            }
            
            response = self.session.post(
                self.url,
                headers=self.headers,
                data=data
            )
            response.raise_for_status()
            return response.json()
            
        except requests.exceptions.RequestException as e:
            raise Exception(f"API request failed: {str(e)}")