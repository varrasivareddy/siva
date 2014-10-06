n = 600851475143
i =2
while i*i <n:
  if n%i ==0:
    n = n/i
    print 'I is ' + str(i)
    print 'N is ' + str(n)
  i += 1

print 'Largest Prime is' + str(n)
