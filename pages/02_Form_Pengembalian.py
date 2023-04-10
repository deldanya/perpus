import time
import sys
import os
import datetime
import streamlit as st

from streamlit_option_menu import option_menu
from streamlit.components.v1 import iframe

st.set_page_config(page_title="Menu Peminjaman Buku", page_icon="📖", layout="centered")

arynama,aryjudul,arytglpinjam,arytglkembali = [],[],[],[]
st.empty()
st.title("📖Menu Pengembalian Buku")
st.write("Silahkan Masukkan Data Diri Anda")
form2 = st.form(key="annotation2",clear_on_submit=True)

with form2:
        nama = form2.text_input("Nama Lengkap :")
        judul = form2.selectbox('Pilih Judul Buku',('','The Great Gatsby by F. Scott Fitzgerald','To Kill a Mockingbird by Harper Lee','1984 by George Orwell','Pride and Prejudice by Jane Austen','The Catcher in the Rye by J.D. Salinger'))
        tglkembali = form2.date_input("Tanggal Pengembalian :")
        submitted = st.form_submit_button(label="Submit")
        tglskg = datetime.datetime.now()
        tglkembali = str(tglkembali)
        tglWajib = tglkembali.split('-')

        tglWajib[0] = int(tglWajib[0])
        tglWajib[1] = int(tglWajib[1])
        tglWajib[2] = int(tglWajib[2])
        
        selisihTahun = tglWajib[0] - tglskg.year
        selisihBulan = tglWajib[1] - tglskg.month 
        selisihTanggal = tglWajib[2] - tglskg.day 

        totalHari = (selisihTahun*365 + selisihBulan*30 + selisihTanggal)
        
        denda = 0

        if(totalHari>0):
            denda = 5000 * totalHari

        if submitted:
            if(denda == 0):
                st.success("Terimakasih sudah mengembalikan buku tepat pada waktunya!")
                st.balloons()
            else:
                st.success("Anda terlambat mengembalikan buku sebanyak "+ str(totalHari) +" hari, maka harap membayar denda sebesar "+ str(denda) +" rupiah")