import requests
   
def sendMessage(token,channel_id,message):
    url = "https://discord.com/api/v9/channels/{}/messages".format(channel_id)
    data = {"content": message}
    header = {"authorization": token}
    r = requests.post(url,data=data,headers=header)
    print(r)
    


