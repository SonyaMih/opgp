vyska = 10
sirka = 30

if vyska%2 == 0:
    polovica_vysky_hore = vyska//2
    polovica_vysky_dole = vyska//2
if vyska%2 == 1:
    polovica_vysky_hore = vyska//2+1
    polovica_vysky_dole = vyska//2


for i in range(polovica_vysky_hore):
    riadok_hore = ""
    riadok_hore+="m"*(i+1)
    riadok_hore+="b"*(sirka-(i+1))
    print(riadok_hore)
for i in range(polovica_vysky_dole):
    riadok_dole = ""
    riadok_dole+="m"*(polovica_vysky_dole-i)
    riadok_dole+="c"*(sirka-(polovica_vysky_dole-i))
    print(riadok_dole)





