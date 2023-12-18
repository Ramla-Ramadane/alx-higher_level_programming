#!/usr/bin/python3
'''function that divides element by
element two lists'''


def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for indx in range(0, list_length):
        division = 0
        try:
            division = my_list_1[indx] / my_list_2[indx]
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        except TypeError:
            print("wrong type")
        finally:
            new_lst.append(division)
    return new_list
