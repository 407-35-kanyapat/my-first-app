import time
import streamlit as st

st.title("⏱️ เกมเติมคำสุภาษิต")

# 1. กำหนดค่าเริ่มต้นใน session_state ถ้ายังไม่มี
if "ans1_val" not in st.session_state:
    st.session_state.ans1_val = ""
if "ans2_val" not in st.session_state:
    st.session_state.ans2_val = ""
if "ans3_val" not in st.session_state:
    st.session_state.ans3_val = ""
if "ans4_val" not in st.session_state:
    st.session_state.ans4_val = ""
if "ans5_val" not in st.session_state:
    st.session_state.ans5_val = ""
if "ans6_val" not in st.session_state:
    st.session_state.ans6_val = ""
if "ans7_val" not in st.session_state:
    st.session_state.ans7_val = ""
  
# 📌 ฟังก์ชันเคลียร์ค่าเมื่อกดปุ่มเif เริ่มใหม่
def reset_game():
    st.session_state.ans1_val = ""  # เคลียร์ค่าช่องข้อ 1
    st.session_state.ans2_val = ""  # เคลียร์ค่าช่องข้อ 2
    st.session_state.ans3_val = ""  # เคลียร์ค่าช่องข้อ 3
    st.session_state.ans4_val = ""  # เคลียร์ค่าช่องข้อ 4
    st.session_state.ans5_val = ""  # เคลียร์ค่าช่องข้อ 5
    st.session_state.ans6_val = ""  # เคลียร์ค่าช่องข้อ 6
    st.session_state.ans7_val = ""  # เคลียร์ค่าช่องข้อ 7
    st.session_state.start = time.time()  # เริ่มเวลาใหม่
    st.session_state.is_ended = False  # ปิด Dialog


# ----------------------------------------------------
# 📌 ฟังก์ชัน MessageBox (Dialog)
# ----------------------------------------------------
@st.dialog("📊 สรุปผลการเล่นเกม")
def show_result_dialog(ans1, ans2, ans3, ans4, ans5, ans6, ans7):
    st.balloons()
    score = 0

    u_ans1 = ans1.strip().lower()
    u_ans2 = ans2.strip().lower()
    u_ans3 = ans3.strip().lower()
    u_ans4 = ans4.strip().lower()
    u_ans5 = ans5.strip().lower()
    u_ans6 = ans6.strip().lower() 
    u_ans7 = ans7.strip().lower()
    # ตรวจข้อ 1
    if u_ans1 == "ขี้บนหลังคา":
        st.success("✅ ข้อ 1: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 1: ยังไม่ถูกต้อง (คุณตอบ '{u_ans1}')")

    # ตรวจข้อ 2
    if u_ans2 == "ผักบุ้งโหรงเหรง":
        st.success("✅ ข้อ 2: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 2: ยังไม่ถูกต้อง (คุณตอบ '{u_ans2}')")

    # ✏️ [พื้นที่สำหรับนักเรียน]: เพิ่มตรวจข้อ 3, 4 ตรงนี้
    
    if u_ans3 == "งูเห็นนมไก่":
        st.success("✅ ข้อ 3: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 3: ยังไม่ถูกต้อง (คุณตอบ '{u_ans3}')")
    if u_ans4 == "จระเข้":
        st.success("✅ ข้อ 4: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 4: ยังไม่ถูกต้อง (คุณตอบ '{u_ans4}')")
    if u_ans5 == "เท้า":
        st.success("✅ ข้อ 5: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 5: ยังไม่ถูกต้อง (คุณตอบ '{u_ans5}')")
    if u_ans6 == "หยก":
        st.success("✅ ข้อ 6: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 6: ยังไม่ถูกต้อง (คุณตอบ '{u_ans6}')")
    if u_ans7 == "ปลา":
        st.success("✅ ข้อ 7: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 7: ยังไม่ถูกต้อง (คุณตอบ '{u_ans7}')")

    st.info(f"🏆 ได้คะแนนรวม: {score} คะแนน")

    if score == 7:
      st.success("เก่งมาก🎉 ")
    elif score >= 4 and score <= 6:
      st.info("พยายามอีกนิดนะ ใกล้เต็มแล้ว!️‍🔥")
    elif score == 3:
      st.info("มาได้ครึ่งทางแล้ว! พยายามอีกหน่อยนะ!💪 ")
    elif score >= 1 and score <= 2:
      st.info("ลองเล่นอีกสักครั้ง..⭐ ")
    else:
      st.error("คุณแพ้แล้ว😭")





