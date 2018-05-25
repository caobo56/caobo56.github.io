# codewars（python）练习笔记二十一：Matrix Determinant

### 题目
Write a function that accepts a square matrix (n x n 2D array) and returns the determinant of the matrix.
How to take the determinant of a matrix -- it is simplest to start with the smallest cases: A 1x1 matrix |a| has determinant a. A 2x2 matrix [[a, b], [c, d]] or
```
|a b|
|c d|
```
has determinant ad - bc.
The determinant of an n x n sized matrix is calculated by reducing the problem to the calculation of the determinants of n n-1 x n-1 matrices. For the 3x3 case, [[a, b, c], [d, e, f], [g, h, i]] or
```
|a b c|
|d e f|
|g h i| 
```
the determinant is: a * det(a_minor) - b * det(b_minor) + c * det(c_minor) where det(a_minor) refers to taking the determinant of the 2x2 matrix created by crossing out the row and column in which the element a occurs, or
```
|e f|
|h i| 
```
Note the alternation of signs. 
The determinant of larger matrices are calculated analogously, e.g. if M is a 4x4 matrix with first row [a, b, c, d], det(M) = a * det(a_minor) - b * det(b_minor) + c * det(c_minor) - d * det(d_minor)

Sample Tests:
```
m1 = [ [1, 3], [2,5]]
m2 = [ [2,5,3], [1,-2,-1], [1, 3, 4]]

Test.assert_equals(determinant([[1]]), 1, "Determinant of a 1 x 1 matrix yields the value of the one element")
Test.assert_equals(determinant(m1), -1, "Should return 1 * 5 - 3 * 2, i.e., -1 ")
Test.expect(determinant(m2) == -20)
```
题目大意：
求出给定矩阵的行列式。
写出一个determinant(A)函数。输入项A为n行n列的矩阵|A|(n>=1)。
若A是一个1X1的矩阵，则determinant(A) 返回 A[0][0];
若A是一个2X2的矩阵,如：
```
|a b|
|c d|
```
则determinant(A) 返回 ad - bc;
若A是一个nXn的矩阵,如：
```
|a b c|
|d e f|
|g h i| 
```
则determinant(A)返回 a * det(a_minor) - b * det(b_minor) + c * det(c_minor)，<font color=#FF0000 size=3 face="黑体">**(注意加减符号的交替)**</font>
det(a_minor)是指通过划掉元素a所在的行和列而创建的2x2矩阵的矩阵，如
```
|e f|
|h i| 
```
若A是更大的矩阵比如5行5列，则determinant(A)返回 a * det(a_minor) - b * det(b_minor) + c * det(c_minor) - d * det(d_minor) + e * det(e_minor)。
依次类推。

### 我的解法：
```
#!/usr/bin/python
    
def determinant(matrix):
    if len(matrix) < 2:
        return matrix[0][0]
    elif len(matrix) == 2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
    while len(matrix) > 2:
        return sum([(1 if y%2 == 0 else -1)*(matrix[0][y])*determinant([[matrix[i][j] for j in range(0,len(matrix[i])) if j != y] for i in range(1,len(matrix))]) for y in range(0,len(matrix[0]))])
             
print determinant([ [2,5,3], [1,-2,-1], [1, 3, 4]])
```

### 我的思路：
先是常规思路，递归求值,将找出matrix[x][y] 的 minor 提出为函数 minor(matrix,x,y)，以优化算法可读性。
### 下面是优化前的第一版能跑通的函数：
```
#!/usr/bin/python

def minor(matrix,x,y):
    arr = []
    for i in range(1,len(matrix)):
        if i != x:
            arr_y = []
            for j in range(0,len(matrix[i])):
                if j != y:arr_y.append(matrix[i][j])
        arr.append(arr_y)
    return arr

def determinant(matrix):
    if len(matrix) < 2:
        return matrix[0][0]
    while len(matrix) >= 2:
        if len(matrix) == 2:
            return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
        else:
            temp = 0
            for y in range(0,len(matrix[0])):
                temp += (1 if y%2 == 0 else -1)*(matrix[0][y])*determinant(minor(matrix,0,y))
            return temp
            
print determinant([ [2,5,3], [1,-2,-1], [1, 3, 4]])
```
#### 1.优化函数 minor(matrix,x,y)
因为函数 minor(matrix,x,y)三个参数中，x一直为0，可以去掉
```
#!/usr/bin/python

def minor(matrix,y):
    arr = []
    for i in range(1,len(matrix)):
        arr_y = []
        for j in range(0,len(matrix[i])):
            if j != y:arr_y.append(matrix[i][j])
        arr.append(arr_y)
    return arr

def determinant(matrix):
    if len(matrix) < 2:
        return matrix[0][0]
    while len(matrix) >= 2:
        if len(matrix) == 2:
            return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
        else:
            temp = 0
            for y in range(0,len(matrix[0])):
                temp += (1 if y%2 == 0 else -1)*(matrix[0][y])*determinant(minor(matrix,y))
            return temp
            
print determinant([ [2,5,3], [1,-2,-1], [1, 3, 4]])
```
#### 2.继续优化minor()函数：
通过嵌套，将函数缩短为一行
```
#!/usr/bin/python

def minor(matrix,y):
    return [[matrix[i][j] for j in range(0,len(matrix[i])) if j != y] for i in range(1,len(matrix))]
    
def determinant(matrix):
    if len(matrix) < 2:
        return matrix[0][0]
    while len(matrix) >= 2:
        if len(matrix) == 2:
            return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
        else:
            temp = 0
            for y in range(0,len(matrix[0])):
                temp += (1 if y%2 == 0 else -1)*(matrix[0][y])*determinant(minor(matrix,y))
            return temp
            
print determinant([ [2,5,3], [1,-2,-1], [1, 3, 4]])
```

