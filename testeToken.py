from endpoints.apiToken import APIToken

if __name__ == "__main__":
    api_token = APIToken()
    try:
        token_info = api_token.get("teste@api.com", "api@123")
        print(token_info)
    except Exception as e:
        print(e)