# requests 笔记

requests 是一个功能强大且易于使用的 Python 库，用于发送 HTTP 请求。它简化了与 Web 服务的交互，支持多种 HTTP 方法（如 GET、POST、PUT、DELETE 等），并提供了丰富的功能来处理请求和响应，广泛应用于 Web 爬虫、API 调用、自动化测试等场景。


## 发送请求

requests 最基本的请求函数是：

- `requests.request(method, url, **kwargs)` 发送 HTTP 请求，`method` 为请求方法，`url` 为请求 URL，`kwargs` 为其他参数
    - `method` 支持 GET、POST、PUT、DELETE、HEAD、OPTIONS 等方法，可以直接使用字符串
    - `params` URL 查询参数，可以是字典、元组列表或字符串
    - `data` 请求正文，可以是字典、元组列表、字符串或文件对象
    - `json` JSON 数据，会自动序列化为 JSON 字符串
    - `headers` 请求头，可以是字典
    - `cookies` Cookie，可以是字典或 CookieJar 对象
    - `files` 上传文件，可以是字典
    - `auth` 认证信息，可以是元组或 Auth 对象
    - `timeout` 超时时间
    - `allow_redirects` 是否允许重定向
    - `proxies` 代理服务器
    - `verify` 是否验证 SSL 证书
    - `stream` 是否使用流式下载
    - `cert` 客户端证书

requests 还提供了一系列函数，用于发送常见的 HTTP 请求：

- `requests.get(url, params=None, **kwargs)` 发送 GET 请求
- `requests.post(url, data=None, json=None, **kwargs)` 发送 POST 请求
- `requests.put(url, data=None, **kwargs)` 发送 PUT 请求
- `requests.delete(url, **kwargs)` 发送 DELETE 请求
- `requests.head(url, **kwargs)` 发送 HEAD 请求
- `requests.options(url, **kwargs)` 发送 OPTIONS 请求
- `requests.patch(url, data=None, **kwargs)` 发送 PATCH 请求



## 处理响应

requests 支持多种响应内容的处理方式：

- `response.status_code` 响应状态码
- `response.headers` 响应头
- `response.text` 响应正文，自动解码为 Unicode 字符串
- `response.content` 响应正文，二进制格式
- `response.json()` 响应正文，JSON 格式
- `response.cookies` 响应中的 Cookie
- `response.raw` 原始套接字响应
- `response.url` 最终 URL
- `response.history` 重定向历史
- `response.request` 请求对象
- `response.elapsed` 请求耗时
- `response.close()` 关闭响应
- `response.raise_for_status()` 如果响应状态码不是 200，抛出异常



## 会话对象

requests 提供了 `requests.Session` 类，用于创建会话对象，可以在多个请求之间保持 Cookie、身份验证等信息。下面是它的一个使用示例：

```python
import requests

session = requests.Session()
session.auth = ('user', 'pass')
session.headers.update({'x-test': 'true'})
session.cookies.set('test', 'true', domain='httpbin.org', path='/')

response = session.get('http://httpbin.org/get')
print(response.json())
```
