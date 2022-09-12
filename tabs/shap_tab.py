import shap
import streamlit as st
import streamlit.components.v1 as components


def st_shap(plot, height=None):
    shap_html = f"<head>{shap.getjs()}</head><body>{plot.html()}</body>"
    components.html(shap_html, height=height)


def render_shap_tab():
    with st.expander('See explanation'):
        st.write(
            """This section includes transparency metrics - in this case SHAP values. These metrics are crucial 
            to create explainability around your model. The metric below describes which attribute of the dataset 
            most heavily influences the final algorithmic decision. """
        )
        st.markdown('**Information source:** automatically tracked using `trail.autotrack()`')
    st.write('SHAP values')

    clf = st.session_state['trained_clf']
    test_x = st.session_state['current_test_x']
    explainer = shap.TreeExplainer(clf)
    shap_values = explainer.shap_values(test_x)
    st_shap(shap.force_plot(explainer.expected_value, shap_values))
