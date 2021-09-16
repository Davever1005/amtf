import streamlit as st

a = 0
b = 0

name = st.text_input("Please set and name: ")
filename = './user/' + name + '.txt'

if name != "":
    st.write("Welcome " + name + "!")
    with open(filename, 'w') as f:
        f.truncate()
        f.write(f"{b}")  # starts as a string


while True:
    with open("file.txt", "r") as f:
        a = f.readline()  # starts as a string
        if a == "":
            a = 0
        else: a = int(a)

    with open(filename, "r") as f:
        b = f.readline()  # starts as a string
        if b == "":
            b = 0
        else: b = int(b)

    # check if its an empty string, otherwise should be able to cast using int()

    if st.button("阿弥陀佛! Amituofo!"):
        a += 1
        b += 1
        with open("file.txt", "w") as f:
            f.truncate()
            f.write(f"{a}")
        with open(filename, "w") as f:
            f.truncate()
            f.write(f"{b}")


    st.write(a, b)

    if a / 100 == 1:
        st.balloons()


