# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 10:37:40 2022

@author: somil.mehta
"""
import streamlit as st
import pickle 
from PIL import Image 

pickle_in = open("Disorder.pkl","rb")
Disorder = pickle.load(pickle_in)


def welcome():
    return "Welcome All"


def Mental_Disorder_Prediction(Feeling_Nervous,Panic,Breathing_Rapidly,Sweating,Trouble_in_Concentration,Having_Trouble_in_Sleeping,Having_Trouble_with_Work,Hopelessness,Anger,Over_React,Change_in_Eating,Suicidal_Thought,Feeling_Tired,Close_Friend,Social_Media_Addiction,Weight_Gain,Material_Possessions,Introvert,Popping_up_Stressful_Memory,Having_Nightmares,Avoids_People_or_Activities,Feeling_Negative,Trouble_Concentrating,Blamming_Yourself):
    
    prediction = Disorder.predict([[Feeling_Nervous,Panic,Breathing_Rapidly,Sweating,Trouble_in_Concentration,Having_Trouble_in_Sleeping,Having_Trouble_with_Work,Hopelessness,Anger,Over_React,Change_in_Eating,Suicidal_Thought,Feeling_Tired,Close_Friend,Social_Media_Addiction,Weight_Gain,Material_Possessions,Introvert,Popping_up_Stressful_Memory,Having_Nightmares,Avoids_People_or_Activities,Feeling_Negative,Trouble_Concentrating,Blamming_Yourself]])
    print(prediction)
    return prediction    


def main():
    html_temp = """
    <div style = "background-color:black;padding:10px">
    <h2 style = "color:white;text-align:center;">Mental Disorder Type Prediction Web Page </h2>
    </div>
    """
    
    st.markdown(html_temp,unsafe_allow_html = True)
    Feeling_Nervous = st.radio("Does Patient Feels always Nervous [YES : 1 & NO : 0]",(1,0))
    Panic = st.radio("Does Patient is always in Panic state [YES : 1 & NO : 0]",(1,0))
    Breathing_Rapidly = st.radio("Does the Patient Breath Rapidly [YES : 1 & NO : 0]",(1,0))
    Sweating = st.radio("Does the Patient Sweats Rapidly [YES : 1 & NO : 0]",(1,0))
    Trouble_in_Concentration = st.radio("Does Patient unable to Concentrate [YES : 1 & NO : 0]",(1,0))
    Having_Trouble_in_Sleeping = st.radio("Does Patient having Trouble in Sleeping [YES : 1 & NO : 0]",(1,0))
    Having_Trouble_with_Work = st.radio("Does Patient Face Trouble During Work [YES : 1 & NO : 0]",(1,0))
    Hopelessness = st.radio("Does Patient feels Hopless all the Time [YES : 1 & NO : 0]",(1,0))
    Anger = st.radio("Does Patient gets Angry all the time [YES : 1 & NO : 0]",(1,0))
    Over_React = st.radio("Does Patient Over React [YES : 1 & NO : 0]",(1,0))
    Change_in_Eating = st.radio("Does Patient has suddenly changes his/her Eating habits [YES : 1 & NO : 0]",(1,0))
    Suicidal_Thought = st.radio("Does Patient have Suicidal Thoughts [YES : 1 & NO : 0]",(1,0))
    Feeling_Tired = st.radio("Does Patient always feels Tired [YES : 1 & NO : 0]",(1,0))
    Close_Friend = st.radio("Does Patient have close Friends [YES : 1 & NO : 0]",(1,0))
    Social_Media_Addiction = st.radio("Does Patient is addicted to Soical Media [YES : 1 & NO : 0]",(1,0))
    Weight_Gain = st.radio("Does Patient gain some extra weights in past few months [YES : 1 & NO : 0]",(1,0))
    Material_Possessions = st.radio("Does Patient has Material Possessions [YES : 1 & NO : 0]",(1,0))
    Introvert = st.radio("Does Patient is an Introvert [YES : 1 & NO : 0]",(1,0))
    Popping_up_Stressful_Memory = st.radio("Does patient Popping up Stressful Memories [YES : 1 & NO : 0]",(1,0))
    Having_Nightmares = st.radio("Does patient have Nightmares [YES : 1 & NO : 0]",(1,0))
    Avoids_People_or_Activities = st.radio("Does patient Avoid People and Activites [YES : 1 & NO : 0]",(1,0))
    Feeling_Negative = st.radio("Does Patient always feels Negative [YES : 1 & NO : 0]",(1,0))
    Trouble_Concentrating = st.radio("Does Patient faces trouble during Concentrating [YES : 1 & NO : 0]",(1,0))
    Blamming_Yourself = st.radio("Does Patient always balme himself/herself [YES : 1 & NO : 0]",(1,0))
    
    result = ""
    
    if st.button("Predict Mental Disorder issue"):
        result =  Mental_Disorder_Prediction(Feeling_Nervous,Panic,Breathing_Rapidly,Sweating,Trouble_in_Concentration,Having_Trouble_in_Sleeping,Having_Trouble_with_Work,Hopelessness,Anger,Over_React,Change_in_Eating,Suicidal_Thought,Feeling_Tired,Close_Friend,Social_Media_Addiction,Weight_Gain,Material_Possessions,Introvert,Popping_up_Stressful_Memory,Having_Nightmares,Avoids_People_or_Activities,Feeling_Negative,Trouble_Concentrating,Blamming_Yourself)
    
    st.success("Patient Mental Disorder Issue : {}".format(result))
    

if __name__ == '__main__':
    main()    
    
    
    
    
    
    
    
    
    
    
    
    
    