import random;

print "Hello to the 'Guess the number' game"
print "I have imagined a number from 0 to 20. Can you guess it? You have 6 tries."


over = False;
number = random.randint(0, 20);
#print number;
for i in range(1, 7):
    guess = int(input());
    if guess == number:
        print "You are correct! Game is over.";
        over = True;
    if guess > number:
        print "Your number is too big";
    if guess < number:
        print "Your number is too small";
    if over == True:
        break;
if over == False:
    print "You did not guess my number. It was " + number + " ."

#print " Game Over "
