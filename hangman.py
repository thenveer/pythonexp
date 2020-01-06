import random
 
def get_secret_word(word_file="/usr/share/dict/words"):
    good_words = []
    with open(word_file) as f:
        for word in f:
            word = word.strip()
            if not word.isalpha():
                continue
            if len(word) < 5:
                continue
            if word[0].isupper():
                continue
            good_words.append(word)
 
    word = random.choice(good_words)
    return word.lower()
def hide_word(s,correct_letter):
    wrong=[]
    a=[]
    a.append(s)
    print(s)
    words=list(a[0])
    wordlist = []
    wordlist.extend(words)
    for i in range(len(wordlist)):
         wordlist[i]= "_"
    for i in correct_letter:
         guessed=i
         for i in range(len(words)):
             if words[i]==guessed:
                 wordlist[i] =guessed

    return (''.join(wordlist))

def game(s,correct_letter,wrong_word,guess):
    a=[]
    a.append(s)
    
    words=list(a[0])
    wordlist = []
    wordlist.extend(words)
    correct_lettre=[]
    for i in correct_letter:
        correct_lettre.extend(i)
    wrong_letter=[]
    for i in wrong_word:
        wrong_letter.append(i)
    for i in guess:
        guessed=i
        if guessed in wordlist and guessed not in correct_lettre:
            correct_lettre.append(guessed)
        elif guessed not in wordlist and guessed not in wrong_letter:
            wrong_letter.append(guessed)
    hidden_letters=hide_word(s,correct_lettre)
    return (hidden_letters,correct_lettre,wrong_letter)

def get_status(s,correct_lettre,wrong_letter,guess):
    guessed=game(s,correct_lettre,wrong_letter,guess)
    #hidden=guessed[0]
    guess_word=''.join(guessed[1]+guessed[2])
    
    #guessed = " ".join(guess_word)
    turn =7-len(guessed[2])
    status_message="""
guess = {}
turn left ={} 
""".format(guess_word,turn)
    return status_message

def continue_or_exit(s,correct_letter,wrong_letter,guess):

    hidden_letters,correct_lettre,wrong_letter=game(s,correct_letter,wrong_letter,guess)

    if len(wrong_letter) < 7:
        state=1
    else:
        state=2

    c=False    
    for i in s:
        if i not in correct_lettre:
            c=False
            break
        else:
            c=True
    if c:
        state=3


    return (hidden_letters,correct_lettre,wrong_letter,state)


def main():
    s=get_secret_word()
    
    #print the hide words
    hidden_words=hide_word(s,"")
    print(hidden_words)
    #print the guessing input
    guess=input('')
    play=continue_or_exit(s,'','',guess)

    

    while(play[3]== 1 or play[3]==2 or play[3]==3):
         if play[3]==1:
             display=get_status(play[0],play[1],play[2],guess=play[1]+play[2])
             print(display)
             #print(play[0])
             #print(f"guessed words : {play[1]+play[2]}")
             #print(f"")
             guess=input('')
             play=continue_or_exit(s,play[1],play[2],guess)

         elif play[3]==2:
             print("you lost")
             break
         else:
             print("you win")
             break


print(main())



# def correct_word():
#     guess=[]
#     list_of_words=hide_word("bigger",guess)
#     print(list_of_words


        #         if guessed not in words:
         #            wrong.append(guessed)
    
                     
    
#j=['b','g','k','g','z','r','o']
#print(hangman("bigger",j))

    
#    word=get_secret_word()
 #   print(word)
  #  ans=list(word[0])
   # words=[]
  #  words.extend(ans)
    
   # for i in range(len(words)):
    #    words[i]="_"

    #print (' '.join(ans))

#  mydic={}
 #   for l in range(len(word)):
  #      mydic[word[l]]=word.count(word[l])
   # print(mydic)
    #for q in range(0,len(word)):
     #   s=input("")
     #for i in s:
      #      print(mydic)
       #     p=mydic['i']
       #     print(p)
       #     if i in word :                
       #         print ("u r rigth")
        #    else:
        #        print("u r weong")

   # count=0
   # while count < len(ans):
    #    guess =input("")
  
