#!/usr/bin/python3
'''function that divides element by
element two lists'''


def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(0, list_lenght):
        division = 0
        try:
            division = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            new_list.append(division)
    return (new_list)
