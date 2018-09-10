def fizzbuzz(d):
    if(d%3==0 and d%5==0):
        return("Fizzbuzz")
    elif (d%3==0 or str(d).find("3") != -1):
        return("Fizz")
    elif(d%5==0 or str(d).find("5") != -1):
        return("Buzz")
    else:
        return(d)

def runner(max):
    for d in range(1, max):
        print(fizzbuzz(d))

if __name__=="__main__":
    runner(100)
