k=input("")

s=k[::-1]
print('reverse:'+s)
for vowel in ['a','e','i','o','u']:
    	s=s.replace(vowel,'')
    
print(s)
