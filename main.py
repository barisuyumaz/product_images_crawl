import pandas as pd
import functionsBaris
from DriverClass import WebScrappingDriver
import os


# columns
columns = ["Görsel 1", "Görsel 2", "Görsel 3", "Görsel 4", "Görsel 5"]
def add_image_columns(pandas_par):
    try:
        url_column_index = pandas_par.columns.get_loc("Link")
    except:
        url_column_index = pandas_par.columns.get_loc("Ürün Sayfası")

    pandas_par.insert(url_column_index + 1, columns[0], None)  # Görsel1 kolonu eklendi
    pandas_par.insert(url_column_index + 2, columns[1], None)
    pandas_par.insert(url_column_index + 3, columns[2], None)
    pandas_par.insert(url_column_index + 4, columns[3], None)
    pandas_par.insert(url_column_index + 5, columns[4], None)


myPath = 'C:/Users/Administrator/Desktop/input/'
excels = os.listdir(myPath)

def website_images(product_link_par, images_par, df_par, df_index_par, index_of_first_img_column_par):
    for index_img, j in enumerate(images_par):
        df_par.at[df_index_par, df_par.columns[index_of_first_img_column_par + index_img]] = j
    #print(str(len(images_par))," görsel var!", product_link_par, df_index_par)

for i in excels:
    print(i)
    input_categories = pd.read_excel(myPath  + i)
    input_categories = input_categories.reset_index(drop=True)

    excel_columns = input_categories.columns.tolist()
    if("Görsel 1" not in excel_columns):
        add_image_columns(input_categories)
    
    index_of_first_img_column = input_categories.columns.get_loc("Görsel 1")

    scraper = WebScrappingDriver() #DRIVER BAŞLAT

    for index, row in input_categories.iterrows():
        try:
            urun_link = row["Link"]
        except:
            urun_link = row["Ürün Sayfası"]    
        
        if(pd.isna(row['Görsel 1'])):
            try:
                urun_link_second_index = urun_link.split("/")[2] #general
                print(index, urun_link)
                #-
                # hepsiburada.com
                if(urun_link_second_index == "www.hepsiburada.com"):
                    website_images(urun_link, functionsBaris.hepsiburada_apisiz(urun_link), input_categories, index, index_of_first_img_column)
                #-
                # n11
                if(urun_link_second_index == "www.n11.com"):
                    website_images(urun_link, functionsBaris.n11(urun_link), input_categories, index, index_of_first_img_column)
                #-
                # pazarama
                if(urun_link_second_index == "www.pazarama.com"):
                    website_images(urun_link, functionsBaris.pazarama(urun_link), input_categories, index, index_of_first_img_column)
                #-
                # teknosa
                if(urun_link_second_index == "www.teknosa.com"):
                    website_images(urun_link, functionsBaris.teknosa(urun_link), input_categories, index, index_of_first_img_column)
                #-
                # beko.com.tr
                if(urun_link_second_index == "www.beko.com.tr"):
                    website_images(urun_link, functionsBaris.beko_tr(urun_link), input_categories, index, index_of_first_img_column)
                #-
                # arcelik.com.tr
                if(urun_link_second_index == "www.arcelik.com.tr"):
                    website_images(urun_link, functionsBaris.arcelik(urun_link), input_categories, index, index_of_first_img_column)
                #-
                # arcelik
                if(urun_link_second_index == "www.koctas.com.tr"):
                    website_images(urun_link, functionsBaris.koctas(urun_link), input_categories, index, index_of_first_img_column)
                #-
                # samsung
                if(urun_link_second_index == "shop.samsung.com"):
                    website_images(urun_link, functionsBaris.samsung(urun_link), input_categories, index, index_of_first_img_column)
                #-
                # watsons
                if(urun_link_second_index == "www.watsons.com.tr"):
                    website_images(urun_link, functionsBaris.watsons(urun_link), input_categories, index, index_of_first_img_column)
                #-
                #----
                #DRIVERLILAR
                # trendyol
                if(urun_link_second_index == "www.trendyol.com"):
                    website_images(urun_link, functionsBaris.trendyol(urun_link, scraper), input_categories, index, index_of_first_img_column)
                #-
                # carrefoursa
                if(urun_link_second_index == "www.carrefoursa.com"):
                    website_images(urun_link, functionsBaris.carrefoursa(urun_link, scraper), input_categories, index, index_of_first_img_column)
                #-
            except:
                pass

    scraper.quit_driver() #DRIVER KAPAT
    excel_name = i.replace(".xlsx","")
    with pd.ExcelWriter('C:/Users/Administrator/Desktop/output/' + excel_name + "_output.xlsx") as writer:
        input_categories.to_excel(writer, sheet_name="sheetName", index=False)