def reverseDigits(num): 
    rev_num=0
    while (num > 0): 
        rev_num = rev_num*10 + num%10
        num = num/10
    return rev_num 
  
def isPalindrome(num): 
    return (reverseDigits(num) == num) 

def ReverseandAdd(num): 

    add_count = 0
    rev_num = 0
    while (num <= 4294967295):
        

        # Reversing number 
        rev_num = reverseDigits(num) 
  
        # Adding reversed number to original
        num = num + rev_num
        add_count+=1
  
        # Checking for palindrome 
        if(isPalindrome(num)): 
            print (add_count, num)
            break
        else: 
            if (num > 4294967295): 
                print ("Nope")
        
        

numbie = input('Enter a number to do the things: ')
int(numbie)
print(numbie)

ReverseandAdd(numbie)