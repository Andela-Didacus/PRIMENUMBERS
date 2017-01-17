def is_Prime(n):

    if type(n)==int and n>0:

        for number in range(o,n+1):
            if number >= 0:
                for i in range(2,number):
                    if (number%i)==0:
                        break
                else:
                    print number

n = input("Enter a range: ")

is_Prime(n)
                       
            
            
