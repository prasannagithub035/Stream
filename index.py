import streamlit as st
import pandas as pd
import sqlite3

conn = sqlite3.connect("samples.db", check_same_thread=False)
curs = conn.cursor()

st.text("Welcome to login page")
user = st.text_input("enter the user")

pasw = st.text_input("enter password")


def update_db(users, passws):
    curs.execute("create table if not exists account(name text(50), password text(50))")
    curs.execute("insert into account values (?,?)", (users, passws))
    conn.commit()


if st.button('login'):
    if user != None or user != 0 or pasw != 0:
        #update_db(user, pasw)
        st.write("user name is ", user)
        st.write('correct user')
    elif user > 0 or pasw > 0:
        st.write("wrong")
