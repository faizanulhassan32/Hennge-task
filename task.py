def takeinput( test_cases , N):

    if ( N==0 ):
        return 

    x = int(input("Number of integars : "))  
    print("Enter numbers now : ")
    temp = input().split(' ')   # all numbers taken input
    numbers = temp[:x]  # numbers from index 0 to x
    test_cases.append(numbers)

    takeinput(test_cases , N-1)

def takesquare( one_test_case , ind , total ):

    if ind < len(one_test_case):
        number = int( one_test_case[ind] )     # getting individual element
        
        if number > 0 :
            total += number*number  # only positive integars

        takesquare( one_test_case , ind+1 , total )

    else:
        sums.append(total)  # appending final total in sums list
        return




def takesum( test_cases , index ):
    if index > len(test_cases)-1:
        return
    
    takesquare(test_cases[index] , 0 , 0)   # sending every test case with 0 index and 0 total

    return takesum( test_cases , index+1 )



def main():
    N =  int(input("Number of test cases : "))

    takeinput(test_cases , N)   # calling function to take input from user

    takesum( test_cases , 0 )   # after input taking sum of test cases

    print("Sums : ",sums)   # printing final sums

    


if __name__ == "__main__":
    test_cases = []     # list to contain all test cases
    sums = []   # to contain all sums
    main()