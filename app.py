import streamlit as st
import google.generativeai as genai

try:
  GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]
exept: 
  st.error("Google API Key not found. Please set it in Streamlit secrets.")
  st.stop()

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('models/gemini-2.5-flash')

st.set_page_config(page_title="Your Study Buddy", page_icon="🦉")

st.title("🦉 Your Study Buddy")
st.write("Ask me anything about your study materials!")

user_input = st.text_area("Enter your question here" , placeholder="Example: What the meaning of automation?")

if st.button("Get Answer"):
  if not user_input:
    st.warning("Please enter a question.")
  else:
    try:
      with st.spinner("🧐"):
        secret_prompt = f"""
        Kamu adalah asisten belajar mahasiswa yang asik, gaul, dan pinter.
        Tugasmu menjelaskan konsep rumit menjadi sangat sederhana.
        Gunakan bahasa Indonesia yang santai (lu-gue atau aku-kamu boleh).
        Berikan contoh nyata di kehidupan sehari-hari. 
        Jawab menggunakan bahasa yang sama dengan yang digunakan user.

        User Question: {user_input}
        """

        response = model.generate_content(secret_prompt)

        st.success("Here is your answer:")
        st.markdown(response.text)

    except Exception as e:
      st.error(f"An error occurred: {e}")

st.markdown("---")
st.markdown("Developed by Oya - [GitHub: karimaulya]")