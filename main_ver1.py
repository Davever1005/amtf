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

with open("temp.txt", "r") as f:
    b = f.readline()  # starts as a string
    if b == "":
        b = 0
    else:
        b = int(b)

with open("./data/heart.txt", "r") as f:
    c = f.readline()  # starts as a string
    if c == "":
        c = 0
    else:
        c = int(c)

with open("./data/amt.txt", "r") as f:
    d = f.readline()  # starts as a string
    if d == "":
        d = 0
    else:
        d = int(d)

with open("./data/ys.txt", "r") as f:
    e = f.readline()  # starts as a string
    if e == "":
        e = 0
    else:
        e = int(e)

with open("./data/dbz.txt", "r") as f:
    g = f.readline()  # starts as a string
    if g == "":
        g = 0
    else:
        g = int(g)

with open("./data/px.txt", "r") as f:
    h = f.readline()  # starts as a string
    if h == "":
        h = 0
    else:
        h = int(h)

sum = a + a2
st.write("阿弥陀佛 佛号总数： " + str(sum) )
st.write("莲少佛号数量： " + str(a))
st.write("莲青佛号数量： " + str(a2))


grp = st.radio("请选择所属组别： ",
                ('莲少','莲青'))

if grp == '莲少':

    if st.button("阿弥陀佛! Amituofo!"):
        a += 1
        b += 1
        with open("./data/amtf1.txt", "w") as f:
            f.truncate()
            f.write(f"{a}")

        with open("temp.txt", "w") as f:
            f.truncate()
            f.write(f"{b}")

elif grp == '莲青':
    if st.button("阿弥陀佛! Amituofo!"):
        a2 += 1
        b += 1
        with open("./data/amtf2.txt", "w") as f:
            f.truncate()
            f.write(f"{a2}")
        with open("temp.txt", "w") as f:
            f.truncate()
            f.write(f"{b}")


#if st.button("个人重置!"):
#    b = 0
#    with open("temp.txt", "w") as f:
#        f.truncate()
#        f.write(f"0")

#st.write("个人： " + str(b))

if st.button("心经"):
    c += 1
    with open("./data/heart.txt", "w") as f:
        f.truncate()
        f.write(f"{c}")

st.write("心经： " + str(c))

if st.button("阿弥陀经"):
    d += 1
    with open("./data/amt.txt", "w") as f:
        f.truncate()
        f.write(f"{d}")

st.write("阿弥陀经： " + str(d))

if st.button("药师经"):
    e += 1
    with open("./data/ys.txt", "w") as f:
        f.truncate()
        f.write(f"{e}")

st.write("药师经： " + str(e))

if st.button("大悲咒"):
    g += 1
    with open("./data/dbz.txt", "w") as f:
        f.truncate()
        f.write(f"{g}")

st.write("大悲咒： " + str(g))

if st.button("普贤行愿品"):
    h += 1
    with open("./data/px.txt", "w") as f:
        f.truncate()
        f.write(f"{g}")

st.write("普贤行愿品： " + str(g))

labels4 = ['莲少','莲青']
values4 = [a, a2]

fig4= go.Figure(data = [go.Pie(title = '念佛数量比例',labels=labels4, values=values4, scalegroup = 'one')])

fig4.update_traces(textposition='none', textinfo= 'percent', insidetextorientation='radial')
fig4.update_layout(font=dict(family="Helvetica",size=14))

st.plotly_chart(fig4)

