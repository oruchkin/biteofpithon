def f(**kwargs):
    print(kwargs)
    for k,v in kwargs.items():
        print(k,v)


f(a=1, b=5,c=6, name=111)