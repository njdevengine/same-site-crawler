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

link_array = []
for i in range(0,(len(my_soup)-1)):
    print(i)
    print(Find(my_soup[i]))
    link_array.append(Find(my_soup[i]))
