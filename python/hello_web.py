# -*- coding: utf-8 -*-


from urllib.parse import parse_qs


# wsgi处理函数
# @environ: 包含所有HTTP请求信息的dict对象
# @start_response: 发送HTTP响应的函数
def application(environ, start_response):
    #print(environ)
    method = environ["REQUEST_METHOD"]
    path = environ["PATH_INFO"]
    
    start_response("200 OK", [("Content-Type", "text/html")])
    
    if path == "/":
        html = """<h1>Hello, web!!</h1><a href="/signin">Sign In</a>"""
        return [html.encode("utf-8")]
    elif method == "GET" and path == "/signin":
        html = """<form action="/signin" method="post">
                  <p><input name="username"></p>
                  <p><input name="password" type="password"></p>
                  <p><button type="submit">Sign In</button></p>
                  </form>"""
        return [html.encode("utf-8")]
    elif method == "POST" and path == "/signin":
        request_body_size = int(environ.get("CONTENT_LENGTH", 0))
        request_body = environ["wsgi.input"].read(request_body_size).decode("utf-8")
        
        #print(request_body)
        
        params = parse_qs(request_body)
        
        print(params)
        
        if params["username"][0] == "admin" and params["password"][0] == "password":
           return ["Hello, admin!!!".encode("utf-8")]
        return ["Bad username or password".encode("utf-8")]


