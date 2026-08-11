
def condition1(ele):
    return ele%2==0
def transform1(ele):
    return ele**2


def myfunc(arr,condition):
    res = []
    for ele in arr:
        if condition(ele):
            res.append(ele**2)
            
    #     elif condition2:
    #         res.append(transform2(ele)

    # res = [process(x) for x in arr]
    return res


def generator(start,end):
    for i in range(start,end):
        if i%2==0:
            yield(i**2)
    

for i in generator(1,11):
    print(i)
    print("in process")