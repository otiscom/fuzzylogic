import streamlit as st

st.title("ℹ️ About This App")

st.markdown(
    """
This app uses **fuzzy logic** to recommend dishes based on user preferences.
Rather than relying on exact matches, it evaluates **how well** each dish fits your needs.

---

### 🤖 What is Fuzzy Logic?

Fuzzy logic is a form of _approximate reasoning_, designed to handle concepts like:

- "somewhat spicy"
- "very expensive"
- "not too filling"

Instead of black-and-white decisions, fuzzy logic allows for shades of grey - just like human judgment.

---

### 📦 Tech Stack

- Python 3.10+
- Streamlit UI
- Plotly for visualization
- Fuzzy logic (scikit-fuzzy)
- Modular structure with multi-page navigation
"""
)
