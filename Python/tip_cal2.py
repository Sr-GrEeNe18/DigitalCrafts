bill_amount = float(input('total bill amount?'))
service = input('what the service level is ')

if service == 'good':
    tip = 0.2
elif service == 'fair':
    tip = 0.15
elif service == 'bad':
    tip = 0.1

split = float(input('split how many ways? '))

tip_amount = bill_amount * tip / split
total = tip_amount + bill_amount
print("%.2f is your bill" % total)