import requests
from schemes.url import GetParams

def mock_get(get_params: GetParams):
    response = requests.get(get_params.url, get_params.params)

    content = response.content
    headers = response.headers
    cookies = response.cookies
    status_code = response.status_code

    response.close()
    
    return {"content": content,
            "headers": headers,
            "cookies": cookies,
            "status_code": status_code
            }