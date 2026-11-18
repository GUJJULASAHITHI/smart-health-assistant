"""
Evidence-Based Health Guidance Module
Provides clinical home-care protocols, hydration guidelines, food suggestions,
foods to avoid, and emergency warning signs for 9 common health concerns.
Strictly non-prescriptive and education-focused.
"""

HEALTH_CONCERNS_GUIDANCE = {
    "Fever": {
        "title": "Fever (Elevated Body Temperature)",
        "explanation": (
            "A fever is a temporary elevation in body temperature (typically 38°C / 100.4°F or higher), "
            "often representing the body's natural immunological response to combat viral or bacterial infections."
        ),
        "possible_causes": [
            "Viral respiratory infections (e.g., influenza, common cold)",
            "Gastrointestinal viral or bacterial infections",
            "Urinary tract infections",
            "Seasonal arboviral illnesses (dengue, chikungunya, malaria in endemic zones)",
            "Post-immunization physiological reactions"
        ],
        "home_care": [
            "Prioritize strict bed rest to conserve metabolic energy.",
            "Wear light, breathable cotton clothing; avoid heavy bundling or multiple thick blankets.",
            "Maintain a comfortable, well-ventilated room temperature.",
            "Apply lukewarm (not cold or iced) water sponge compresses to the forehead and neck if uncomfortable.",
            "Monitor body temperature periodically using a clean digital oral or armpit thermometer."
        ],
        "suitable_foods": [
            "Warm vegetable or lentil soups (easy to swallow, replenishes minerals)",
            "Moong dal khichdi or soft mashed rice (easily digestible carbohydrate source)",
            "Oatmeal, porridge, or broken wheat (dalia)",
            "Cooked apples (applesauce) or ripe bananas",
            "Steamed carrots and pumpkins"
        ],
        "hydration_advice": (
            "Drink plenty of clean fluids throughout the day: warm boiled water, tender coconut water, "
            "dilute clear broth, or weak decaffeinated herbal infusions. Aim for pale straw-colored urine. "
            "Frequent small sips are better than large gulps."
        ),
        "foods_to_avoid": [
            "Deep-fried, heavy oily foods that demand excessive digestive strain",
            "Extremely spicy curries or sauces that cause gastric irritation",
            "Caffeinated beverages (coffee, energy drinks) and alcohol (worsen dehydration)",
            "Raw or unpasteurized foods with microbial contamination risks"
        ],
        "warning_signs": [
            "High fever exceeding 39.4°C (103°F) that persists despite cooling measures",
            "Fever lasting longer than 3 consecutive days",
            "Stiff neck, severe photophobia (eye pain in light), or confusion/drowsiness",
            "New unexplained purple skin rash or petechiae",
            "Severe breathlessness, chest tightness, or persistent vomiting"
        ],
        "when_to_consult": (
            "Consult a medical doctor immediately if any warning sign appears. In infants under 3 months, "
            "any fever requires urgent emergency evaluation. Otherwise, seek clinical review if the fever persists past 72 hours."
        )
    },

    "Common Cold and Cough": {
        "title": "Common Cold and Acute Cough",
        "explanation": (
            "An acute viral infection of the upper respiratory tract involving the mucosal membranes of the "
            "nose, sinuses, and pharynx. It is usually self-limiting and resolves within 7 to 10 days."
        ),
        "possible_causes": [
            "Rhinoviruses, Coronaviruses, Adenoviruses, or Respiratory Syncytial Virus (RSV)",
            "Seasonal changes in ambient temperature and humidity",
            "Allergen exposure or environmental particulate irritants (smoke, dust)"
        ],
        "home_care": [
            "Perform warm saline nasal rinses or steam inhalation to loosen stubborn mucus.",
            "Use warm saline water gargles (1/2 tsp salt in 1 cup warm water) 3 times daily to soothe throat irritation.",
            "Elevate the head with an extra pillow during sleep to ease nasal drainage.",
            "Rest your vocal cords and avoid exposure to active or passive cigarette smoke."
        ],
        "suitable_foods": [
            "Warm ginger-tulsi herbal infusions or warm water with a teaspoon of honey (for individuals >1 year old)",
            "Clear chicken or vegetable broth with mild garlic and black pepper",
            "Soft mashed potatoes, idli, or warm dal soup",
            "Vitamin C-rich fruits (oranges, amla/Indian gooseberry, sweet lime) eaten fresh at room temperature"
        ],
        "hydration_advice": (
            "Maintain continuous mucosal hydration by sipping warm water, herbal teas, or thin broths. "
            "Adequate hydration thins airway secretions, facilitating natural clearance."
        ),
        "foods_to_avoid": [
            "Very cold iced beverages or ice creams (can trigger reactive bronchospasm in sensitive airways)",
            "Excessively dry, crunchy, or coarse foods that scratch and irritate an inflamed pharynx",
            "Heavy dairy cream or greasy curries if they cause thick sensation in the throat"
        ],
        "warning_signs": [
            "Shortness of breath, wheezing, or stridor (noisy high-pitched breathing)",
            "Coughing up blood or rust-colored sputum",
            "Chest pain when inhaling deeply",
            "Inability to swallow liquids or open the mouth fully (possible peritonsillar abscess)",
            "Symptoms worsening significantly after starting to improve ('double sickening')"
        ],
        "when_to_consult": (
            "Seek medical care if a cough persists for more than 2 to 3 weeks, if you have high fever, "
            "or if you have underlying respiratory conditions like asthma or COPD."
        )
    },

    "Headache": {
        "title": "Headache (Tension, Eye Strain, or Dehydration)",
        "explanation": (
            "Pain or aching sensation in the head or upper neck. Most everyday headaches are primary headaches "
            "such as tension headaches, fatigue-related cephalalgia, or dehydration headaches."
        ),
        "possible_causes": [
            "Physical or mental fatigue, emotional stress, lack of adequate sleep",
            "Dehydration or missed/irregular meals (hypoglycemia)",
            "Prolonged digital screen time without blue light filtration or eye breaks",
            "Poor posture causing cervical muscle strain",
            "Caffeine withdrawal or excessive caffeine intake"
        ],
        "home_care": [
            "Rest in a quiet, dimly lit, well-ventilated room with eyes closed.",
            "Apply a warm or cool compress across the forehead or the back of the neck.",
            "Gently massage the temples, scalp, and shoulder muscles to relieve muscular tension.",
            "Practice the 20-20-20 rule during screen use: look 20 feet away for 20 seconds every 20 minutes."
        ],
        "suitable_foods": [
            "A light, balanced snack if a meal was missed: a banana, handful of soaked almonds, or a slice of whole-grain toast",
            "Fresh hydrating fruits: watermelon, cucumber, muskmelon",
            "Complex carbohydrate meals that stabilize blood sugar without sudden spikes"
        ],
        "hydration_advice": (
            "Drink 1 to 2 large glasses of fresh drinking water immediately. Dehydration is one of the most "
            "frequent hidden triggers for mild-to-moderate throbbing tension headaches."
        ),
        "foods_to_avoid": [
            "Aged cheeses, processed cured meats, and artificial sweeteners if known to trigger migraines",
            "Excessive coffee or energy drinks",
            "Alcoholic beverages, particularly red wine"
        ],
        "warning_signs": [
            "'Thunderclap' headache: sudden, explosive pain reaching maximum intensity within seconds",
            "Headache accompanied by fever, stiff neck, altered consciousness, or speech slurring",
            "Headache following a head trauma or fall",
            "New onset focal neurological deficits (weakness on one side of face/body, vision loss)",
            "Headache progressively worsening over weeks in individuals over 50 years of age"
        ],
        "when_to_consult": (
            "Seek emergency medical evaluation for any thunderclap or post-injury headache. "
            "Consult a physician if headaches occur more than 2 to 3 times a week or interfere with daily living."
        )
    },

    "Loose Motions or Diarrhoea": {
        "title": "Loose Motions / Acute Diarrhoea",
        "explanation": (
            "The passage of three or more loose, liquid, or watery stools per day. The critical health danger "
            "in acute diarrhea is fluid and electrolyte loss rather than the stool frequency itself."
        ),
        "possible_causes": [
            "Infectious gastroenteritis (viral pathogens like Rotavirus/Norovirus, or foodborne bacteria)",
            "Contaminated drinking water or unhygienically prepared food",
            "Medication side-effects (e.g., broad-spectrum antibiotics)",
            "Food intolerances (lactose, sorbitol) or dietary sudden changes"
        ],
        "home_care": [
            "Prioritize Oral Rehydration Salts (ORS) prepared precisely according to the packaging instructions.",
            "Continue nutritional feeding; do not fast or starve the digestive tract.",
            "Maintain strict hand hygiene using soap and safe water before meals and after restroom use.",
            "Rest the body to avoid exertion-induced dehydration."
        ],
        "suitable_foods": [
            "Boiled rice with light curd/yogurt (source of probiotics and gentle carbohydrates)",
            "Rice kanji or rice water with a pinch of safe salt",
            "Boiled potatoes, plain toast, or khichdi made with yellow moong dal",
            "Ripe bananas (provides gentle potassium and pectin to firm stools)",
            "Steamed apples or tender coconut water"
        ],
        "hydration_advice": (
            "Oral Rehydration Salts (WHO standard ORS) is the gold standard: dissolve 1 full sachet in 1 liter "
            "of safe drinking water. Sip 100-200 ml after each loose bowel movement. Do not boil ORS once mixed. "
            "Never substitute with high-sugar soda or sweetened commercial juice."
        ),
        "foods_to_avoid": [
            "Milk and creamy dairy products (temporary secondary lactase enzyme deficiency during diarrhea)",
            "High-fat, spicy, fried foods that stimulate gastrocolic reflex",
            "Artificial sweeteners (sorbitol, mannitol) and sugary packaged sodas (osmotic diarrhea)",
            "Raw vegetables, unwashed salads, and unpeeled fruits"
        ],
        "warning_signs": [
            "Visible blood or black tarry substance in stools (dysentery)",
            "High fever persisting with severe abdominal cramping",
            "Signs of severe dehydration: sunken eyes, no urine passed for over 6-8 hours, extreme lethargy, dizziness upon standing",
            "Inability to retain any oral fluids due to continuous vomiting",
            "Diarrhea lasting longer than 48 hours without improvement"
        ],
        "when_to_consult": (
            "Immediately seek clinical attention at the nearest clinic or Primary Health Centre (PHC) if signs "
            "of dehydration, blood in stool, or inability to take fluids occurs."
        )
    },

    "Vomiting": {
        "title": "Vomiting and Nausea",
        "explanation": (
            "The forceful expulsion of stomach contents through the mouth, controlled by the brainstem vomiting center. "
            "Acute vomiting requires careful fluid preservation to prevent rapid electrolyte decompensation."
        ),
        "possible_causes": [
            "Acute gastroenteritis or food poisoning",
            "Gastric irritation, acid reflux, or motion sickness",
            "Early viral illnesses or inner ear vestibular disturbance",
            "Severe migraine episode"
        ],
        "home_care": [
            "Allow the stomach to rest for 30 to 60 minutes immediately following an episode of vomiting.",
            "Do not gulp large volumes of water immediately; this stretches the stomach and triggers nausea reflex.",
            "Sit upright; avoid lying flat on your back immediately after fluid intake to prevent aspiration.",
            "Rinse the mouth with cool water to remove acidic taste and protect dental enamel."
        ],
        "suitable_foods": [
            "Once vomiting has stopped for at least 4 to 6 hours, reintroduce bland foods:",
            "Dry toast or plain saltine crackers",
            "Plain boiled white rice or simple dal water (soup)",
            "Clear light vegetable broth",
            "Dilute applesauce"
        ],
        "hydration_advice": (
            "Start with tiny sips of ORS or cool boiled water: 1 teaspoon (5 ml) every 5 minutes. "
            "If tolerated for an hour, gradually increase to 1-2 tablespoons. Frozen electrolyte ice chips "
            "are also gentle and well tolerated."
        ),
        "foods_to_avoid": [
            "Oily, pungent, spicy, or fried foods",
            "Citrus juices, tomato-based sauces, and vinegar-rich foods (acidic triggers)",
            "Coffee, tea, alcohol, and carbonated beverages",
            "Dairy milk products during the acute vomiting phase"
        ],
        "warning_signs": [
            "Inability to keep any fluids down for more than 12-24 hours",
            "Vomit containing blood ('coffee ground' appearance or bright red)",
            "Severe localized abdominal pain or rigid, hard belly",
            "Concurrent severe headache and stiff neck",
            "Signs of severe dehydration (fainting, confusion, very dark concentrated urine)"
        ],
        "when_to_consult": (
            "Seek urgent medical evaluation if fluids cannot be retained, if vomiting contains blood, or if symptoms "
            "persist beyond 24 hours in adults or 12 hours in young children."
        )
    },

    "Mild Stomach Discomfort": {
        "title": "Mild Stomach Discomfort and Dyspepsia",
        "explanation": (
            "A sensation of fullness, bloating, mild upper abdominal burning, or mild cramping often related to "
            "delayed gastric emptying, acid reflux, or dietary indiscretion."
        ),
        "possible_causes": [
            "Overeating, eating too rapidly, or consuming excessively spicy or fatty meals",
            "Mild acid reflux / indigestion (dyspepsia)",
            "Stress, irregular meal timings, or prolonged empty stomach",
            "Mild gas accumulation from fermentable foods"
        ],
        "home_care": [
            "Eat smaller, more frequent meals rather than large, heavy sittings.",
            "Chew food thoroughly in a relaxed, seated posture.",
            "Avoid lying down or going to sleep for at least 2 to 3 hours after a meal.",
            "A warm hot-water bag placed over the abdomen can help ease mild muscle cramping."
        ],
        "suitable_foods": [
            "Boiled rice, moong dal khichdi, or soft oatmeal",
            "Fresh buttermilk (chaas) with a pinch of roasted cumin and mint",
            "Steamed squash, carrots, or boiled potatoes",
            "Chamomile, mint, or ginger tea"
        ],
        "hydration_advice": (
            "Sip room-temperature water throughout the day. Avoid drinking large amounts of water "
            "during meals as it dilutes digestive secretions."
        ),
        "foods_to_avoid": [
            "Deep-fried samosas, pakoras, oily gravies, and heavy cheeses",
            "Carbonated fizzy sodas (introduces excess gas into the gastric lumen)",
            "Excessive black pepper, chili powder, and raw garlic/onion",
            "Alcohol and smoking"
        ],
        "warning_signs": [
            "Severe, sharp, agonizing abdominal pain that radiates to the back or shoulder",
            "Stomach pain accompanied by fever, jaundice (yellow eyes/skin), or persistent vomiting",
            "Unexplained rapid weight loss or persistent difficulty swallowing food",
            "Black, tarry bowel movements or vomiting blood"
        ],
        "when_to_consult": (
            "Consult a physician if stomach discomfort persists for more than 7 days, wakes you from sleep, "
            "or fails to respond to mild dietary adjustments."
        )
    },

    "Weakness and Tiredness": {
        "title": "General Weakness and Fatigue",
        "explanation": (
            "A persistent feeling of physical exhaustion, reduced energy, and diminished stamina that is not "
            "relieved by brief rest. It can arise from lifestyle factors, convalescence after illness, or metabolic imbalances."
        ),
        "possible_causes": [
            "Recent recovery from a viral or febrile illness (post-viral asthenia)",
            "Chronic sleep deprivation, irregular sleep-wake schedules, or sleep apnea",
            "Inadequate caloric intake or poorly balanced diet lacking micronutrients",
            "Dehydration or sustained occupational/academic stress",
            "Possible underlying medical conditions (e.g., anemia, thyroid dysfunction, diabetes) that require testing"
        ],
        "home_care": [
            "Establish a consistent sleep schedule aiming for 7 to 9 hours of restorative sleep.",
            "Engage in gentle daily movement (e.g., 20-30 minutes of brisk walking) to stimulate circulation.",
            "Take scheduled cognitive and physical breaks throughout the workday.",
            "Keep an objective log of energy levels, meals, and sleep to discuss with your healthcare provider."
        ],
        "suitable_foods": [
            "Complex whole grains: brown rice, millets (ragi, jowar, bajra), whole-wheat rotis",
            "Protein-rich legumes: lentils, sprouted moong, chickpeas, paneer, tofu, or eggs",
            "Iron and folate rich greens: spinach, fenugreek (methi), moringa (drumstick leaves)",
            "Nuts and seeds: soaked almonds, walnuts, pumpkin seeds, and sesame seeds",
            "Seasonal fresh fruits for natural vitamins and minerals"
        ],
        "hydration_advice": (
            "Maintain consistent hydration: mild chronic dehydration is a very common cause of fatigue and brain fog. "
            "Aim for 2 to 2.5 liters of clean water daily, supplemented with fresh coconut water or buttermilk."
        ),
        "foods_to_avoid": [
            "Sugary snacks, candies, and sugary drinks that cause rapid blood sugar surges followed by fatigue crashes",
            "Excessive reliance on caffeine (more than 2-3 cups of strong coffee/tea)",
            "Highly refined white flour (maida) bakery products lacking fiber and micronutrients"
        ],
        "warning_signs": [
            "Weakness accompanied by breathlessness on minimal exertion or chest discomfort",
            "Extreme pallor (pale inner eyelids, tongue, or nail beds) with rapid heart rate",
            "Sudden focal weakness in one limb, facial droop, or difficulty speaking (requires emergency 112/108 call)",
            "Unintended significant weight loss, night sweats, or persistent low-grade fever",
            "Severe fatigue lasting beyond 3 to 4 weeks despite adequate rest and diet"
        ],
        "when_to_consult": (
            "Schedule a clinical evaluation with a doctor for persistent fatigue. Do not assume it is just a simple "
            "vitamin deficiency without proper medical blood tests (e.g., Complete Blood Count, Ferritin, Thyroid Panel, Vitamin D & B12)."
        )
    },

    "Dehydration": {
        "title": "Dehydration (Fluid & Electrolyte Depletion)",
        "explanation": (
            "A condition that occurs when the loss of body fluids—principally water and electrolytes like sodium, "
            "potassium, and chloride—exceeds fluid intake, disrupting cellular and metabolic equilibrium."
        ),
        "possible_causes": [
            "Prolonged heat exposure or heavy exertion without adequate water replacement",
            "Excessive fluid loss from diarrhea, vomiting, or high fever",
            "Insufficient fluid intake in elderly individuals or busy individuals",
            "Diuretic medications or untreated hyperglycemia"
        ],
        "home_care": [
            "Move immediately to a cool, shaded, or air-conditioned environment.",
            "Loosen tight clothing to encourage heat dissipation.",
            "Rest in a reclining position with legs slightly elevated if feeling lightheaded.",
            "Perform simple self-checks: check urine color (should be light yellow, not dark amber)."
        ],
        "suitable_foods": [
            "Water-dense fresh fruits: watermelon, muskmelon, oranges, sweet lime, pineapples",
            "Hydrating vegetables: cucumber, tomatoes, zucchini, bottle gourd (lauki)",
            "Light curd (dahi) or salted buttermilk with mint and coriander",
            "Clear vegetable soups with added mineral salts"
        ],
        "hydration_advice": (
            "For mild-to-moderate dehydration, rehydrate with an electrolyte-balanced fluid like WHO-formulated ORS, "
            "tender coconut water, or salted lemon water. Sip continuously rather than drinking excessive plain water "
            "all at once, which could dilute blood sodium levels."
        ),
        "foods_to_avoid": [
            "Sugary packaged energy drinks, colas, and fruit concentrates (high osmolarity draws water into intestines)",
            "Alcohol and caffeinated drinks (act as mild diuretics)",
            "Dry, salty, highly processed snack foods (chips, salted nuts) without concurrent water intake"
        ],
        "warning_signs": [
            "Severe thirst accompanied by dry, shriveled mouth and tongue",
            "Absence of urination for more than 8 hours, or dark brown urine",
            "Extreme dizziness, orthostatic hypotension (blackout upon standing), or fainting",
            "Confusion, lethargy, or rapid shallow breathing and weak thready pulse",
            "Sunken eyes and loss of skin turgor (skin tenting test)"
        ],
        "when_to_consult": (
            "Moderate to severe dehydration requires urgent outpatient or emergency medical management, "
            "often including intravenous (IV) fluid resuscitation. Seek medical help without delay."
        )
    },

    "Nutritional Concerns": {
        "title": "Nutritional Inadequacy and Dietary Imbalance",
        "explanation": (
            "Situations where dietary intake does not consistently provide sufficient macro- or micronutrients "
            "(vitamins, minerals, proteins, essential fatty acids) necessary for optimal physiological maintenance."
        ),
        "possible_causes": [
            "Monotonous diets lacking diverse fruits, vegetables, pulses, and whole grains",
            "Socio-economic constraints or restricted food access",
            "Malabsorption issues (celiac disease, chronic gut inflammation)",
            "Restrictive fad diets or prolonged irregular meal patterns",
            "Increased physiological demands (adolescence, pregnancy, lactation, heavy labor)"
        ],
        "home_care": [
            "Incorporate 'MyPlate' principles: fill half the plate with colorful vegetables and fruits, "
            "one quarter with whole grains, and one quarter with protein-dense foods.",
            "Diversify the plate with local, seasonal produce rather than expensive imported superfoods.",
            "Include traditional fermented foods (idli, dosa, curd, pickles in moderation) for gut microbiome health.",
            "Maintain food safety and hygienic preparation to maximize nutrient bioavailability."
        ],
        "suitable_foods": [
            "Protein and Iron rich pulses: sprouted lentils, chickpeas, rajma, soybean, eggs, fish",
            "Calcium rich sources: milk, paneer, ragi (finger millet), sesame seeds (til), dark green leafy vegetables",
            "Vitamin C enhancers: amla, guava, lemon, tomatoes (enhancing iron absorption from plant meals)",
            "Micronutrient seeds: flaxseeds, chia seeds, sunflower seeds, pumpkin seeds",
            "Traditional wholesome staples: millets, brown rice, whole wheat"
        ],
        "hydration_advice": (
            "Drink 2 to 3 liters of clean, safe drinking water. Avoid drinking tea or coffee immediately "
            "with iron-rich meals, as tannins inhibit non-heme iron absorption."
        ),
        "foods_to_avoid": [
            "Ultra-processed packaged foods with high empty calories, excessive sodium, and trans fats",
            "Sweetened breakfast cereals and sugary carbonated beverages",
            "Excessive unmonitored dietary supplements without doctor's blood tests"
        ],
        "warning_signs": [
            "Severe pallor, brittle spoon-shaped nails (koilonychia), or cracking at the corners of the mouth (angular cheilitis)",
            "Significant unintended weight loss or muscle wasting",
            "Persistent numbness or tingling in the hands and feet (peripheral neuropathy)",
            "Recurrent infections or poor wound healing",
            "Bone pain or frequent unexplained fractures"
        ],
        "when_to_consult": (
            "Visit a healthcare professional or clinical nutritionist for a comprehensive physical examination "
            "and laboratory blood profiling before taking high-dose pharmacological supplements."
        )
    }
}
