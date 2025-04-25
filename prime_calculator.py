import copy
class Prime:
    def __init__(self,num):
        self.number = num
        self.cur_prime =2

    def get_next_prime(self,**kwargs):
        cur = kwargs.get('cur_number',self.number)
        got = False
        for i in range(self.cur_prime+1,cur):
            for j in range(2,int(i**0.5)+2):
                if i%j==0:
                    got =True
            if not got:
                return i
            got =False
        return cur

    def prime_factors(self):
        result = {}
        cur_num = copy.copy(self.number)
        if cur_num<=2:
            return {cur_num:1}
        
        while cur_num >1:
            if cur_num%self.cur_prime ==0:
                result[self.cur_prime] = result.get(self.cur_prime,0) +1
                cur_num =cur_num//self.cur_prime
            else:
                self.cur_prime = self.get_next_prime(cur_number=cur_num)
        return result
    

    def is_prime(self):
        if self.number<=2:
            return True
        for i in range(2,int(self.number**0.5)+2):
            if self.number%i ==0:
                return False
        return True
    
    def all_prime_numbers(self):
        
        if self.number<=2:
            return list(range(1,self.number+1))
        result =[2]
        got =True
        for i in range(3,self.number+1):
            for j in range(2,int(i**0.5)+2):
                if i%j==0:
                    got =False
            if got:
                result.append(i)
            got =True
        return result
                
  

