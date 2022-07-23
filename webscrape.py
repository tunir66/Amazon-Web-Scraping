import csv 
from bs4 import BeautifulSoup

r=requests.get('https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_1')
def extract_record(item):
    atag=item.h2.a
    title=atag.text.strip()
    url='https://amaxon.in' + atag.get('href')
    try:
        price_prent=item.find('span','a-price')
        price=price_parent.find('span',a-offscreen).text
    except AttributeError:
        return
    try:
        rating = item.i.text
        review_count = item.find('span',{'class':'a-size-base','dir':'auto'}).text
    except:
        rating=''
        review_count=''
        
    result=(title,price,rating,review_count,url)
    return result

def main(search):
    for page in range(1,21):
        soup=BeautifulSoup(r.content,'html.parser')
        results=soup.find_all('div',{'class':'sg-col-inner'})
        for item in results:
            record=extract_record(item)
            if record:
                records.append(record)
                
#Save data to CSV

    with open('Python_Assignment.csv','w',newline='',encoding='utf-8') as f:
        writer=csv.writer(f)
        writer.writerow(['title', 'price', 'stars', 'review_count', 'url'])
        writer.writerows(records)
