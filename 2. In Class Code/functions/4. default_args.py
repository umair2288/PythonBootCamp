
def join_words(*args , seperator=","):
    final_text = ""
    for i ,word in enumerate(args):
        if len(args) - 1 == i :
            final_text += word 
        else:
            final_text += word + seperator
       
    
    print(final_text)

join_words("one", "two", "three" , "four" , seperator="*")
join_words("one", "two")
join_words("one", "two", "three" , "four", "five" )
join_words("one", "two", "three" , "four", "five", "six" , seperator=" $$ " )



def greet_me(lang="English"):
    if lang == "English":
        print("Good Morning")
    if lang == "Tamil":
        print("Vanakkam")

greet_me("Tamil")
