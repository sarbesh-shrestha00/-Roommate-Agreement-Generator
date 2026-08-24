## the roommate agreement

# 🏠 ROOMMATE AGREEMENT GENERATOR

```text
┌──────────────────────────────────────────────────────────────┐
│                 ROOMMATE AGREEMENT GENERATOR                 │
│                                                              │
│  > AI-powered roommate agreement creation                   │
│  > Built with Streamlit + Google Gemini                      │
│  > Generate → Preview → Download PDF                        │
└──────────────────────────────────────────────────────────────┘
```

## `> PROJECT STATUS`

```text
[✓] Streamlit interface
[✓] Gemini AI integration
[✓] Roommate management
[✓] Quiet-hour configuration
[✓] Guest rules
[✓] Automatic chore distribution
[✓] Shared expense calculation
[✓] AI-generated agreement
[✓] PDF generation
[✓] PDF download
[✓] GitHub-ready
```

---

## `> ABOUT`

The **Roommate Agreement Generator** is an AI-powered web application that helps roommates create a customized agreement based on their shared living preferences.

Instead of manually writing rules, users enter information about:

```text
Roommates
    ↓
Quiet Hours
    ↓
Guest Rules
    ↓
Chores
    ↓
Shared Expenses
    ↓
Agreement Style
```

The application sends these details to **Google Gemini**, which generates a structured roommate agreement.

The final agreement can be viewed directly inside the application and downloaded as a PDF.

---

## `> FEATURES`

```text
01  👥 Multiple roommates
02  🔇 Custom quiet hours
03  👨‍👩‍👧 Guest and overnight guest rules
04  🧹 Automatic chore distribution
05  💰 Shared expense calculation
06  🎭 Multiple agreement styles
07  🤖 Gemini AI agreement generation
08  📜 Agreement preview
09  📥 PDF download
```

---

## `> TECHNOLOGY STACK`

```text
Frontend / UI
    └── Streamlit

AI
    └── Google Gemini API

Backend Logic
    └── Python

PDF Generation
    └── ReportLab

Configuration
    └── Streamlit Secrets

Deployment
    └── Streamlit Community Cloud
```

---

## `> ARCHITECTURE`

```text
                 ┌─────────────────────┐
                 │       USER          │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │    STREAMLIT UI     │
                 │                     │
                 │ • Roommates         │
                 │ • Quiet Hours       │
                 │ • Guest Rules       │
                 │ • Chores            │
                 │ • Expenses          │
                 │ • Agreement Style   │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │   PYTHON LOGIC      │
                 │                     │
                 │ • Validate input    │
                 │ • Split expenses    │
                 │ • Assign chores     │
                 │ • Build prompt      │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │    GEMINI API       │
                 │                     │
                 │ Generate Agreement  │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │ GENERATED AGREEMENT │
                 └──────────┬──────────┘
                            │
                    ┌───────┴────────┐
                    ▼                ▼
             ┌─────────────┐  ┌─────────────┐
             │  Streamlit  │  │  ReportLab  │
             │   Preview   │  │ PDF Builder │
             └─────────────┘  └──────┬──────┘
                                      │
                                      ▼
                              ┌───────────────┐
                              │  PDF DOWNLOAD │
                              └───────────────┘
```

---

## `> DATA FLOW`

```text
USER INPUT
   │
   ├── Roommate names
   ├── Quiet hours
   ├── Guest preferences
   ├── Chore preferences
   ├── Shared expenses
   └── Agreement style
           │
           ▼
     PYTHON PROCESSING
           │
           ├── Equal expense calculation
           ├── Chore assignment
           └── Prompt construction
           │
           ▼
       GEMINI API
           │
           ▼
   AI GENERATED AGREEMENT
           │
           ├───────────────► Streamlit Preview
           │
           ▼
      REPORTLAB
           │
           ▼
       PDF OUTPUT
```

---

## `> API INTEGRATION`

The application uses Google's Gemini API through the `google-genai` Python SDK.

The API key is loaded from Streamlit Secrets:

```python
client = genai.Client(
    api_key=st.secrets["GEMINI_API_KEY"]
)
```

The user's form data is converted into a structured prompt and sent to Gemini.

```python
response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=prompt
)
```

The generated response is then displayed in Streamlit and passed to ReportLab for PDF generation.

### Security

API credentials are never stored directly in the source code.

```text
.streamlit/secrets.toml
        │
        └── GEMINI_API_KEY
```

The secrets file is excluded through `.gitignore`.

---

## `> PROJECT MODULES`

### 01 — Input Module

Collects roommate information and agreement preferences.

### 02 — Chore Module

Automatically distributes predefined chores among roommates.

### 03 — Expense Module

Calculates equal shares for:

```text
Rent
Wi-Fi
Electricity
```

### 04 — Prompt Module

Combines all user inputs into a structured Gemini prompt.

### 05 — AI Generation Module

Sends the prompt to Gemini and receives the generated agreement.

### 06 — PDF Module

Converts the generated agreement into a downloadable PDF using ReportLab.

### 07 — UI Module

Displays the form, generation status, agreement preview, and download button.

---

## `> INSTALLATION`

### Clone repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd roommate-agreement-generator
```

### Create virtual environment

```bash
python -m venv .venv
```

### Activate environment — macOS/Linux

```bash
source .venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## `> CONFIGURATION`

Create:

```text
.streamlit/secrets.toml
```

Add:

```toml
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"
```

Never commit this file to GitHub.

---

## `> RUN LOCALLY`

```bash
streamlit run app001.py
```

The application will open in your browser.

---

## `> 🌐 Live Application
[Click here to view the Streamlit Live App](https://shhfpcuu4ybsxhtvyiem9x.streamlit.app)




---

## `> GITHUB`

```text
📦 SOURCE CODE
https://github.com/sarbesh-shrestha00/-Roommate-Agreement-Generator```

---

## `> PROJECT STRUCTURE`

```text
roommate-agreement-generator/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── .streamlit/
│   └── secrets.toml
│
└── docs/
    └── system-design.md
```

---

## `> DISCLAIMER`

```text
This application generates agreements using artificial intelligence.

The generated agreement is for informational and practical
roommate-planning purposes only.

It is NOT professional legal advice.
```

---

## `> AUTHOR`

```text
Developer : YOUR NAME
Project   : Roommate Agreement Generator
Stack     : Python | Streamlit | Gemini AI | ReportLab
```

```text
┌──────────────────────────────────────────────────────────────┐
│                     END OF README                            │
│                                                              │
│              > Generate better agreements.                   │
│              > Live together. Live better.                   │
└──────────────────────────────────────────────────────────────┘
```
