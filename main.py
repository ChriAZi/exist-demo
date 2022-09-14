import time

import streamlit as st

from tabs.analysis_tab import render_analysis_tab
from tabs.demo_tab import render_demo_tab
from tabs.integrations_tab import render_integrations_tab
from tabs.performance_tab import render_performance_tab
from tabs.run_tab import render_run_tab
from tabs.shap_tab import render_shap_tab
from train_model import train_model

st.set_option('deprecation.showPyplotGlobalUse', False)

show_run_button = 'show_run_button'
show_model_card = 'show_model_card'
last_accuracy = 'last_accuracy'
last_precision = 'last_precision'
last_f1 = 'last_f1'
current_survival_prediction = 'current_survival_prediction'
show_prediction = 'show_prediction'
if show_run_button not in st.session_state:
    st.session_state[show_run_button] = True
if show_model_card not in st.session_state:
    st.session_state[show_model_card] = False
if last_accuracy not in st.session_state:
    st.session_state[last_accuracy] = 0
if last_precision not in st.session_state:
    st.session_state[last_precision] = 0
if last_f1 not in st.session_state:
    st.session_state[last_f1] = 0
if current_survival_prediction not in st.session_state:
    st.session_state[current_survival_prediction] = 0
if show_prediction not in st.session_state:
    st.session_state[show_prediction] = False

st.title('Trail Demo')

st.subheader('Instructions')
st.markdown(
    """This demo guides you through the process of training, tracking and evaluating the run of a model training 
    using **Trail**. You can navigate through the demo by following the prompts further down the page. If you want 
    to reset the demo, you can use the **Rerun**-Button on the top right or just press `R` on your keyboard. """
)

st.subheader('Use Case')
st.markdown(
    """Imagine you want to build an AI system that can classify the survival chance of a passenger in the 
    **infamous Titanic crash**. To do so, you have already: """
)
st.markdown(
    """1. **integrated Trail** into your code base using `import trail` 
    \n2. **tracked two experiment runs** using `trail.autotrack()`
    \n3. and evaluated the first run results in the **Trail UI** (seen in the image below)"""
)

st.subheader('Next Steps')
st.markdown(
    """You are now ready to further improve your model and test your new hypothesis. As a seasoned 
    data scientist, you know that you now need to run your training script, so Trail can **log all relevant 
    metrics**. ***Good thing is:*** we have all things already setup for you, so that you can inspect the Trail 
    experience by just using the prompts below."""
)
st.image('https://i.ibb.co/vXYsNZB/Expriment-Overview.jpg', caption='Trail Tree View', use_column_width="always")
st.markdown('If you are ready to go, click the **Run Experiment**-Button below.')

if st.button('Run experiment'):
    with st.spinner('Running experiment..'):
        train_model()
        time.sleep(2)
    st.session_state[show_model_card] = True

if st.session_state[show_model_card]:
    st.subheader('Trail Card')
    st.write(
        """Below you can see all information of the last experiment run that is relevant for deciding on how to 
        further improve your model. Each section includes different information addressing different aspects of the 
        model. This information will be shown right next to the selected node from the Trail tree view as 
        seen in our design prototype screenshots in our next product iteration. """
    )

    st.info('If you click on a button inside a tab, the app will reload and show the first tab. '
            'This, unfortunately, cannot be fixed as its a bug of the underlying framework of this app. '
            'To inspect the changes in your previously selected tab, simply click on it again.')

    run_tab, performance_tab, shap_tab, demo_tab, analysis_tab, integration_tab = \
        st.tabs(["👟 Input information",
                 "📊 Model performance",
                 "🔍 Explainability",
                 "🦾 Demo space",
                 "🧑‍🔬 Analysis",
                 "🧩 Integrations"])
    with run_tab:
        render_run_tab()
    with performance_tab:
        render_performance_tab()
    with shap_tab:
        render_shap_tab()
    with demo_tab:
        render_demo_tab()
    with analysis_tab:
        render_analysis_tab()
    with integration_tab:
        render_integrations_tab()
