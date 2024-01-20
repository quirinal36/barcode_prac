import urllib.parse
import urllib.request

api_url = "http://127.0.0.1:8000/buddy/"

req = urllib.request.Request(api_url)
with urllib.request.urlopen(req) as response :
    the_page = response.read()
    string_data = the_page.decode('utf-8')
    print(string_data)