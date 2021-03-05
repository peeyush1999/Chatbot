from googlesearch import search
import requests
import bs4
import webbrowser
from bs4 import BeautifulSoup
import re

class Travis:
    def fetch_data(self,url):
        headers = {'User-Agent': 'Mozilla/5.0'}
        res=requests.get(url,headers=headers)
        return BeautifulSoup(res.content, 'html5lib')

    def google(self,query):
        result_link=[]
        for j in search(query, num=1, stop=1): 
            result_link.append(j)

        url=result_link[0];
        return url

    def tell_me_about(self,location):
        query="holidify "+location
        url=self.google(query)
        soup =self.fetch_data(url)
        text=soup.find('div',attrs={'class':'readMoreText'})
        st = text.text
        st = st.replace('\xa0','').replace('\n        ','').split('.')
        speech = ""
        i=0
        while(len(speech) < 200):
            speech = speech + st[i]
            i+=1
        
        print(speech)

        return speech

    def places_to_visit(self,location):
        query="holidify places to visit "+location
        url=self.google(query)
        if "sightseeing-and-things-to-do.html" not in url:
            url=url+"sightseeing-and-things-to-do.html"
        soup = self.fetch_data(url)
        places=soup.findAll('h3',attrs={'class':'card-heading'})
        result=""
        i=0
        for place in places:
            i+=1
            print(place.text)
            result=result+place.text+"\n"    
            if(i>=11):
                break;
        speech = "Top Ten Places to visit in \n"+location+result
        print(speech)
        return speech
    def best_time_to_visit(self,location):
        query="holidify best time to visit "+location
        url=self.google(query)
        if "best-time-to-visit.html" not in url:
            url=url+"best-time-to-visit.html"
        soup = self.fetch_data(url)
        summary=soup.findAll('p')
        print(summary[1].text)
        return summary[1].text
    
    def current_temperature(self,location):
        query="timeanddate.com weather "+location
        url=self.google(query)
        soup=self.fetch_data(url)
        summary=soup.find('div',attrs={'class':'h2'})
        desc=summary.next_element.next_element
        print(summary.text)
        print(desc.text)
        result=summary.text+"\n"+desc.text
        return result

    def how_to_reach(self,location):
        query="holidify how to reach "+location
        url=self.google(query)
        if "how-to-reach.html" not in url:
            url=url+"how-to-reach.html"
        soup=self.fetch_data(url)
        summary=soup.findAll('p')
        print(summary[1].text)
        return summary[1].text

    def restaurants_near_me(self,location):
        query="zomato restaurant near "+location
        url=self.google(query)
        # print(url)
        soup=self.fetch_data(url)
        stores=soup.findAll('a',attrs={'data-result-type':'ResCard_Name'})
        i=0
        result=""
        for store in stores:
            i+=1
            print(store.text)
            result=result+store.text+"\n"
            if(i>=10):
                break

        return "Top Restaurants Near You \n" + result

    def hotels_near_me(self,location,stars):
        query="makemytrip "+str(stars)+" star hotels near "+location
        url=self.google(query)
        soup=self.fetch_data(url)
        hotels=soup.findAll('p',attrs={'id':'hlistpg_hotel_name'})
        i=0
        result=""
        for hotel in hotels:
            i+=1
            print(hotel.text)
            result=result+hotel.text+"<br>"
            if(i>=10):
                break

        return "Top Hotels Near You \n" + result
    
    def nearest_railway_station(self,location):
        query="train spy nearest railway station to "+location
        url=self.google(query)
        soup=self.fetch_data(url)
        # print(url)
        result=""
        t=1
        tables = soup.findAll('table', attrs={'id':'trains'})
        for table in tables:    
            

            data = []
            table_body = table.find('tbody')

            rows = table_body.find_all('tr')
            for row in rows:
                cols = row.find_all('td')
                cols = [ele.text.strip() for ele in cols]
                data.append([ele for ele in cols if ele])     

            c=4
            if t==1:
                print("Minor Stations")
                result+="Minor Stations<br>"
                t=t+1
            else:
                print("\n\nMajor Stations")
                result+="<br><br>Major Stations<br>"

            for row in data:
                if(c==0):
                    break
                if(c==4):
                    c=c-1
                    continue

                print(row[0].split(')')[1]+" around "+row[2])
                result+=row[0].split(')')[1]+" around "+row[2]+"\n"
                c=c-1
        return result
    
    def nearest_airport(self,location):
        query="globefeed nearest airport to "+location
        url=self.google(query)
        soup=self.fetch_data(url)
        result=""
        table = soup.find('table')
        data = []
        table_body = table.find('tbody')

        rows = table_body.find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]
            data.append([ele for ele in cols if ele])     
        row=data[1:]
        try:
            for data in row:
                print(data[0]+" in "+data[1]+" around "+data[3]+"\n")
                result+=data[0]+" in "+data[1]+" around "+data[3]+"\n"
        except:
            pass

        return result



def fetch_data(url):
    headers = {'User-Agent': 'Mozilla/5.0'}
    res=requests.get(url,headers=headers)
    return BeautifulSoup(res.content, 'html5lib')

