
def say_hello(first_name , last_name , times ): 
    count = 0
    while count < times:
        print(f"Hello {first_name} {last_name}")
        count += 1

say_hello("Umair", "Ramzan" , 5)


#
def join_words(word1 , word2 , word3 , word4):
    print( f"{word1},{word2},{word3},{word4}" )


join_words("one", "two", "three" , "four")
# join_words("one", "two") # error
# join_words("one", "two", "three" , "four", "five") #error

#enumerate

# 1. list [1, 2, 3]
# 2. tuple
# 3. dictionay

def join_words(*args):
    final_text = ""
    for word in args:
        final_text += word + ","   
    
    print(final_text)


join_words("one", "two", "three" , "four")
join_words("one", "two")
join_words("one", "two", "three" , "four", "five")





def join_words(*args):
    final_text = ""
    for i ,word in enumerate(args):
        if len(args) - 1 == i :
            final_text += word 
        else:
            final_text += word + "," 
       
    
    print(final_text)



join_words("one", "two", "three" , "four")
join_words("one", "two")
join_words("one", "two", "three" , "four", "five")