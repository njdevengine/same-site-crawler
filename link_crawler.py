sites = ["https://yoursitesarray.com/"]
from urllib.request import Request, urlopen
my_soup = []
for i in range(0,length):
    req = Request(sites[i], headers={"user-agent" : "Mozilla/5.0"})
    webpage = urlopen(req).read()
    print(webpage)
    my_soup.append(webpage.decode("utf-8"))
    
import re 
def Find(string): 
    links = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', string) 
    return links
    
Find(my_soup[0])