def google(query):
    result_link=[]
    for j in search(query, num=1, stop=1): 
        result_link.append(j)

    url=result_link[0];
    return url

def tell_me_about(location):
    query="holidify "+location
    url=google(query)
    soup = fetch_data(url)
    text=soup.find('div',attrs={'class':'readMoreText'})
    st = text.text
    st = st.replace('\xa0','').replace('\n        ','').split('.')
    speech = ""
    i=0
    while(len(speech) < 200):
        speech = speech + st[i]
        i+=1
    
    print(speech)

    return speech

def places_to_visit(location):
    query="holidify places to visit "+location
    url=google(query)
    if "sightseeing-and-things-to-do.html" not in url:
        url=url+"sightseeing-and-things-to-do.html"
    soup = fetch_data(url)
    places=soup.findAll('h3',attrs={'class':'card-heading'})
    result=""
    for place in places:
        print(place.text)
        result=result+place.text+"<br>"    
    return result

def best_time_to_visit(location):
    query="holidify best time to visit "+location
    url=google(query)
    if "best-time-to-visit.html" not in url:
        url=url+"best-time-to-visit.html"
    soup = fetch_data(url)
    summary=soup.findAll('p')
    print(summary[1].text)
    return summary[1].text
    
def current_temperature(location):
    query="timeanddate.com weather "+location
    url=google(query)
    soup=fetch_data(url)
    summary=soup.find('div',attrs={'class':'h2'})
    desc=summary.next_element.next_element
    print(summary.text)
    print(desc.text)
    result=summary.text+"<br><br>"+desc.text
    return result

def how_to_reach(location):
    query="holidify how to reach "+location
    url=google(query)
    if "how-to-reach.html" not in url:
        url=url+"how-to-reach.html"
    soup=fetch_data(url)
    summary=soup.findAll('p')
    print(summary[1].text)
    return summary[1].text

def restaurants_near_me(location):
    query="zomato restaurant near "+location
    url=google(query)
    # print(url)
    soup=fetch_data(url)
    stores=soup.findAll('a',attrs={'data-result-type':'ResCard_Name'})

    i=0
    result=""
    for store in stores:
        i+=1
        print(store.text)
        result=result+store.text+", "
        if(i>=10):
            break

    return "Top Restaurants Near You \n" + result
        
def hotels_near_me(location,stars):
    query="makemytrip "+str(stars)+" star hotels near "+location
    url=google(query)
    soup=fetch_data(url)
    hotels=soup.findAll('p',attrs={'id':'hlistpg_hotel_name'})

    result=""
    for hotel in hotels:
        print(hotel.text)
        result=result+hotel.text+"<br>"
    return result
'''
def book_air_tickets(src,dest):
    query="paytm flight from "+src+" to "+dest
    url=google(query)
    webbrowser.open_new_tab(url)
    return "Opened Link in New Tab"

def book_rail_tickets(src,dest):
    query="paytm book train from "+src+" to "+dest
    url=google(query)
    webbrowser.open_new_tab(url)
    return "Opened Link in New Tab"

def book_bus_tickets(src,dest):
    query="paytm bus tickets from "+src+" to "+dest
    url=google(query)
    webbrowser.open_new_tab(url)
    return "Opened Link in New Tab"
'''
def nearest_railway_station(location):
    query="train spy nearest railway station to "+location
    url=google(query)
    soup=fetch_data(url)
    # print(url)
    result=""
    t=1
    tables = soup.findAll('table', attrs={'id':'trains'})
    for table in tables:    
        

        data = []
        table_body = table.find('tbody')

        rows = table_body.find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]
            data.append([ele for ele in cols if ele])     

        c=4
        if t==1:
            print("Minor Stations")
            result+="Minor Stations<br>"
            t=t+1
        else:
            print("\n\nMajor Stations")
            result+="<br><br>Major Stations<br>"
        print("\nStation\t\tDistance")
        result+="<br>Station\t\tDistance<br>"
        for row in data:
            if(c==0):
                break
            if(c==4):
                c=c-1
                continue
            print(row[0]+"\t"+row[2])
            result+=row[0]+"\t"+row[2]+"<br>"
            c=c-1
    return result

def nearest_airport(location):
    query="globefeed nearest airport to "+location
    url=google(query)
    soup=fetch_data(url)
    result=""
    table = soup.find('table')
    data = []
    table_body = table.find('tbody')

    rows = table_body.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele])     
    row=data[1:]
    try:
        for data in row:
            print(data[0]+"\n"+data[1]+"\t"+data[2]+"\t"+data[3]+"\n")
            result+=data[0]+"<br>"+data[1]+"\t"+data[2]+"\t"+data[3]+"<br>"+"<br>"
    except:
        pass

    return result

t = Travis()
#t.tell_me_about('Haridwar')
#t.places_to_visit('haridwar')
#t.best_time_to_visit('haridwar')
#t.current_temperature('hyderabad')
#t.how_to_reach('auli')
#restaurants_near_me("harki pauri")
hotels_near_me("near harki pauri",3)
#nearest_railway_station("near qutub minar")
#t.nearest_airport("moradabad")
#book airticket
#book rail ticket
#book bus ticket
