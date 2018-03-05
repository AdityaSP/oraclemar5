a = raw_input('Enter a string: ')
print "-" * 30
print "The reverse of your string is"
print a[::-1]

if a.lower() == a[::-1].lower():
    print "Its a Palindrome!"
else:
    print "Not a Palindrome"

print "-" * 30