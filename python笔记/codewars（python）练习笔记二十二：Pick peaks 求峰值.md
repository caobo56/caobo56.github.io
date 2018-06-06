# codewars（python）练习笔记二十二：Pick peaks(求峰值)
### 题目
In this kata, you will write a function that returns the positions and the values of the "peaks" (or local maxima) of a numeric array.

For example, the array arr = [0, 1, 2, 5, 1, 0] has a peak at position 3 with a value of 5 (since arr[3] equals 5).

The output will be returned as an object with two properties: pos and peaks. Both of these properties should be arrays. If there is no peak in the given array, then the output should be {pos: [], peaks: []}.

Example: pickPeaks([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 3]) should return {pos: [3, 7], peaks: [6, 3]} (or equivalent in other languages)
All input arrays will be valid integer arrays (although it could still be empty), so you won't need to validate the input.

The first and last elements of the array will not be considered as peaks (in the context of a mathematical function, we don't know what is after and before and therefore, we don't know if it is a peak or not).

Also, beware of plateaus !!! [1, 2, 2, 2, 1] has a peak while [1, 2, 2, 2, 3] does not. In case of a plateau-peak, please only return the position and value of the beginning of the plateau. For example: pickPeaks([1, 2, 2, 2, 1]) returns {pos: [1], peaks: [2]} (or equivalent in other languages)

题目大意：
求出数组的峰值和峰值对应的位置。
例如：[3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 3]
![屏幕快照 2018-05-28 下午5.31.21](https://dn-dn-caobo.qbox.me/屏幕快照 2018-05-28 下午5.31.21.png)
去除左右两端的峰值之后，发现峰值的位置出现在6，3 两个值，其对应的位置为 3，7.那么，应该输出的是 {pos: [3, 7], peaks: [6, 3]} 。
注意：
1. 入参为integer数组，不用验证数组
2. 峰值，则输出 {pos: [], peaks: []} 
3. 两端的峰值
4.  [1, 2, 2, 2, 1] 有峰值而 [1, 2, 2, 2, 3] 没有。 [1, 2, 2, 2, 1]的峰值为 {pos: [1], peaks: [2]} .

#### Sample Tests:
```
Test.it('should support finding peaks')
Test.assert_equals(pick_peaks([1,2,3,6,4,1,2,3,2,1]), {"pos":[3,7], "peaks":[6,3]})

Test.it('should support finding peaks, but should ignore peaks on the edge of the array')
Test.assert_equals(pick_peaks([3,2,3,6,4,1,2,3,2,1,2,3]), {"pos":[3,7], "peaks":[6,3]})

Test.it('should support finding peaks; if the peak is a plateau, it should only return the position of the first element of the plateau')
Test.assert_equals(pick_peaks([3,2,3,6,4,1,2,3,2,1,2,2,2,1]), {"pos":[3,7,10], "peaks":[6,3,2]})

Test.it('should support finding peaks; if the peak is a plateau, it should only return the position of the first element of the plateau')
Test.assert_equals(pick_peaks([2,1,3,1,2,2,2,2,1]), {"pos":[2,4], "peaks":[3,2]})

Test.it('should support finding peaks, but should ignore peaks on the edge of the array')
Test.assert_equals(pick_peaks([2,1,3,1,2,2,2,2]), {"pos":[2], "peaks":[3]})
```

### 我的解法

```
#!/usr/bin/python

def pick_peaks(arr):
    pos = [] 
    peaks = []
    for i in range(0,len(arr)):
        if i == 0 or i == len(arr)-1:
            pass
        elif arr[i] > arr[i-1] and arr[i] > arr[i+1]:
            pos.append(i)
            peaks.append(arr[i])
        elif arr[i] > arr[i-1] and arr[i] == arr[i+1]:
            for j in range(i,len(arr)):
                if arr[j] < arr[i]:
                    pos.append(i)
                    peaks.append(arr[i])
                if arr[j] != arr[i]:
                    i = j
                    break
    return {"pos":pos,"peaks":peaks}

```

### 照例，codewar 上的高赞解法：

```
def pick_peaks(arr):
    peak, pos = [], []
    res = { "peaks":[], "pos":[] }
    for i in range(1, len(arr)) :
        if arr[i]>arr[i-1] :
            peak, pos = [arr[i]], [i]
        elif arr[i]<arr[i-1] :
            res["peaks"] += peak
            res["pos"] += pos
            peak, pos = [], []
    return res
```
的确，这是一个压栈出栈的思路，我没想清楚。

