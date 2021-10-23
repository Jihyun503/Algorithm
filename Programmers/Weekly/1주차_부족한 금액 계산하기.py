def solution(price, money, count):
    saveprice = 0
    for i in range(1, count+1):
        saveprice += price * i

    if saveprice <= money:
        return 0
    else:
        return saveprice - money