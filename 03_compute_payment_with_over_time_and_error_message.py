while True:

 hours = input('Enter Hours: ')
 rate = input('Enter Rate:')

 try:
    hours = int(hours)
    rate = int(rate)
 except :
    print ('Error, please enter numeric input')
    break
        

 pay=hours*rate 
 if hours>40:
  pay=40*rate+(hours-40)*rate*1.5

 print('Pay: {:.2f}'.format(pay))
