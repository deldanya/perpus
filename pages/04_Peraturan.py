import time
import sys
import os
import datetime
import streamlit as st
from PIL import Image

st.set_page_config(page_title="Menu Peraturan Perpustakaan", page_icon="📌", layout="centered")

st.title("📌Peraturan Perpustakaan📌")
st.write("Berikut ini adalah peraturan dari perpustakaan kami: ")
st.write("1. Peminjaman maksimal 2 (dua) buku.")
st.write("2. Lama peminjaman 1 (satu) minggu dari tanggal peminjaman.")
st.write("3. Setiap peminjam harus mengembalikan pinjaman buku, majalah, surat kabar dan lain-lain sesuai dengan waktu yang sudah ditentukan oleh perpustakaan.")
st.write("4. Peminjam wajib memiliki Struk Bukti Pinjam saat akan hendak meminjam buku.")
st.write("5. Saat mengembalikan buku, peminjam wajib membawa dan menunjukkan Struk Kertas Bukti Pinjam kepada pengawas perpustakaan.")
st.write("6. Perpanjangan masa peminjaman buku hanya boleh dilakukan satu kali.")
st.write("7. Apabila buku-buku,majalah,surat kabar yang dipinjam rusak atau hilang harap segera melapor kepada pengelola atau petugas perpustakaan.")

st.title("📌Sanksi📌")
st.write("Berikut ini adalah sanksi yang berlaku di perpustakaan kami: ")
st.write("1. Keterlambatan pengembalian buku dikenakan sanksi denda sesuai dengan peraturan dan tata tertib yang telah ditentukan, yaitu Rp. 5.000,- untuk 1 (satu) buku per hari.")
st.write("2. Apabila buku yang dipinjam rusak atau hilang, maka peminjam wajib mengganti dengan buku yang sama, atau membayar 3 (tiga) kali lipat dari harga buku tersebut (ditambah biaya sanksi denda keterlambatan pengembalian buku bila ada).")
st.write("3. Jika peminjam tidak mentaati peraturan dan tata tertib dari Perpustakaan Minimalism maka peminjam akan di-blacklist dari perpustakaan ini")