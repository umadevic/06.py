import sys 
yr0=int(input())
if yr0%400==0 or (yr0%4==0 and yr0%100!=0):
 print('yes')
else:
 print('no')
