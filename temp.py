def foo():
    promolink = [(lambda i: '?promo=offer'+str(i))(i) for i in range(0, 10)]
    print(promolink)


foo()
