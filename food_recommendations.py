"""
Food and Nutrition Recommendation Engine
Contains comprehensive food items across 9 categories with macro/micronutrient breakdown,
suitability context, affordable alternatives, vegetarian substitutes, seasonal availability,
and allergy/dietary precautions.
"""

FOOD_DATABASE = [
    # 1. Whole Grains & Staples
    {
        "name": "Moong Dal Khichdi",
        "category": "Whole grains",
        "dietary_types": ["Vegetarian", "Vegan", "Gluten-free"],
        "nutrients": "Carbohydrates, plant-based protein, dietary fiber, potassium, B-complex vitamins",
        "benefits": "Provides gentle, sustained glucose release; easy on the digestive tract; supports gut recovery.",
        "why_suitable": "Golden standard for digestive rest during fever, diarrhea, vomiting recovery, or stomach upset.",
        "affordable_alternative": "Plain broken rice (kanji) with boiled yellow lentils and a pinch of salt.",
        "vegetarian_alternative": "Naturally vegetarian and vegan.",
        "seasonal_availability": "All-season staple across all regions.",
        "precautions": "Avoid heavy ghee or harsh whole spices if recovering from acute diarrhea or active nausea."
    },
    {
        "name": "Ragi Porridge / Malt (Finger Millet)",
        "category": "Whole grains",
        "dietary_types": ["Vegetarian", "Vegan", "Gluten-free"],
        "nutrients": "Extremely rich in Calcium (344mg/100g), Iron, Dietary Fiber, Polyphenols",
        "benefits": "Supports bone mineral density, strengthens muscle stamina, helps combat nutritional fatigue.",
        "why_suitable": "Excellent nutritional dense food during general weakness and long-term nutritional rehabilitation.",
        "affordable_alternative": "Jowar (sorghum) flour porridge or whole wheat dalia.",
        "vegetarian_alternative": "Can be prepared with water or soy milk for dairy-free/vegan diets.",
        "seasonal_availability": "Year-round availability; traditionally warming in winter.",
        "precautions": "Introduce gradually if not used to high-fiber millets to prevent mild initial bloating."
    },
    {
        "name": "Rolled Oatmeal with Stewed Apple",
        "category": "Whole grains",
        "dietary_types": ["Vegetarian", "Vegan", "Gluten-free"],
        "nutrients": "Beta-glucan soluble fiber, Manganese, Phosphorus, Magnesium, Iron, B1",
        "benefits": "Soluble beta-glucans form a soothing gel in the gut, stabilizing blood sugar and supporting immunity.",
        "why_suitable": "Comfort food during cough, cold, mild fever, or low appetite.",
        "affordable_alternative": "Broken wheat (dalia) porridge with sliced banana or jaggery.",
        "vegetarian_alternative": "Naturally vegetarian; prepare with water or plant milk for vegan.",
        "seasonal_availability": "All-season.",
        "precautions": "Ensure certified gluten-free oats if diagnosed with celiac disease."
    },

    # 2. Pulses, Beans & Legumes
    {
        "name": "Sprouted Green Moong (Mung Bean) Salad or Curry",
        "category": "Pulses and beans",
        "dietary_types": ["Vegetarian", "Vegan", "Gluten-free"],
        "nutrients": "High digestible protein, Vitamin C, Folate, Iron, Potassium, Enzymes",
        "benefits": "Sprouting enhances vitamin C synthesis and multiplies bioavailability of iron and amino acids.",
        "why_suitable": "Ideal for rebuilding cellular strength after illness, addressing weakness and iron inadequacy.",
        "affordable_alternative": "Boiled whole green gram or soaked roasted Bengal gram (chana).",
        "vegetarian_alternative": "Plant-based protein powerhouse.",
        "seasonal_availability": "All-season (easily sprouted at home in 24 hours).",
        "precautions": "Steam sprouts lightly if digestive fire is weak; avoid raw sprouts during acute loose stools."
    },
    {
        "name": "Steamed Chickpeas (Sundal / Chana Bowl)",
        "category": "Pulses and beans",
        "dietary_types": ["Vegetarian", "Vegan", "Gluten-free"],
        "nutrients": "Plant protein, complex carbs, soluble fiber, Folate, Phosphorus, Zinc",
        "benefits": "Promotes satiety, repairs tissues, provides sustained energy for active individuals.",
        "why_suitable": "Overcomes chronic physical fatigue and nutritional protein shortfall.",
        "affordable_alternative": "Boiled brown horse gram (kulthi) or cowpeas (lobia).",
        "vegetarian_alternative": "Complete plant protein when paired with brown rice or millet rotis.",
        "seasonal_availability": "All-year pantry staple.",
        "precautions": "Soak for 8-10 hours and cook thoroughly with a pinch of hing (asafoetida) to reduce oligosaccharide gas."
    },

    # 3. Fruits
    {
        "name": "Fresh Ripe Bananas",
        "category": "Fruits",
        "dietary_types": ["Vegetarian", "Vegan", "Gluten-free"],
        "nutrients": "Potassium, Vitamin B6, Vitamin C, Magnesium, Pectin, Fructose",
        "benefits": "Rapidly replenishes depleted potassium electrolytes, provides soothing soluble pectin to firm bowel movements.",
        "why_suitable": "Core component of the BRAT diet; essential during diarrhea, dehydration, and exercise fatigue.",
        "affordable_alternative": "Locally grown regional varieties (Pachabale, Yelakki, Cavendish) are widely budget-friendly.",
        "vegetarian_alternative": "Naturally vegan.",
        "seasonal_availability": "Ubiquitous year-round across India and global markets.",
        "precautions": "Ensure banana is ripe; raw unripe green bananas are astringent and harder to digest unless cooked."
    },
    {
        "name": "Indian Gooseberry (Amla) / Guava",
        "category": "Fruits",
        "dietary_types": ["Vegetarian", "Vegan", "Gluten-free"],
        "nutrients": "Exceptional Vitamin C (600-900mg/100g in Amla), Polyphenols, Gallic acid, Flavonoids",
        "benefits": "Potent antioxidant; promotes neutrophil activity, enhances non-heme iron absorption in gut.",
        "why_suitable": "Supports immune defense during colds, respiratory cough, and iron deficiency states.",
        "affordable_alternative": "Local guavas, sweet limes (mosambi), or freshly squeezed lemon in warm water.",
        "vegetarian_alternative": "Naturally plant-based.",
        "seasonal_availability": "Amla in winter; Guava post-monsoon and winter; Lemon all year.",
        "precautions": "Eat whole fruit or freshly crushed; avoid boiling amla excessively as heat degrades ascorbic acid."
    },
    {
        "name": "Tender Coconut Water",
        "category": "Fruits",
        "dietary_types": ["Vegetarian", "Vegan", "Gluten-free"],
        "nutrients": "Natural isotonic electrolytes: Potassium, Sodium, Magnesium, Calcium, gentle sugars",
        "benefits": "Rapid cellular rehydration; soothes gastric mucosal inflammation and balances cellular osmolarity.",
        "why_suitable": "Superior natural hydrator for fever convalescence, diarrhea recovery, and summer heat exhaustion.",
        "affordable_alternative": "Homemade salted lemon water with a pinch of salt and sugar, or standard WHO ORS.",
        "vegetarian_alternative": "Naturally vegan.",
        "seasonal_availability": "Year-round in tropical/subtropical regions; peak summer abundance.",
        "precautions": "Those with severe end-stage renal disease (ESRD) must monitor high potassium intake with their doctor."
    },

    # 4. Vegetables
    {
        "name": "Steamed Moringa / Drumstick Leaves (Moringa Oleifera)",
        "category": "Vegetables",
        "dietary_types": ["Vegetarian", "Vegan", "Gluten-free"],
        "nutrients": "Iron, Vitamin A (Beta-carotene), Vitamin C, Calcium, Plant Protein, Quercetin",
        "benefits": "One of nature's most nutrient-dense greens; boosts hemoglobin synthesis and immune cellular repair.",
        "why_suitable": "Combats iron deficiency, post-viral weakness, and micronutrient malnutrition.",
        "affordable_alternative": "Spinach (palak), methi (fenugreek leaves), or amaranth greens (chaulai).",
        "vegetarian_alternative": "Premier plant-based micronutrient powerhouse.",
        "seasonal_availability": "Plentiful year-round in backyards, villages, and local markets.",
        "precautions": "Always cook drumstick leaves; avoid consuming raw in large quantities during early pregnancy without medical guidance."
    },
    {
        "name": "Boiled / Steamed Bottle Gourd (Lauki / Sorakaya)",
        "category": "Vegetables",
        "dietary_types": ["Vegetarian", "Vegan", "Gluten-free"],
        "nutrients": "96% water content, Potassium, Zinc, soluble dietary fiber, Vitamin B-complex",
        "benefits": "Extremely soothing to the gastrointestinal mucosa, diuretic, cooling, effortless to assimilate.",
        "why_suitable": "Perfect for dyspepsia, mild gastritis, urinary burning, fever hydration, and convalescence.",
        "affordable_alternative": "Ridge gourd (turai / beerakaya), ash gourd (safed petha), or snake gourd (potlakaya).",
        "vegetarian_alternative": "Naturally vegan.",
        "seasonal_availability": "Summer and monsoon peak, available year-round.",
        "precautions": "Taste a drop before cooking: discard immediately if bitter (indicates toxic cucurbitacins)."
    },

    # 5. Dairy & Plant-Based Alternatives
    {
        "name": "Fresh Curd (Dahi) / Probiotic Buttermilk (Chaas)",
        "category": "Dairy products and suitable alternatives",
        "dietary_types": ["Vegetarian", "Gluten-free"],
        "nutrients": "Lactobacillus probiotics, Bioavailable Calcium, Vitamin B12, High-quality Whey and Casein Protein",
        "benefits": "Restores beneficial commensal gut microflora, inhibits enteropathogens, cools internal heat.",
        "why_suitable": "Accelerates recovery in loose motions, antibiotic-associated diarrhea, and acid indigestion.",
        "affordable_alternative": "Home-set milk curd diluted with clean water and roasted cumin.",
        "vegetarian_alternative": "Fortified soy curd, coconut yogurt, or fermented rice water for strict vegans.",
        "seasonal_availability": "All-season household staple.",
        "precautions": "Avoid heavily sweetened commercial flavored yogurts; choose unsweetened, freshly set dahi."
    },
    {
        "name": "Fresh Cottage Cheese (Paneer) or Tofu",
        "category": "Dairy products and suitable alternatives",
        "dietary_types": ["Vegetarian", "Gluten-free"],
        "nutrients": "Complete protein, Calcium, Phosphorus, Selenium, Vitamin B12 (in paneer), Isoflavones (in tofu)",
        "benefits": "Accelerates tissue rebuilding, increases muscular strength, supports bone health.",
        "why_suitable": "Overcomes protein deficiency and general fatigue in vegetarian diets.",
        "affordable_alternative": "Sprouted black chana or roasted Bengal gram (sattu flour).",
        "vegetarian_alternative": "Tofu (soy paneer) serves as an identical 100% plant-based/vegan substitute.",
        "seasonal_availability": "All-year.",
        "precautions": "Do not deep fry into heavy gravies during digestive ailments; consume lightly steamed or raw."
    },

    # 6. Protein & Iron-Dense Foods
    {
        "name": "Boiled Eggs",
        "category": "Protein-rich foods",
        "dietary_types": ["Non-Vegetarian", "Gluten-free"],
        "nutrients": "Complete amino acid profile (6g protein/egg), Choline, Iron, Vitamin B12, Vitamin D, Lutein",
        "benefits": "The biological reference standard for dietary protein; effortlessly absorbed; repairs muscle wasting.",
        "why_suitable": "Rapidly replenishes stamina in post-fever convalescence, athletic fatigue, and nutritional deficiency.",
        "affordable_alternative": "Roasted gram flour (sattu) or boiled chickpeas (chana).",
        "vegetarian_alternative": "Paneer, tofu, sprouted green moong, or tempeh.",
        "seasonal_availability": "All-year.",
        "precautions": "Ensure eggs are boiled through (firm yolk and white) to avoid Salmonella risks."
    },
    {
        "name": "Sesame Seeds (Til) with Jaggery (Chikki / Ladoo)",
        "category": "Iron-rich foods",
        "dietary_types": ["Vegetarian", "Vegan", "Gluten-free"],
        "nutrients": "Very high Calcium (975mg/100g), Non-heme Iron, Copper, Zinc, healthy polyunsaturated fats",
        "benefits": "Synergistic traditional combination: unrefined jaggery provides natural iron, sesame supplies calcium and minerals.",
        "why_suitable": "Exceptional traditional snack for fatigue, adolescent anemia prevention, and bone strength.",
        "affordable_alternative": "Roasted groundnuts (peanuts) with organic jaggery.",
        "vegetarian_alternative": "100% plant-based traditional sweet.",
        "seasonal_availability": "All-year; traditional staple during winter and festive harvest season.",
        "precautions": "Consume in moderate portions (1-2 small pieces) due to high caloric density; verify sesame allergy."
    }
]

def recommend_foods(health_concern=None, dietary_pref="All", category_filter="All"):
    """
    Filters the food database according to health concern, dietary preferences,
    and specific food categories.
    """
    results = []

    for item in FOOD_DATABASE:
        # Filter dietary preference
        if dietary_pref != "All":
            if dietary_pref not in item["dietary_types"]:
                continue

        # Filter category
        if category_filter != "All":
            if item["category"] != category_filter:
                continue

        # Score relevance to health concern
        relevance_score = 1
        if health_concern:
            hc_lower = health_concern.lower()
            text_context = (item["why_suitable"] + " " + item["benefits"] + " " + item["name"]).lower()
            if any(term in text_context for term in hc_lower.split()):
                relevance_score = 2

        item_copy = dict(item)
        item_copy["relevance"] = relevance_score
        results.append(item_copy)

    # Sort so most relevant foods show first
    results.sort(key=lambda x: x["relevance"], reverse=True)
    return results
