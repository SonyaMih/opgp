TEXT = "Ahoj! Ja som Soňa"
statistika = {}
for i in TEXT:
    if i in statistika:
        statistika[i]+=1
    else:
        statistika[i]=1
for k,v in statistika.items():
    print(f"{k}: {v}")
