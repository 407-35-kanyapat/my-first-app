import streamlit as st
st.title("🛒แอปพลิเคชั่นคำนวณราคาสินค้ารวม VAT 7%")
price = st.number_input("กรอกราคาสินค้า (บาท):", value=0.0)

net_price = price - vat
vat = price * 0.07
st.header(f"• ราคาสุทธิ: {net_price:.2f} บาท")
st.divider()
st.write("นางสาวกัญญาพัชร ศักดิ์เสือ เลขที่ 35  ม.4/7")
