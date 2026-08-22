
import streamlit as st




st.title("The roommate agreement generator")

st.write("fill the form below")
num_roommates=st.number_input("enter the no of roomates",max_value=6,min_value=2)
    

with st.form(" user detail form"):
    
    st.subheader("Roomates")
    Roommates=[]
   
    cols = st.columns(min(int(num_roommates), 3))
    for i in range(int(num_roommates)):
        col = cols[i % 3]
        name = col.text_input(f"Roommate {i + 1}", value=f"Roommate {i + 1}", key=f"rm_{i}")
        Roommates.append(name)

    st.divider()

    # ─── 🔇 2. QUIET HOURS ───
    st.subheader("🔇 2. Quiet Hours")
    col1, col2 = st.columns(2)
    with col1:
        quiet_start = st.time_input("Start", value=None)  # Defaults or set explicit time
    with col2:
        quiet_end = st.time_input("End", value=None)

    col_chk1, col_chk2 = st.columns(2)
    with col_chk1:
        quiet_weekdays = st.checkbox("Weekdays", value=True)
    with col_chk2:
        quiet_weekends = st.checkbox("Weekends", value=True)

    st.divider()

    # ─── 👨‍👩‍👧 3. GUEST RULES ───
    st.subheader("👨‍👩‍👧 3. Guest Rules")
    g_col1, g_col2 = st.columns(2)
    with g_col1:
        guests_allowed = st.radio("Guests allowed?", ["Yes", "No"], horizontal=True)
        overnight_guests = st.radio("Overnight guests?", ["Yes", "No"], index=1, horizontal=True)
    with g_col2:
        max_guests = st.number_input("Maximum guests", min_value=1, max_value=10, value=2)
        advance_notice = st.selectbox("Advance notice", ["None", "12 hours", "24 hours", "48 hours"], index=2)

    st.divider()

    # ─── 🧹 4. CHORE DISTRIBUTION ───
    st.subheader("🧹 4. Chore Distribution")
    ch_col1, ch_col2, ch_col3 = st.columns(3)
    with ch_col1:
        cleaning_person = st.selectbox("Cleaning", options=Roommates, index=0)
    with ch_col2:
        kitchen_person = st.selectbox("Kitchen", options=Roommates, index=min(1, len(Roommates)-1))
    with ch_col3:
        garbage_person = st.selectbox("Garbage", options=Roommates, index=min(2, len(Roommates)-1))

    st.divider()

    # ─── 💰 5. SHARED EXPENSES ───
    st.subheader("💰 5. Shared Expenses")
    e_col1, e_col2, e_col3 = st.columns(3)
    with e_col1:
        rent_split = st.text_input("Rent split", value="50 / 50")
    with e_col2:
        wifi_split = st.text_input("Wi-Fi split", value="50 / 50")
    with e_col3:
        elec_split = st.text_input("Electricity split", value="50 / 50")

    st.divider()

    # ─── 🎭 AGREEMENT STYLE ───
    st.subheader("🎭 Agreement Style")
    style = st.radio(
        "Select Tone:",
        ["Professional", "Friendly", "Legally-sounding + humorous"],
        index=2,
        label_visibility="collapsed"
    )

    st.write("")
    # Form submission button
    submitted = st.form_submit_button("Generate Agreement", use_container_width=True)

    
# ─── OUTPUT PROCESSING ───
if submitted:
       st.success("Agreement Generated Successfully!")