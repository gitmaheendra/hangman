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


def play_hangman(secret_word):
    #homework
    
    for letter in secret_word:
        print "*",
    i=0
    while(i< len(secret_word)):
        n = raw_input("Guess the letter \t ")
        for letter in secret_word:
            if (n==letter):
                print letter,
            else:
                print "*",
               
        i+=1
    


wordlist = get_wordlist()
secret_word = select_word(wordlist)
play_hangman(secret_word)
    
    
