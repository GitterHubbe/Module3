# Import random tool
import random

# Open and close word list file
filename = 'word_list.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

# Select random word
for line in lines:
    word = random.choice(lines)
# Check word output
#print(word)

# Identify length of word
length = len(word) - 1
# Check output of length
#print(length)

# Convert to list
answer = list(word)
# Remove /n
answer.pop(-1)
# Check output of list conversion
#print(answer)

# Setup answer_progress
answer_progress = list("*" * length)

# Setup life counter
life_count = 7

#if '*' in answer_progress:
while answer_progress != answer:
   # Answer before player input
   print(''.join(answer_progress))
   # Input from player
   guess = input("Please enter your next guess: ")
   # Update to answer_progress with each guess
   if str(guess) in answer:
       for i, item in enumerate(answer):
           if item == guess:
               answer_progress[i] = guess;
   else:
       life_count -= 1
   # Check life counter
   #print(life_count)
   if life_count == 0:
       print("You lose!")
       break

# If break out of while loop and word completed:
if answer_progress == answer:
    print("Congratulations you win!")
