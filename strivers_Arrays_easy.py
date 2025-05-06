######
#max of array
def max_array(arr):
    return max(arr)
#######
#second largest and smallest number in array:
#method 1: sorting arry
def sco_lar_smal(arr):
    if len(set(arr))<=1:
        return -1
    sor_arr = sorted(arr)
    print(sor_arr)
    s =1
    l = len(arr)-2
    ind_sml =False
    ind_lar =False
    while not ind_sml and not ind_lar:
        if sor_arr[s]!=sor_arr[s-1]:
            small = sor_arr[s]
            ind_sml =True

        else:
            s +=1
        if sor_arr[l] != sor_arr[l+1]:
            large = sor_arr[l]
            ind_lar=True
        else:
            l-=1
    return {'scod_small':small,'scod_large':large}
#method 2 :without sorting array
def sml_lrg(arr):
    if len(arr)<=1:
        return (-1,-1)
    sml = arr[0]
    s_sml =float('inf')
    lrg = arr[0]
    s_lrg = float('-inf')
    
    for i in range(1,len(arr)):
        if arr[i]<s_sml:
            s_sml,sml=arr[i],min(arr[i],sml)
        if arr[i]>s_lrg:
            s_lrg,lrg = lrg,max(arr[i],lrg)
    return (s_sml,s_lrg)
if __name__=='__main__':
    print(sml_lrg([1,3,2,4]))