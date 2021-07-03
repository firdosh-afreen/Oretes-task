def count(str):
    d={}
    for n in str:
        keys=d.keys()
        if n in keys:
            d[n]+= 1
        else:
            d[n] = 1
    return d

print(count("dfttttuinnnjkkggd"))
