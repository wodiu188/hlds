
def findMedianSortedArrays(A,B):
    m = len(A)
    n = len(B)
    if m > n:
        return findMedianSortedArrays(B,A)

    iMin = 0
    iMax = m
    while iMin <= iMax:
        i = int((iMin + iMax) / 2)
        j = int((m + n + 1) / 2 - i)
        if (j != 0 and i != m and B[j-1] > A[i]):
            iMin = i + 1

        elif i != 0 and j != n and A[i-1] > B[j]:
            iMax = i - 1

        else:
            maxLeft = 0
            if i == 0:
                maxLeft = B[j-1]
            elif j == 0:
                maxLeft = A[i-1]
            else:
                maxLeft = max(A[i-1], B[j-1])
            if  (m + n) % 2 == 1:
                return maxLeft

            minRight = 0
            if i == m:
                minRight = B[j]
            elif j == n:
                minRight = A[i]
            else:
                minRight = min(B[j], A[i])
            return (maxLeft + minRight) / 2.0
    return 0.0





# 示例用法
nums1 = [284, 1152, 1159, 1419, 1440, 1517, 2044, 2452, 2755, 2880, 2975, 5455, 5870, 6001, 7124, 8611, 8613]
nums2 = [190, 1151, 2351, 3084, 3941, 4223, 4638, 4750, 4810, 5025, 5124, 6563, 6660, 7092, 7562, 7693, 8029, 8952, 9248, 9935]
result = findMedianSortedArrays(nums1, nums2)
print(result)  # 输出 2.0
