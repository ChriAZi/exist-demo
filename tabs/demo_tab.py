import streamlit as st


def render_demo_tab():
    with st.expander('See explanation'):
        st.write(
            """This section makes it possible to test new datapoints on the currently trained model. This helps 
            to understand how new data affects the model's performance and what the final output of the model 
            looks like."""
        )
    st.write('Demo Space')
