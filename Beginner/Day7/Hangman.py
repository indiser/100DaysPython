import random
import hangman_art

hangman_art.p()
print("Welcome To The Hangman Game....")
words=["zookeeper","tiger","god","camel"]
lives=6

random_word=random.choice(words)
blanks=""
for char in random_word:
    blanks+="-"

list1=list(blanks)

while lives != 0:
    guess=input("Enter the letter:").lower()
    if len(guess) != 1 or not guess.isalpha():
        print("Enter only a valid single charecter")
        continue
    if guess  in random_word:
        for i in range(0,len(random_word)):
            if guess==random_word[i]:
                list1[i]=guess
        print(''.join(list1))
        if ''.join(list1)==random_word:
            print("You Won.")
            print("Congratualtions!!!!!")
            break
    else:
        lives-=1
        if lives==0:
            print(hangman_art.hangman)
            print(f"Game Over! The word was: {random_word}")
            break
        elif lives==1:
            print(hangman_art.life1)
        elif lives==2:
            print(hangman_art.life2)
        elif lives==3:
            print(hangman_art.life3)
        elif lives==4:
            print(hangman_art.life4)
        elif lives==5:
            print(hangman_art.life5)
        print(f"You have {lives} lives left")
        print(''.join(list1))