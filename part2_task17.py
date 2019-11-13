choice=['google_san_francisco.txt\n','google_moscow.txt\n','google_kyrgyzstan.txt\n','google_kazakstan.txt\n','google_sweden.txt\n','google_uar.txt\n','google_germany.txt\n','google_paris.txt\n']
for i in choice:
    print(i)

choose = input('Choose one of them: ')
san_francisco='google_san_francisco.txt'
moscow='google_moscow.txt'
kg='google_kyrgyzstan.txt'
kz='google_kazakstan.txt'
sweden='google_sweden.txt'
uar='google_uar.txt'
germany='google_germany.txt'
paris='google_paris.txt'
if choose == san_francisco:
    with open('google_san_francisco.txt', 'r+') as f: 
        f.write('Hello')
elif choose == moscow:
    with open('google_moscow.txt', 'r+') as f: 
        f.write('Hello')
elif choose == kg:
    with open('google_kyrgyzstan.txt', 'r+') as f: 
        f.write('Hello')
elif choose == kz:
    with open('google_kazakstan.txt', 'r+') as f: 
        f.write('Hello')
elif choose == sweden:
    with open('google_sweden.txt', 'r+') as f: 
        f.write('Hello')
elif choose == uar:
    with open('google_uar.txt', 'r+') as f: 
        f.write('Hello')
elif choose == paris:
    with open('google_paris.txt', 'r+') as f: 
        f.write('Hello') 
