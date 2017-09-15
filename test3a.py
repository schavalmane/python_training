#Write a program that secretly selects a number between 1 and 100, and repeatedly asks the user to guess it until the guess is correct. If the guess is incorrect and lower than the secret number, the program should print "too low". If the guess is incorrect and higher than the secret number, the program should print "too high".
#

def ChekGuess(userguess,systemguess):
   if userguess == systemguess:
       return('TRUE')
   else:
       if userguess > systemguess :
           return ('GREATER')
       else:
           return ('SMALLER')


systemguess = 25
print ("Please guess the number")
guess='FALSE'
while guess != 'TRUE':
 userguess=int(input())
 guess=ChekGuess(userguess,systemguess)
 if guess =='TRUE':
    print ("Congrats the Number you gussed is correct %d " ,systemguess)
    guess='TRUE'
 elif guess == 'GREATER':
      print ('Too High')
      guess='FALSE'
 else :
   print ('Too Low')
   guess='FALSE' 
    
