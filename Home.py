import streamlit as st
import pandas

#st.set_page_config(layout = "wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/photo1.jpg", width=295)

with col2:
    st.title("Shantanu Vispute")
    info = """Hello! I am Shantanu Vispute. I have graduated 12th grade and am currently
     attending college and MIT-ADT in Pune. My major is computer engineering core and I 
     aspire to have a career in cyber security and game development. I am currently attending
     a python course on Udemy course and will soon be at your service. Until then feel free to 
      check out the apps I have made! """
    st.info(info)

message = """ Below you can find some of apps that I have built in python. Feel free to contact me!"""
st.write(message)

col3, empty_column, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep = ";")

with col3 :
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.image("images/" + row["image"])
        st.write(row["description"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.image("images/" + row["image"])
        st.write(row["description"])
        st.write(f"[Source Code]({row['url']})")

