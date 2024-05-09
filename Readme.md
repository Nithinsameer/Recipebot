# Recipe Mate

## Problem Statement
1. Users often have ingredients on hand but lack recipe ideas that utilize those ingredients.
2. Existing recipes may not cater to specific regional preferences (e.g., Indian cuisine).
3. Cooking instructions in recipes may lack clarity and grammatical correctness.

## Solution
Recipe Mate is a comprehensive solution that addresses these challenges by providing:

1. **Ingredient-based Recipe Recommendation System**: This system suggests recipes based on the ingredients provided by the user, ensuring that they can utilize the ingredients they already have.

2. **Recipe Enhancement and Indianization**: Recipe Mate utilizes OpenAI's GPT-3.5-turbo language model to enhance the cooking instructions, making them more complete and grammatically correct. Additionally, it can adapt recipes to an Indian style, catering to regional preferences.

## Examples

### Recipe Recommendation
![[Pasted image 20240509182237.png]]

### Recipe Indianization
![[Pasted image 20240509182306.png]]

## Setup and Running the System

### Prerequisites
- Python 3.7 or later
- Required Python packages: pandas, scikit-learn, openai, streamlit

### Installation
1. Clone the repository or download the source code.
2. Install the required Python packages by running `pip install -r requirements.txt`.
3. Obtain an OpenAI API key from https://openai.com/ and create a `config.py` file in the project directory with the following content:
   ```python
   OPENAI_API_KEY = "your_openai_api_key"
   ```
4. Download the "Food.com Recipes and Interactions" dataset from Kaggle ([https://www.kaggle.com/shuyangli94/food-com-recipes-and-user-interactions](https://www.kaggle.com/shuyangli94/food-com-recipes-and-user-interactions)) and place the `Cleaned_raw_recipes_df.csv` file in the `data` directory.

### Running the Application

1. Navigate to the project directory.
2. Run the Streamlit application by executing `streamlit run app.py`.
3. The application will open in your default web browser, where you can interact with the Recipe Recommendation and Indianization Bot features.

### Dataset

The project utilizes the "Food.com Recipes and Interactions" dataset from Kaggle ([https://www.kaggle.com/shuyangli94/food-com-recipes-and-user-interactions](https://www.kaggle.com/shuyangli94/food-com-recipes-and-user-interactions)). The dataset is preprocessed and cleaned to extract the ingredients and cooking steps for each recipe.