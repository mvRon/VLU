def bt_567():
    import datetime
    x = datetime.datetime.now()
    ngay = x.day
    thang = x.month
    nam = x.year
    return ngay, thang, nam
ngay, thang, nam = bt_567()
# print('ngày =',ngay, 'tháng =', thang, 'năm =', nam)


def bt_9():
    import datetime
    x = datetime.datetime.now()
    return x.strftime("%A")
# print(bt_9())