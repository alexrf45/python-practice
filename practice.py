import httpx

def http_get():
    r = httpx.get('https://r0land.link')
    print (r.status_code)
    print (r.headers['content-type'])
    print (r.text)


http_get()