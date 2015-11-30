    
import random

def get_wordlist():
    f=open("/usr/share/dict/words")
    clean_words = []
    for i in f:
        i=i.strip()
        if i.isalpha() and len(i)>5:
            clean_words.append(i.lower())
    return clean_words


def select_word(word_list):
    return random.sample(wordlist,1)[0]

def printstar():
    for letter in secret_word:
        print "*",


def play_hangman(secret_word):
    i=0
    leng = len(secret_word)
    word_array = ["*"]*leng
    k=0
    corrctlettrs=0
    w_guess=0
    error=0
    
    while(w_guess<=10):
        n =raw_input("\nGuess the letter \t ")

        for letter in secret_word:
            if (n==letter):
                word_array[k]=letter
                corrctlettrs+=1
            else:
                error=error+1
            k=k+1
        
        k=0

        for letter in word_array:
            print letter,
       
        if error==leng:
            w_guess+=1
            print "\nWrong Guess"

        i=i+1
        error=0
        
        if w_guess>9:
            print "Game Over"
            print "The secret word is %r" % secret_word
            break;
        elif corrctlettrs==leng:
            print "\nYou found it !!"
            break;
        
         

wordlist = get_wordlist()
secret_word = select_word(wordlist)
printstar()
play_hangman(secret_word)







    
    
