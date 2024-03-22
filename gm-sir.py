import time 
t= time.strftime('%H:%M:%S')
hour = int(time.strftime('%H'))
hour = int(input('Enter hour:'))
# minute = int(time.strftime('%M'))
print('HOUR:',hour)
# print('MINUTE:',minute)
if(hour>=0 and hour<12):
    print('GOOD MORNING SIR')
elif(hour>12 and hour <15):
    print('GOOD AFTERNOON SIR')
if(hour>15 and hour<23):
    print('GOOD EVENING SIR')