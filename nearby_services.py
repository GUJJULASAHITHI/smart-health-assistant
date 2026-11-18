"""
Nearby Services & Emergency Care Finder
Generates verified search links for healthcare facilities, government health centers,
local grocery markets, and delivery platforms based on user-entered location or PIN code.
Displays official Indian emergency helplines and triage warnings.
"""

import urllib.parse

EMERGENCY_HELPLINES_INDIA = [
    {
        "service": "National Emergency Number",
        "number": "112",
        "description": "All-in-one 24/7 emergency response for Police, Fire, and Ambulance across India.",
        "badge": "24/7 ALL EMERGENCIES"
    },
    {
        "service": "Ambulance Emergency Service",
        "number": "108",
        "description": "Toll-free emergency medical dispatch and ambulance transport to nearest trauma/hospital.",
        "badge": "URGENT AMBULANCE"
    },
    {
        "service": "Maternal & Infant Ambulance (JSSK)",
        "number": "102",
        "description": "Dedicated free transport for pregnant women in labor and sick infants under 1 year.",
        "badge": "MATERNAL & CHILD"
    },
    {
        "service": "State Health & Telemedicine Helpline",
        "number": "104",
        "description": "Toll-free medical information, disease outbreak notification, and remote doctor advice.",
        "badge": "TELE-TRIAGE"
    },
    {
        "service": "National Health Helpline (MoHFW)",
        "number": "1075",
        "description": "Central ministry health guidance, communicable disease info, and national programs.",
        "badge": "GOVT OF INDIA"
    },
    {
        "service": "Tele-MANAS Mental Health Helpline",
        "number": "14416 / 1800-891-4416",
        "description": "24/7 multi-lingual confidential counseling and psychological support.",
        "badge": "MENTAL HEALTH"
    }
]

def generate_healthcare_links(location_str: str):
    """
    Builds direct, verified Google Maps and OpenStreetMap search query links
    for hospitals, PHCs, CHCs, clinics, and pharmacies in the specified location.
    """
    loc_clean = location_str.strip()
    encoded_loc = urllib.parse.quote_plus(loc_clean)

    categories = [
        {
            "facility_type": "Government Hospitals & Medical Colleges",
            "icon": "🏥",
            "description": "District hospitals and secondary/tertiary public medical institutions.",
            "gmaps_url": f"https://www.google.com/maps/search/government+hospital+near+{encoded_loc}",
            "osm_url": f"https://www.openstreetmap.org/search?query=hospital+{encoded_loc}"
        },
        {
            "facility_type": "Primary & Community Health Centres (PHC / CHC)",
            "icon": "🩺",
            "description": "Rural and urban primary public clinics offering basic emergency and maternal care.",
            "gmaps_url": f"https://www.google.com/maps/search/Primary+Health+Centre+OR+CHC+near+{encoded_loc}",
            "osm_url": f"https://www.openstreetmap.org/search?query=health+centre+{encoded_loc}"
        },
        {
            "facility_type": "Private Hospitals & Multi-Specialty Clinics",
            "icon": "🏢",
            "description": "Private healthcare providers, nursing homes, and outpatient doctors.",
            "gmaps_url": f"https://www.google.com/maps/search/hospital+or+clinic+near+{encoded_loc}",
            "osm_url": f"https://www.openstreetmap.org/search?query=clinic+{encoded_loc}"
        },
        {
            "facility_type": "Pharmacies & Medical Stores (Jan Aushadhi)",
            "icon": "💊",
            "description": "Licensed chemist shops and Pradhan Mantri Jan Aushadhi Kendras for affordable medicines.",
            "gmaps_url": f"https://www.google.com/maps/search/pharmacy+or+Jan+Aushadhi+kendra+near+{encoded_loc}",
            "osm_url": f"https://www.openstreetmap.org/search?query=pharmacy+{encoded_loc}"
        }
    ]
    return categories

