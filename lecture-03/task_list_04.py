def work(function, parameter):
    try:
        function(parameter)
    except Exception as e:
        print(e)


a = 42
b = 'Hello world!'
c = [1, 3, 5, 7]
my_list = [None]
work(my_list.extend, a)
print(my_list)
work(my_list.extend, b)
print(my_list)
work(my_list.extend, c)
print(my_list)
work(my_list.extend, my_list)
print(my_list)
