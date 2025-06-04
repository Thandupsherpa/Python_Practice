import os

que = input(os.system("espeak 'Wanna hear something cool?' : "))

if que == 'YES':
    os.system("espeak 'Just kidding there is no such thing as cool'")
    
elif que == 'NO':
    print('okok')
else:
    print('Invalid option')