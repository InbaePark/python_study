"""
2�̃x�N�g�� x, y���󂯎��A���̘ax+y��Ԃ��֐�
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
2�̍s�� X, Y���󂯎��A���̘aX+Y��Ԃ��֐�
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
�s�� X�ƃx�N�g�� y���󂯎��A���̐� Xy��Ԃ��֐�
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
2�̍s�� X, Y���󂯎��A���̐� XY��Ԃ��֐�
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
�s�� X���󂯎��A���̓]�u XT��Ԃ��֐�
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
