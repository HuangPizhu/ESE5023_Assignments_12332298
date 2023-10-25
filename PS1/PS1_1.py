def Print_values(a,b,c):
    if a>b:
        if b>c:
            return a,b,c
        else:
            if a>c:
                return a,c,b
            else:
                return c,a,b
    else:
        if b>c:
            return None
        else:
            return c,b,a