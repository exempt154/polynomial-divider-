#basic linear search algorythm that returns a boolean value
def LinearSearch(li,tofind):
    found = False
    for i in range(len(li)):
        if li[i] == tofind:
            found = True
            break
    return found

#makes use of the linear search function to see if there are any powers missing from the power list, then adds the missing number and a 0 to the corrosponding lists
def MissingFix(power_li,coefficient_li):
    missingnum_li = []
    for i in range(0,len(power_li)+1):
        if LinearSearch(power_li,i) == False:
            power_li.append(i)
            coefficient_li.append(0)
    return power_li, coefficient_li

def SortedCheck(power_li):
    issorted = True
    for i in range(len(power_li)-1):
        if power_li[i]-1 != power_li[i+1]:
            issorted = False
    
def SortPowers(power_li,coefficient_li):
    i = 0
    while SortedCheck(power_li) == False:
        print(i)
        temp = 0
        if power_li[i] < power_li[i+1]:
            temp = power_li[i+1]
            power_li[i+1] = power_li[i]
            power_li[i] = temp
            temp = coefficient_li[i+1]
            coefficient_li[i+1] = coefficient_li[i]
            coefficient_li[i] = temp
        if i == len(power_li):
            i = 0
    return power_li,coefficient_li 
    
def FetchDividend():
    total_terms = int(input("enter the number of X terms in the polynomial"))
    coefficient_li = []
    power_li
    counter = 0
    while counter <= total_terms:
        counter += 1
        coefficient = int(input(f"coefficient of the {counter} term: "))
        coefficient_li.append(coefficient)
        power = int(input(f"enter the power of the {counter} term: "))
        power_li.append(power)
    return power_li, coefficient_li

    
print(SortPowers([3,2,6,1,0],[1,2,3,4,5]))
