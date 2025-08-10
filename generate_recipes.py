# generate_recipes.py
import json, random, textwrap

dishes = [
"Chole Bhature","Rajma Chawal","Pav Bhaji","Butter Chicken","Palak Paneer","Masala Dosa","Hyderabadi Biryani",
"Kadhi Pakora","Aloo Paratha","Samosa","Vada Pav","Pani Puri","Dhokla","Idli Sambhar","Rogan Josh","Matar Paneer",
"Paneer Butter Masala","Dal Makhani","Tandoori Chicken","Chicken 65","Chicken Tikka Masala","Korma","Baingan Bharta",
"Aloo Gobi","Bhindi Masala","Prawn Curry","Fish Curry","Litti Chokha","Gulab Jamun","Jalebi","Rasgulla",
"Rabri","Kheer","Seviyan","Malai Kofta","Haleem","Keema Pav","Pesarattu","Neer Dosa","Appam","Kaju Katli",
"Besan Ladoo","Puttu","Egg Curry","Egg Biryani","Mutton Biryani","Nihari","Sheermal","Aloo Tikki","Chana Masala",
"Methi Paratha","Sarson Ka Saag","Makki Ki Roti","Khichdi","Dal Tadka","Lauki Ki Sabzi","Gatte ki Sabzi","Churma Ladoo",
"Sattu Paratha","Pork Vindaloo","Xacuti","Kolkata Biryani","Chingri Malai Curry","Chole","Amritsari Fish","Momos",
"Chowmein","Hakka Noodles","Manchurian","Kebabs","Seekh Kebab","Tikka","Bhelpuri","Dahi Vada","Shrikhand","Basundi",
"Bombay Sandwich","Keema Curry","Bombil Fry","Patra Ni Machhi","Mysore Masala Dosa","Moong Dal Halwa","Shahi Paneer",
"Paneer Tikka","Pahadi Chicken","Bhatura","Kalakand","Thalipeeth","Upma","Poha","Chaas","Lassi","Masala Chai",
"Nihari Gosht","Chhena Poda","Patrode","Korma Curry","Chicken Xacuti","Ambur Biryani","Mutton Curry","Methi Thepla",
"Kadhi Chawal","Prawn Masala","Tindora Fry","Khandvi","Batata Vada","Makhani Dal"
]

# ensure 100 items
if len(dishes) < 100:
    dishes = (dishes * ((100 // len(dishes)) + 1))[:100]

def gen_ingredients(name):
    base = ["Salt", "Turmeric", "Red chili powder", "Oil"]
    extras = name.split()[:2]
    ing = extras + random.sample(base, 3)
    if "Biryani" in name:
        ing = ["Basmati Rice","Meat or Veg","Yogurt","Spices","Saffron"] + ing
    if "Dosa" in name or "Idli" in name:
        ing = ["Rice","Urad Dal","Fenugreek"] + ing
    if "Paneer" in name:
        ing = ["Paneer","Tomato","Cream","Spices"] + ing
    return ing

def gen_instructions(name):
    return f"Simple steps to make {name}: prepare ingredients, follow standard cooking/process steps (marinate/cook/temper), and serve hot."

recipes = []
for i, name in enumerate(dishes, start=1):
    recipe = {
        "id": i,
        "name": name,
        "cuisine": "Indian",
        "ingredients": gen_ingredients(name),
        "instructions": gen_instructions(name),
        "prep_time": f"{random.randint(10,60)} mins",
        "cook_time": f"{random.randint(10,120)} mins",
        "servings": random.choice([1,2,3,4,6]),
        "image": f"https://via.placeholder.com/600x400.png?text={name.replace(' ','+')}"
    }
    recipes.append(recipe)

with open("recipes.json", "w", encoding="utf-8") as f:
    json.dump(recipes, f, indent=2, ensure_ascii=False)

print("recipes.json saved with", len(recipes), "recipes")
