import streamlit as st

def convert(text,var_dict):
    for var, val in var_dict.items():
        in_text = "{" + var + "}"
        text = text.replace(in_text, str(val))
    return text

st.header('Replace words in text')

with st.expander("How it works"):
    st.write('Add variables and their values on the left, then type variables to be replaced in text using curly brackets on the right.')
    
    st.caption('Example:')
    st.caption('Variable 1 = surname, Value 1 = John')          
    st.caption('input text: Hi my name is {surname}')
    st.caption('output text: Hi my name is John')
    

amount = st.number_input('Amount of variables', value=1, min_value=1, max_value=100)
varz, valz, textz = st.columns([1,1,2])

with varz:
    d_var = {f'var{i}': st.text_input(f'Variable {i}') for i in range(1,int(amount+1))}
    locals().update(d_var)

with valz:
    d_val = {f'val{i}': st.text_input(f'Value {i}') for i in range(1,int(amount+1))}
    locals().update(d_val)

the_dict = dict(zip(d_var.values(),d_val.values()))

with textz:
    input_text = st.text_area('Input text', height=300)
    st.caption('Output text')
    st.write(convert(text=input_text, var_dict=the_dict))