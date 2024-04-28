import os
import sys
import streamlit as st

# Get the current script directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Add the parent directory to the Python path to find the 'scripts' package
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from scripts.recipe_matching_logic import find_matching_recipes, load_and_preprocess_data, calculate_similarity

st.title('Recipe Chatbot')

csv_file_path = "data/Cleaned_raw_recipes_df.csv"
recipes_df = load_and_preprocess_data(csv_file_path)

# Streamlit user input for ingredients
user_input = st.text_area('Enter your ingredients separated by commas:', 'milk, butter, flour')

if user_input:
    # Find recipes based on matching ingredients count
    matched_recipes = find_matching_recipes(user_input, recipes_df)
    recipe_names_match = matched_recipes['name'].tolist()
    
    # Find recipes based on TF-IDF cosine similarity
    similar_recipes = calculate_similarity(user_input, recipes_df)
    # Show only the top 5 recipes based on similarity
    top_similar_recipes = similar_recipes.head(5)
    recipe_names_similarity = top_similar_recipes['name'].tolist()

    # Display the top 5 TF-IDF cosine similarity scores and names before selection
    st.write("Top recipes based on TF-IDF cosine similarity:")
    for index, row in top_similar_recipes.iterrows():
        st.write(f"{row['name']} - Similarity Score: {row['similarity']:.2f}")

    # Selection box for recipes from TF-IDF similarity
    recipe_selection = st.selectbox('Select a recipe to see the cooking steps:', [''] + recipe_names_similarity)
    
    # When a recipe is selected, display its cooking steps
    if recipe_selection:
        # Get the recipe details from the similar_recipes DataFrame
        steps = top_similar_recipes[top_similar_recipes['name'] == recipe_selection].iloc[0]['steps']
        
        st.write('Cooking steps:')
        for i, step in enumerate(steps, start=1):
            st.write(f'Step {i}: {step}')