"""
Nutritional Deficiency Education Module
Educational guide covering the 7 essential nutrient deficiencies, physiological roles,
symptom presentations, food sources, risk factors, and recommended clinical lab tests.
Emphasizes symptom overlap and the necessity of laboratory confirmation.
"""

DEFICIENCY_TOPICS = {
    "Iron Deficiency": {
        "title": "Iron Deficiency & Nutritional Anemia",
        "role": (
            "Iron is the central functional atom in hemoglobin, the red blood cell protein responsible for "
            "transporting oxygen from the lungs to all tissues and vital organs. It also powers myoglobin in muscles "
            "and enzymatic cellular respiration."
        ),
        "common_symptoms": [
            "Generalized chronic fatigue and low physical endurance",
            "Exertional breathlessness or rapid heart palpitations",
            "Unusual pallor of conjunctiva (inner eyelids), nail beds, or tongue",
            "Cold extremities (hands and feet)",
            "Brittle, flat, or spoon-shaped nails (koilonychia)",
            "Unusual cravings for non-nutritive substances such as ice, clay, or chalk (pica)"
        ],
        "food_sources": {
            "Plant Sources (Non-Heme)": "Moringa (drumstick leaves), spinach, fenugreek leaves, lentils, chickpeas, raisins, figs, black sesame seeds, and jaggery.",
            "Animal Sources (Heme Iron)": "Lean chicken, eggs, fish, organ meats (liver - highly bioavailable).",
            "Absorption Tips": "Pair non-heme plant iron with Vitamin C (lemon juice, amla, tomatoes); avoid tea/coffee within 1 hour of meals."
        },
        "risk_factors": [
            "Women of reproductive age with heavy menstrual blood loss",
            "Rapid growth phases in children and adolescents",
            "Pregnancy and lactation with heightened fetal iron demands",
            "Strict vegetarian or vegan diets without intentional iron-pairing",
            "Occult gastrointestinal bleeding or malabsorption (celiac disease, H. pylori)"
        ],
        "clinical_tests": (
            "Never self-treat with high-dose iron pills without testing! A physician will typically order a "
            "Complete Blood Count (CBC) with peripheral smear, Serum Ferritin (evaluates bone marrow iron stores), "
            "Serum Iron, and Total Iron-Binding Capacity (TIBC). High-dose iron when not deficient can cause dangerous iron overload (hemochromatosis)."
        )
    },

    "Vitamin B12 Deficiency": {
        "title": "Vitamin B12 (Cobalamin) Deficiency",
        "role": (
            "Vitamin B12 is essential for DNA synthesis during red blood cell division in bone marrow, "
            "and for maintaining the protective myelin sheath insulating peripheral and central nerve fibers."
        ),
        "common_symptoms": [
            "Tingling, 'pins and needles' sensations, or numbness in the fingers and toes (paresthesia)",
            "Unsteady gait, balance difficulties, or frequent stumbling",
            "Persistent fatigue, brain fog, difficulty concentrating, or memory slips",
            "Smooth, red, sore, beefy tongue (glossitis)",
            "Mood fluctuations, mild depressive symptoms, or irritability"
        ],
        "food_sources": {
            "Vegetarian / Plant Sources": "Milk, curd, paneer, fortified breakfast cereals, nutritional yeast, fermented foods.",
            "Animal Sources": "Eggs, fish (salmon, tuna), poultry, meat, dairy.",
            "Special Note for Vegans": "Plants do not synthesize active B12. Strict vegans generally require fortified foods or medically advised oral cyanocobalamin / methylcobalamin."
        },
        "risk_factors": [
            "Long-term strict vegetarian or vegan lifestyle without supplementation",
            "Older adults (>60 years) with decreased gastric acid production (atrophic gastritis)",
            "Individuals taking prolonged metformin (diabetes) or proton-pump inhibitors (acid reflux)",
            "Autoimmune conditions affecting intrinsic factor (pernicious anemia)"
        ],
        "clinical_tests": (
            "Serum Vitamin B12 levels, Complete Blood Count (to check for elevated Mean Corpuscular Volume / megaloblastic anemia), "
            "and in borderline cases, Serum Methylmalonic Acid (MMA) or Homocysteine to confirm cellular deficiency."
        )
    },

    "Vitamin D Deficiency": {
        "title": "Vitamin D ('Sunshine Vitamin') Deficiency",
        "role": (
            "Vitamin D functions as a steroid hormone modulating calcium and phosphate absorption in the small intestine, "
            "directing bone mineralization, and regulating innate and adaptive immune cell signaling."
        ),
        "common_symptoms": [
            "Deep, aching bone pain, especially in the shin, lower back, or hips",
            "Proximal muscle weakness, difficulty rising from low chairs or climbing stairs",
            "Recurrent seasonal respiratory infections and slower healing",
            "Persistent lethargy and low daytime mood (seasonal affective tendencies)"
        ],
        "food_sources": {
            "Natural Sources": "Sunlight (15-20 minutes of midday sunlight on face, arms, and legs without sunscreen).",
            "Dietary Sources": "Egg yolks, fatty fish, mushrooms exposed to UV light, fortified milk, fortified cooking oils."
        },
        "risk_factors": [
            "Modern indoor lifestyles, desk jobs, or minimal sun exposure",
            "Darker skin pigmentation (melanin naturally reduces cutaneous synthesis of vitamin D3)",
            "Strict body covering or clothing habits",
            "Obesity (vitamin D is fat-soluble and becomes sequestered in adipose tissue)",
            "Aging kidneys with reduced conversion of 25-OH to active 1,25-(OH)2D"
        ],
        "clinical_tests": (
            "Serum 25-Hydroxyvitamin D [25(OH)D] blood test. Clinical ranges: Deficient (<20 ng/mL), "
            "Insufficient (20-29 ng/mL), Sufficient (30-100 ng/mL). Doctors prescribe tailored weekly or daily therapeutic doses based on this level."
        )
    },

    "Vitamin C Deficiency": {
        "title": "Vitamin C (Ascorbic Acid) Deficiency",
        "role": (
            "Vitamin C is an essential water-soluble antioxidant cofactor required for collagen biosynthesis "
            "(vital for blood vessel walls, gums, cartilage, and skin repair) and immune leukocyte activation."
        ),
        "common_symptoms": [
            "Bleeding, swollen, or tender gums upon brushing teeth",
            "Easy bruising or pinpoint red/purple spots around hair follicles (petechiae)",
            "Slow, delayed healing of minor cuts and abrasions",
            "Dry, rough, or bumpy skin ('keratosis pilaris')",
            "Joint pain and general malaise"
        ],
        "food_sources": {
            "Top Sources": "Amla (Indian gooseberry - unrivaled concentration), Guava, Oranges, Lemons, Kiwis, Strawberries.",
            "Vegetables": "Bell peppers (capsicum), green chilies, tomatoes, broccoli, cabbage.",
            "Preparation Note": "Vitamin C is heat-labile and destroyed by prolonged cooking; consume fresh raw fruits and salads."
        },
        "risk_factors": [
            "Diets devoid of fresh fruits and vegetables",
            "Chronic active tobacco smoking (nicotine accelerates metabolic turnover of ascorbic acid)",
            "Alcohol dependency and restricted elderly diets"
        ],
        "clinical_tests": (
            "Plasma ascorbic acid level test. Scurvy occurs when total body pool drops severely, but subclinical "
            "insufficiency is frequently diagnosed clinically through dietary history and physical examination of gums and skin."
        )
    },

    "Vitamin A Deficiency": {
        "title": "Vitamin A (Retinol & Carotenoids) Deficiency",
        "role": (
            "Critical for synthesizing rhodopsin (photoreceptor pigment in the retina for night vision), "
            "preserving the integrity of mucosal epithelial linings (respiratory, GI, urinary tracts), and child immune defense."
        ),
        "common_symptoms": [
            "Night blindness (difficulty seeing in twilight or dark rooms)",
            "Extreme dryness of the eyes (xerophthalmia) and Bitot's spots (foamy keratin plaques on conjunctiva)",
            "Frequent recurrent chest infections and prolonged diarrhea",
            "Dry, scaly, hyperkeratotic skin"
        ],
        "food_sources": {
            "Pro-Vitamin A (Beta-carotene)": "Carrots, sweet potatoes, pumpkins, ripe mangoes, papayas, dark leafy greens (moringa, spinach).",
            "Preformed Vitamin A (Retinol)": "Egg yolks, whole milk, butter, fish liver oils.",
            "Absorption Tip": "Beta-carotene is fat-soluble; consume with a small drop of healthy oil or fat to maximize absorption."
        },
        "risk_factors": [
            "Young preschool children in resource-constrained communities",
            "Diets lacking dairy, eggs, and yellow/orange fruits and vegetables",
            "Severe protein-calorie malnutrition or fat malabsorption syndromes"
        ],
        "clinical_tests": (
            "Serum Retinol concentration test. Because the liver stores large amounts of Vitamin A, serum levels "
            "may only fall when liver stores are virtually exhausted."
        )
    },

    "Calcium Concerns": {
        "title": "Calcium Balance & Bone Health",
        "role": (
            "The most abundant mineral in the human body; 99% resides in teeth and skeleton, while 1% circulating in blood "
            "is strictly required for cardiac muscle contraction, neuromuscular transmission, and blood coagulation."
        ),
        "common_symptoms": [
            "Muscle cramps, spasms, or twitching, particularly in the calves and hands",
            "Numbness around the lips or fingertips",
            "Brittle, weak fingernails and poor dental enamel",
            "Progressive, silent loss of bone density (osteopenia, leading to osteoporosis in later life)"
        ],
        "food_sources": {
            "Plant Sources": "Ragi (finger millet), sesame seeds (til - exceptionally high), tofu, chickpeas, amaranth, moringa leaves.",
            "Dairy Sources": "Milk, yogurt (curd), paneer, cheese.",
            "Cofactors": "Calcium requires adequate Vitamin D and Magnesium for proper intestinal absorption and bone deposition."
        },
        "risk_factors": [
            "Postmenopausal women with declining estrogen levels",
            "Inadequate dietary intake during peak bone-mass accumulation (ages 10-25)",
            "Lactose intolerance without compensatory plant calcium sources",
            "Excessive carbonated cola intake (phosphates can compete with calcium absorption)"
        ],
        "clinical_tests": (
            "Serum Total and Ionized Calcium, Serum Albumin (for corrected calcium), Parathyroid Hormone (PTH), "
            "and Dual-Energy X-ray Absorptiometry (DEXA scan) to evaluate bone mineral density."
        )
    },

    "Protein & General Inadequacy": {
        "title": "Protein Inadequacy & Macro-Nutritional Balance",
        "role": (
            "Proteins provide amino acids—the building blocks for all bodily tissues, muscle fibers, immune antibodies, "
            "peptide hormones, and transport enzymes. Adequate caloric balance ensures proteins are not burned as fuel."
        ),
        "common_symptoms": [
            "Loss of muscle mass, decreased physical strength, and flabbiness",
            "Thinning, dull, or easily pluckable hair, and slow-growing brittle nails",
            "Slow wound healing and vulnerability to recurrent infections",
            "Edema (swelling) of the feet, ankles, and legs in severe cases (hypoalbuminemia)",
            "Constant hunger and intense sugar/carb cravings"
        ],
        "food_sources": {
            "Vegetarian": "Lentils (dals), sprouted beans, chickpeas, rajma, paneer, curd, soy chunks, tofu, peanuts, sattu flour.",
            "Non-Vegetarian": "Eggs, chicken, fish, lean meat.",
            "Balanced Target": "Aim for approximately 0.8g to 1.0g of quality protein per kilogram of body weight daily."
        },
        "risk_factors": [
            "Elderly individuals with poor appetite or dental chewing difficulties",
            "High-carb, low-protein diets heavy in polished rice or refined flour without pulses",
            "Chronic wasting illnesses, kidney protein loss, or malabsorption",
            "Crash diets or unmonitored extreme calorie restrictions"
        ],
        "clinical_tests": (
            "Serum Total Protein, Serum Albumin, Blood Urea Nitrogen (BUN), and comprehensive dietary evaluation "
            "by a registered clinical dietitian."
        )
    }
}
