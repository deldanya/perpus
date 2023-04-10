import time
import sys
import os
import datetime
import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu
from streamlit.components.v1 import iframe
# st.markdown('#Home Page')


st.set_page_config(page_title="Menu Peminjaman Buku", page_icon="📖", layout="centered")

st.title("🏢Selamat Datang Di Perpus PROA Digitalent")
st.write("Berikut ini adalah daftar buku yang tersedia di perpustakaan kami")
image = Image.open('./assets/images/1.jpg')
image1 = Image.open('./assets/images/2.jpg')
image2 = Image.open('./assets/images/3.jpg')
image3 = Image.open('./assets/images/4.jpg')
image4 = Image.open('./assets/images/5.jpg')
image5 = Image.open('./assets/images/6.jpg')
image6 = Image.open('./assets/images/7.jpg')

cols = st.columns((1,1,1))
cols1 = st.columns((1,1,1))
cols2 = st.columns((1,1,1))

cols[0].image(image,width=200)
cols[1].image(image1,width=200)
cols[2].image(image2,width=200)

cols1[0].image(image3,width=200)
cols1[1].image(image5,width=200)
cols1[2].image(image6,width=200)

cols2[0].image(image,width=200)
cols2[1].image(image,width=200)
cols2[2].image(image,width=200)

# cols[1].image("https://images-na.ssl-images-amazon.com/images/I/51ZyqZQZQlL._SX331_BO1,204,203,200_.jpg",width=200)
# cols[2].image("https://images-na.ssl-images-amazon.com/images/I/51ZyqZQZQlL._SX331_BO1,204,203,200_.jpg",width=200)



# form = st.form(key="annotation")

# with form:
#     cols = st.columns((1,1,1))

    
#     submitted = st.form_submit_button(label="Submit")
    # cols1 = st.columns((1,1,1))
    # cols2 = st.columns((1,1,1))

    # cols[0].image("https://images-na.ssl-images-amazon.com/images/I/51ZyqZQZQlL._SX331_BO1,204,203,200_.jpg",width=200)
    # cols[1].image("https://images-na.ssl-images-amazon.com/images/I/51ZyqZQZQlL._SX331_BO1,204,203,200_.jpg",width=200)
    # cols[2].image("https://images-na.ssl-images-amazon.com/images/I/51ZyqZQZQlL._SX331_BO1,204,203,200_.jpg",width=200)

    # cols1[0].image("https://images-na.ssl-images-amazon.com/images/I/51ZyqZQZQlL._SX331_BO1,204,203,200_.jpg",width=200)
    # cols1[1].image("https://images-na.ssl-images-amazon.com/images/I/51ZyqZQZQlL._SX331_BO1,204,203,200_.jpg",width=200)
    # cols1[2].image("https://images-na.ssl-images-amazon.com/images/I/51ZyqZQZQlL._SX331_BO1,204,203,200_.jpg",width=200)

    # cols2[0].image("https://images-na.ssl-images-amazon.com/images/I/51ZyqZQZQlL._SX331_BO1,204,203,200_.jpg",width=200)
    # cols2[1].image("https://images-na.ssl-images-amazon.com/images/I/51ZyqZQZQlL._SX331_BO1,204,203,200_.jpg",width=200)
    # cols2[2].image("https://images-na.ssl-images-amazon.com/images/I/51ZyqZQZQlL._SX331_BO1,204,203,200_.jpg",width=200)
    
    

