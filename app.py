import streamlit as st
import openai

st.title('Recipe Generator')
st.write('Please enter the food ingredients you have, and I will suggest a recipe!')

ingredients = st.text_input('Enter your ingredients')

if ingredients:
    api_key = st.text_input('Enter your OpenAI API key', type="password")
    openai.api_key = api_key.strip()

    response = openai.ChatCompletion.create(
      model="gpt-3",
      messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"I have {ingredients}, what can I cook?"}
        ]
    )
    message_content = response.choices[0].message.content.strip()
    st.write(message_content)