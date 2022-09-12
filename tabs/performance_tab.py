import streamlit as st

from plots.performance_plots import render_tabs, render_confusion_matrix


def render_performance_tab():
    with st.expander('See explanation'):
        st.write(
            """This section includes all run metrics produced by the experiment. It helps to understand the 
            current performance of the model. """
        )
        st.markdown('**Information source:** automatically tracked using `trail.autotrack()`')
    st.markdown('**Modelarchitecture:** Random-Forest-Classifier')
    render_tabs()
    render_confusion_matrix()
