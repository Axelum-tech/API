name=input("Enter a domain/ip: ")

#request info
import requests
res=requests.get('http://ip-api.com/csv/'+ name)
data=res.text.split(",")
if (data[0])=='success':
    print("Info found")
    print("Location",data[1])
else:
    print("no info found")
#process info
#print info