#### 3.优化递归的语法：
```
#!/usr/bin/python

def minor(matrix,y):
    return [[matrix[i][j] for j in range(0,len(matrix[i])) if j != y] for i in range(1,len(matrix))]
    
def determinant(matrix):
    if len(matrix) < 2:
        return matrix[0][0]
    while len(matrix) > 2:
        if len(matrix) == 2:
            return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
        else:
            return sum([(1 if y%2 == 0 else -1)*(matrix[0][y])*determinant(minor(matrix,y)) for y in range(0,len(matrix[0]))])
             
print determinant([ [2,5,3], [1,-2,-1], [1, 3, 4]])
```
#### 4.调整判断矩阵的行数的顺序：
```
#!/usr/bin/python

def minor(matrix,y):
    return [[matrix[i][j] for j in range(0,len(matrix[i])) if j != y] for i in range(1,len(matrix))]
    
def determinant(matrix):
    if len(matrix) < 2:
        return matrix[0][0]
    elif len(matrix) == 2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
    while len(matrix) > 2:
        minor(matrix,y) = [[matrix[i][j] for j in range(0,len(matrix[i])) if j != y] for i in range(1,len(matrix))]
        return sum([(1 if y%2 == 0 else -1)*(matrix[0][y])*determinant(minor(matrix,y)) for y in range(0,len(matrix[0]))])
             
print determinant([ [2,5,3], [1,-2,-1], [1, 3, 4]])
```

#### 5.将minor()函数嵌套进determinant()。
```
#!/usr/bin/python

    
def determinant(matrix):
    if len(matrix) < 2:
        return matrix[0][0]
    elif len(matrix) == 2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
    def minor(matrix,y):return [[matrix[i][j] for j in range(0,len(matrix[i])) if j != y] for i in range(1,len(matrix))]
    while len(matrix) > 2:
        return sum([(1 if y%2 == 0 else -1)*(matrix[0][y])*determinant(minor(matrix,y)) for y in range(0,len(matrix[0]))])
             
print determinant([ [2,5,3], [1,-2,-1], [1, 3, 4]])
```
#### 6.可以直接将 minor() 嵌套进语句：
```
#!/usr/bin/python
    
def determinant(matrix):
    if len(matrix) < 2:
        return matrix[0][0]
    elif len(matrix) == 2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
    while len(matrix) > 2:
        return sum([(1 if y%2 == 0 else -1)*(matrix[0][y])*determinant([[matrix[i][j] for j in range(0,len(matrix[i])) if j != y] for i in range(1,len(matrix))]) for y in range(0,len(matrix[0]))])
             
print determinant([ [2,5,3], [1,-2,-1], [1, 3, 4]])
```
代码效果：
![屏幕快照 2018-05-24 下午9.03.39.png](https://upload-images.jianshu.io/upload_images/1136127-09048c023bb001e3.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

#### 7.可以直接 elif len(matrix) == 2这一步去掉：
```
#!/usr/bin/python

def determinant(matrix):
    if len(matrix) < 2: return matrix[0][0]
    while len(matrix) >= 2:
        return sum([(1 if y%2 == 0 else -1)*(matrix[0][y])*determinant([[matrix[i][j] for j in range(0,len(matrix[i])) if j != y] for i in range(1,len(matrix))]) for y in range(0,len(matrix[0]))])
            
print determinant([ [2,5,3], [1,-2,-1], [1, 3, 4]])
```

这个是我最为满意的一次编写算法过程。

###  其他解法：
解法一：
```
def determinant(m):
    a = 0
    if len(m) == 1:
        a = m[0][0]
    else:
        for n in xrange(len(m)):
            if (n + 1) % 2 == 0:
                a -= m[0][n] * determinant([o[:n] + o[n+1:] for o in m[1:]])
            else:
                a += m[0][n] * determinant([o[:n] + o[n+1:] for o in m[1:]])
                
    return a

```
解法二：
```
import numpy as np

def determinant(a):
    return round(np.linalg.det(np.matrix(a)))

```
解法三：
```
def determinant(matrix):
    return reduce(lambda r, i:r+(-1)**i*matrix[0][i]*determinant([m[:i]+m[i+1:] for m in matrix[1:]]),range(len(matrix[0])),0) if len(matrix) != 1 else matrix[0][0]

```
解法四：
```
from numpy.linalg import det
def determinant(matrix):
    return round(det(matrix))
```

解法五：
```
def determinant(m):
    return m[0][0] if len(m) == 1 else sum([n*determinant(map(lambda x: x[:i]+x[i+1:],m[1:]))*(-1)**i for i,n in enumerate(m[0])])

```
解法六：
```
def determinant(matrix):
    det = 0
    l=len(matrix)
    if(l==1):
        return matrix[0][0]
    for i in range(l):
        minor = [matrix[r][1:l] for r in range(l) if r!=i]
        det+=(1-i%2*2)*matrix[i][0]*determinant(minor)
    return det
```
解法七：
```
determinant = lambda m: m[0][0] if len(m) == 1 else sum([(1 if i % 2 == 0 else -1) * m[0][i] * determinant([[r[j] for j in range(len(r)) if j != i] for r in m[1:]]) for i in range(len(m))])

```


看了codewars 上大神的解法，的的确确有比我更好的解法。
想起来那句经典的话，**你考98分是实力只有这么多人家考100分是试卷只有这么多分。**

