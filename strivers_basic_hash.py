###########

#frequency of eement in array
def frequency(arr):
    res ={}
    for i in arr:
        res[i]= res.get(i,0)+1

    return res

###########
# highest and lowest frequncy element
def h_l_freq(arr):
    frq= frequency(arr)
    max_e= max(frq,key = frq.get)
    min_e= min(frq, key = frq.get)
    return {'min':min_e,'max':max_e}

if __name__=='__main__':
    #print(frequency([1,2,2,3]))
    print(h_l_freq([1,2,2,2,5]))