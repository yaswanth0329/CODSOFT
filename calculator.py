
import streamlit as st
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b==0:
        return "'Sorry not defined'"
    return a/b
def calculator():
    st.title("SIMPLE CALCULATOR")
    st.write("**CALCULATOR FOR BASIC ARITHMETIC OPERATIONS**")
    n1=st.number_input("Enter first number:",step=1.0)
    n2=st.number_input("Enter second number:",step=1.0)
    operator=st.selectbox("Select an operator:",["+","-","*","/"])
    result=0
    if operator=="+":
        result=add(n1,n2)
    elif operator=="-":
        result=sub(n1,n2)
    elif operator=="*":
        result=multiply(n1,n2)        
    elif operator=="/":
        result=divide(n1,n2)
    st.write("The Result Is :",result)

if __name__=='__main__' :
   calculator()
