
while True:

 hours = input('Enter Hours: ')
 rate = input('Enter Rate:')

 try:
    hours = int(hours)
    rate = int(rate)
 except :
    print ('Error, please enter numeric input')
    break
 
 def computepay(hours, rate):
  if hours<40:
   pay=hours*rate-(40-hours)*rate*.5
  else:
   pay=40*rate+(hours-40)*rate*1.5  
  print('pay: {:.2f}'.format(pay))

  
 pay = computepay(hours, rate)
 
 