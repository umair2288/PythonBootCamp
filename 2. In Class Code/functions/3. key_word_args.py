
def join_words(*args , seperator):
    final_text = ""
    for i ,word in enumerate(args):
        if len(args) - 1 == i :
            final_text += word 
        else:
            final_text += word + seperator
       
    
    print(final_text)



join_words("one", "two", "three" , "four" , seperator="*")
join_words("one", "two")
join_words("one", "two", "three" , "four", "five")



def full_name(first_name , last_name):
    print(f"{first_name} {last_name}")

full_name("Umair" , "Ramzan")
full_name("Ramzan" , "Umair")
full_name(last_name="Ramzan" , first_name="Umair")