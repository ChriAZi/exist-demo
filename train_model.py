import streamlit as st
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score, precision_score
from sklearn.model_selection import train_test_split

from plots.dataframe import get_df_cleaned

current_train_x = 'current_train_x'
current_test_x = 'current_test_x'
current_train_y = 'current_train_y'
current_test_y = 'current_test_y'
columns = 'columns'
trained_clf = 'trained_clf'
current_predict_y = 'current_predict_y'
current_accuracy = 'current_accuracy'
current_precision = 'current_precision'
current_f1 = 'current_f1'
if current_train_x not in st.session_state:
    st.session_state[current_train_x] = None
if current_test_x not in st.session_state:
    st.session_state[current_test_x] = None
if current_train_y not in st.session_state:
    st.session_state[current_train_y] = None
if current_test_y not in st.session_state:
    st.session_state[current_test_y] = None
if columns not in st.session_state:
    st.session_state[columns] = None
if trained_clf not in st.session_state:
    st.session_state[trained_clf] = None
if current_predict_y not in st.session_state:
    st.session_state[current_predict_y] = None
if current_accuracy not in st.session_state:
    st.session_state[current_accuracy] = None
if current_precision not in st.session_state:
    st.session_state[current_precision] = None
if current_f1 not in st.session_state:
    st.session_state[current_f1] = None


def get_training_data():
    df_cleaned = get_df_cleaned()
    train_data = df_cleaned.values
    train_features = train_data[:, 1:]
    train_target = train_data[:, 0]
    train_x, test_x, train_y, test_y = train_test_split(train_features,
                                                        train_target,
                                                        test_size=0.2,
                                                        train_size=0.8,
                                                        random_state=0)
    return train_x, test_x, train_y, test_y, df_cleaned.columns[1:]


def get_classifier(train_x, train_y):
    clf = RandomForestClassifier(n_estimators=100)
    return clf.fit(train_x, train_y)


def get_predict_y(test_x, clf):
    return clf.predict(test_x)


def get_accuracy(test_y, predict_y):
    return accuracy_score(test_y, predict_y)


def get_precision(test_y, predict_y):
    return precision_score(test_y, predict_y, average='binary')


def get_f1(test_y, predict_y):
    return f1_score(test_y, predict_y, average='binary')


def train_model():
    train_x, test_x, train_y, test_y, df_columns = get_training_data()
    st.session_state[current_train_x] = train_x
    st.session_state[current_test_x] = test_x
    st.session_state[current_train_y] = train_y
    st.session_state[current_test_y] = test_y
    st.session_state[columns] = df_columns.tolist()

    clf = get_classifier(train_x, train_y)
    st.session_state[trained_clf] = clf

    predict_y = get_predict_y(test_x, clf)
    st.session_state[current_predict_y] = predict_y

    st.session_state[current_accuracy] = get_accuracy(test_y, predict_y)
    st.session_state[current_precision] = get_precision(test_y, predict_y)
    st.session_state[current_f1] = get_f1(test_y, predict_y)
