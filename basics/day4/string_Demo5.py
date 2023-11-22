st = '101,John,Pune,TL'
ls = st.split(",")
print(ls)
st1 = "This is string"
ls1 = st1.split()
print(ls1)

st2 = "         This is string"
print(st2)
st2= st2.lstrip()
print(st2)
st2= st2.lstrip().rstrip()
ls2 = st2.split()
print(ls2)
