import requests
from schemes.url import DeleteParams

def mock_delete(delete_params: DeleteParams):

    response = requests.post(url=delete_params.url, 
                             params=delete_params.params, )
    
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