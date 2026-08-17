import time
import streamlit as st

st.title("⏱️ เกมเติมศัพท์จับเวลา")

# 1. กำหนดค่าเริ่มต้นใน session_state ถ้ายังไม่มี
if "ans1_val" not in st.session_state:
    st.session_state.ans1_val = ""
if "ans2_val" not in st.session_state:
    st.session_state.ans2_val = ""


# 📌 ฟังก์ชันเคลียร์ค่าเมื่อกดปุ่มเริ่มใหม่
def reset_game():
    st.session_state.ans1_val = ""  # เคลียร์ค่าช่องข้อ 1
    st.session_state.ans2_val = ""  # เคลียร์ค่าช่องข้อ 2
    st.session_state.start = time.time()  # เริ่มเวลาใหม่
    st.session_state.is_ended = False  # ปิด Dialog


# ----------------------------------------------------
# 📌 ฟังก์ชัน MessageBox (Dialog)
# ----------------------------------------------------
@st.dialog("📊 สรุปผลการเล่นเกม")
def show_result_dialog(ans1, ans2):
    st.balloons()
    score = 0

    u_ans1 = ans1.strip().lower()
    u_ans2 = ans2.strip().lower()

    # ตรวจข้อ 1
    if u_ans1 == "apple":
        st.success("✅ ข้อ 1: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 1: ยังไม่ถูกต้อง (คุณตอบ '{u_ans1}')")

    # ตรวจข้อ 2
    if u_ans2 == "fish":
        st.success("✅ ข้อ 2: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 2: ยังไม่ถูกต้อง (คุณตอบ '{u_ans2}')")

    # ✏️ [พื้นที่สำหรับนักเรียน]: เพิ่มตรวจข้อ 3, 4 ตรงนี้

    st.info(f"🏆 ได้คะแนนรวม: {score} คะแนน")

    if score == 2:
        st.success("🎉 You win!")
    else:
        st.error("💀 You lose!")


# ----------------------------------------------------
# 1. ปุ่มเริ่มเล่นเกม
# ----------------------------------------------------
st.button("🎮 เริ่มเล่นเกม", on_click=reset_game)

# 2. แถบแสดงเวลานับถอยหลัง
if "start" in st.session_state and not st.session_state.get("is_ended", False):
    time_left = int(30 - (time.time() - st.session_state.start))

    if time_left > 0:
        st.error(f"⏳ เหลือเวลา: {time_left} วินาที")
    else:
        st.session_state.is_ended = True
        st.rerun()

st.divider()

# 3. ช่องรับคำตอบ (ใช้ value ผูกกับตัวแปรตรงๆ เพื่อสั่งเคลียร์ได้)
ans1 = st.text_input(
    "ข้อ 1: An `a _ _ l e` a day keeps the doctor away. 🍎",
    value=st.session_state.ans1_val,
)
ans2 = st.text_input(
    "ข้อ 2: Cats love to eat `f _ s h`. 🐟",
    value=st.session_state.ans2_val,
)

# อัปเดตค่าล่าสุดเข้าตัวแปร
st.session_state.ans1_val = ans1
st.session_state.ans2_val = ans2

# ✏️ [พื้นที่สำหรับนักเรียน]: เพิ่มข้อ 3, 4 ตรงนี้


# 4. ปุ่มส่งคำตอบ
if "start" in st.session_state and not st.session_state.get("is_ended", False):
    if st.button("📥 ส่งคำตอบ"):
        st.session_state.is_ended = True
        st.rerun()

    time.sleep(1)
    st.rerun()

# 5. แสดง Dialog ผลลัพธ์
if st.session_state.get("is_ended", False):
    show_result_dialog(ans1, ans2)

st.divider()
st.write("นางสาวจารุณี รุ่งเรือง เลขที่ 19 ม.4/14")import streamlit as st

# จุดที่ 1: เพิ่มการกำหนดค่าเริ่มต้นใน session_state
if 'ans3_val' not in st.session_state:
    st.session_state.ans3_val = ""
if 'ans4_val' not in st.session_state:
    st.session_state.ans4_val = ""

# จุดที่ 2: เพิ่มการเคลียร์ค่าเมื่อกดปุ่มเริ่มใหม่ (ในปุ่ม Reset/Play Again)
if st.button("เริ่มใหม่ / Reset"):
    st.session_state.ans3_val = ""
    st.session_state.ans4_val = ""

# จุดที่ 6: เพิ่มช่องรับคำตอบ ans3 และ ans4
ans3 = st.text_input("ข้อ 3: 🍎 A_p_e", value=st.session_state.ans3_val)
ans4 = st.text_input("ข้อ 4: 🍌 B_n_n_a", value=st.session_state.ans4_val)

# จุดที่ 7: เพิ่มการอัปเดตค่าล่าสุดเข้าตัวแปร st.session_state
st.session_state.ans3_val = ans3
st.session_state.ans4_val = ans4

# ปุ่มส่งคำตอบ / ตรวจผล
if st.button("ตรวจคำตอบ 🎯"):
    score = 0
    
    # (สมมติข้อ 1 และ 2 ตรวจสอบตรงนี้)
    # ...
    
    # จุดที่ 3 & 4: สรุปผลและการตรวจข้อ 3 และข้อ 4
    u_ans3 = ans3.strip().lower()
    u_ans4 = ans4.strip().lower()

    if u_ans3 == "apple":
        score += 1
    if u_ans4 == "banana":
        score += 1

    # จุดที่ 5: เพิ่มคะแนนเป็น score == 4 (รวม 4 ข้อ)
    if score == 4:
        st.balloons()
        st.success("🎉 สุดยอดมาก! คุณตอบถูกครบทั้ง 4 ข้อ!")
    else:
        st.info(f"คุณได้คะแนน {score} / 4 คะแนน")

    # จุดที่ 8: เพิ่มการแสดง Dialog ผลลัพธ์ ans3, ans4
    st.write(f"คำตอบข้อ 3 ที่คุณตอบ: {ans3}")
    st.write(f"คำตอบข้อ 4 ที่คุณตอบ: {ans4}")

st.write("นางสาวจารุณี รุ่งเรือง เลขที่ 19 ม.4/14")

