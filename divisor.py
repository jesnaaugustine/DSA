from prime_calculator import Prime
from functools import reduce

if __name__=='__main__':
    number = int(input('provide a number: '))
    prime = Prime(number)
    prime_factors = prime.prime_factors()
    total_divisor=  reduce(lambda x,y: x*y, [x+1 for x in prime_factors.values()])
    print(total_divisor)