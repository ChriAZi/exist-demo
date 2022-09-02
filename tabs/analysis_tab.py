import streamlit as st


def render_analysis_tab():
    with st.expander('See explanation'):
        st.write(
            """This section enables data scientists and PMs to write down their thoughts about the last 
            experiment. It enables them to include qualitative information about their runs that help them 
            to document, version and track their decision making over time. """
        )
    with st.form("Analysis"):
        st.radio(
            "Could you validate your hypothesis?",
            ('Yes', 'No'))
        st.text_input('Why or why not?')
        st.text_area(label='Learnings',
                     placeholder='Here goes all information regarding why the performance of the model was as it '
                                 'was. You can also write down thoughts about your development process if you '
                                 'have changed anything.')
        st.text_area(label='Limitations',
                     placeholder='Here goes all information about potential limitations of your model. It might '
                                 'be that it performs very well but only on a sub population of your dataset. ')
        submitted = st.form_submit_button("Save analysis")
        if submitted:
            st.success('Successfully saved your analysis.')
            st.balloons()