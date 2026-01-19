import streamlit as st
from PIL import Image
import google.generativeai as genai # Using Gemini for high-speed vision

# 1. Setup & Configuration
st.set_page_config(page_title="Fridge Vision AI", page_icon="🥗")
st.title("🥗 Fridge Vision")
st.subheader("Turn your 'random stuff' into dinner.")

# User enters their API Key (or you can hardcode it for personal use)
api_key = st.sidebar.text_input("Enter Gemini API Key", type="password")

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-2.0-flash')

    # 2. Image Input
    img_file = st.camera_input("Take a photo of your fridge or pantry")

    if img_file:
        img = Image.open(img_file)
        st.image(img, caption="What the AI sees...", use_container_width=True)

        with st.spinner('Analyzing ingredients and cooking...'):
            # 3. The Prompt (The "Secret Sauce")
            prompt = """
            Act as a 5-star chef. Identify all food items in this image. 
            Suggest ONE simple, delicious recipe using only these items plus basic staples (oil, salt, pepper).
            Format the output as:
            1. Identified Ingredients
            2. Recipe Name
            3. Prep Time
            4. Step-by-Step Instructions
            """
            
            response = model.generate_content([prompt, img])
            
            # 4. Display Result
            st.success("Recipe Found!")
            st.markdown(response.text)
else:
    st.info("Please enter your API key in the sidebar to start cooking.")
