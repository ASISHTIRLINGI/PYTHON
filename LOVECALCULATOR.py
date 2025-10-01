name1=input("Enter your Name:")
name2=input("Enter your Partner's Name:")
Bothnames=name1+name2
small_letters=Bothnames.lower()
print(Bothnames)
t=small_letters.count('t')
r=small_letters.count('r')
u=small_letters.count('u')
e=small_letters.count('e')
true=t+r+u+e
l=small_letters.count('l')
o=small_letters.count('o')
v=small_letters.count('v')
e=small_letters.count('e')
love=l+o+v+e
lovescore=int(str(true)+str(love))
if lovescore<10 or lovescore>=90:
    print("Your are Made for each other")
elif lovescore<=40 or lovescore>=50:
    print("You are Lucky to have your partner")
else:
    print("You are the Unique couple in the World")
