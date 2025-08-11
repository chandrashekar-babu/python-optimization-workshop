import timeit

# Compare list comprehension vs. for loop
list_comp = timeit.timeit(
    '[i*2 for i in range(1000)]', 
    number=10000
)

for_loop = timeit.timeit(
    '''
    result = []
    for i in range(1000):
        result.append(i*2)
    ''', 
    number=10000
)

print(f"List comprehension: {list_comp:.5f} seconds")
print(f"For loop: {for_loop:.5f} seconds")