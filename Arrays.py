def comparearrays(list1, list2):
    if len(list1) == len(list2):
        flag = True
        for index in range(0, len(list1)):
            if list1[index]!= list2[index]:
                flag = False
        if flag:
            print "The lists are the same"
        else: 
            print "the lists are not the same"
    else:
        print "the lists are not the same"
    
comparearrays([1,2,5,6,2],[1,2,5,6,2])
# list_one = [1,2,5,6,5]
# list_two = [1,2,5,6,5,3]

# list_one = [1,2,5,6,5,16]
# list_two = [1,2,5,6,5]

# list_one = ['celery','carrots','bread','milk']
# list_two = ['celery','carrots','bread','cream']
