"""A simple inference UI using Streamlit

Run this application using `streamlit run {filename}`

"""

import streamlit as st
import minillm as ml

st.title("[minillm](https://github.com/IMApurbo/minillm) Demo")

st.text_input("Prompt (passed to `ml.do()`)", key="prompt")

# Prompt LLM to get response
response = ml.do(st.session_state.prompt)

st.write(response)
