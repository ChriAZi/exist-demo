import streamlit as st

from plots.data_plots import render_data_plots
from plots.dataframe import load_dataframe, get_df_cleaned


def render_run_tab():
    with st.expander('See explanation'):
        st.write(
            """This section includes all run and data specific information. It helps to understand the data the 
            model was trained on and how parameters were calibrated. """
        )
        st.markdown('**Information source:** automatically tracked using `trail.autotrack()`')

    df_train = load_dataframe()
    st.subheader('Before Transformation')
    left, right = st.columns(2)
    with left:
        st.metric('Number of entries', len(df_train))
    with right:
        st.metric('Number of columns', len(df_train.columns))
    st.dataframe(df_train, height=100)
    st.markdown('---')

    df_cleaned = get_df_cleaned()
    st.subheader('After Transformation')
    left_transformed, right_transformed = st.columns(2)
    with left_transformed:
        st.metric('Number of entries', len(df_cleaned), 0)
    with right_transformed:
        st.metric('Number of columns', len(df_cleaned.columns), -1)
    st.dataframe(df_cleaned, height=100)
    st.markdown('---')
    render_data_plots()
