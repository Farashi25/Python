print "hello world"
first_name = "Zen"
last_name = "Coder"
print "My name is {} {}".format(first_name, last_name)

x = "Hello World"
print x.upper()

age = 17
if age >= 18:
    print 'Legal age'
elif age == 17:
    print 'you are seventeen'
else:
    print 'You are so young!'

for count in range(0, 5):
    print "looping-", count

my_list =[4, 'dog',99,['list','inside','another'],'hello world!']
for element in my_list:
    print element


x = 3
y = x
while y > 0:
  print y
  y = y - 1
else:
  print "Final else statement"


x = 3
y = x
while y > 0:
  print y
  y = y - 1
  if y == 0:
    break
else:
 print "Final else statement"