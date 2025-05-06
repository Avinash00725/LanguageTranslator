import streamlit as st
from translator import EnglishToHindiTranslator

# App title
st.title("English to Hindi Language")
st.markdown("Translate any English sentence into Hindi")

# Initialize translator
translator = EnglishToHindiTranslator()

# User input
text = st.text_area("Enter English text to translate:", height=150)

# Translate button
if st.button("Translate"):
    if text.strip() != "":
        with st.spinner("Translating..."):
            result = translator.translate(text)
        st.success("Translation completed!")
        st.subheader("Hindi Translation:")
        st.write(result)
    else:
        st.warning("Please enter some text to translate.")
