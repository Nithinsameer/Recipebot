import os
import openai

# Initialize the OpenAI client with the API key
openai.api_key = 'sk-proj-4nA8mk64m2ZDzjRGcedpT3BlbkFJCHZ7ukA9SLIkw3SANJkS'

""""
def parse_recipe(recipe):
    ingredients = ', '.join(recipe['ingredients'])
    #method = '. '.join(recipe['steps'])
    return f"Ingredients: {ingredients}"
"""
def parse_recipe(recipe):
    ingredients = recipe['ingredients']
    validated_ingredients = validate_ingredients(ingredients)
    ingredients_str = ', '.join(validated_ingredients)
    return f"Ingredients: {ingredients_str}"

def validate_ingredients(recipe_text):
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an assistant that validates ingredients for recipes."},
                {"role": "user", "content": f"Here is a list of ingredients: {', '.join(recipe_text)}. Please confirm if these are valid ingredients and remove any invalid items."}
            ]
        )
        validated_ingredients = response.choices[0].message.content.strip().split(', ')
        return validated_ingredients
    except Exception as e:
        return f"Error in validating ingredients: {str(e)}"

def indianize_recipe(recipe_text):
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": f"Here is a recipe: {recipe_text} Can you adapt this recipe to an Indian style?"}
            ]
        )
        # Accessing the response correctly
        adapted_text = response.choices[0].message.content
        return adapted_text
    except Exception as e:
        return f"Error in generating recipe: {str(e)}"

def get_indian_recipe(recipe):
    recipe_text = parse_recipe(recipe)
    return indianize_recipe(recipe_text)

if __name__ == '__main__':
    recipe = {
        'ingredients': ['Butter', 'Tomatoes', 'Spaghetti', 'Human']
        #'steps': ['Boil the water.', 'Add the rice and salt.', 'Cook for 15 minutes.']
    }
    print(get_indian_recipe(recipe))
