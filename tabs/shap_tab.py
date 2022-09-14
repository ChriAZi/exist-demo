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
    st.subheader('Feature importance for this run')
    st.markdown(
        'Using the chart below you can identify which features the model uses to make its prediction. '
        '**For example:** '
        'The `FamilySize`-feature is the **4th** most important feature for the model decision. The **bigger** the '
        'family (red) the **higher** the change of survival (x-axis). However, most family sizes did not impact the '
        'model decision at all (point cloud at the center).')
    clf = st.session_state['trained_clf']
    test_x = st.session_state['current_test_x']
    columns = st.session_state['columns']

    explainer = shap.TreeExplainer(clf)
    shap_values = explainer.shap_values(test_x)
    shap.summary_plot(shap_values[0], test_x, max_display=8, feature_names=columns[:9])
    st.pyplot()
