"""
Smart Health Assistant - Web Application
A Comprehensive Health Guidance, Nutrition, and Local Services Platform
Built with Streamlit, Python, and SQLite.
"""

import os
import sys
from datetime import date, datetime
import pandas as pd
import streamlit as st

# Add src to path
SRC_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "src")
if SRC_DIR not in sys.path:
    sys.path.append(SRC_DIR)

from predict import HealthPredictor
from health_guidance import HEALTH_CONCERNS_GUIDANCE
from food_recommendations import recommend_foods, FOOD_DATABASE
from deficiency_education import DEFICIENCY_TOPICS
from nearby_services import generate_healthcare_links, generate_food_shop_links, EMERGENCY_HELPLINES_INDIA, check_emergency_red_flags
import followup_db
import assistant_bot

# Set Streamlit Page Configuration
st.set_page_config(
    page_title="Smart Health Assistant",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown("""
<style>
    .main-title {
        font-size: 2.2rem;
        font-weight: 800;
        color: #1a365d;
        margin-bottom: 0.2rem;
    }
    .sub-title {
        font-size: 1.05rem;
        color: #4a5568;
        margin-bottom: 1.2rem;
    }
    .emergency-banner {
        background-color: #fff5f5;
        border-left: 6px solid #e53e3e;
        padding: 12px 18px;
        border-radius: 6px;
        margin-bottom: 1.2rem;
        font-size: 0.95rem;
        color: #9b2c2c;
    }
    .card-box {
        background-color: #f7fafc;
        border: 1px solid #e2e8f0;
        border-radius: 8px;
        padding: 18px;
        margin-bottom: 15px;
    }
    .badge-primary {
        background-color: #ebf8ff;
        color: #2b6cb0;
        padding: 4px 10px;
        border-radius: 12px;
        font-size: 0.8rem;
        font-weight: 600;
        display: inline-block;
    }
    .badge-danger {
        background-color: #fff5f5;
        color: #c53030;
        padding: 4px 10px;
        border-radius: 12px;
        font-size: 0.8rem;
        font-weight: 600;
        display: inline-block;
    }
</style>
""", unsafe_allow_html=True)

# Initialize Session State
if "assessment_result" not in st.session_state:
    st.session_state.assessment_result = None
if "selected_concern" not in st.session_state:
    st.session_state.selected_concern = "Fever"
if "user_location" not in st.session_state:
    st.session_state.user_location = "Hyderabad"

# Global Emergency Banner
st.markdown("""
<div class="emergency-banner">
    🚨 <strong>EMERGENCY NOTICE:</strong> This application provides <strong>general home-care and nutrition guidance</strong> only. 
    If anyone is experiencing emergency symptoms (severe chest pain, sudden difficulty breathing, loss of consciousness, persistent high fever in infants, or severe dehydration), 
    call <strong>112 (National Emergency)</strong> or <strong>108 (Ambulance)</strong> immediately!
</div>
""", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/2966/2966327.png", width=65)
st.sidebar.title("Smart Health Assistant")
st.sidebar.markdown("**Navigation Menu**")

pages = [
    "1. Home Dashboard",
    "2. Symptom Assessment & Guidance",
    "3. Home-Care & Food Recommendations",
    "4. Nutritional Deficiency Education",
    "5. Nearby Food Shops & Ordering",
    "6. Nearby Healthcare Services",
    "7. Health Follow-Up & Reminders"
]

selected_page = st.sidebar.radio("Go to:", pages, index=0)

st.sidebar.markdown("---")
st.sidebar.markdown("### 🇮🇳 Emergency Helplines")
st.sidebar.markdown("- **112**: All Emergencies")
st.sidebar.markdown("- **108**: Medical Ambulance")
st.sidebar.markdown("- **104**: Tele-Health Advice")
st.sidebar.markdown("- **102**: Maternal & Infant")

st.sidebar.markdown("---")
st.sidebar.caption("Smart Health Assistant | Public Health & Nutrition System")


# Mapping from ML category to common concern for direct guidance
CATEGORY_TO_CONCERN = {
    "Acute Febrile Syndrome": "Fever",
    "Upper Respiratory Illness": "Common Cold and Cough",
    "Acute Gastroenteritis Risk": "Loose Motions or Diarrhoea",
    "Tension / Fatigue Headache": "Headache",
    "General Physical Fatigue": "Weakness and Tiredness",
    "Mild Dyspepsia / Gastric Discomfort": "Mild Stomach Discomfort",
    "Nutritional Inadequacy Concern": "Nutritional Concerns"
}


# ==========================================
# PAGE 1: HOME DASHBOARD
# ==========================================
if selected_page.startswith("1."):
    st.markdown('<div class="main-title">🩺 Smart Health Assistant</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">A Practical Healthcare Education & Personalized Nutrition Platform for Students, Families & Communities</div>', unsafe_allow_html=True)

    col_dash1, col_dash2, col_dash3 = st.columns(3)
    with col_dash1:
        st.info("📋 **Symptom Assessment**\nEnter your current symptoms and duration to receive clear educational health categories and immediate home care.")
    with col_dash2:
        st.success("🥗 **Personalized Nutrition**\nTailored foods, budget-friendly options, vegetarian alternatives, and essential nutrient deficiency education.")
    with col_dash3:
        st.warning("📍 **Verified Local Services**\nDirect Google Maps & OSM search links for local clinics, PHCs, pharmacies, and grocery markets without fake data.")

    st.markdown("---")
    st.markdown("### 🚀 Quick Actions")
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown("**Check Symptoms**")
        st.caption("Assess symptoms and get instant home-care instructions.")
    with c2:
        st.markdown("**Nutrition & Diet**")
        st.caption("Wholesome foods for recovery and budget-friendly alternatives.")
    with c3:
        st.markdown("**Nearby Clinics**")
        st.caption("Find nearby government hospitals, PHCs, and pharmacies.")
    with c4:
        st.markdown("**Follow-Up Tracker**")
        st.caption("Track your daily symptoms and monitor if you are improving.")

    st.markdown("---")
    st.markdown("### 💬 Interactive Health Assistant (Bilingual)")
    st.markdown("Ask general questions about safe home care, hydration, ORS preparation, food suggestions, or emergency numbers:")

    lang_choice = st.radio("Select Language / భాషను ఎంచుకోండి:", ["English", "Telugu (తెలుగు)"], horizontal=True)
    user_chat = st.text_input("Type your question here (e.g. 'How to prepare ORS?', 'fever care', 'weakness diet', 'emergency number'):")
    
    if user_chat:
        response_text = assistant_bot.get_assistant_response(user_chat, lang=lang_choice)
        st.markdown(f"""
        <div class="card-box" style="border-left: 5px solid #3182ce;">
            {response_text}
        </div>
        """, unsafe_allow_html=True)


# ==========================================
# PAGE 2: SYMPTOM ASSESSMENT & GUIDANCE
# ==========================================
elif selected_page.startswith("2."):
    st.markdown('<div class="main-title">📋 Symptom Assessment & Guidance</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">Select your symptoms to receive an educational assessment, safe home-care measures, and tailored food suggestions.</div>', unsafe_allow_html=True)

    with st.form("symptom_form"):
        st.markdown("#### 1. Basic Details")
        col_demo1, col_demo2, col_demo3 = st.columns(3)
        with col_demo1:
            age_group = st.selectbox("Age Group:", [
                "Young Adult (18-35)", "Child (2-12)", "Adolescent (13-17)", "Middle-Aged (36-59)", "Senior (60+)"
            ])
        with col_demo2:
            duration_days = st.slider("Duration of Symptoms (in Days):", min_value=1, max_value=30, value=2)
        with col_demo3:
            severity_score = st.select_slider("Self-Assessed Discomfort (1: Mild to 5: High):", options=[1, 2, 3, 4, 5], value=2)

        st.markdown("#### 2. Select All Symptoms You Currently Experience")
        col_sym1, col_sym2, col_sym3 = st.columns(3)
        with col_sym1:
            fever = st.checkbox("Fever / High Body Temperature")
            cough = st.checkbox("Cough / Sore Throat")
            headache = st.checkbox("Headache / Head Pressure")
            chills = st.checkbox("Chills or Shivering")
        with col_sym2:
            loose_stools = st.checkbox("Loose Motions / Diarrhoea")
            vomiting = st.checkbox("Vomiting or Nausea")
            mild_stomach_pain = st.checkbox("Mild Stomach Pain / Cramping")
            loss_of_appetite = st.checkbox("Loss of Appetite")
        with col_sym3:
            weakness_fatigue = st.checkbox("Generalized Weakness / Fatigue")
            dehydration_signs = st.checkbox("Dehydration Signs (Dry mouth, Dark urine)")
            body_ache = st.checkbox("Body Ache or Muscle Pain")

        submit_symptoms = st.form_submit_button("🔍 Get Health Assessment & Guidance", use_container_width=True)

    if submit_symptoms:
        active_symptom_keys = []
        if fever: active_symptom_keys.append("fever")
        if cough: active_symptom_keys.append("cough")
        if headache: active_symptom_keys.append("headache")
        if loose_stools: active_symptom_keys.append("loose_stools")
        if vomiting: active_symptom_keys.append("vomiting")
        if mild_stomach_pain: active_symptom_keys.append("mild_stomach_pain")
        if weakness_fatigue: active_symptom_keys.append("weakness_fatigue")
        if dehydration_signs: active_symptom_keys.append("dehydration_signs")
        if loss_of_appetite: active_symptom_keys.append("loss_of_appetite")
        if body_ache: active_symptom_keys.append("body_ache")
        if chills: active_symptom_keys.append("chills")

        # Emergency Red-Flag Triage
        red_flags = check_emergency_red_flags(active_symptom_keys, duration_days)
        if red_flags:
            st.error("⚠️ **CRITICAL WARNING SIGNS DETECTED:**")
            for rf in red_flags:
                st.write(f"- {rf}")
            st.warning("Please do not delay. Call 108 or visit the nearest clinic / hospital immediately.")

        user_input_dict = {
            "fever": int(fever),
            "cough": int(cough),
            "headache": int(headache),
            "loose_stools": int(loose_stools),
            "vomiting": int(vomiting),
            "mild_stomach_pain": int(mild_stomach_pain),
            "weakness_fatigue": int(weakness_fatigue),
            "dehydration_signs": int(dehydration_signs),
            "loss_of_appetite": int(loss_of_appetite),
            "body_ache": int(body_ache),
            "chills": int(chills),
            "symptom_duration_days": duration_days,
            "age_group": age_group,
            "severity_score": severity_score
        }

        predictor = HealthPredictor()
        result = predictor.predict(user_input_dict)
        st.session_state.assessment_result = result

        pred_cat = result["predicted_category"]
        mapped_concern = CATEGORY_TO_CONCERN.get(pred_cat, "Fever")
        st.session_state.selected_concern = mapped_concern

        st.success("✅ Assessment Completed Successfully!")

        st.markdown(f"""
        <div class="card-box" style="border-left: 6px solid #3182ce;">
            <h3 style="margin-top:0; color:#2b6cb0;">Health Assessment: <strong>{pred_cat}</strong></h3>
            <p><strong>Associated Health Concern:</strong> {mapped_concern}</p>
            <p><strong>Reported Symptoms:</strong> {', '.join(result['active_symptoms']) if result['active_symptoms'] else 'None reported'}</p>
            <p><strong>Duration:</strong> {duration_days} day(s) | <strong>Discomfort Level:</strong> {severity_score}/5</p>
        </div>
        """, unsafe_allow_html=True)

        # Immediate Care Snapshot
        if mapped_concern in HEALTH_CONCERNS_GUIDANCE:
            guide = HEALTH_CONCERNS_GUIDANCE[mapped_concern]
            st.markdown("### 🛡️ Immediate Home-Care Steps")
            for hc in guide["home_care"][:3]:
                st.write(f"• {hc}")

            st.markdown("### 💧 Hydration Advice")
            st.write(guide["hydration_advice"])

            st.info(f"💡 For complete food suggestions and home care, visit **Page 3: Home-Care & Food Recommendations** (Pre-selected: {mapped_concern}).")


# ==========================================
# PAGE 3: HOME-CARE & FOOD RECOMMENDATIONS
# ==========================================
elif selected_page.startswith("3."):
    st.markdown('<div class="main-title">🍲 Home-Care & Food Recommendations</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">Safe, non-prescriptive, evidence-based home-care guidance and nutrition suggestions for common health concerns.</div>', unsafe_allow_html=True)

    concern_options = list(HEALTH_CONCERNS_GUIDANCE.keys())
    default_idx = concern_options.index(st.session_state.selected_concern) if st.session_state.selected_concern in concern_options else 0
    selected_concern = st.selectbox("Select Health Concern:", concern_options, index=default_idx)

    guidance = HEALTH_CONCERNS_GUIDANCE[selected_concern]

    tab_home, tab_food = st.tabs(["🏠 Safe Home-Care Guidelines", "🥗 Recommended Wholesome Foods"])

    with tab_home:
        st.markdown(f"### {guidance['title']}")
        st.info(f"**Explanation:** {guidance['explanation']}")

        col_c1, col_c2 = st.columns(2)
        with col_c1:
            st.markdown("#### 🔍 Possible Causes (General):")
            for pc in guidance["possible_causes"]:
                st.write(f"- {pc}")

            st.markdown("#### 🛡️ Safe Home-Care Measures:")
            for hc in guidance["home_care"]:
                st.write(f"- {hc}")

            st.markdown("#### 💧 Hydration Advice:")
            st.write(guidance["hydration_advice"])

        with col_c2:
            st.markdown("#### 🚫 Foods & Drinks to Avoid:")
            for fa in guidance["foods_to_avoid"]:
                st.write(f"- {fa}")

            st.markdown("#### ⚠️ WARNING SIGNS (Seek Immediate Care):")
            for ws in guidance["warning_signs"]:
                st.markdown(f"<span style='color:#e53e3e; font-weight:600;'>• {ws}</span>", unsafe_allow_html=True)

            st.markdown("#### 👨‍⚕️ When to Consult a Doctor:")
            st.write(guidance["when_to_consult"])

    with tab_food:
        st.markdown("### 🍎 Wholesome Food & Nutrition Suggestions")
        
        filter_col1, filter_col2 = st.columns(2)
        with filter_col1:
            diet_pref = st.selectbox("Dietary Preference:", ["All", "Vegetarian", "Vegan", "Non-Vegetarian", "Gluten-free"])
        with filter_col2:
            cat_filter = st.selectbox("Food Category:", [
                "All", "Whole grains", "Pulses and beans", "Fruits", "Vegetables",
                "Dairy products and suitable alternatives", "Protein-rich foods", "Iron-rich foods"
            ])

        foods = recommend_foods(health_concern=selected_concern, dietary_pref=diet_pref, category_filter=cat_filter)

        st.caption(f"Showing {len(foods)} recommended food options for {selected_concern}:")

        for f in foods:
            with st.expander(f"✨ {f['name']} ({f['category']})", expanded=(f['relevance'] > 1)):
                st.markdown(f"**Nutrients Present:** {f['nutrients']}")
                st.markdown(f"**Potential Health Benefits:** {f['benefits']}")
                st.markdown(f"**Why Suitable in this Context:** {f['why_suitable']}")
                
                fc1, fc2 = st.columns(2)
                with fc1:
                    st.markdown(f"💰 **Affordable Alternative:** {f['affordable_alternative']}")
                    st.markdown(f"🌱 **Vegetarian/Vegan Option:** {f['vegetarian_alternative']}")
                with fc2:
                    st.markdown(f"📅 **Seasonal Availability:** {f['seasonal_availability']}")
                    st.markdown(f"⚠️ **Precautions:** {f['precautions']}")

    st.markdown("---")
    st.caption("DISCLAIMER: Food recommendations support overall nutritional recovery and are not medicine substitutes.")


# ==========================================
# PAGE 4: NUTRITIONAL DEFICIENCY EDUCATION
# ==========================================
elif selected_page.startswith("4."):
    st.markdown('<div class="main-title">🧬 Nutritional Deficiency Education</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">Learn about vital micro and macronutrients, symptoms of inadequacy, dietary sources, and the necessity of clinical blood testing.</div>', unsafe_allow_html=True)

    st.warning("""
    📌 **CRITICAL MEDICAL PRINCIPLE: SYMPTOMS OVERLAP**
    Fatigue, weakness, headaches, and hair thinning can be caused by Iron deficiency, Vitamin B12 deficiency, Vitamin D deficiency, thyroid disorders, or simple lack of sleep. 
    **Never self-prescribe high-dose supplements without laboratory blood confirmation.**
    """)

    def_keys = list(DEFICIENCY_TOPICS.keys())
    selected_def = st.selectbox("Choose Nutritional Topic:", def_keys)

    def_data = DEFICIENCY_TOPICS[selected_def]

    st.markdown(f"### {def_data['title']}")
    st.info(f"**Biological Function & Role:** {def_data['role']}")

    c_sym, c_food = st.columns(2)
    with c_sym:
        st.markdown("#### 🩺 Common Educational Symptoms:")
        for s in def_data["common_symptoms"]:
            st.write(f"- {s}")

        st.markdown("#### 👥 Populations at Higher Risk:")
        for r in def_data["risk_factors"]:
            st.write(f"- {r}")

    with c_food:
        st.markdown("#### 🥗 Wholesome Food Sources:")
        for src_type, src_desc in def_data["food_sources"].items():
            st.markdown(f"**{src_type}:** {src_desc}")

        st.markdown("#### 🔬 Recommended Diagnostic Blood Tests:")
        st.markdown(f"""
        <div class="card-box" style="border-left: 4px solid #38a169;">
            {def_data['clinical_tests']}
        </div>
        """, unsafe_allow_html=True)


# ==========================================
# PAGE 5: NEARBY FOOD SHOPS & ORDERING
# ==========================================
elif selected_page.startswith("5."):
    st.markdown('<div class="main-title">🛒 Nearby Food Shops & Grocery Ordering</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">Find nearby fruit markets, vegetable mandis, grocery stores, and online delivery links for your village, town, or PIN code.</div>', unsafe_allow_html=True)

    col_loc1, col_loc2 = st.columns([2, 1])
    with col_loc1:
        loc_input = st.text_input("Enter your Village, Town, City, or PIN Code:", value=st.session_state.user_location)
    with col_loc2:
        item_search = st.text_input("Optional Food Item (e.g., 'bananas', 'curd', 'moringa'):", value="")

    if loc_input:
        st.session_state.user_location = loc_input
        local_shops, online_platforms = generate_food_shop_links(loc_input, item_search)

        st.markdown(f"### 📍 Local Markets & Physical Shops near `{loc_input}`")
        st.caption("Direct verified map search queries via Google Maps and OpenStreetMap:")

        for shop in local_shops:
            with st.container():
                st.markdown(f"#### {shop['icon']} {shop['name']}")
                st.write(shop['description'])
                btn_col1, btn_col2 = st.columns(2)
                with btn_col1:
                    st.link_button(f"🔍 Search on Google Maps", shop['gmaps_url'])
                with btn_col2:
                    st.link_button(f"🗺️ View on OpenStreetMap", shop['osm_url'])
                st.markdown("---")

        st.markdown(f"### 🚚 Online Grocery Delivery Platforms (Verified Links)")
        st.caption("Direct search URLs for major platforms (availability depends on PIN code coverage):")

        for plat in online_platforms:
            p_col1, p_col2 = st.columns([3, 1])
            with p_col1:
                st.markdown(f"**{plat['platform']}**: {plat['tagline']}")
            with p_col2:
                st.link_button(f"Visit {plat['platform']}", plat['search_url'])

    st.info("ℹ️ **Integrity Notice:** This project does not invent fake stock levels, fake prices, or fake delivery guarantees. All links connect to genuine search engines and platform homepages.")


# ==========================================
# PAGE 6: NEARBY HEALTHCARE SERVICES
# ==========================================
elif selected_page.startswith("6."):
    st.markdown('<div class="main-title">🏥 Nearby Healthcare Services & Emergency Triage</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">Locate nearby Government Hospitals, Primary Health Centres (PHC), Clinics, and Pharmacies, and access national helplines.</div>', unsafe_allow_html=True)

    st.markdown("### 🚨 Official Indian Emergency Numbers")
    h_cols = st.columns(3)
    for idx, h in enumerate(EMERGENCY_HELPLINES_INDIA):
        with h_cols[idx % 3]:
            st.markdown(f"""
            <div class="card-box" style="border-top: 4px solid #e53e3e;">
                <span class="badge-danger">{h['badge']}</span>
                <h3 style="margin: 6px 0; color: #c53030;">📞 {h['number']}</h3>
                <strong>{h['service']}</strong>
                <p style="font-size: 0.85rem; color: #4a5568; margin-top: 4px;">{h['description']}</p>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### 🗺️ Search Healthcare Facilities by Location")
    med_loc = st.text_input("Enter your District, Town, Mandal, or PIN Code:", value=st.session_state.user_location, key="med_loc_input")

    if med_loc:
        facilities = generate_healthcare_links(med_loc)
        for f in facilities:
            with st.container():
                st.markdown(f"#### {f['icon']} {f['facility_type']}")
                st.write(f['description'])
                f_btn1, f_btn2 = st.columns(2)
                with f_btn1:
                    st.link_button(f"📍 Find on Google Maps", f['gmaps_url'])
                with f_btn2:
                    st.link_button(f"🗺️ View on OpenStreetMap", f['osm_url'])
                st.markdown("---")


# ==========================================
# PAGE 7: HEALTH FOLLOW-UP & REMINDERS
# ==========================================
elif selected_page.startswith("7."):
    st.markdown('<div class="main-title">📅 Health Follow-Up & Symptom Tracker</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">Locally stored progression tracker (SQLite) to log symptoms, evaluate improvement, and receive persistent safety alerts.</div>', unsafe_allow_html=True)

    tab_log_new, tab_checkin, tab_view = st.tabs(["📝 Log New Concern", "🔄 Daily Check-In", "📊 View Follow-Up History"])

    with tab_log_new:
        st.markdown("#### Create a New Health Observation Entry")
        with st.form("new_concern_form"):
            pat_name = st.text_input("User / Patient Name:", value="Student / Self")
            concern_select = st.selectbox("Health Concern:", list(HEALTH_CONCERNS_GUIDANCE.keys()))
            start_d = st.date_input("Date Symptoms Started:", value=date.today())
            init_sev = st.slider("Initial Severity (1: Mild to 5: High):", 1, 5, 2)
            c_notes = st.text_area("Initial Notes / Observations:", placeholder="e.g. Mild headache and low fever after exam stress.")
            
            save_log_btn = st.form_submit_button("💾 Save Health Log")

        if save_log_btn:
            new_id = followup_db.create_health_log(pat_name, concern_select, str(start_d), init_sev, c_notes)
            st.success(f"Health log saved successfully with ID #{new_id}!")

    with tab_checkin:
        logs = followup_db.get_all_logs()
        if not logs:
            st.info("No active health logs found. Please log a concern first.")
        else:
            log_choices = {f"#{l['id']} - {l['patient_name']} ({l['concern_name']} started {l['start_date']})": l['id'] for l in logs}
            chosen_log = st.selectbox("Select Active Concern to Update:", list(log_choices.keys()))
            chosen_id = log_choices[chosen_log]

            with st.form("checkin_form"):
                checkin_date = st.date_input("Check-In Date:", value=date.today())
                status_prog = st.selectbox("How are your symptoms progressing?", ["Improving", "Unchanged", "Worsening"])
                warning_reported = st.checkbox("Are any Warning Signs present? (e.g. high fever >103°F, severe dehydration, blood in stool, severe pain)")
                daily_notes = st.text_input("Today's Notes:", placeholder="e.g. Fever reduced to 99°F, drinking plenty of ORS.")
                
                submit_checkin = st.form_submit_button("📌 Submit Progression Check-In")

            if submit_checkin:
                alert_msg = followup_db.record_checkin(chosen_id, str(checkin_date), status_prog, warning_reported, daily_notes)
                if "CRITICAL" in alert_msg or "Worsening" in status_prog:
                    st.error(alert_msg)
                elif "Unchanged" in status_prog:
                    st.warning(alert_msg)
                else:
                    st.success(alert_msg)

    with tab_view:
        logs = followup_db.get_all_logs()
        if not logs:
            st.info("No health logs recorded yet.")
        else:
            st.markdown("#### Active Health Records:")
            df_logs = pd.DataFrame(logs)
            st.dataframe(df_logs[["id", "patient_name", "concern_name", "start_date", "initial_severity", "latest_status", "checkin_count"]], use_container_width=True)

            sel_view_id = st.number_input("Enter Log ID to view progression timeline:", min_value=1, value=logs[0]["id"])
            checkins = followup_db.get_checkins_for_log(sel_view_id)
            if checkins:
                st.markdown(f"#### Check-In Timeline for Record #{sel_view_id}:")
                for c in checkins:
                    color = "#38a169" if c["status"] == "Improving" else ("#e53e3e" if c["status"] == "Worsening" else "#d69e2e")
                    st.markdown(f"""
                    <div class="card-box" style="border-left: 5px solid {color};">
                        <strong>Date:</strong> {c['checkin_date']} | <strong>Status:</strong> <span style="color:{color}; font-weight:700;">{c['status']}</span><br>
                        <strong>Warning Signs Reported:</strong> {c['reported_warning_signs']}<br>
                        <strong>Notes:</strong> {c['notes']}<br>
                        <small style="color: #4a5568;">{c['safety_alert']}</small>
                    </div>
                    """, unsafe_allow_html=True)
            else:
                st.caption(f"No check-ins logged yet for Record #{sel_view_id}.")

st.markdown("---")
st.markdown("<div style='text-align: center; color: #718096; font-size: 0.85rem;'>Smart Health Assistant • Public Health & Nutrition Guidance Platform</div>", unsafe_allow_html=True)
