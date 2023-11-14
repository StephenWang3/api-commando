import requests
from schemes.url import PutParams

def mock_put(put_params: PutParams):


    response = requests.post(url=put_params.url, 
                             params=put_params.params, 
                             json=put_params.data,
                             headers=put_params.headers)
    
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