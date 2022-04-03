number_input = int(input("Enter a number: "))

if number_input>1:
    for x in range(2,number_input):
        if(number_input/x)==0:
            print("not prime")
            break
        else:
                print("prime")
                break
else:
    print("not prime")
