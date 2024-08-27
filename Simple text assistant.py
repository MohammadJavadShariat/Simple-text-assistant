# In this section there are texts that are shown according to the search.
Bank = ['In text processing, different texts are analyzed and the ultimate goal is to model and understand human language, which can be done with machine learning methods.' ,
'Its applications are in self-driving cars, in this case, the videos received from the outside environment will be understandable to the computer using deep learning methods and image processing.',
'Expert systems are another type of sub-branches of artificial intelligence, the main purpose of these systems is to model phenomena in the form of text and draw different conclusions from it.',
' This simple text assistant is made based on Python and its purpose is to help you search for texts. We hope you will help us in developing this program so that we can compete with Google soon!',
"Python is a high-level, interpreted programming language that is widely used for various purposes such as web development, scientific computing, data analysis, artificial intelligence, etc. Its simplicity, flexibility, and extensive community support make it a popular choice among developers and researchers. Python's syntax is easy to learn and has a wide range of libraries and frameworks that make it suitable for rapid prototyping and development.",
'Artificial intelligence (AI) refers to the development of computer systems that can perform tasks that normally require human intelligence, such as learning, problem solving, and decision making. Artificial intelligence systems can be classified into two types: narrow or weak AI, which focuses on a specific task, and general or strong AI, which aims to replicate human-like intelligence. Artificial intelligence has numerous applications in industries such as healthcare, finance, transportation, and customer service, and its potential to transform businesses and societies is enormous.',
'C# is a modern, object-oriented programming language developed by Microsoft as part of the .NET initiative. It is designed to work with the .NET framework and is widely used for building Windows applications, web applications, and games. C# is known for its strong safety, garbage collection, and multi-paradigm programming capabilities, making it a popular choice among developers for building robust and scalable software systems.',
] 


History = [] # History storage list

while (True): # to search again
    
    answer = False # be means there is an answer and it is shown True if
    print("(Enter 'End Search' to end the search.\n If you want to access your history, enter 'History'. \nIf you want to help us develop this text assistant, enter 'Development' )")
    search = input("search...") # Saves the searched phrase.
  
    # Enter "end search" to end the search
    
    if search == 'end of search':
        answer = True
        break

    # Search for the word "history" and display the search history
    
    elif search == "History":
        print(f"\n{History}\n")
        answer = True

    # Enter the word "development" to develop the text assistant
    
    elif search == 'Development':
        Add = input("\n(If you give up, enter the word 'I gave up.') Enter your text:\n")
        if Add != 'I gave up' :
            Bank.append(Add)
            answer = True


    # Show texts if there are words in them
    
    for text in Bank:
        if search in text:
            print(f"\n-----------Beginning of the answer-----------\n{text}\n-------------End-------------\n")
            answer = True
            
    # Saving search history other than keywords such as "development"
    if search != 'History' and search != 'Development':
        History.append(search)

    # Request to add your text to the program 
    # If there is no word in the texts
    if answer == False :
        print("\nNot available.")
        while (True) :
            ask = input("Do you want to enter your own text and help us develop this text assistant? ('yes/no')\n")
                
            #If you enter "yes", it will ask you for input 
            # Enter your text.
                
            if ask == "yes" :
                add = input("\nEnter your text (if you opt out, enter the word 'I've opted out'):\n")
                if add != 'I gave up' :
                    Bank.append(add)
                    break
                if add == 'I gave up' :
                    break
                
            # But if you press "No" it will not ask you to enter any text.
                
            elif ask == "no" :
                print("\nAnyway you are comfortable.\n")
                break
                
            # Asking the question again if you enter another word
                
            else :
                print('\nPlease enter the word "yes" or "no".\n')
                    
