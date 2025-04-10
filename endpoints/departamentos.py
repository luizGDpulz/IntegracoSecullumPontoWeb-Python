import requests
from typing import Dict, Any
from endpoints.apiToken import APIToken

class Departamentos:
    def __init__(self, token: str, id_banco: str):
        self.url = "https://pontowebintegracaoexterna.secullum.com.br/IntegracaoExterna/Departamentos"
        self.headers = {
            "Authorization": f"Bearer {token}",
            "secullumidbancoselecionado": f"{id_banco}",
            "Accept": "application/json",
            "Content-Type": "application/x-www-form-urlencoded",
            "charset": "utf-8",
        }
        self.session = requests.Session()
        
    def get_all(self) -> Dict[str, Any]:
        try:
            response = self.session.get(
                self.url,
                headers=self.headers
            )
            response.raise_for_status()
            return response.json()
            
        except requests.exceptions.RequestException as e:
            raise Exception(f"API request failed: {str(e)}")
            
    def get_by_description(self, description: str) -> Dict[str, Any]:
        try:
            response = self.session.get(
                f"{self.url}?descricao={description}",
                headers=self.headers
            )
            response.raise_for_status()
            return response.json()
            
        except requests.exceptions.RequestException as e:
            raise Exception(f"API request failed: {str(e)}")

    def create_or_update(self, department_data: Dict[str, Any]) -> Dict[str, Any]:
        try:
            response = self.session.post(
                self.url,
                headers=self.headers,
                json=department_data
            )
            response.raise_for_status()
            return response.json()
            
        except requests.exceptions.RequestException as e:
            raise Exception(f"API request failed: {str(e)}")

    def delete_by_description(self, description: str) -> None:
        try:
            response = self.session.delete(
                f"{self.url}?descricao={description}",
                headers=self.headers
            )
            response.raise_for_status()
            
        except requests.exceptions.RequestException as e:
            raise Exception(f"API request failed: {str(e)}")