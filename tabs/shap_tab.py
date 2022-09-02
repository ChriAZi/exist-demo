import streamlit as st


def render_shap_tab():
    with st.expander('See explanation'):
        st.write(
            """This section includes transparency metrics - in this case SHAP values. These metrics are crucial 
            to create explainability around your model. The metric below describes which attribute of the dataset 
            most heavily influences the final algorithmic decision. """
        )
        st.markdown('**Information source:** automatically tracked using `trail.autotrack()`')
    st.write('SHAP values')
