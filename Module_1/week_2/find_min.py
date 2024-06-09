def my_function(n):
    min_num = n[0]
    for i in n:
        if i < min_num:
            min_num = i
    return min_num
if __name__=="__main__":
    my_list = [1, 22, 93, -100]
    assert my_function(my_list) == -100
    my_list = [1, 2, 3, -1]
    print(my_function(my_list))