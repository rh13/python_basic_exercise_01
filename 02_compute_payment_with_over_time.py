hours = int(input('Enter Hours: '))
rate = float(input('Enter Rate:'))
pay=hours*rate
if hours>40:
 pay=40*rate+(hours-40)*rate*1.5

print('Pay: {:.2f}'.format(pay))
