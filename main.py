import streamlit as st

with open("file.txt", "r") as f:
    a = f.readline()  # starts as a string
    a = int(a)
    if a == "":
        a = 0
    elif a >= 100:
        a = 0

# check if its an empty string, otherwise should be able to cast using int()

if st.button("AMTF!"):
    a += 1
    with open("file.txt", "w") as f:
        f.truncate()
        f.write(f"{a}")
        st.write(a)
        st.progress(a)