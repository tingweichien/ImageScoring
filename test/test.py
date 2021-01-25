import requests
client_id = "FrUZcCiLsmTZEM1rJbjvmtQh"
client_secret = "XEIEFK9xB3V4dajy4AtT0hXyxMY7dn2LymiSmWkaXrAj6lFG"

with open("C:/Users/Admin/Desktop/生態/gradonfly_2.jpg", 'rb') as image:
    data = {'data': image}
    authorization = (client_id, client_secret)
    quality_ugc = requests.post('https://api.everypixel.com/v1/quality_ugc', files=data, auth=authorization).json()
    print(quality_ugc)
