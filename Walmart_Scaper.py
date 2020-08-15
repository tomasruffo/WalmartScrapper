# -*- coding: utf-8 -*-
""" 
Created on Thu Aug  6 18:07:38 2020

@author: Tomas
"""
from selenium import webdriver
from time import sleep
from numpy import random
import pandas as pd
from selenium.webdriver.common.by import By

from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome('C:/Users/Tomas/Documents/GitHub/Waltmart_scrapper/chromedriver.exe')

#links necesarios
path= "https://www.walmart.com.ar"
categorias=["aceites-y-aderezos","alimento-perro","desayuno-y-golosinas","alfombras-fundas-y-cobertores-para-auto","parrillas-y-carbon"]
#Pagina Web
d= []

def scrapper(categoria_walmart):
        #funcion que recibe la categoria de waltmare
        #devuelve los productos en una lista llamada "d"
        
        #obtiene el link (el path fue defindio al principio, y la categoria es la entrada de la funcion)
        driver.get(path+"/"+categoria_walmart)
    
        #d= []

        
        #while(q==0):
        for i in range(20):
            #Scroll
            sleep(random.uniform(5,8)) 
            driver.execute_script("window.scrollBy(0,3000)","")
            
            driver.execute_script("window.scrollBy(0,3000)","")
            sleep(random.uniform(4,7)) 
            #detecta todos los productos y los convierte en una lista
            productos =  driver.find_elements_by_xpath('//li[@layout="63c6cac5-a4b5-4191-a52a-65582db8f8b3"]')
            
            # Bucle que extrae cada caracteristca de cada elemeto de la lista
            for producto in productos:
                #los try y except estan para evitar que se rompan el programa si falta algun dato
                try:
                    nombre = producto.find_element_by_xpath('.//a[@itemprop="name"]').text
                    print(nombre)
                except:
                    nombre ="No Encontrado"
                try:
                    precio = producto.find_element_by_xpath('.//span[@itemprop="price"]').text
                    print(precio)
                except:
                    precio = ("No Encontrado")
                    
                categoria = categoria_walmart
                print(categoria)
                #agreago las variables "nombre" y "precio" a "d"
                d.append({"nombre":nombre,"precio":precio,"categoria":categoria_walmart})
            
            sleep(random.uniform(4,7)) 
            boton = driver.find_element(By.XPATH, '(//li[@class="page-number pgCurrent"]/following-sibling::li)[1]')
            actions = ActionChains(driver)
            actions.move_to_element(boton)
            actions.perform()
            boton.click()
    
            if boton.get_attribute("class") == "last":
                
                break
            #else:
             #   print("o fim do siclo")
            
        return d

#Bucle que aplica la funcion a todas las categorias y junta todo en "diccionario"
diccionario=[]
for categoria in categorias:
    d = scrapper(categoria)
    diccionario.append(d)
    
#convierte diccionario en un DataFrame
Final=pd.DataFrame(diccionario)
diccionario.head()

diccionario.to_csv("./Scrapping")

#d.to_csv("C:/Users/Tomas/Documents/GitHub/Waltmart_scrapper/Walmart_0.csv")
         
#Boton siguente
#boton = driver.find_element_by_xpath('//li[@class="page-number pgCurrent"]/following-sibling::li')[1]
#valor = driver.find_element_by_xpath('//li[@class="page-number pgCurrent"]')
#int(valor)
#valor += 1
'''boton = driver.find_element_by_xpath('//li[contains(@class,"page-number") and text() = valor]')
try:
    boton.click()
except:
    print("no encontre el boton")'''
