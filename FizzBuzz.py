def fizz_buzz(N):
        if N%3==0 and N%5!=0:
            return 'Fizz'
        elif N%5==0 and N%3!=0:
            return 'Buzz'
        elif (N%3==0 and N%5==0):
            return 'FizzBuzz'
        else:
            return N