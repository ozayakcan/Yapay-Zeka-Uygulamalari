# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 17:44:06 2022

@author: Özay Akcan
"""

#pip install googletrans==3.1.0a0
#pip install pandas

import googletrans
from googletrans import Translator
import pandas as pd

#Desteklenen Dil Sayısı
#print(len(googletrans.LANGUAGES))

#Desteklenen Diller
#print(googletrans.LANGUAGES)


translator = Translator()
sentence = "Olmak ya da olmamak."
example = translator.translate(sentence)

#Nesne tipini verir
#print(type(example))

#Kaynak cümle dilini verir.
print(example.src)

#Hedef cümle dilini verir.
print(example.dest)

#Orijinal cümle
print(example.origin)

#Çevirilen cümle
print(example.text)


print("**********************")

sentence2 = "To be or not to be."
example2 = translator.translate(sentence2, dest="tr")

print(example2.src)
print(example2.dest)
print(example2.origin)
print(example2.text)


word_tr = ["Elma","Armut","Kiraz","Üzüm","Portakal"]

df = pd.DataFrame(columns=["Türkçe", "İngilizce", "Almanca", "Fransızca"])

#print(df)

for word in word_tr:
    df = df.append({
        "Türkçe":word,
        "İngilizce": translator.translate(word, dest="en").text,
        "Almanca": translator.translate(word, dest="de").text,
        "Fransızca": translator.translate(word, dest="fr").text
        }, ignore_index=True)

print(df)

print("**********************")

print(df.head(1))
print("**********************")
print(df.iloc[0])
print("**********************")

print(df[{'Türkçe','İngilizce'}])
print("**********************")
print(df[{'Türkçe','İngilizce'}].values[0])