import requests
api_url = "http://site.api.espn.com/apis/site/v2/sports/football/college-football/rankings"
response = requests.get(api_url)
print(response.status_code)


#clear
# response.headers

print(response.json())