import requests
from schemes.url import PostParams

def mock_post(post_params: PostParams):
    '''
    test url:
        http://127.0.0.1:8000/test/post/
        https://httpbin.org/post
    '''
    # response = requests.post(url=post_params.url, 
    #                          params=post_params.params, 
    #                          # data={'b': '456'}, 
    #                          headers=post_params.headers)
    # print("post_params", post_params)
    # print("body type", type(post_params.body))
    # print("body", post_params.body)
    # print(response.content)
    # print("1 post_params", post_params)

    # data = {'url': 'https://t.hk', 'headers': {}, 'params': {}}
    # data2 = {'post_params': {'url': 'https://t.hk', 'headers': {}, 'params': {}, 'data': {}}}
    # data3 = {'url': 'https://t.hk', 'headers': {}, 'params': {}, 'data': {}}
    # resp2 = requests.post("http://127.0.0.1:8000/test/post/", json=data3)
    # print("resp2:", resp2.content)

    response = requests.post(url=post_params.url, 
                             params=post_params.params, 
                             json=post_params.data,
                             headers=post_params.headers)
    
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