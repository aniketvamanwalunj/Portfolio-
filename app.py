import streamlit as st

st.set_page_config(page_title="Aniket V. Walunj | Portfolio", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css');
* {font-family: 'Inter', sans-serif;}
body {background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);}
.section {background: rgba(255,255,255,0.95);backdrop-filter: blur(10px);padding: 40px;border-radius: 20px;margin-bottom: 30px;box-shadow: 0 20px 40px rgba(0,0,0,0.1);}
.title {font-size: 48px;font-weight: 800;background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);-webkit-background-clip: text;-webkit-text-fill-color: transparent;background-clip: text;}
.subtitle {color: #64748b;font-size: 18px;margin-top: 12px;}
.h2 {font-size: 28px;font-weight: 700;color: #1e293b;margin-bottom: 20px;position: relative;}
.h2::after {content: '';position: absolute;bottom: -8px;left: 0;width: 60px;height: 4px;background: linear-gradient(135deg, #667eea, #764ba2);border-radius: 2px;}
.text {font-size: 16px;color: #334155;line-height: 1.8;}
.list li {margin-bottom: 12px;color: #334155;font-size: 15px;}
.entry-title {font-size: 20px;font-weight: 700;color: #1e293b;margin-bottom: 8px;}
.entry-sub {font-size: 15px;color: #64748b;margin-bottom: 12px;background: linear-gradient(135deg, #f0f9ff, #e0f2fe);padding: 8px 16px;border-radius: 25px;display: inline-block;}
.skill-tag {background: linear-gradient(135deg, #667eea, #764ba2);color: white;padding: 6px 16px;border-radius: 25px;font-size: 14px;font-weight: 500;margin: 4px 4px 4px 0;display: inline-block;}
.icon-link {font-size: 24px;margin: 0 15px;color: #64748b;transition: all 0.3s ease;display: inline-block;}
.icon-link:hover {color: #667eea !important;transform: scale(1.2);}
.cert-badge {background: linear-gradient(135deg, #10b981, #059669);color: white;padding: 4px 12px;border-radius: 20px;font-size: 13px;font-weight: 600;margin-right: 8px;}
.project-link {background: linear-gradient(135deg, #3b82f6, #1d4ed8);color: white;padding: 8px 16px;border-radius: 25px;font-size: 14px;font-weight: 600;text-decoration: none;display: inline-block;margin-top: 8px;transition: all 0.3s ease;}
.project-link:hover {background: linear-gradient(135deg, #1d4ed8, #1e3a8a);transform: translateY(-2px);}
.volunteer-badge {background: linear-gradient(135deg, #f59e0b, #d97706);color: white;padding: 6px 12px;border-radius: 20px;font-size: 13px;font-weight: 600;margin-right: 12px;}
</style>
""", unsafe_allow_html=True)

# HEADER
st.markdown("""
<div class="section">
<div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 20px;">
    <div>
        <div class="title">Aniket V. Walunj</div>
        <div class="subtitle">Data Analyst & Scientist | Pune, Maharashtra | +91 9112990772</div>
    </div>
    <div style="display: flex; gap: 20px;">
        <a href="mailto:aniketvamanwalunj@gmail.com" class="icon-link" title="Email"><i class="fas fa-envelope"></i></a>
        <a href="https://linkedin.com/in/aniketwalunj" class="icon-link" target="_blank" title="LinkedIn"><i class="fab fa-linkedin-in"></i></a>
        <a href="https://github.com/aniketvamanwalunj" class="icon-link" target="_blank" title="GitHub"><i class="fab fa-github"></i></a>
    </div>
</div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="section"><div class="h2">Summary</div><div class="text">Passionate data analyst skilled in Excel, Power BI, SQL, NoSQL, Python, and data visualization. Currently pursuing P.G. Diploma in Cyber & National Security while building advanced ML forecasting systems, web applications, and leading community initiatives.</div></div>', unsafe_allow_html=True)

st.markdown("""
<div class="section">
  <div class="h2">Experience</div>

  <div class="entry-title">Data Analytics Intern</div>
  <div class="entry-sub">
    National Skill Development Corporation (NSDC) |
    <span class="volunteer-badge">Dec 2025 – Feb 2026</span>
    Remote · Pune, Maharashtra, India
  </div>

  <div class="text">
    <ul class="list">
      <li>Applied <b>Python-based analytics</b> to support dynamic pricing and eCommerce decision-making.</li>
      <li>Cleaned, preprocessed, and analyzed real-world <b>pricing and sales datasets</b> using Python and Pandas.</li>
      <li>Performed <b>Exploratory Data Analysis (EDA)</b> to identify trends, seasonality, correlations, and pricing patterns.</li>
      <li>Developed basic <b>predictive models</b> for demand-based and time-series price forecasting.</li>
      <li>Created <b>data visualizations and analytical reports</b> to communicate insights for pricing and revenue optimization.</li>
      <li>Gained hands-on exposure to <b>business analytics, market intelligence, and data-driven strategy formulation</b>.</li>
    </ul>
""", unsafe_allow_html=True)


st.markdown("""
<div class="section">
  <div class="h2">Skills</div>

  <div><b>Programming & Query Languages:</b>
    <span class="skill-tag">Python</span><span class="skill-tag">SQL</span><span class="skill-tag">NoSQL</span>
  </div>

  <div><b>Databases:</b>
    <span class="skill-tag">MySQL</span><span class="skill-tag">MongoDB</span>
  </div>

  <div><b>Data Analysis & BI Tools:</b>
    <span class="skill-tag">MS Excel</span><span class="skill-tag">Power Query</span><span class="skill-tag">Power BI</span>
  </div>


  <div><b>Python Libraries:</b>
    <span class="skill-tag">NumPy</span><span class="skill-tag">Pandas</span><span class="skill-tag">Scikit-learn</span><span class="skill-tag">Matplotlib</span>
  </div>

  <div><b>Platforms & Environments:</b>
    <span class="skill-tag">Jupyter Notebook</span><span class="skill-tag">Google Colab</span><span class="skill-tag">Visual Studio</span>
  </div>

  <div><b>Web & Deployment:</b>
    <span class="skill-tag">Flask</span><span class="skill-tag">HTML/CSS</span><span class="skill-tag">Render</span>
  </div>
</div>
""", unsafe_allow_html=True)



st.markdown("""
<div class="section">
<div class="h2">Education</div>

<div class="entry-title">P.G. Diploma / Advanced Course in Cyber & India's National Security</div>
<div class="entry-sub">Department of Defence and Strategic Studies, Savitribai Phule Pune University | Oct 2025 – Aug 2026</div>
<div class="text">Grade: Pursuing<br>Activities: Cyber Security Workshops, Defence & Strategic Studies Events, Research Methodology Sessions, Guest Lectures, Cyber Lab Work, Case Studies<br><b>Skills:</b> Cyber Security, Cyber Risk Management, Cyber Laws, National Security Strategy, Critical Infrastructure Protection, Intelligence & Threat Analysis</div><br>

<div class="entry-title">Foundation Course – Fast Track – German Level 1</div>
<div class="entry-sub">Department of Foreign Languages, Savitribai Phule Pune University | Jan 2025 – May 2025</div>
<div class="text">Grade: C<br><b>Skills:</b> German Speaking, German Literature</div><br>

<div class="entry-title">B.Sc. Data Science</div>
<div class="entry-sub">Department of Technology, Savitribai Phule Pune University | Sep 2022 – May 2025</div>
<div class="text">Grade: A+, GPA: 8.52<br><b>Skills:</b> Excel, Power Query, Power BI, Python, MySQL, NoSQL, Machine Learning, Deep Learning, Time Series Analysis, AI, Cloud Computing, Big Data Analytics, MLOps</div><br>

<div class="entry-title">HSC (Science – PCMB)</div>
<div class="entry-sub">Agasti College, Akole | Jun 2021 – Mar 2022</div>
<div class="text">Grade: Second Class<br><b>Skills:</b> HTML, JavaScript</div><br>

<div class="entry-title">SSC</div>
<div class="entry-sub">Agasti Vidyalaya, Akole | Jun 2019 – Mar 2020</div>
<div class="text">Grade: First Class with Distinction</div>
</div>
""", unsafe_allow_html=True)

# CORRECTED PROJECTS SECTION - PROPER LINKS & COLORS

st.markdown("""
<div class="section"><div class="h2">Featured Projects</div><div class="entry-title">☀️ Solar Panel Performance Monitoring & Prediction</div><div class="entry-sub">Department of Technology, SPPU | Feb 2025 - May 2025</div><div class="text">Streamlit dashboard for solar power monitoring & forecasting. Features seasonal decomposition, ARIMA/SARIMA, XGBoost, LightGBM, Random Forest, Plotly visualizations & CSV export.<br><b>Tech:</b> Python, Pandas, NumPy, Streamlit, Plotly, ARIMA, SARIMA, XGBoost, LightGBM, scikit-learn, statsmodels</div><div><a href="https://solar-panel-performance-monitoring-and-prediction.streamlit.app/" class="project-link" target="_blank" style="background: linear-gradient(135deg, #10b981, #059669); color: white; padding: 10px 20px; border-radius: 25px; font-weight: 600; text-decoration: none; margin-right: 10px;">🚀 Live Demo</a></div><br><div class="entry-title">💧 Water Resources Management & Prediction</div><div class="entry-sub">Time Series Forecasting | May 2025</div><div class="text">Streamlit app for reservoir level forecasting (97+% accuracy) with ARIMA, geospatial maps, customizable parameters, performance metrics & CSV export.<br><b>Tech:</b> Python, Pandas, NumPy, Matplotlib, Plotly, ARIMA, Statsmodels, scikit-learn, Streamlit</div><div><a href="https://water-resources-management-prediction.streamlit.app/" class="project-link" target="_blank" style="background: linear-gradient(135deg, #10b981, #059669); color: white; padding: 10px 20px; border-radius: 25px; font-weight: 600; text-decoration: none;">🚀 Live Demo</a></div><br><div class="entry-title">📱 DataLens: Smartphone Sales Dashboard</div><div class="entry-sub">Power BI | Mar 2025</div><div class="text">Interactive Power BI dashboard analyzing smartphone sales, profits, brands, discounts & quarterly trends.<br><b>Tech:</b> Power BI, Data Analytics, Business Intelligence</div><div><a href="https://github.com/aniketvamanwalunj/DataLens--Smartphone-Sales-Dashboard" class="project-link" target="_blank" style="background: linear-gradient(135deg, #1f2937, #111827); color: white; padding: 10px 20px; border-radius: 25px; font-weight: 600; text-decoration: none;">📂 GitHub</a></div><br><div class="entry-title">🛡️ Detecting Malware Websites</div><div class="entry-sub">Department of Technology, SPPU | Sep 2024 - Dec 2024</div><div class="text">Flask ML app with TF-IDF + Random Forest (97.11% accuracy) for real-time URL safety detection.<br><b>Tech:</b> Flask, Scikit-learn, TF-IDF, Random Forest, HTML, CSS</div><div><a href="https://detecting-malware-websites-1.onrender.com/" class="project-link" target="_blank" style="background: linear-gradient(135deg, #10b981, #059669); color: white; padding: 10px 20px; border-radius: 25px; font-weight: 600; text-decoration: none; margin-right: 10px;">🚀 Live Demo</a><a href="https://malware-websites-detection-project.onrender.com/" class="project-link" target="_blank" style="background: linear-gradient(135deg, #f59e0b, #d97706); color: white; padding: 10px 20px; border-radius: 25px; font-weight: 600; text-decoration: none; margin-left: 10px;">📋 Details</a></div><br><div class="entry-title">🎬 Sentiment Analysis of Movie Reviews</div><div class="entry-sub">NLP & Streamlit | Jun 2024 - Aug 2024</div><div class="text">Streamlit app with Logistic Regression + TfidfVectorizer (90% accuracy) on IMDB dataset for real-time sentiment analysis.<br><b>Tech:</b> Streamlit, NLP, Scikit-learn, Logistic Regression, TfidfVectorizer</div><div><a href="https://sentiment-analysis-of-movie-reviews.onrender.com/" class="project-link" target="_blank" style="background: linear-gradient(135deg, #10b981, #059669); color: white; padding: 10px 20px; border-radius: 25px; font-weight: 600; text-decoration: none;">🚀 Live Demo</a></div></div>
""", unsafe_allow_html=True)




# NEW VOLUNTEERING SECTION
st.markdown("""
<div class="section">
<div class="h2">Volunteering & Leadership</div>

<div class="entry-title">🎯 Organizing Committee (Tantra Fest) - Puzzle Game Leader</div>
<div class="entry-sub"><span class="volunteer-badge">Feb 2024</span>Department of Technology, SPPU | 1 month</div>
<div class="text">Led team of 10 students for DoT Tantra Fest puzzle game. Managed planning, coordination & execution. Received Certificate of Excellence & Tantra 2024 Memento.<br><b>Skills Gained:</b> Leadership, Team Management, Event Planning</div><br>

<div class="entry-title">📚 Pune Book Festival - Leadership Team</div>
<div class="entry-sub"><span class="volunteer-badge">Dec 2023</span>Pune Book Festival | 1 month</div>
<div class="text">Leadership role in Guinness World Record project. Team recorded 13,696 videos (11,546 finalized) for 'Largest Online Video Album of People Reading'. Managed video recording, data cleaning & duplication handling. Featured in newspaper.<br><b>Results:</b> Guinness World Record submission</div><br>

<div class="entry-title">🌍 MMMD (Meri Maati Mera Desh) - Project Leader</div>
<div class="entry-sub"><span class="volunteer-badge">Oct-Nov 2023</span>Central Government Initiative | 2 months</div>
<div class="text">Led 150 students to capture 25+ lakh photos. Developed Streamlit tools for image cropping, sorting, renaming & duplicate detection. Submitted 10.28 lakh processed images to Guinness World Records. Received certificates from University VC.<br><b>Scale:</b> National initiative, massive dataset processing</div>
</div>
""", unsafe_allow_html=True)

# NEW PUBLICATIONS SECTION
st.markdown("""
<div class="section">
<div class="h2">Publications</div>


<div class="entry-title">📚 Advanced Data-Driven Approach for Forecasting Reservoir Water Levels and Optimizing Water Resource Management Through ARIMA and Geospatial Analytics</div>
<div class="entry-sub"><span class="publication-badge">Oct 17, 2025</span>IJFMR (International Journal for Multidisciplinary Research)</div>
<div class="text">Published research paper presenting ARIMA-based forecasting framework with geospatial analytics for reservoir water level prediction. Developed interactive Streamlit dashboards for policymakers combining time-series modeling with Python visualization tools.<br><b>Impact:</b> Supports sustainable water resource management & decision-making</div>
<div><a href="https://www.ijfmr.com/research-paper.php?id=58189" class="project-link" target="_blank">Read Publication →</a></div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="section">
<div class="h2">Licenses & Certifications</div>
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(350px, 1fr)); gap: 12px;">
<li><span class="cert-badge">Jan 2025</span>Digital Empowerment – Lighthouse Communities Foundation</li>
<li><span class="cert-badge">Aug 2024</span>Google Data Analytics – Google</li>
<li><span class="cert-badge">Aug 2024</span>SQL – MySQL for Data Analytics & BI – Udemy</li>
<li><span class="cert-badge">Jul 2024</span>NLP with Python – Udemy</li>
<li><span class="cert-badge">May 2024</span>Microsoft Excel – Udemy</li>
<li><span class="cert-badge">Sep 2023</span>Machine Learning – NPTEL IIT Kharagpur</li>
</div>
</div>
""", unsafe_allow_html=True)

# FIXED LANGUAGES SECTION - CORRECT COLORS

st.markdown("""
<div class="section"><div class="h2">Languages</div><div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px;"><div style="text-align: center;"><div class="entry-title">🇮🇳 Marathi</div><div style="background: linear-gradient(135deg, #10b981, #059669); color: white; padding: 12px 20px; border-radius: 25px; font-weight: 600; font-size: 15px; margin-top: 8px; display: inline-block;">Native or Bilingual</div></div><div style="text-align: center;"><div class="entry-title">🇮🇳 Hindi</div><div style="background: linear-gradient(135deg, #f59e0b, #d97706); color: white; padding: 12px 20px; border-radius: 25px; font-weight: 600; font-size: 15px; margin-top: 8px; display: inline-block;">Full Professional</div></div><div style="text-align: center;"><div class="entry-title">🇺🇸 English</div><div style="background: linear-gradient(135deg, #3b82f6, #1d4ed8); color: white; padding: 12px 20px; border-radius: 25px; font-weight: 600; font-size: 15px; margin-top: 8px; display: inline-block;">Limited Working</div></div><div style="text-align: center;"><div class="entry-title">🇩🇪 German</div><div style="background: linear-gradient(135deg, #8b5cf6, #7c3aed); color: white; padding: 12px 20px; border-radius: 25px; font-weight: 600; font-size: 15px; margin-top: 8px; display: inline-block;">Elementary</div></div></div></div>
""", unsafe_allow_html=True)


# ADD THIS AT THE VERY END OF YOUR CODE (after Languages section)

# SIMPLE RESUME SECTION
st.markdown("""
<div class="section" style="text-align: center; padding: 30px;">
<div style="font-size: 24px; font-weight: 700; color: #1e293b; margin-bottom: 8px;">📄 Download My Resume</div>
<div style="font-size: 16px; color: #64748b; margin-bottom: 25px;">Latest PDF version</div>
<a href="https://drive.google.com/uc?export=download&id=1HK7wBdvoLZxvaoJv6v45D6dblGsXjYcj" class="resume-btn" target="_blank">⬇️ Download Resume</a>
</div>
""", unsafe_allow_html=True)

# OPTION 1: MINIMAL & CLEAN
st.markdown('<div style="text-align: center; padding: 30px; background: rgba(30,41,59,0.9); color: #94a3b8; font-size: 14px; margin-top: 40px;">© 2026 | Aniket V. Walunj | All rights reserved.</div>', unsafe_allow_html=True)
