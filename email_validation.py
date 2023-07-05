email=input("enter your Email : ")
k,j,d=0,0,0
if len(email)>=6: # this function checks length of input
    if email[0].isalpha(): # this condition checks first letter is alphabhet or not
        if("@" in email) and (email.count("@")==1): # this condition checks Email must contain only one @
            if(email[-4]==".") ^ (email[-3]=="."): # this condition checks .in and .com in email
                for i in email:
                    if i==i.isspace(): # it checks space in email
                        k=1
                    elif i.isalpha():  # it checks first character is in uppercase or not
                        if i==i.upper():
                            j=1
                    elif i.isdigit(): 
                        continue
                    elif i=="_" or i=="." or i=="@":
                        continue
                    else:
                        d=1              
                if k==1 or j==1 or d==1:
                    print("Space or special character is not allowed in Email, please try again")

                else:
                    print("You Have Entered Correct Email")    
            else:
                print("You have Entered wrong email, please make it correct")
        else:
            print("Email must contain only one @,please try again")
    else:
        print("First Character should be Alphabhet,please try again")
else:
    print("Length of the Entered character is small, please try again")                                        