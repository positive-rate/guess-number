import random

print("Hello! Guess the number or die. And be quick. Or I will kill you LOL")

secret = random.randint(-1, 50)

answer=int(input())

if answer == secret:
  print("You're not dead, congratulations.")
  exit()

if answer > secret:
  print("Too bad. the number that you picked is bigger. You will die soon LOL")
else:
  print("Too bad. the number that you picked is smaller. You will die soon LOL")



                            
# Yeonseo
answer=int(input())
if answer==secret:
  print("you're not dead,congratulation.")
  exit()
if answer>secret:
  print("too bad.the number that you picked is bigger.you will die soon")
else:
  print("too bad. the number that you picked is smaller.you will die soon")
  

# Eunseo
answer=int(input())

if answer == secret: 
  print("You are not dead, congratulations.")
  exit()
  
if answer > secret:
  print("Too bad. them numbert that you picked is bigger. You'll die soon.")
  
else:
  print("Too bad. the number that you picked is smaller. You'll die soon.")



# 현겸
answer = int(input())

if answer == secret:
  print("You're not dead, congratulations.")
  exit()
 
if answer > secret:
  
  print("Too bad. them numbert that you picked is bigger.   YOu'll die soon.")

else:
  print("Too bad. them numbert that you picked is bigger. YOu'll die soon.")


  
# 태건
answer = int(input())

if answer == secret:
  print("너는 죽지 않았어. 그러나 곧 죽겠지")
  exit()

if answer > secret:
  print("수가 너무 커") 
else:
  print("수가 너무 작네")
  
    
# Lily
answer = int(input())

if answer != secret:
  print("Too bad. You're dying. Meet you at the hell. Bye Bye my friend ^^")