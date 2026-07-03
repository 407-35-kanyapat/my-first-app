import streamlit as st
st.title("แอปพลิเคชั่นแปลงปี พ.ศ. เป็น ค.ศ.")

bh_year=st.number_input("กรอกปี พ.ศ. ที่ต้องการเปลี่ยนแปลง",value=2569)
ceyear=bh_year-543
st.header(f"ปี พ.ศ. คือ : {ce_year}")
