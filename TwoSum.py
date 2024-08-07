
#Brute force method is simply
#Find every permutation and stop once the integer is found since only 1 solution
#For example, for [4,2,5,1]
#(0,1), (0,2), (0,3), (0,4)
#(1,2), (1,3), (1,4)
#(2,3), (2,4)
#(3,4)

#for a list with 4 elements, the number of searches is 10

#for 5, I suspect it will be 15
# x x x x x
# x x x x
# x x x
# x x 
# x

# list_of_Integers = [4,2,5,1,4,6,3,1]
# target = 7

# for i in range(0,len(list_of_Integers)-1):
#     for j in range(i+1,len(list_of_Integers)-1):


#     if list_of_Integers[i] + list_of_Integers[i+1] == target:
#         print(f'indices are {i} and {i+1}')


# print(len(list_of_Integers))

# for a in list_of_Integers:
#     for b in list_of_Integers:
#         print(a,b)

iterable = [9,1,3,5]
r = 2
target = 8

def combinations(iterable, r):
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))

    yield indices, tuple(pool[i] for i in indices)  # Changed this line
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield indices.copy(), tuple(pool[i] for i in indices)  # Changed this line

for indices, combo in combinations(iterable, r):
    if sum(combo) == target:
        print(f"Indices: {tuple(indices)}, Values: {combo}")



