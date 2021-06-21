def even(n):
    if n%2==0:
        return "even"
    else:
        return "odd"
    

def leapyears(l,u):
    for year in range(l,u+1):
        if (year%4==0 and year%100!=0) or year%400==0:
            print(year,end=" ")

def duplicates(l): #[25,25,26,27,26,28]
    li=[] #25,26,27,28
    for i in l: #25,25,26,27,26,28
        if i not in li:
            li.append(i)
    print(li)