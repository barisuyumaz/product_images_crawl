import requests
from bs4 import BeautifulSoup
import time

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}
#FUNCTIONS
#MAIN FUNC---
def request_n_soup_special_for_epey(link):
    pageSource = requests.get(link, headers=headers).content
    soup = BeautifulSoup(pageSource,"html.parser")
    return soup
#----------------------------------------------------

#WEBSITE FUNCS---
#www.n11.com
def n11(link_par):
    soup = request_n_soup_special_for_epey(link_par)
    photos = soup.find_all("div",{"class":"unf-p-thumbs-item"})

    for i in photos[:5]:
        #print("https://www.beko.com.tr" + i.find("img")['data-srcset'].split(" ")[-2])
        img =  i["data-full"]
        yield img
#----------------------------------------------------

#www.hepsiburada.com
def hepsiburada_apisiz(link_par):
    soup = request_n_soup_special_for_epey(link_par)
    photos = soup.find("div",{"id":"productDetailsCarousel"}).find_all("picture")
    #ilk img
    first_img = photos[0].find("source")['srcset'].split(" ")[0].split("/")
    first_img[5] = "1200"
    first_img = "/".join(first_img)
    yield first_img

    #kalan imgler
    for i in photos[1:5]:
        rest_images = i.find("source")['data-srcset'].split(" ")[0].split("/")
        rest_images[5] = "1200"
        rest_images = "/".join(rest_images)
        yield rest_images
#----------------------------------------------------

#watsons    
def watsons(link_par):
    soup = request_n_soup_special_for_epey(link_par)
    photos = soup.find("div",{"class":"product-thumbnails__preview"}) #div class product-thumbnails
    
    if(photos):
        photos = photos.find_all("img")
        for i in photos[:5]:
            yield "https://www.watsons.com.tr/" + i['data-src']
#----------------------------------------------------

#pazarama
def pazarama(link_par):
    soup = request_n_soup_special_for_epey(link_par)
    try:
        photos = soup.find("div",{"class":"swiper-wrapper"}).find_all("img",{"class":"object-contain w-full h-full"})
        if(photos):
            for i in photos[:5]:
                img_elements = i["data-src"].split("/")
                img_elements[4], img_elements[5] = "1000", "1000"
                yield "/".join(img_elements)
        else:
            photo = soup.find("img",{"class":"object-contain w-full h-full"})#.find('img')
            yield photo['data-src']
    except:
        yield
#----------------------------------------------------

#teknosa
def teknosa(link_par):
    soup = request_n_soup_special_for_epey(link_par)
    try:
        photos = soup.find_all("div",{"class":"swiper-slide responsive-image-swiper-slide"})
        for i in photos[:5]:
            yield i['data-zoom']
    except:
        yield
#----------------------------------------------------

#www.carrefoursa.com
def carrefoursa(link_par, driver_scraper):
    try:
        driver_scraper.scrap_data(link_par)
        try:
            driver_scraper.click_By_id('cboxClose')
        except:
            pass
        time.sleep(1)
        soup = driver_scraper.get_page_source_soup()
        try:
            photo = soup.find("div",{"id":"cboxLoadedContent"}).find("img",{"class":"cboxPhoto"})
            img = photo['src']
            yield img
        except:
            photos = soup.find("div",{"class":"owl-wrapper clearfix"}).find_all("div",{"class":"item"})#['src']
            
            for index, j in enumerate(photos[:5]):
                if(index > 0):
                    img = j.find("img")['data-src']
                    yield img
                else:
                    img = j.find("img")['src']
                    yield img
    except:
        pass
#----------------------------------------------------

#trendyol
def trendyol(link_par, driver_scraper):
    driver_scraper.scrap_data(link_par)
    soup = driver_scraper.get_page_source_soup()

    all_images = soup.find("div", {"class": "styles-module_slider__o0fqa"})
    if(all_images):
        all_images = all_images.find_all("img")
        for i in all_images[:5]:
            img = i['src'].split("/")
            img[4] = "1200"
            img[5] = "1800"
            img = "/".join(img)
            yield img
    else:
        one_image = soup.find("div", {"class": "base-product-image"})
        yield one_image.find("img")['src']
#----------------------------------------------------

#www.beko.com.tr
def beko_tr(link_par):
    soup = request_n_soup_special_for_epey(link_par)
    photos = soup.find_all("div",{"class":"swiper-zoom-container"})#[1].find_all("img",{"class":"w-100"})
    try:
        for i in photos[:5]:
            result = "https://www.beko.com.tr" + i.find("img")['data-srcset'].split(" ")[-2]
            yield result
    except:
        pass
#----------------------------------------------------

#www.arcelik.com.tr
def arcelik(link_par):
    soup = request_n_soup_special_for_epey(link_par)
    photos = soup.find("div",{"class":"swiper-wrapper"}).find_all("img")
    try:
        for i in photos[:5]:
            source = i['data-srcset'].split(", ")
            img = source[-1][0:-3]
            img_link = "https://www.arcelik.com.tr" + img
            yield img_link
    except:
        pass
#----------------------------------------------------

#koçtaş
def koctas(link_par):
    soup = request_n_soup_special_for_epey(link_par)
    photos = soup.find_all("li",{"class":"swiper-slide mr-lg-0"})
    try:
        for i in photos[:5]:
            img_list = i['data-large'].split("/")
            img_list[4] , img_list[5]  = "1200" , "1200"
            img_link = "/".join(img_list)
            yield img_link
    except:
        pass
#----------------------------------------------------

#samsung
def samsung(link_par):
    soup = request_n_soup_special_for_epey(link_par)
    photos = soup.find("div",{"class":"swiper-wrapper"}).find_all("img")
    try:
        for i in photos[:5]:
            img_link = i['src'].replace("77x77","616x616")
            yield img_link
    except:
        pass
#----------------------------------------------------
