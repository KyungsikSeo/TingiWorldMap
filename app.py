# icons = ["glyphicon-cloud", "glyphicon-star", "glyphicon-home", "glyphicon-tree-conifer",
#          "glyphicon-tree-deciduous", "glyphicon-fire", "glyphicon-flash", "glyphicon-road",
#          "glyphicon-cutlery", "glyphicon-plane", "glyphicon-phone", "glyphicon-globe",
#          "glyphicon-heart", "glyphicon-info-sign", "glyphicon-exclamation-sign", 
#          "glyphicon-thumbs-up", "glyphicon-thumbs-down", "glyphicon-fullscreen", 
#          "glyphicon-screenshot", "glyphicon-cloud-upload", "glyphicon-cloud-download"]
#colors = ‘red’, ‘blue’, ‘green’, ‘purple’, ‘orange’, ‘darkred’, ’lightred’, ‘beige’, ‘darkblue’, ‘darkgreen’, ‘cadetblue’, ‘darkpurple’, ‘white’, ‘pink’, ‘lightblue’, ‘lightgreen’, ‘gray’, ‘black’, ‘lightgray’

# marker = folium.Marker(
#     [49.61068, 6.13127],
#     popup="<a href=https://fr.wikipedia.org/wiki/Place_Guillaume_II>Place Guillaume II</a>",
#     tooltip=tooltip
# )
# https://glyphsearch.com/?library=glyphicons
# https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app

import plotly.graph_objects as go
import pandas as pd
import numpy as np
import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt
import folium
import openpyxl
from pyxlsb import open_workbook as open_xlsb
# 권한주기
from io import BytesIO
from xlsxwriter import Workbook


st.set_page_config(
    page_title="Tingi",
    page_icon=":world_map:️",
    layout="wide",
)




st.header('🍰먹고, 😎놀고, ✈️여행하는')
st.header(' 팅이의 탐방 지도! 👍')
st.subheader("Tingi's World Map!")

data = pd.read_csv('./TingiMap_.csv')
filter_data=data
last_data=filter_data
down_data=last_data


map=folium.Map(location=[36.238772,127.948923], zoom_start=7)

for n in filter_data.index:
    name=filter_data.loc[n,'업체명']
    address=filter_data.loc[n,'시도명']
    address_spc=filter_data.loc[n,'시군구명']
    name_link=filter_data.loc[n,'게시물링크']
   
    
    #popup=folium.Popup(f'<i>{name}-{address}{address_spc}</i>', max_width=1000, max_height=1000) # 상호명과 도로명주소 이어붙이기
    popup=folium.Popup(f"<a href={name_link} target='_blank'>{name}</a>", max_width=1000, max_height=1000)
    location=[filter_data.loc[n,'경도'],filter_data.loc[n,'위도']] # n번 행의 위도, 경도
    icon=filter_data.loc[n,'Icon']
    color=filter_data.loc[n,'Color']
    folium.Marker(
        location=location, # 위도 경도 위치에
        #popup=popup, # 상호명과 도로명 주소 popup 띄우기
        popup=popup,
        icon=folium.Icon(color=color, icon=icon, prefix='fa')
    ).add_to(map) # 마커를 지도에 추가하기
st.components.v1.html(map._repr_html_(), width=1200, height=800)

#popup="<a href=https://fr.wikipedia.org/wiki/Place_Guillaume_II>Place Guillaume II</a>",tooltip=tooltip
#popup=f"<a href=http://127.0.0.1:8000>{ data.iloc[i]['name'] }</a>",


st.sidebar.header('🏖️ Naver Blog Home ↓')
st.sidebar.subheader('https://blog.naver.com/tingi40')
st.sidebar.header('✉️ Tingi e-mail')
st.sidebar.subheader('jlovemelove@naver.com')