# ----------------------------------------------------
# 1. ปุ่มเริ่มเล่นเกม
# ----------------------------------------------------
st.button("🎮 เริ่มเล่นเกม", on_click=reset_game)

# 2. แถบแสดงเวลานับถอยหลัง
if "start" in st.session_state and not st.session_state.get("is_ended", False):
    time_left = int(90 - (time.time() - st.session_state.start))

    if time_left > 0:
        st.error(f"⏳ เหลือเวลา: {time_left} วินาที")
    else:
        st.session_state.is_ended = True
        st.rerun()

st.divider()

# 3. ช่องรับคำตอบ (ใช้ value ผูกกับตัวแปรตรงๆ เพื่อสั่งเคลียร์ได้)
ans1 = st.text_input(
    "ข้อ 1: กินบนเรือน ____ 🏠(หมายถึง ต่างฝ่ายต่างรู้ความลับของกันและกัน) ",
    value=st.session_state.ans1_val,
)
ans2 = st.text_input(
    "ข้อ 2: น้ำท่วมทุ่ง____ 🌾🍃 (หมายถึง พูดมาก แต่มีเนื้อหาสาระน้อยหรือไม่ได้ใจความสำคัญ)",
    value=st.session_state.ans2_val,
)
ans3 = st.text_input(
    "ข้อ 3:ไก่เห็นตีนงู ____🐓🐍",
    value=st.session_state.ans3_val,
)
ans4 = st.text_input(
    "ข้อ 4: สอน__ว่ายน้ำ🐊(หมายถึง การไปชี้แนะในสิ่งทักษะที่ผู้รับฟังมีความเชี่ยวชาญในเรื่องนั้นดีอยู่แล้ว )",
    value=st.session_state.ans4_val,
)
ans5 = st.text_input(
    "ข้อ 5: แกว่ง__หาเสี้ยน🦶(หมายถึง การอยู่ดีไม่ว่าดีแต่กลับไปหาเรื่องเดือดร้อนใส่ตัว)",
    value=st.session_state.ans5_val,
)
ans6 = st.text_input(
    "ข้อ 6:กิ่งทองใบ__ 🟢(หมายถึง คู่รักที่มีความเหมาะสมกันมากในทุก ๆ ด้าน)",
    value=st.session_state.ans6_val,
)

ans7 = st.text_input(
    "ข้อ 7: จับ__สองมือ🫱🐟🫲(หมายถึง การทำอะไรสองอย่างพร้อม ๆ กันในเวลาเดียวกัน ทำให้ผลลัพธ์ออกมาไม่ดีสักอย่าง)",
    value=st.session_state.ans7_val,
)
# อัปเดตค่าล่าสุดเข้าตัวแปร
st.session_state.ans1_val = ans1
st.session_state.ans2_val = ans2
st.session_state.ans3_val = ans3
st.session_state.ans4_val = ans4
st.session_state.ans5_val = ans5
st.session_state.ans6_val = ans6
st.session_state.ans7_val = ans7

# 4. ปุ่มส่งคำตอบ
if "start" in st.session_state and not st.session_state.get("is_ended", False):
    if st.button("📥 ส่งคำตอบ"):
        st.session_state.is_ended = True
        st.rerun()

    time.sleep(1)
    st.rerun()

# 5. แสดง Dialog ผลลัพธ์
if st.session_state.get("is_ended", False):
    show_result_dialog(ans1,ans2,ans3,ans4,ans5,ans6,ans7)

st.divider()

