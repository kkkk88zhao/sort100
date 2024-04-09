import random

# 生成100个0至1000之间的随机整数
random_numbers = [random.randint(0, 1000) for _ in range(100)]

# 对生成的随机数列表进行排序
sorted_numbers = sorted(random_numbers)

# 输出排序后的随机数列表
print(sorted_numbers)
