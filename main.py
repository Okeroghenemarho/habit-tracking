import requests
from datetime import datetime
USERNAME = "agirlnamedmaro"
TOKEN = "myn@me1sOke"


pixela_endpoint = "https://pixe.la/v1/users"
parameter = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response = requests.post(url=pixela_endpoint, json=parameter)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": "graph1",
    "name": "Coding Graph",
    "unit": "minutes",
    "type": "int",
    "color": "shibafu"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response  = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
today = datetime.now()
date = today.strftime("%Y%m%d")
pixel_endpoint = f"{graph_endpoint}/graph1"
pixel_config = {
    "date": date,  # using formatted datetime to make the date
    "quantity": input("How many minutes did you code today? ")
}
pixel_response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
print(pixel_response.text)

# pixel_update_endpoint = f"{pixel_endpoint}/20230810"
# update_config = {
#     "quantity": "180"
# }
# response = requests.put(url=pixel_update_endpoint, json=update_config, headers=headers)
# print(response.text)