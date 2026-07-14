#pip install streamlit
#to run : python -m streamlit run filname.py
#if not in root dir than write cd
#we hav
#it is ready to use ui liberary
# pip install list 
import streamlit as st
#use when data matter not ui


st.title("welcome to my Calulator ")
st.markdown("perform all the operations easily")
st.write("the ")



c1,c2=st.columns(2)
fnum = c1.number_input("enter first no.")
snum = c2.number_input("enter second no.")


operations =["add", "sub" ,"mul","div"]
choice =st.radio("select an operation",operations)

button = st.button("calculate")

result= 0
if button:
    if choice=="add":
        result = fnum+snum
    if choice=='sub':
        result=fnum-snum
    if choice=='mul':
        result=fnum*snum
    if choice =='div':
        result ==fnum/snum
    
st.success(f"result is {result}")
    
st.balloons()
st.snow()
st.toast("Saved Successfully! 🎉")









