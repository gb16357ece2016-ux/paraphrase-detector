import streamlit as st
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load model (this is your brain)
model = SentenceTransformer('all-MiniLM-L6-v2')

# UI Title
st.title("Paraphrase Detection App 🚀")

# User inputs
s1 = st.text_input("Enter Sentence 1")
s2 = st.text_input("Enter Sentence 2")

# Button
if st.button("Check Paraphrase"):
    
    if s1 and s2:
        # Convert text → embeddings
        e1 = model.encode([s1])
        e2 = model.encode([s2])

        # Compute similarity
        sim = cosine_similarity(e1, e2)[0][0]

        # Decision
        if sim > 0.7:
            st.success(f"Paraphrase ✅ (Score: {sim:.2f})")
        else:
            st.error(f"Not Paraphrase ❌ (Score: {sim:.2f})")
    else:
        st.warning("Please enter both sentences")
