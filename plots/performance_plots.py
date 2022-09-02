import streamlit as st
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score, precision_score
from sklearn.model_selection import train_test_split

from plots.dataframe import get_df_cleaned


def get_training_data():
    df_cleaned = get_df_cleaned()
    train_data = df_cleaned.values
    train_features = train_data[:, 1:]
    train_target = train_data[:, 0]
    train_x, test_x, train_y, test_y = train_test_split(train_features,
                                                        train_target,
                                                        test_size=0.2,
                                                        random_state=0)
    return train_x, test_x, train_y, test_y


def get_classification_metrics():
    clf = RandomForestClassifier(n_estimators=100)
    train_x, test_x, train_y, test_y = get_training_data()
    clf = clf.fit(train_x, train_y)

    predict_y = clf.predict(test_x)
    accuracy = accuracy_score(test_y, predict_y)
    precision = precision_score(test_y, predict_y, average='micro')
    f1 = f1_score(test_y, predict_y, average='micro')
    return accuracy, precision, f1


def render_metrics():
    accuracy, precision, f1 = get_classification_metrics()
    accuracy = round(accuracy * 100, 2)
    precision = round(precision * 100, 2)
    a, p, f = st.columns(3)
    with a:
        st.metric(value=str(accuracy) + "%", label='Accuracy',
                  delta=str(accuracy - st.session_state['last_accuracy']) + "%")
        st.session_state['last_accuracy'] = accuracy
    with p:
        st.metric(value=str(precision) + "%", label='Precision',
                  delta=str(precision - st.session_state['last_precision']) + "%")
        st.session_state['last_precision'] = precision
    with f:
        st.metric(value=f1, label='F1-Score',
                  delta=f1 - st.session_state['last_f1'])
        st.session_state['last_f1'] = f1
