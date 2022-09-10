def mmc(a,b):
    ma = a
    mb = b
    while ma != mb:
        if ma > mb:
            mb += b
        if mb > ma:
            ma += a
    return ma

print(mmc(15,10))
