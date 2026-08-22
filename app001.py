
import streamlit as st
from google import genai
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from io import BytesIO






# -----------------------------
# PAGE
# -----------------------------

st.title("🏠 Roommate Agreement Generator")
st.write("Fill in the details and generate your agreement using Gemini AI.")


# -----------------------------
# NUMBER OF ROOMMATES
# -----------------------------

num_roommates = st.number_input(
    "Number of roommates",
    min_value=2,
    max_value=6,
    value=2
)


# -----------------------------
# FORM
# -----------------------------

with st.form("roommate_form"):

    # Roommates
    st.subheader("👥 Roommates")

    roommates = []

    for i in range(num_roommates):

        name = st.text_input(
            f"Roommate {i + 1}",
            value=f"Roommate {i + 1}"
        )

        roommates.append(name)

    # -------------------------
    # QUIET HOURS
    # -------------------------

    st.subheader("🔇 Quiet Hours")

    col1, col2 = st.columns(2)

    with col1:
        quiet_start = st.time_input("Start")

    with col2:
        quiet_end = st.time_input("End")

    weekdays = st.checkbox("Weekdays", value=True)
    weekends = st.checkbox("Weekends", value=True)

    # -------------------------
    # GUESTS
    # -------------------------

    st.subheader("👨‍👩‍👧 Guest Rules")

    guests = st.radio(
        "Are guests allowed?",
        ["Yes", "No"],
        horizontal=True
    )

    overnight = st.radio(
        "Are overnight guests allowed?",
        ["Yes", "No"],
        horizontal=True
    )

    max_guests = st.number_input(
        "Maximum guests",
        min_value=1,
        max_value=10,
        value=2
    )

    notice = st.selectbox(
        "Advance notice",
        ["None", "12 hours", "24 hours", "48 hours"]
    )

    # -------------------------
    # CHORES
    # -------------------------

    st.subheader("🧹 Chores")

    chores = [
        "Cleaning",
        "Kitchen",
        "Bathroom",
        "Garbage",
        "Floor cleaning",
        "Dusting"
    ]

    # Equal distribution
    chore_distribution = {}

    for i, roommate in enumerate(roommates):

        roommate_chores = []

        for j, chore in enumerate(chores):

            if j % num_roommates == i:
                roommate_chores.append(chore)

        chore_distribution[roommate] = roommate_chores

        st.write(
            f"**{roommate}:** "
            + ", ".join(roommate_chores)
        )

    # -------------------------
    # EXPENSES
    # -------------------------

    st.subheader("💰 Shared Expenses")

    rent = st.number_input(
        "Monthly Rent (₹)",
        min_value=0.0
    )

    wifi = st.number_input(
        "Wi-Fi (₹)",
        min_value=0.0
    )

    electricity = st.number_input(
        "Electricity (₹)",
        min_value=0.0
    )

    # Equal split
    rent_each = rent / num_roommates
    wifi_each = wifi / num_roommates
    electricity_each = electricity / num_roommates

    st.write(
        f"Each roommate pays: "
        f"Rent ₹{rent_each}, "
        f"Wi-Fi ₹{wifi_each}, "
        f"Electricity ₹{electricity_each}"
    )

    # -------------------------
    # STYLE
    # -------------------------

    st.subheader("🎭 Agreement Style")

    style = st.radio(
        "Choose style",
        [
            "Professional",
            "Friendly",
            "Legally-sounding + humorous"
        ]
    )

    # -------------------------
    # BUTTON
    # -------------------------

    submitted = st.form_submit_button(
        "🤖 Generate Agreement"
    )


# -----------------------------
# GEMINI
# -----------------------------

if submitted:

    # Gemini API
    client = genai.Client(
        api_key=st.secrets["GEMINI_API_KEY"]
    )

    prompt = f"""
Create a roommate agreement using the following information.

Agreement style:
{style}

Roommates:
{roommates}

Quiet hours:
{quiet_start} to {quiet_end}

Quiet hours apply on:
Weekdays = {weekdays}
Weekends = {weekends}

Guests allowed:
{guests}

Overnight guests:
{overnight}

Maximum guests:
{max_guests}

Advance notice:
{notice}

Chore distribution:
{chore_distribution}

Shared expenses:
Rent = ₹{rent}
Wi-Fi = ₹{wifi}
Electricity = ₹{electricity}

Each roommate pays equally:
Rent = ₹{rent_each:.2f}
Wi-Fi = ₹{wifi_each:.2f}
Electricity = ₹{electricity_each:.2f}

Write a complete roommate agreement.

Include:
1. Roommates
2. Quiet hours
3. Guest rules
4. Chores
5. Shared expenses
6. Cleanliness
7. Conflict resolution
8. Agreement changes

Use the selected agreement style.

At the end add:
"This agreement was generated using AI and is not professional legal advice."
"""

    with st.spinner("Generating agreement..."):

        response = client.models.generate_content(
            model="gemini-3.7-flash",
            contents=prompt
        )

        agreement = response.text

    # -----------------------------
    # SHOW AGREEMENT
    # -----------------------------

    st.success("Agreement generated!")

    st.subheader("📜 Your Agreement")

    st.markdown(agreement)

    # -----------------------------
    # PDF
    # -----------------------------

    pdf = BytesIO()

    document = SimpleDocTemplate(
        pdf,
        pagesize=A4
    )

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            "ROOMMATE AGREEMENT",
            styles["Title"]
        )
    )

    content.append(Spacer(1, 20))

    # Convert Gemini text into PDF paragraphs
    for line in agreement.split("\n"):

        if line.strip():

            content.append(
                Paragraph(
                    line.replace("**", ""),
                    styles["BodyText"]
                )
            )

            content.append(Spacer(1, 8))

    document.build(content)

    pdf.seek(0)

    # -----------------------------
    # DOWNLOAD
    # -----------------------------

    st.download_button(
        "📥 Download PDF",
        data=pdf,
        file_name="roommate_agreement.pdf",
        mime="application/pdf"
    )