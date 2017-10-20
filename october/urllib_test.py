import urllib3

http = urllib3.PoolManager()

r = http.request('GET', 'http://www.google.com', preload_content=False)


r.

for chunk in r.stream(32):
    print(chunk)


r.release_conn()
