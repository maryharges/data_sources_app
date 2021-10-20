import streamlit as st

st.write(f"You filled in the following secrets: {st.secrets}")

st.write("---")

with st.echo():
    st.image("big-query-3.png", None, 300)
    st.image("big-query-3.png", None, 600)
    st.image("big-query-3.png", None, 900)
    st.image("big-query-3.png")