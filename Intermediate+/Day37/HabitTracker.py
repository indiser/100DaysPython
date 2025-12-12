import requests
from datetime import datetime


pixela_end_point="https://pixe.la/v1/users"

user_params={
    "token":"sydasdvsaghghfwdfwtdfwdvghwc",
    "username":"indiser",
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}

# response=requests.post(url=pixela_end_point, json=user_params)

# print(response.text)

graph_config={
    "id":"code1",
    "name":"Daily Coding",
    "unit":"commit",
    "type":"float",
    "color":"ajisai"
}

graph_user_config={
    "X-USER-TOKEN":user_params["token"]
}

graph_endpoint=f"{pixela_end_point}/{user_params['username']}/graphs"
# response=requests.post(url=graph_endpoint,headers=graph_user_config,json=graph_config)

# print(response.text)
today=datetime.now()


my_graph_endpoint=f"{pixela_end_point}/{user_params['username']}/graphs/{graph_config['id']}"
my_graph_config={
    "date":today.strftime("%Y%m%d"),
    "quantity":"10.5",
}
# response=requests.post(url=my_graph_endpoint,headers=graph_user_config,json=my_graph_config)
# print(response.text)

update_graph_endpoint=f"{my_graph_endpoint}/{my_graph_config['date']}"

update_graph_config={
    "quantity":"6.7",
}

# response=requests.put(url=update_graph_endpoint,headers=graph_user_config,json=update_graph_config)
# print(response.text)

response=requests.delete(url=update_graph_endpoint,headers=graph_user_config)
print(response.text)