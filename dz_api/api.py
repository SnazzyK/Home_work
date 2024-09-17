import requests
url = "https://api.spacexdata.com/v3/landpads"
response = requests.get(url)
lanpad = response.json()

list_name=[]
for value in lanpad:
    if value["status"]=='active':
        list_name.append(value['full_name'])
print(list_name)




