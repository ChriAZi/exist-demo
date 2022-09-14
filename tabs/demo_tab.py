import pandas as pd
import streamlit as st


def transform_data(sex_choice, age_choice, family_choice, embarked_choice, class_choice, fare_choice):
    sex_choices = ['Female', 'Male']
    sex_mapping = dict(zip(sex_choices, range(0, len(sex_choices))))
    sex_choice = sex_mapping[sex_choice]

    embarked_choice_c = embarked_choice_q = embarked_choice_s = embarked_choice_nan = 0
    if embarked_choice == 'Cherbourg':
        embarked_choice_c = 1
    elif embarked_choice == 'Queenstown':
        embarked_choice_q = 1
    elif embarked_choice == 'Southampton':
        embarked_choice_s = 1

    class_choices = ['First', 'Second', 'Third']
    class_mapping = dict(zip(class_choices, range(1, len(class_choices) + 1)))
    class_choice = class_mapping[class_choice]

    data = [class_choice, fare_choice, sex_choice, embarked_choice_c, embarked_choice_q, embarked_choice_s,
            embarked_choice_nan, age_choice, family_choice]
    df = pd.DataFrame(data).T
    return df


def render_demo_tab():
    with st.expander('See explanation'):
        st.write(
            """This section makes it possible to test new datapoints on the currently trained model. This helps 
            to understand how new data affects the model's performance and what the final output of the model 
            looks like."""
        )
    st.subheader('Create your own passenger')
    with st.form('Passenger'):
        sex_choice = st.selectbox('Choose your sex', ('Male', 'Female'))
        age_choice = st.slider('Choose your age', 1, 99, 25)
        family_choice = st.slider('Choose your family size', 1, 10, 4)
        embarked_choice = st.selectbox('Choose your departure location', ('Cherbourg', 'Queenstown', 'Southampton'))
        class_choice = st.selectbox('Choose your class', ('First', 'Second', 'Third'))
        fare_choice = st.slider('Choose your fare amount', 1, 100, 25)
        if st.form_submit_button("Predict survival chance"):
            passenger = transform_data(sex_choice, age_choice, family_choice, embarked_choice, class_choice,
                                       fare_choice)
            clf = st.session_state['trained_clf']
            prediction = clf.predict(passenger.values.reshape(1, -1))
            st.session_state['current_survival_prediction'] = prediction
            st.session_state['show_prediction'] = True
        if st.session_state['show_prediction']:
            if st.session_state['current_survival_prediction'] == 0:
                st.warning('Your selected passenger would have died.')
            else:
                st.success('Your selected passenger would have survived.')
