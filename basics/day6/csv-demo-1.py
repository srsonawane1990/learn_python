fh = open('./Day7/emp.csv')

next(fh) # This is skip my fist line
for rec in fh:
    print(rec)
    print(rec.split(","))
fh.close()

fh = open('./Day7/emp.csv',"a")
fh.writelines(["shiv,2,ch","madhav,44,Delhi"])
fh.close()
