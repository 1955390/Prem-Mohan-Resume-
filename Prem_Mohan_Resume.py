import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Prem Mohan | Portfolio",
    page_icon="👨‍💻",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for better styling
st.markdown("""
<style>
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Custom animations */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(30px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .main-container {
        animation: fadeIn 0.8s ease;
    }
</style>
""", unsafe_allow_html=True)

# Complete HTML content
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Prem Mohan | Portfolio</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            overflow: hidden;
            animation: fadeIn 0.8s ease;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(30px); }
            to { opacity: 1; transform: translateY(0); }
        }

        header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 40px;
            text-align: center;
        }

        .profile-img {
            width: 150px;
            height: 150px;
            background: white;
            border-radius: 50%;
            margin: 0 auto 20px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 70px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        }

        h1 {
            font-size: 2.5rem;
            margin-bottom: 10px;
        }

        .tagline {
            font-size: 1.2rem;
            opacity: 0.95;
        }

        .content {
            padding: 40px;
        }

        .section {
            margin-bottom: 40px;
            background: #f8f9fa;
            padding: 25px;
            border-radius: 15px;
            transition: transform 0.3s;
        }

        .section:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        }

        h2 {
            color: #667eea;
            margin-bottom: 20px;
            border-left: 4px solid #764ba2;
            padding-left: 15px;
        }

        .contact-info {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 15px;
            margin-bottom: 20px;
        }

        .contact-item {
            display: flex;
            align-items: center;
            gap: 10px;
            padding: 10px;
            background: white;
            border-radius: 10px;
            transition: all 0.3s;
        }

        .contact-item:hover {
            background: #667eea;
            color: white;
            transform: translateX(5px);
        }

        .contact-item i {
            font-size: 20px;
            color: #667eea;
        }

        .contact-item:hover i {
            color: white;
        }

        .social-links {
            display: flex;
            gap: 15px;
            flex-wrap: wrap;
            margin-top: 20px;
        }

        .social-btn {
            padding: 12px 25px;
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            text-decoration: none;
            border-radius: 25px;
            transition: all 0.3s;
            display: inline-flex;
            align-items: center;
            gap: 8px;
        }

        .social-btn:hover {
            transform: translateY(-3px);
            box-shadow: 0 5px 15px rgba(102,126,234,0.4);
        }

        .projects-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 20px;
            margin-top: 20px;
        }

        .project-card {
            background: white;
            padding: 20px;
            border-radius: 15px;
            transition: all 0.3s;
            border: 1px solid #e0e0e0;
        }

        .project-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 25px rgba(0,0,0,0.1);
            border-color: #667eea;
        }

        .project-title {
            font-size: 1.2rem;
            font-weight: bold;
            color: #667eea;
            margin-bottom: 10px;
        }

        .project-date {
            font-size: 0.85rem;
            color: #666;
            margin-bottom: 10px;
        }

        .project-desc {
            font-size: 0.9rem;
            color: #555;
            margin-bottom: 15px;
            line-height: 1.5;
        }

        .project-link {
            display: inline-flex;
            align-items: center;
            gap: 5px;
            color: #764ba2;
            text-decoration: none;
            font-weight: bold;
        }

        .project-link:hover {
            gap: 10px;
        }

        .skills {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
        }

        .skill-badge {
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            padding: 5px 15px;
            border-radius: 20px;
            font-size: 0.85rem;
        }

        .interests {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
        }

        .interest-badge {
            background: #e0e0e0;
            padding: 8px 16px;
            border-radius: 20px;
            font-size: 0.85rem;
            transition: all 0.3s;
        }

        .interest-badge:hover {
            background: #667eea;
            color: white;
            transform: scale(1.05);
        }

        .live-badge {
            position: fixed;
            top: 20px;
            right: 20px;
            background: #28a745;
            color: white;
            padding: 8px 16px;
            border-radius: 30px;
            font-size: 0.8rem;
            font-weight: bold;
            animation: pulse 2s infinite;
            z-index: 1000;
        }

        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.05); }
            100% { transform: scale(1); }
        }

        footer {
            background: #333;
            color: white;
            text-align: center;
            padding: 20px;
        }

        @media (max-width: 768px) {
            .content {
                padding: 20px;
            }
            h1 {
                font-size: 1.8rem;
            }
            .projects-grid {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <div class="live-badge">
        🌐 LIVE PORTFOLIO
    </div>
    
    <div class="container">
        <header>
            <div class="profile-img">
                👨‍💻
            </div>
            <h1>Prem Mohan</h1>
            <p class="tagline">Data Analyst | Java Developer | AI Enthusiast | Translator</p>
        </header>

        <div class="content">
            <!-- Contact Section -->
            <div class="section">
                <h2>📞 Contact Information</h2>
                <div class="contact-info">
                    <div class="contact-item">📧 premmohan966@gmail.com</div>
                    <div class="contact-item">📱 +91 8174083966 / 9532006520</div>
                    <div class="contact-item">📍 Vikalp Khand, Gomti Nagar, Lucknow - 226010</div>
                    <div class="contact-item">🎂 DOB: 05/10/2004</div>
                    <div class="contact-item">🇮🇳 Indian | OBC</div>
                    <div class="contact-item">👤 Male | Unmarried</div>
                </div>
                
                <div class="social-links">
                    <a href="https://youtube.com/c/PremMohanofficial" class="social-btn" target="_blank">▶️ YouTube</a>
                    <a href="https://t.me/premmohanofficial" class="social-btn" target="_blank">📨 Telegram</a>
                    <a href="https://linkedin.com/in/prem-mohan-842924330" class="social-btn" target="_blank">🔗 LinkedIn</a>
                    <a href="https://x.com/premmohan83966" class="social-btn" target="_blank">🐦 Twitter</a>
                    <a href="https://github.com/1955390" class="social-btn" target="_blank">🐙 GitHub</a>
                </div>
            </div>

            <!-- Profile Summary -->
            <div class="section">
                <h2>👨‍💼 Profile Summary</h2>
                <p style="line-height: 1.8; color: #555;">
                    Detail-oriented Data Analyst & Entry-Level Java Developer with professional certifications in ADCA, CCC, and CTS in AI Programming Assistant. 
                    Proficient in Python, SQL, Java, Excel, and data visualization (Matplotlib, Seaborn, Power BI). Skilled English-Hindi translator with experience 
                    in CO₂ emission prediction, sales analysis, and customer churn modeling. Currently building efficient applications as a Java Developer.
                </p>
            </div>

            <!-- Skills -->
            <div class="section">
                <h2>⚡ Technical Skills</h2>
                <div class="skills">
                    <span class="skill-badge">Python</span>
                    <span class="skill-badge">SQL/MySQL</span>
                    <span class="skill-badge">Java</span>
                    <span class="skill-badge">Pandas/NumPy</span>
                    <span class="skill-badge">Matplotlib/Seaborn</span>
                    <span class="skill-badge">Power BI</span>
                    <span class="skill-badge">Streamlit</span>
                    <span class="skill-badge">HTML/CSS</span>
                    <span class="skill-badge">Machine Learning</span>
                    <span class="skill-badge">Excel Advanced</span>
                    <span class="skill-badge">Data Cleaning</span>
                    <span class="skill-badge">Translation (EN/HI)</span>
                </div>
            </div>

            <!-- Projects (ALL 9 Projects) -->
            <div class="section">
                <h2>🚀 Featured Projects (9 Live Apps)</h2>
                <div class="projects-grid">
                    <div class="project-card">
                        <div class="project-title">🐠 Surya Aquarium Lucknow</div>
                        <div class="project-date">March 2026 – April 2026</div>
                        <div class="project-desc">Web-based aquarium platform using Streamlit. User-friendly interface for fish products, aquarium guidance, real-world business solution.</div>
                        <a href="https://suryaaquariumlucknow.streamlit.app" class="project-link" target="_blank">Live Demo →</a>
                    </div>
                    
                    <div class="project-card">
                        <div class="project-title">📘 NIMI Books ITI App</div>
                        <div class="project-date">Oct 2025 – Nov 2025</div>
                        <div class="project-desc">Digitalized book purchasing with discounts, inventory management, dual email receipts for ITI students.</div>
                        <a href="https://nimibooksalesapp.streamlit.app" class="project-link" target="_blank">Live Demo →</a>
                    </div>
                    
                    <div class="project-card">
                        <div class="project-title">🛠️ SSC Wallah Technician</div>
                        <div class="project-date">Feb 2026 – Mar 2026</div>
                        <div class="project-desc">Comprehensive app for technicians with troubleshooting guides, video tutorials, and system diagnostics.</div>
                        <a href="https://ssc-wallah-technician.streamlit.app" class="project-link" target="_blank">Live Demo →</a>
                    </div>
                    
                    <div class="project-card">
                        <div class="project-title">💰 Placement Prediction System</div>
                        <div class="project-date">Nov 2025 – Dec 2025</div>
                        <div class="project-desc">AI platform analyzing academics & skills for career recommendations and placement readiness.</div>
                        <a href="https://placement-prediction-pre.streamlit.app" class="project-link" target="_blank">Live Demo →</a>
                    </div>
                    
                    <div class="project-card">
                        <div class="project-title">🧮 Smart Calculator</div>
                        <div class="project-date">Jul 2025 – Aug 2025</div>
                        <div class="project-desc">Advanced calculator with scientific, statistical & AI-assisted features.</div>
                        <a href="https://calculator-app-prem.streamlit.app" class="project-link" target="_blank">Live Demo →</a>
                    </div>
                    
                    <div class="project-card">
                        <div class="project-title">🎮 Guessing Game</div>
                        <div class="project-date">Jun 2025 – Jul 2025</div>
                        <div class="project-desc">Interactive number guessing game with instant feedback and score tracking.</div>
                        <a href="https://gameplay-withst-reamlit.streamlit.app" class="project-link" target="_blank">Live Demo →</a>
                    </div>
                    
                    <div class="project-card">
                        <div class="project-title">🌤️ Weather Forecast App</div>
                        <div class="project-date">May 2025 – Jun 2025</div>
                        <div class="project-desc">Real-time weather updates using OpenWeather API.</div>
                        <a href="https://prem-mohan-s-weather-forecast.streamlit.app" class="project-link" target="_blank">Live Demo →</a>
                    </div>
                    
                    <div class="project-card">
                        <div class="project-title">🚛 CO₂ Footprint Optimization</div>
                        <div class="project-date">Mar 2025 – May 2025</div>
                        <div class="project-desc">Predicts vehicle CO₂ emissions and suggests reduction actions.</div>
                        <a href="https://carbonemissionpredictorpy.streamlit.app" class="project-link" target="_blank">Live Demo →</a>
                    </div>
                    
                    <div class="project-card">
                        <div class="project-title">🧑‍🎓 NextGen Career Guide</div>
                        <div class="project-date">Jan 2025 – Mar 2025</div>
                        <div class="project-desc">Career guidance platform with job search and learning resources.</div>
                        <a href="https://nextgen-career-guide.streamlit.app" class="project-link" target="_blank">Live Demo →</a>
                    </div>
                </div>
            </div>

            <!-- Education & Certifications -->
<div class="section">
    <h2>🎓 Education & Certifications</h2>

    <div style="margin-bottom: 20px;">
        <strong>🎓 Bachelor of Science (B.Sc.) – PCM Stream</strong><br>
        Awadh University, Ayodhya | 2022–2025 | Score: 85%
    </div>

    <div style="margin-bottom: 20px;">
        <strong>🤖 AIPA (Artificial Intelligence Programming Assistant)</strong><br>
        NSTI Kanpur | DGT, Government of India | 2024–2025 | Score: 87%
    </div>

    <div style="margin-bottom: 20px;">
        <strong>📜 O Level – IT & Computer Science</strong><br>
        NIELIT, Government of India | Grade: B+ | 2026 | Expected Completion
    </div>
    
    <div style="margin-bottom: 20px;">
    <strong>🪖 National Cadet Corps (NCC) – ABC Certificate</strong><br>
    2026 (Expected Completion) | Leadership, Discipline, Teamwork & Social Service
</div>

    <div style="margin-bottom: 20px;">
        <strong>💻 COPA (Computer Operator & Programming Assistant)</strong><br>
        NCVT | 2025–2026 | Skills: Programming, Computer Operation, Office Tools
    </div>

    <div style="margin-bottom: 20px;">
        <strong>🌐 CCC (Course on Computer Concepts) – NIELIT</strong><br>
        Government of India | Grade: A+ | 2024
    </div> 

    <div style="margin-bottom: 20px;">
        <strong>💻 ADCA (Advanced Diploma in Computer Applications)</strong><br>
        2023–2024 | Subjects: MS Office, Python, HTML, MySQL
    </div>

    <div>
        <strong>📖 Intermediate (PCM)</strong><br>
        UP Board | First Division | 2022 | Percentage: 75%
    </div>
</div>

            <!-- Interests -->
<div class="section">
    <h2>💡 Interests & Expertise</h2>
    <div class="interests">
        <span class="interest-badge">Artificial Intelligence</span>
        <span class="interest-badge">Machine Learning</span>
        <span class="interest-badge">Deep Learning</span>
        <span class="interest-badge">Data Analysis</span>
        <span class="interest-badge">Data Visualization</span>
        <span class="interest-badge">Python Programming</span>
        <span class="interest-badge">Java Development</span>
        <span class="interest-badge">Web Development</span>
        <span class="interest-badge">Frontend Development</span>
        <span class="interest-badge">Backend Development</span>
        <span class="interest-badge">Streamlit Apps</span>
        <span class="interest-badge">Database Management</span>
        <span class="interest-badge">MySQL</span>
        <span class="interest-badge">Computer Vision</span>
        <span class="interest-badge">NLP</span>
        <span class="interest-badge">Generative AI</span>
        <span class="interest-badge">AI Tools</span>
        <span class="interest-badge">Prompt Engineering</span>
        <span class="interest-badge">API Integration</span>
        <span class="interest-badge">IoT Projects</span>
        <span class="interest-badge">Recommendation Systems</span>
        <span class="interest-badge">Business Solutions</span>
        <span class="interest-badge">Problem Solving</span>
        <span class="interest-badge">Technical Research</span>
        <span class="interest-badge">Translation</span>
        <span class="interest-badge">Content Creation</span>
        <span class="interest-badge">Career Guidance Platforms</span>
        <span class="interest-badge">Educational Technology</span>
    </div>
</div>
            </div>
        </div>

        <footer>
            <p>© 2026 Prem Mohan | Data Analyst & Java Developer | All Projects Live on Streamlit Cloud</p>
            <p style="margin-top: 10px; font-size: 0.8rem;">📧 premmohan966@gmail.com | 📱 +91 8174083966</p>
        </footer>
    </div>
</body>
</html>
"""

# Display the HTML in Streamlit
st.components.v1.html(html_content, height=2000, scrolling=True)
