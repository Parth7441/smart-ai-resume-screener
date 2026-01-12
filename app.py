
import streamlit as st
from resume_parser import extract_text_from_pdf
from text_preprocessing import clean_text
from skill_matcher import extract_skills, calculate_match_score
from skills import SKILL_SET

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Smart AI Resume Screener",
    layout="wide"
)

st.title("🧠 Smart AI Resume Screener")
st.write("AI-powered resume screening using NLP and skill matching")

# ---------- INPUT SECTION ----------
col1, col2 = st.columns(2)

with col1:
    uploaded_file = st.file_uploader("📄 Upload Resume (PDF)", type=["pdf"])

with col2:
    job_description = st.text_area(
        "📝 Paste Job Description",
        height=180,
        placeholder="Paste the job description here..."
    )

# ---------- PROCESSING ----------
if uploaded_file and job_description:
    # Resume processing
    resume_text = extract_text_from_pdf(uploaded_file)
    resume_tokens = clean_text(resume_text)
    resume_skills = extract_skills(resume_tokens, SKILL_SET)

    # Job description processing
    jd_tokens = clean_text(job_description)
    jd_skills = extract_skills(jd_tokens, SKILL_SET)

    # Match score
    score, matched_skills = calculate_match_score(resume_skills, jd_skills)

    st.divider()

    # ---------- RESULTS ----------
    col3, col4, col5 = st.columns(3)

    with col3:
        st.subheader("📌 Resume Skills")
        st.write(resume_skills)

    with col4:
        st.subheader("📌 Job Required Skills")
        st.write(jd_skills)

    with col5:
        st.subheader("✅ Matched Skills")
        st.write(matched_skills)

    st.success(f"🎯 Match Score: {score}%")

    # ---------- VISUALIZATION ----------
    st.subheader("📊 Skill Match Overview")
    st.progress(int(score))

    # ---------- DOWNLOADABLE REPORT ----------
    report = f"""
SMART AI RESUME SCREENER REPORT
--------------------------------

Match Score: {score}%

Resume Skills:
{', '.join(resume_skills)}

Job Description Skills:
{', '.join(jd_skills)}

Matched Skills:
{', '.join(matched_skills)}
"""

    st.download_button(
        label="⬇️ Download Screening Report",
        data=report,
        file_name="resume_screening_report.txt",
        mime="text/plain"
    )
import streamlit as st
from resume_parser import extract_text_from_pdf
from text_preprocessing import clean_text
from skill_matcher import extract_skills, calculate_match_score
from skills import SKILL_SET

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Smart AI Resume Screener",
    layout="wide"
)

st.title("🧠 Smart AI Resume Screener")
st.write("AI-powered resume screening using NLP and skill matching")

# ---------- INPUT SECTION ----------
col1, col2 = st.columns(2)

with col1:
    uploaded_file = st.file_uploader("📄 Upload Resume (PDF)", type=["pdf"])

with col2:
    job_description = st.text_area(
        "📝 Paste Job Description",
        height=180,
        placeholder="Paste the job description here..."
    )

# ---------- PROCESSING ----------
if uploaded_file and job_description:
    # Resume processing
    resume_text = extract_text_from_pdf(uploaded_file)
    resume_tokens = clean_text(resume_text)
    resume_skills = extract_skills(resume_tokens, SKILL_SET)

    # Job description processing
    jd_tokens = clean_text(job_description)
    jd_skills = extract_skills(jd_tokens, SKILL_SET)

    # Match score
    score, matched_skills = calculate_match_score(resume_skills, jd_skills)

    st.divider()

    # ---------- RESULTS ----------
    col3, col4, col5 = st.columns(3)

    with col3:
        st.subheader("📌 Resume Skills")
        st.write(resume_skills)

    with col4:
        st.subheader("📌 Job Required Skills")
        st.write(jd_skills)

    with col5:
        st.subheader("✅ Matched Skills")
        st.write(matched_skills)

    st.success(f"🎯 Match Score: {score}%")

    # ---------- VISUALIZATION ----------
    st.subheader("📊 Skill Match Overview")
    st.progress(int(score))

    # ---------- DOWNLOADABLE REPORT ----------
    report = f"""
SMART AI RESUME SCREENER REPORT
--------------------------------

Match Score: {score}%

Resume Skills:
{', '.join(resume_skills)}

Job Description Skills:
{', '.join(jd_skills)}

Matched Skills:
{', '.join(matched_skills)}
"""

    st.download_button(
        label="⬇️ Download Screening Report",
        data=report,
        file_name="resume_screening_report.txt",
        mime="text/plain"
    )

