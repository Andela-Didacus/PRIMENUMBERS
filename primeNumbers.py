def is_Prime(n):

    if type(n)==int and n>0:                    #checks for type error and ensures n is not a positive number     

        for number in range(0,n+1):
            if number >= 1:
                for i in range(2,number):       #checks if the number is only divisible by 1 and itself
                    if (number%i)==0:
                        break
                else:
                    print number
            
    else:
        return "TypeError"

        

n = input("Enter a range: ")

if type(n)==int:                                #checks the input from the user 
    
    is_Prime(n)
    
else:
    
    print  "TypeError"

                       
            
            
