import copy
nums1 = [10, 20, 30, 40]
nums2 = copy.copy(nums1)
nums2[3] = 99

print(nums1) # [10, 20, 30, 40]
print(nums2) # [10, 20, 30, 99]

# 浅拷贝存在的问题：嵌套数据任是共享的
nums1 = [10, 20, 30, [40, 50]]
nums2 = copy.copy(nums1)
nums2[3][0] = 99

print(nums1[3][0]) # 99
print(nums2[3][0]) # 99



nums1 = [10, 20, 30, [40, 50]]
nums2 = copy.deepcopy(nums1)
nums2[3][0] = 99

print(nums1[3][0])
print(nums2[3][0])