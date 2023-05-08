import time
import sys
import os
import datetime
import streamlit as st
from PIL import Image

st.set_page_config(page_title="Home Page", page_icon="📚", layout="centered")

st.title(body="📚Selamat Datang Di Perpustakaan")
st.title("📚Minimalism")
st.write("Berikut ini adalah daftar buku yang tersedia di perpustakaan kami")
image = Image.open('./assets/images/1.jpg')
image1 = Image.open('./assets/images/2.jpg')
image2 = Image.open('./assets/images/3.jpg')
image3 = Image.open('./assets/images/4.jpg')
image4 = Image.open('./assets/images/5.jpg')
image5 = Image.open('./assets/images/6.jpg')
image6 = Image.open('./assets/images/7.jpg')
image7 = Image.open('./assets/images/8.jpg')
image8 = Image.open('./assets/images/9.jpg')
image9 = Image.open('./assets/images/10.jpg')

cols = st.columns((1,1,1))
cols1 = st.columns((1,1,1))
cols2 = st.columns((1,1,1))
cols3 = st.columns((1))

cols[0].image(image,width=200)
cols[0].write("Tersedia 3 Buku")
cols[1].image(image1,width=200)
cols[1].write("Tersedia 2 Buku")
cols[2].image(image2,width=200)
cols[2].write("Tersedia 4 Buku")

cols1[0].image(image3,width=200)
cols1[0].write("Tersedia 1 Buku")
cols1[1].image(image4,width=200)
cols1[1].write("Tersedia 2 Buku")
cols1[2].image(image5,width=200)
cols1[2].write("Tersedia 2 Buku")

cols2[0].image(image6,width=200)
cols2[0].write("Tersedia 4 Buku")
cols2[1].image(image7,width=200)
cols2[1].write("Tersedia 0 Buku")
cols2[2].image(image8,width=200)
cols2[2].write("Tersedia 2 Buku")

cols3[0].image(image9,width=200)
cols3[0].write("Tersedia 0 Buku")
