from datetime import datetime

import requests
# ------------------------------------------
# // POST     Create your user account
GRAPH_ID = "graph4"
pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "sivaji"
TOKEN = "sjdh3u9y94fg89409rf"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",


}
#
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)
# ---------------------------------------------------------------------------

# Create a graph definition
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_params = {
    "id": "graph4",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "timezone": "IST",
    "color": "ajisai"
}
headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.put(url=graph_endpoint,json=graph_params, headers=headers)
# print(response.text)
# https://www.udemy.com/course/100-days-of-code/learn/lecture/21489872#content

# -------------------------------------------------------------------------------------

#                   Post value to the graph
graph_value_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}"
today = datetime.now()
graph_value_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many kilometers did you cycle today?"),


}

response = requests.post(url=graph_value_endpoint, json=graph_value_params, headers=headers)
print(response.text)

# ----------------------------------------------------------------------------------------
#                        Update the value in graph
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "4.8"
}

# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)
# ----------------------------------------------------------------------------------------
#                        Delete the value in graph
# DELETE
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20240128"

# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)