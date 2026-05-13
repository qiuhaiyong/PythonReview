# 1. 给参数和返回值加类型注解
def add(x: int, y: int) -> int:
    return x + y


# 2.带默认值的参数，可以不写注解
def add(x = 1 , y = 1) -> int:
    return x + y


# 3.设置多个返回值的类型注解
def show_nus_info(nums: list[int])-> tuple[int,...]:
    max_v = max(nums)
    min_v = min(nums)
    return max_v, min_v

# 4. 可变参数类型注解
# 设置 *args 的类型注解，要求 args 中的每个参数都必须是 int 类型
def add(*args: int) -> int:
    return sum(args)

# 设置 **kwargs 的类型注解，要求 kwargs 中的每组参数的值，必须是 str 或 int 类型
def show_info(**kwargs: str | int):
    print(kwargs)