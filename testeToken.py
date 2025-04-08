from endpoints.apiToken import APIToken

if __name__ == "__main__":
    api_token = APIToken()
    try:
        token_info = api_token.get("luiz.pulz@secullum.com.br", "Sanduiche@55")
        print(token_info)
    except Exception as e:
        print(e)