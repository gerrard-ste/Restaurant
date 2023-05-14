from bs4 import BeautifulSoup
import requests
import mysql.connector
url= requests.get(f'https://www.bestrestaurantsmaroc.com/fr/recherche/ville/marrakech.html')
def main(url):
    cnx = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='datarestau')
    cursor = cnx.cursor()
    src= url.content
    soup = BeautifulSoup(src,"html.parser")
    restaurants = soup.find_all("div", {'class': 'filterData rs-container br-bg-grey'})
    for restaurant in restaurants:
        restaurant_nom = restaurant.find('h3').text.strip()
        restaurant_ville = restaurant.find("div", {'class': 'rs-city rs-info'}).text.strip()
        restaurant_image_tag = restaurant.find('img')
        restaurant_image = restaurant_image_tag['src']
        description = restaurant.find("div", {'class': 'rs-cuisine rs-info'}).text.strip()
        query = "INSERT INTO websiterecrestau_restaurant(name,description,ville,image) VALUES(%s,%s,%s,%s)"
        values = (restaurant_nom,description , restaurant_ville, restaurant_image)
        cursor.execute(query, values)
    cnx.commit()
    cursor.close()
    cnx.close()
    '''
    def get_cat_info(restaurants):
            for restaurant in restaurants:
                cat_title = restaurant.find("div", {'class': 'rs-cuisine rs-info'}).text.strip()
                print(cat_title)
    get_cat_info(restaurants)
    ''' 
main(url)   