def generate_food_shop_links(location_str: str, food_item: str = ""):
    """
    Builds direct search links for local vegetable mandis, fruit markets,
    supermarkets, and verified grocery ordering platforms.
    """
    loc_clean = location_str.strip()
    item_clean = food_item.strip()
    
    query = f"{item_clean} in {loc_clean}" if item_clean else f"grocery markets in {loc_clean}"
    encoded_query = urllib.parse.quote_plus(query)
    encoded_loc = urllib.parse.quote_plus(loc_clean)

    local_shops = [
        {
            "name": "Local Fruit & Vegetable Mandis / Rythu Bazaars",
            "icon": "🥬",
            "description": "Direct farmers markets and local sabzi mandis offering fresh, low-cost produce.",
            "gmaps_url": f"https://www.google.com/maps/search/vegetable+market+OR+Rythu+Bazaar+near+{encoded_loc}",
            "osm_url": f"https://www.openstreetmap.org/search?query=marketplace+{encoded_loc}"
        },
        {
            "name": "Supermarkets & Provision Stores (Kirana)",
            "icon": "🛒",
            "description": "Neighborhood grocery stores for pulses, whole grains, millets, and dairy.",
            "gmaps_url": f"https://www.google.com/maps/search/grocery+store+OR+supermarket+near+{encoded_loc}",
            "osm_url": f"https://www.openstreetmap.org/search?query=supermarket+{encoded_loc}"
        },
        {
            "name": "Fresh Dairy & Milk Centers",
            "icon": "🥛",
            "description": "Dairy booths (Amul, Vijaya, Mother Dairy, Nandini) for curd, buttermilk, and milk.",
            "gmaps_url": f"https://www.google.com/maps/search/milk+dairy+booth+near+{encoded_loc}",
            "osm_url": f"https://www.openstreetmap.org/search?query=dairy+{encoded_loc}"
        }
    ]

    online_platforms = [
        {
            "platform": "BigBasket",
            "tagline": "Wide range of groceries, staples, millets, and fresh produce across India.",
            "search_url": "https://www.bigbasket.com/"
        },
        {
            "platform": "Blinkit",
            "tagline": "Quick 10-15 min grocery delivery in supported urban and tier-2 zones.",
            "search_url": "https://blinkit.com/"
        },
        {
            "platform": "Zepto",
            "tagline": "Rapid grocery, fresh fruit, and daily essentials delivery.",
            "search_url": "https://www.zeptonow.com/"
        },
        {
            "platform": "Swiggy Instamart",
            "tagline": "Instamart grocery and fresh snacks delivery via Swiggy network.",
            "search_url": "https://www.swiggy.com/instamart"
        },
        {
            "platform": "Amazon Grocery / Fresh",
            "tagline": "Nationwide grocery and pantry delivery to verified PIN codes.",
            "search_url": "https://www.amazon.in/alm/storefront?almBrandId=ctnow"
        }
    ]

    return local_shops, online_platforms

def check_emergency_red_flags(symptoms: list, duration_days: int = 1):
    """
    Evaluates whether active symptoms represent critical red flags
    requiring immediate medical intervention rather than home observation.
    """
    red_flag_triggers = []

    symptom_set = set([s.lower() for s in symptoms])

    if "dehydration_signs" in symptom_set and ("vomiting" in symptom_set or "loose_stools" in symptom_set):
        red_flag_triggers.append("High dehydration risk: Fluid loss coupled with visible dehydration signs requires urgent clinical rehydration.")

    if "fever" in symptom_set and duration_days >= 4:
        red_flag_triggers.append("Prolonged high fever: Fever exceeding 72-96 hours requires blood investigation for malaria, dengue, or typhoid.")

    if "vomiting" in symptom_set and duration_days >= 2:
        red_flag_triggers.append("Persistent intractable vomiting: Inability to retain fluids beyond 24 hours demands parenteral hydration.")

    return red_flag_triggers
