import random
# colors
yellow='\033[93m'
gren='\033[92m'
cyan='\033[96m'
pink='\033[95m'
red='\033[91m'
b='\033[1m'
# code
print (red+b+"""


         ██████╗        ██████╗ ███████╗███╗   ██╗
         ██╔══██╗      ██╔════╝ ██╔════╝████╗  ██║
         ██████╔╝█████╗██║  ███╗█████╗  ██╔██╗ ██║
         ██╔═══╝ ╚════╝██║   ██║██╔══╝  ██║╚██╗██║
         ██║           ╚██████╔╝███████╗██║ ╚████║
         ╚═╝            ╚═════╝ ╚══════╝╚═╝  ╚═══╝
                                                   v 1.0
"""+b+red)

print (gren+b+"              <===[[ coded by Nitro Hacker ]]===>"+b+gren)
print (" ")
print (yellow+b+"        <---( search on youtube Nitro Hacker)--->"+b+yellow)
print (" ")

length=int(input(cyan+b+"Enter The Length Of The Password: "+b+cyan))
print (" ")
print (yellow+b+"-----> password  generated <----"+b+yellow)
print (" ")
char="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890@#$%&*^"
password= (gren+b+" "+b+gren)
for i in range(length):

     password+=random.choice(char)

print(password)
print (" ")
print (yellow+b+"-----> grab your password <----"+b+yellow)
print (" ")
print ("subscribe Out Channel Nitro Hacker")