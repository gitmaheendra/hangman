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
    print secret_word
    for letter in secret_word:
        print "*",
    i=0
    leng = len(secret_word)
    wordry = ["*"]*leng
    k=0
    while(i< leng):
        n =raw_input("\nGuess the letter \t ")
        for letter in secret_word:
            if (n==letter):
                wordry[k]=letter
                      
            k=k+1
        k=0            
        for letter in wordry:
            print letter,
        print "\none life gone.. %r more !\n" % (leng-i)
        i=i+1


wordlist = get_wordlist()
secret_word = select_word(wordlist)
play_hangman(secret_word)
print "The secret word is %r" % secret_word
    
    
