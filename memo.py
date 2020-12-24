def vector_sum(x, y):
    res = []
    
    for i in range(len(x)):
        res.append(x[i]+y[i])
    
    return res

def matrix_sum(X, Y):
    res = []
    
    for i in range(len(X)):
        x = X[i]
        y = Y[i]
        z = vector_sum(x, y)
        res.append(z)
        
    return res
