import streamlit as st
from plotly import express as px

from plots.dataframe import get_df_cleaned


def render_data_plots():
    df_cleaned = get_df_cleaned(True)
    st.subheader('Feature Distributions')
    age_dist = px.histogram(df_cleaned['Age'], color=df_cleaned['SurvivedText'], title='Age distribution by '
                                                                                       'survival')
    st.plotly_chart(age_dist)
    gender_dist = px.histogram(df_cleaned['Sex'], color=df_cleaned['SurvivedText'], title='Sex distribution by '
                                                                                          'survival')
    st.plotly_chart(gender_dist)
