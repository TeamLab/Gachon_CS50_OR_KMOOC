vector_a = [1, 2, 10] # List로 표현했을 경우
vector_b = (1, 2, 10) # Tuple로 표현했을 경우
vector_c = {'x': 1, 'y': 1, 'z': 10} # dict 표현했을 경우

print(vector_a, vector_b, vector_c)


# Vector Addition Example #1

u = [2, 2]
v = [2, 3]
z = [3, 5]
result = []
for i in range(len(u)):
    result.append(u[i] + v[i] + z[i])

print(result)

# List Comprehenstion
u = [2, 2]
v = [2, 3]
z = [3, 5]

result = [sum(t) for t in zip(u,v,z)]
print (result)

# Vector Scalar Product
u = [1, 2, 3]
v = [4, 4, 4]
alpha = 2

result = [alpha*sum(t) for t in zip(u,v)]
print(result)
