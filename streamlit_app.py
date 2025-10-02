from time import sleep

import pandas as pd
import streamlit as st


@st.cache_data
def cache_sleep(i: int, seconds: float = 0.1):
    sleep(seconds)
    return None


# ! Fragments do not trigger a full app rerun, so the fragment will updated after
# ! the entire code is run
# @st.fragment
def render_button():
    with st.echo():
        st.button("Click me")
        with st.spinner("Loading data ..."):
            sleep(5)


st.title("Streamlit App Example")

st.write(
    """
Streamlit runs from top to bottom, executing all code on each interaction.

- streamlit is fast and simple to prototype
- simple one-time calculations are easy conceptually (vuegen reports)
    - load your data
    - create interactive plots
- user interactions with widgets cause a full rerun of the script
- user-data upload makes things even more tricky
"""
)

render_button()

st.write(
    "This takes a while to load...simulating a heavy computation or IO process. "
    "But it works!"
)

sleep(2)

sample_df = pd.DataFrame(
    {
        "gene_expression": [1.2, 2.5, 3.1, 4.5, 5.2, 6.8, 3.9, 2.1],
        "log_p_value": [0.5, 1.5, 2.0, 3.5, 4.0, 5.5, 1.8, 0.9],
        "regulation": ["Up", "Up", "None", "Down", "Down", "Down", "None", "Up"],
        "significance_score": [10, 20, 5, 40, 55, 80, 15, 25],
        "gene_name": [
            "GENE_A",
            "GENE_B",
            "GENE_C",
            "GENE_D",
            "GENE_E",
            "GENE_F",
            "GENE_G",
            "GENE_H",
        ],
        "cell_type": ["A", "B", "A", "B", "A", "B", "A", "B"],
    }
)
st.write(sample_df)

with st.echo():
    progress_text = "Operation in progress. Please wait."
    my_bar = st.progress(0, text=progress_text)

    for i in range(100):
        my_bar.progress(i + 1, text=progress_text)
        cache_sleep(i)
