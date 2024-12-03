import random

random.randint(1, 6)  # 返回[a,b]之间的整数
random.randrange(1, 6, 2)  # 返回[a,b)之间的整数,步长为2
random.choice(range(1, 7))  # 返回iterable之间的整数
random.choices(range(1, 4), [4, 2, 1], k=20)  # 返回iterable之间的整数，权重为4:2:1，采样数为k个，返回list
random.shuffle(list(range(1, 7)))  # 打乱list里的元素，返回list，返回值None
random.sample(range(1, 7), 3)  # 返回iterable之间的整数，不重复，采样数为3个，返回list
