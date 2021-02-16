import requests
from bs4 import BeautifulSoup
import random
import time
import re
import sys
import logging
import addurl

text = 'python'
starturl = "https://www.google.com/search?q=%22" 
company = "amazon"
midurl = "+site:linkedin.com/in/&rlz=1C1CHBF_enUS910US910&sxsrf=ALeKk01C2Wv5f7khyihsT6H9OXbSSrLl1g:1613001093372&ei=hXEkYM6VFoCl5NoPpPe6uAs&start="
pagenum = 0
endurl = "&sa=N&ved=2ahUKEwiO7MSpweDuAhWAElkFHaS7DrcQ8NMDegQIERBI&biw=1536&bih=666&dpr=1.25"
A = ("Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
       "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36",
       "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
       )
 
Agent = A[random.randrange(len(A))]

#Pulls the first 50 pages (Which is where google caps your search results)
def scrape(company, pagenum):
    while(pagenum<50): 
        headers = {'user-agent': Agent}
        r = requests.get(starturl +company + midurl +str(pagenum*10)+endurl, headers=headers)
 
        soup = BeautifulSoup(r.text, 'html.parser')
        print("Page: " + str(pagenum+1))
        m = ""
        for info in soup.find_all('a'):
            contact = re.search("https:\/\/www.linkedin.com\/in\/([^&]*)", info.get('href'))
            if contact != None:
                print(contact)
                #FOR THE DATABASE ADDITION (Not yet implemented)
                #addurl(contact.string)
        #Sleeping for a second before switching pages should prevent google from flagging the searches as unusual activity
        time.sleep(1)
        pagenum+=1


if __name__ == '__main__':
    if len(sys.argv) > 1:
        company = sys.argv[1]
        logging.info("Company is {}".format(company))
    else:
        print("Whoops, we need you to put in a company to search for!")
    scrape(company, pagenum)

