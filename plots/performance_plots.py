import streamlit as st
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay


def render_metrics():
    accuracy = round(st.session_state['current_accuracy'] * 100, 2)
    precision = round(st.session_state['current_precision'] * 100, 2)
    f1 = round(st.session_state['current_f1'] * 100, 2)
    a, p, f = st.columns(3)
    with a:
        st.metric(value=str(accuracy) + "%", label='Accuracy',
                  delta=str(round(accuracy - st.session_state['last_accuracy'], 2)) + "%")
        st.session_state['last_accuracy'] = accuracy
    with p:
        st.metric(value=str(precision) + "%", label='Precision',
                  delta=str(round(precision - st.session_state['last_precision'], 2)) + "%")
        st.session_state['last_precision'] = precision
    with f:
        st.metric(value=str(round(f1, 2)) + "%", label='F1-Score',
                  delta=str(round(f1 - st.session_state['last_f1'], 2)) + "%")
        st.session_state['last_f1'] = f1


def render_confusion_matrix():
    st.subheader('Confusion Matrix')
    clf = st.session_state['trained_clf']
    cm = confusion_matrix(st.session_state['current_test_y'], st.session_state['current_predict_y'],
                          labels=clf.classes_)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=clf.classes_)
    disp.plot()
    st.pyplot()
