import streamlit as st
import pandas as pd
import pickle


pickle_in = open("E:/random_forest.pkl", "rb") 
classifier = pickle.load(pickle_in)

def predict_note_authentication(age, pc, su ,al, bp, bgr, bu, sg, pcc):
    prediction = classifier.predict([[age, pc, su ,al, bp, bgr, bu, sg, pcc]])
    print(prediction)
    return prediction


def main():

    st.title("Chronic Kidney Disease Predictor")

    html_temp = """
    <div style="background-color:green;padding:10px">
    <h2 style="color:white;text-align:center;">The Smart Way To Handle Your Health </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)

    age  =  st.number_input("age")

    pc = st.number_input("Pus cell")

    su = st.number_input("Sugar")

    al = st.number_input("Albumin")

    bp = st.number_input("Blood Pressure")

    bgr = st.number_input("Blood Glucose Random")

    bu = st.number_input("Blood Urea")

    sg = st.number_input("Specific Gravity")

    pcc = st.number_input("Pus Cell Clumps")

    result= ""

    if st.button("Predict"):
        result = predict_note_authentication(age, pc, su ,al, bp, bgr, bu, sg, pcc)
    st.success('The Chronic Disease  Prediction is {}'.format(result))
    st.write("0 : CKD means  disease not Present,  if 1 : CKD means disease Present")



if __name__=='__main__':
    main()