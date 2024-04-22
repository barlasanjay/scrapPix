import streamlit as st
import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import webbrowser
st.set_page_config(page_title="Web Scrapper", page_icon="🌎")
st.markdown("""
<style>
            .ef3psqc4{
                visibility:hidden;
            }
            .ezrtsby0{
                visibility:hidden;
            }
            .ea3mdgi1{
                visibility:hidden;
            }
</style>

""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center'>Image Web Scrapper</h1>",unsafe_allow_html=True)
st.markdown("---")


with st.form("search"):
    keyword= st.text_input("Enter Image Name You Want!!")

    search = st.form_submit_button("Get Images")


placeholder = st.empty()

if keyword:
    page = requests.get(f"https://unsplash.com/s/photos/{keyword}")
    soup = BeautifulSoup(page.content,"lxml")
    rows = soup.find_all("div", class_="ripi6")
    col1,col2 = placeholder.columns(2)
    for index,row in enumerate(rows):
        figures = row.find_all("figure")
        for i in range(2):
            img = figures[i].find("img",class_="tB6UZ a5VGX")
            # anchor = figures[i].find("a",class_="rEAWd")
            # print(anchor['href'])
            src = img['srcset'].split("?")
            if i==0:
                col1.image(src[0])
                btn = col1.button("Download",key=str(index)+str(i))
                if btn:
                    webbrowser.open_new_tab("https://unsplash.com"+anchor['href'])
            else:
                col2.image(src[0])
                btn = col2.button("Download",key=str(index)+str(i))
                if btn:
                    webbrowser.open_new_tab("https://unsplash.com"+anchor['href'])
            print("\n\n")