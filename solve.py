import pandas as pd
data = pd.read_csv('new.csv')

mini = data.iloc[0]['price']
maxi = 0
ans = maxi - mini
a = data['price']
for i in range(1, len(a)):
    if a[i] - mini > ans:
        ans = a[i] - mini
        maxi = data.iloc[i]['price']
        date_sell = data.iloc[i]['date']
        time_sell = data.iloc[i]['time']
    if a[i] < mini:
        mini = data.iloc[i]['price']
        date_buy = data.iloc[i]['date']
        time_buy = data.iloc[i]['time']
        
date_buy = str(int(date_buy))
time_buy = str(int(time_buy))
date_sell = str(int(date_sell))
time_sell = str(int(time_sell))

if ans <= 0:
    print('Ничего покупать не надо, прибыли не будет')
else:    
    print("Изменение стоимости акций: {}".format(ans))
    print("Время покупки: {}.{}.{} в {}:{}".format(date_buy[6:8], date_buy[4:6], date_buy[:4], time_buy[:2], time_buy[2:4]))
    print("Время продажи: {}.{}.{} в {}:{}".format(date_sell[6:8], date_sell[4:6], date_sell[:4], time_sell[:2], time_sell[2:4]))
