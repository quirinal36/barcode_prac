import urllib.parse
import urllib.request
import xml.etree.ElementTree as elemTree 

secret_key = "N2MuvoyktD4Y9l8V2Mn8EaZctLDNoFbUNUlGeDFGWxPTRUIX1IRS37TE2jXjkwPWh73bq1oLv%2BmPJojowmQZSg%3D%3D"
numOfRows = 10
pageNo = 1
base_date = "20240120"
base_time = "0800"
nx = 61
ny = 89
api_url = f"http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst?ServiceKey={secret_key}&numOfRows={numOfRows}&pageNo={pageNo}&base_date={base_date}&base_time={base_time}&nx={nx}&ny={ny}"

print(api_url)
req = urllib.request.Request(api_url)
with urllib.request.urlopen(req) as response :
    the_page = response.read()
    string_data = the_page.decode('utf-8')
    root = elemTree.fromstring(string_data)
    
    body = root.find("body")
    items = body.find("items")
    print(f"items length: {len(items)}")
    for item in items:
        print(f"category: {item.find('category').text}, fcstValue:{item.find('fcstValue').text}")
 