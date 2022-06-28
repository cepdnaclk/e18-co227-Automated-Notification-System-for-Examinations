import requests
   
def sendMessage(token,channel_id,message):
    url = "https://discord.com/api/v9/channels/{}/messages".format(channel_id)
      
    #set content and authorization
    data = {"content": message}
    header = {"authorization": token}
    
    #send the message using post method and store the status in variable 'r'
    r = requests.post(url,data=data,headers=header)
   
    #to check the status
    print(r)
    


