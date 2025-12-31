import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Aniket V. Walunj | Portfolio",
    layout="centered"
)

# Custom CSS
st.markdown("""
<style>
/* Center content vertically & horizontally */
.main {
    height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
}

/* Main card */
.card {
    max-width: 560px;
    padding: 48px 44px;
    border-radius: 16px;
    text-align: center;
    background: #ffffff;
    box-shadow: 0 20px 50px rgba(0,0,0,0.12);
    animation: slideUp 1s ease;
}

/* Name */
.name {
    font-size: 16px;
    color: #475569;
    font-weight: 600;
    margin-bottom: 6px;
}

/* Title */
.title {
    font-size: 32px;
    font-weight: 800;
    color: #0f172a;
    margin-bottom: 14px;
}

/* Divider */
.divider {
    width: 60px;
    height: 3px;
    background: #0f172a;
    margin: 18px auto;
    border-radius: 2px;
}

/* Description */
.desc {
    font-size: 17px;
    color: #475569;
    line-height: 1.7;
}

/* Signature */
.signature {
    margin-top: 26px;
    font-size: 14px;
    color: #64748b;
    font-style: italic;
}

/* Page background */
body {
    background: linear-gradient(180deg, #f8fafc, #eef2f7);
}

/* Animation */
@keyframes slideUp {
    from {
        opacity: 0;
        transform: translateY(35px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}
</style>
""", unsafe_allow_html=True)

# Page Content
st.markdown("""
<div class="card">
    <div class="name">Aniket V. Walunj</div>
    <div class="title">Portfolio Under Maintenance</div>
    <div class="divider"></div>
    <div class="desc">
        I’m currently refining my personal portfolio to better showcase
        my projects, skills, and professional journey in data analytics
        and technology.
        <br><br>
        This space will be live very soon with meaningful work and insights.
    </div>
    <div class="signature">
        — See you soon 🚀
    </div>
</div>
""", unsafe_allow_html=True)
