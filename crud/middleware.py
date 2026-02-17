import time 

def request_timing_middleware(get_response):
    def middleware(request):
        start = time.time()
        res = get_response(request)
        duration = time.time() -start
        print(f"{request.path} took {duration} to complete with status {res.status_code}")
        return res
    return middleware