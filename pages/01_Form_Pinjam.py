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
st.title("📖Menu Peminjaman Buku")
st.write("Silahkan Masukkan Data Diri Anda")
form1 = st.form(key="annotation1",clear_on_submit=True)
    

with form1:
        cols = st.columns((1,1))
        nama = cols[0].text_input("Nama Lengkap :")
        judul = cols[1].selectbox('Pilih Judul Buku',('','The Great Gatsby by F. Scott Fitzgerald','To Kill a Mockingbird by Harper Lee','1984 by George Orwell','Pride and Prejudice by Jane Austen','The Catcher in the Rye by J.D. Salinger','Little Women by Lousia May Alcott','Poor Dad Rich Dad by Robert T. Kiyosaki'))
        cols = st.columns(2)
        tglpinjam = cols[0].date_input("Tanggal Peminjaman :")
        tglkembali = cols[1].date_input("Tanggal Kembali :")
        submitted = st.form_submit_button(label="Submit")

        if submitted:
            st.success("Terimakasih sudah meminjam buku di perpustakaan PROA Digitalent! Jangan lupa simpan struk peminjaman ya")
            st.balloons()
            for i in range(1):
                arynama.append(nama)
                aryjudul.append(judul)
                arytglpinjam.append(tglpinjam)
                arytglkembali.append(tglkembali)
                sys.stdout = open("struk-"+nama+"-"+str(tglpinjam)+".txt", "w")
                print('''
                    *********************  PERPUS PROA DIGITALENT  **********************
                    ************ Sistem Peminjaman Buku Perpustakaan Digital ************
                    ************************ Struk Bukti Pinjam *************************
                    ''')
                print('\t\t\tTanggal : ',tglpinjam,"2023")
                print("\t\t\tNama Peminjam Buku : ",nama)
                print("\t\t\tJudul Buku : ",judul)
                print("\t\t\tTanggal Peminjaman : ",tglpinjam)
                print("\t\t\tTanggal Kembali : ",tglkembali)
                print('''
                            ---Terima Kasih Telah Meminjam Buku Ditempat Kami---
                            ---Struk Harap Dibawa pada saat pengembalian Buku---
                    ''')
                sys.stdout.close()
                sys.stdout = sys.__stdout__
                time.sleep(1)
                os.system("struk-"+nama+"-"+str(tglpinjam)+".txt")