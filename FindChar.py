word_list = ['hello','world','my','name','is','Anna']
char = 'e'
# new_list = ['hello','world']

def character(char, word_list):
    new_list = []
    for word in word_list:
        if word.find(char)>=0:
            new_list.append(word)
        # print word
    print new_list

character(char, word_list)