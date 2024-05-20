####  #   #     ####  #####   ####    ##    ####       ##   #    # #####      ####  # #    #  ####  #    # 
#    #  # #     #    # #    # #    #  #  #  #          #  #  ##   # #    #    #      # ##  ## #    # ##   # 
#####    #      #    # #    # #      #    #  ####     #    # # #  # #    #     ####  # # ## # #    # # #  # 
#    #   #      #    # #####  #      ######      #    ###### #  # # #    #         # # #    # #    # #  # # 
#    #   #      #    # #   #  #    # #    # #    #    #    # #   ## #    #    #    # # #    # #    # #   ## 
#####    #       ####  #    #  ####  #    #  ####     #    # #    # #####      ####  # #    #  ####  #    #

#by John Simon , The orcas

#input from user
def main ():
    sFullName = input("Enter your full name like John Simon:").lower()
    sNames = sFullName.split()
    sName1 = sNames [0][0]
    sName2 = sNames [1][0]
    sInitials = [sName1 + sName2]
    
# password complextion
    sPassword = input ("What string of random 8-12 characters will you choose")
    sSymbols = ['!@#$%^&']
# if statements

bValid = True
bHasUpper = False
bHasLower = False
bHasSymbols = False
bhasDigits = False

sPassword if 8 < len.sPassword > 12 ()
        print('8-12 char needed')                        
    
for sCharacter in sPassword:
    if sCharacter.isupper():
         bHasUpper = True
    elif sCharacter.islower():
            bHaslower = True
    elif sCharacter.isdigits():
            bhasDigits = True
    else: sCharacter.isalpha()
    bhasSymbols = True
         
    while true:
             if sCharacter in dictCharacterCount:
                  dictCharacterCount[sCharacter] += 1
             else:
                    dictCharacterCount[sCharacter] = 1
        ##PUT MORE CODE HERE
        
print ("good password")               


main()
