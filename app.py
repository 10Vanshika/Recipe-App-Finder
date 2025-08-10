# app.py
import streamlit as st
import json
from pathlib import Path

st.set_page_config(page_title="Indian Recipe Finder", layout="wide")
st.title("🍛 Indian Recipe Finder")
# hello
# Load recipes
DATA_PATH = Path(__file__).parent / "recipes.json"
with open(DATA_PATH, "r", encoding="utf-8") as f:
    recipes = json.load(f)

# Sidebar controls
st.sidebar.header("Search & Filters")
query = st.sidebar.text_input("Search (name or ingredient)", "")
cuisine = st.sidebar.selectbox("Cuisine", ["All"] + sorted(list({r.get('cuisine','Indian') for r in recipes})))
max_results = st.sidebar.slider("Max results", 6, 60, 24, 6)

# Preprocess query
q = query.strip().lower()

# Filter
filtered = []
for r in recipes:
    if cuisine != "All" and r.get("cuisine","Indian") != cuisine:
        continue
    if q:
        if q in r["name"].lower() or any(q in ing.lower() for ing in r.get("ingredients",[])):
            filtered.append(r)
    else:
        filtered.append(r)

filtered = filtered[:max_results]

# Display grid of compact cards
cols = st.columns(3)
for idx, r in enumerate(filtered):
    col = cols[idx % 3]
    with col:
        st.image(r.get("image"), width=250)
        st.subheader(r["name"])
        st.caption(f"{r.get('cuisine','Indian')} • {r.get('prep_time','')}")
        if st.button("View Recipe", key=f"view_{r['id']}"):
            st.session_state['selected'] = r['id']

# Detail view
if 'selected' in st.session_state:
    sel = next((x for x in recipes if x['id']==st.session_state['selected']), None)
    if sel:
        st.markdown("---")
        left, right = st.columns([1,1])
        with left:
            st.image(sel.get('image'), width=420)
        with right:
            st.header(sel['name'])
            st.write(f"**Cuisine:** {sel.get('cuisine','Indian')}")
            st.write(f"**Prep:** {sel.get('prep_time','')} • **Cook:** {sel.get('cook_time','')} • **Serves:** {sel.get('servings','')}")
            st.subheader("Ingredients")
            for ing in sel.get('ingredients',[]):
                st.write("- " + ing)
            st.subheader("Instructions")
            st.write(sel.get('instructions',''))
            if st.button("Back to results"):
                del st.session_state['selected']
