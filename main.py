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

with open("./data/rec.txt", "r") as f:
    rec = f.readlines()  # starts as a string
    young = rec[0].split(',')
    young[-1] = young[-1].strip('\n')
    old = rec[1].split(',')


sum = a + a2
st.title("阿弥陀佛 佛号总数： " + str(sum) )
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


labels = ['莲少','莲青']
values = [a, a2]

st.header("念佛数量比例")

fig= go.Figure(data = [go.Pie(labels=labels, values=values, scalegroup = 'one')])

fig.update_traces(textposition='none', textinfo= 'percent', insidetextorientation='radial')
fig.update_layout(font=dict(family="Helvetica",size=14))

st.plotly_chart(fig)

#comparison
#st.text('=========================================================================================================')
st.header("一周内的佛号总数量")

#dataset
apps = ['Day 1', 'Day 2', 'Day 3', 'Day 4', 'Day 5', 'Day 6', 'Day 7']
young = [int(i) for i in young]
old = [int(i) for i in old]
y_s1 = young
y_s2 = old

#create bar
fig13 = go.Figure()
fig13.add_trace(go.Bar(
    x = apps,
    y = y_s1,
    name = '莲少',
    marker_color = 'cyan',
    text = y_s1
    ))
fig13.add_trace(go.Bar(
    x= apps,
    y = y_s2,
    name = '莲青',
    marker_color = 'royalblue',
    text = y_s2
    ))

#labelling
fig13.update_layout(barmode='group', xaxis_tickangle=-45)
fig13.update_traces(textposition='none')
fig13.update_layout(
    xaxis = dict(
                title = '天',
                titlefont_size=18,
                tickfont_size=18,
                showgrid=False),
    yaxis = dict(
                title = '佛号数量',
                titlefont_size=18,
                tickfont_size=18,
                showgrid=True),
    width=900,
    height=600)

#plot bar
st.plotly_chart(fig13)