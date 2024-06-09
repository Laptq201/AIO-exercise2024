def my_function(n):
    max_num = n[0]
    for i in n:
        if i > max_num:
            max_num = i
    return max_num

if __name__ =="__main__":
    my_list = [1001, 9, 100, 0]
    assert my_function(my_list) == 1001
    my_list = [1, 9, 9, 0]
    print(my_function(my_list))