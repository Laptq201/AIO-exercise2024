def my_function(integers, number=1):
    if number in integers:
        return True
    else:
        return False
    
    

if __name__=="__main__":
    my_list = [1, 3, 9, 4]
    assert my_function(my_list, -1) == False
    my_list = [1, 2, 3, 4]
    print(my_function(my_list, 2))