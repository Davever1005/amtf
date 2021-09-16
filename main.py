import streamlit as st
import plotly.graph_objects as go



with open("./data/amtf1.txt", "r") as f:
    a = f.readline()  # starts as a string
    if a == "":
        a = 0
    else: a = int(a)

with open("./data/amtf2.txt", "r") as f:
    a2 = f.readline()  # starts as a string
    if a2 == "":
        a2 = 0
    else: a2 = int(a2)


sum = a + a2
st.write("阿弥陀佛 佛号总数： " + str(sum) )
st.write("莲少佛号数量： " + str(a))
st.write("莲青佛号数量： " + str(a2))


grp = st.radio("请选择所属组别： ",
                ('莲少','莲青'))

if grp == '莲少':

    if st.button("阿弥陀佛! Amituofo!"):
        a += 1

        with open("./data/amtf1.txt", "w") as f:
            f.truncate()
            f.write(f"{a}")


elif grp == '莲青':
    if st.button("阿弥陀佛! Amituofo!"):
        a2 += 1

        with open("./data/amtf2.txt", "w") as f:
            f.truncate()
            f.write(f"{a2}")


labels4 = ['莲少','莲青']
values4 = [a, a2]

fig4= go.Figure(data = [go.Pie(title = '念佛数量比例',labels=labels4, values=values4, scalegroup = 'one')])

fig4.update_traces(textposition='none', textinfo= 'percent', insidetextorientation='radial')
fig4.update_layout(font=dict(family="Helvetica",size=14))

st.plotly_chart(fig4)

