"""
2つのベクトル x, yを受け取り、その和x+yを返す関数
x = [1, 2, 3]
y = [8, 1, 2]
answer = vector_sum(x, y)
print(answer)  # => [9, 3, 5]
"""
def vector_sum(x, y):
    res = []
    
    for i in range(len(x)):
        res.append(x[i]+y[i])
    
    return res

"""
2つの行列 X, Yを受け取り、その和X+Yを返す関数
X = [[1, 2, 3],
     [4, 5, 6]]
Y = [[8, 1, 2],
     [-1, 0, -2]]
answer = matrix_sum(X, Y)
print(answer)  # => [[9, 3, 5], [3, 5, 4]]
"""
def matrix_sum(X, Y):
    res = []
    
    for i in range(len(X)):
        x = X[i]
        y = Y[i]
        z = vector_sum(x, y)
        res.append(z)
        
    return res

"""
行列 Xとベクトル yを受け取り、その積 Xyを返す関数
X = [[1, 2, 3],
     [4, 5, 6]]
y = [8, 1, 2]
answer = matrix_vector_product(X, y)
print(answer)  # => [16, 49]
"""
def matrix_vector_product(X, y):
    res = []
    
    for i in range(len(X)):
        x = X[i]
        t = 0
        for j in range(len(x)):
            t += x[j]*y[j]
        res.append(t)
        
    return res

"""
2つの行列 X, Yを受け取り、その積 XYを返す関数
X = [[1, 2, 3],
     [4, 5, 6]]
Y = [[8, 1],
     [-1, 0],
     [0, 1]]
answer = matrix_product(X, Y)
print(answer)  # => [[6, 4], [27, 10]]
"""
def matrix_product(X, Y):
    res = []
    
    for i in range(len(X)):
        x = X[i]
        y = []
        for j in range(len(X)):
            t = 0
            for k in range(len(x)):
                t += x[k]*Y[k][j]
            y.append(t)
        
        res.append(y)
        
    return res

"""
行列 Xを受け取り、その転置 XTを返す関数
X = [[1, 2, 3],
     [4, 5, 6]]
answer = matrix_transpose(X)
print(answer)  # => [[1, 4], [2, 5], [3, 6]]
print(matrix_transpose(answer)) # => [[1, 2, 3], [4, 5, 6]]
"""
def matrix_transpose(X):
    n = len(X)
    m = len(X[0])
    res = []
    
    for i in range(m):
        t = []
        
        for j in range(n):
            t.append(X[j][i])
        
        res.append(t)
        
    return res
