st = "Milky Way; Ukraine, Kiev; 34.4556 uah; 56.4567 Uah"
st1 = st.split(";")
st2 = st1[1].split(",")
st3 = st1[2].split()
st4 = st1[3].split()
st3[1] = 980
st4[1] = 980
d = {"name":st1[0], 
     "produced":{"country": st2[0], "city": st2[1]},
     "min_price":{"currency": st3[1], "amount": st3[0]},
     "max_price": {"currency": st4[1], "amount": st4[0]}}
print (d)
