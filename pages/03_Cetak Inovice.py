import time
import sys
import os
import datetime
import streamlit as st

# from streamlit_option_menu import option_menu
# from streamlit.components.v1 import iframe

st.set_page_config(page_title="Menu Peminjaman Buku", page_icon="📖", layout="centered")

arynama,aryjudul,arytglpinjam,arytglkembali = [],[],[],[]
st.empty()
st.title("📖 Invoice Generator")
form3 = st.form(key="annotation3",clear_on_submit=True)

with form3:
    cols = st.columns((1,1))
    nama = cols[0].text_input("Nama Lengkap :")
    judul = cols[1].selectbox('Pilih Judul Buku',('','The Great Gatsby by F. Scott Fitzgerald','To Kill a Mockingbird by Harper Lee','1984 by George Orwell','Pride and Prejudice by Jane Austen','The Catcher in the Rye by J.D. Salinger'))
    cols = st.columns(2)
    tglpinjam = cols[0].date_input("Tanggal Peminjaman :")
    tglkembali = cols[1].date_input("Tanggal Kembali :")
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
        for i in range(1):
                arynama.append(nama)
                aryjudul.append(judul)
                arytglpinjam.append(tglpinjam)
                arytglkembali.append(tglkembali)
                sys.stdout = open("invoice-"+nama+"-"+str(tglkembali)+".txt", "w")
                print('''
                    *********************  PERPUS PROA DIGITALENT  **********************
                    ************ Sistem Peminjaman Buku Perpustakaan Digital ************
                    ************************ Invoice Peminjaman *************************
                    ''')
                print('\t\t\tTanggal : ',tglpinjam)
                print("\t\t\tNama Peminjam Buku : ",nama)
                print("\t\t\tJudul Buku : ",judul)
                print("\t\t\tTanggal Peminjaman : ",tglpinjam)
                print("\t\t\tTanggal Kembali : ",tglkembali)
                print("\t\t\tDenda : ",denda)
                print('''
                            ---Terima Kasih Telah Meminjam Buku Ditempat Kami---
                                                    ---LUNAS---
                    ''')
                sys.stdout.close()
                sys.stdout = sys.__stdout__
                time.sleep(1)
                os.system("invoice-"+nama+"-"+str(tglkembali)+".txt")