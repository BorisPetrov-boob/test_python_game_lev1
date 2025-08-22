

def say_hello(name):
    print (f"Hello,{name}")

# вместо декоратора создаем функцию обертку
def repeat_func(func, num_times, *args, ** kwargs):
    for _ in range(num_times):
        func(*args, **kwargs)


# вызываем функцию через обертку

repeat_func(say_hello,3, "Alice")
