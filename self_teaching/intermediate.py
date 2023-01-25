#Following intermediate tutorials
#https://www.python-engineer.com/courses/advancedpython/

from multiprocessing import dummy
import sys
import timeit

class main():
    """Main program instance"""
    def __init__(self):
        pass
    def lists(self):
        """Listing your bitches. ERROR: Index out of range"""
        #Using 'list' as var name is not a good idea considering it's usually a function
        _list = ['banana', True, 5, 'banana']
        print(_list)

        alt_list = list() #creating list
        print(alt_list)

        item=_list[2]
        item=_list[-1] #Last item
        print(item)

        for i in _list:
            print(i)

        if True in _list:
            print('_list is positive')
        else:
            print('_list is negative')
        

        _list.append('lemon')
        print(_list)

        _list.insert(0, "first!")
        print(_list)

        print(_list.pop()) #bye bye lemon

        print(_list.remove(True))
        print(_list)

        _list.clear() #Remove everything

        _list = [1, 2, 3 ,4]
        _list.reverse()
        print(_list)

        _list.sort()
        print(_list)

        _list.reverse()
        sorted_list = sorted(_list)
        print("Original: " + str(_list))
        print("Sorted: " + str(sorted_list))
        print("Special Sorted: " + str(_list[::-1]))


        zero_list = [0] * 5
        print(zero_list)

        list_concat = zero_list + _list
        print(list_concat)

        string_list = list('Characters')
        print(string_list)

        #Reference to list. Modifying copylist will modify _list
        copylist = _list 

        #To create copy values to a new list, use the copy() function
        copylist = _list.copy()
        #Or those
        copylist = list(_list)
        copylist = _list[:] #More about this in Slicing

        #Slicing
        # a[start:stop:step], default step is 1
        a = [1,2,3,4,5,6,7,8,9,10]
        print(a[1:3]) #Should be 2 and 3 as the last index is not included 
        print(a[4:]) #From 5 (index 4) to end (10)
        print(a[:5]) #From start to unincluded 5th index
        a[0:3] = [0] * 3 #Replace indexes by value. If not *3, it replaces them all with one zero
        print(a)
        a[0:3] = [1, 2, 3]
        print(a)
        print(a[::2]) #Every 2 steps; In this case, it returns all odd numbers

        #Create new lists from a list
        a = list(range(1,11))
        print(a)
        b = [i * i for i in a] #sqr each number
        print(b)

        #Nested lists
        c = [a,b] #List contains lists
        print(c)
        print(c[0])

    def tuples(self):
        """Tuples of the morning"""
        #Tuples are similar to lists
        my_tuple = ("Max", 28, "New York")
        #Generally, we use lists to contain on data type and tuples to contain multiple
        #Iterating through a tuple is slightly faster
        #Tuples are immutables, meaning their elements cannot be changed once it is defined
        
        #Ways to create a tuple
        my_tuple = 25,
        my_tuple = (25,)
        my_tuple = ("Raph", 17, "Canada")
        my_tuple = "Audrey", 17, "Canada"
        my_tuple = tuple(range(1,6)) #Converting an iterable 
        print(my_tuple)

        my_tuple = "Audrey", 17, "Canada"
        country = my_tuple[-1]
        name = my_tuple[0]
        tuple_1 = name, country
        print(tuple_1)

        del tuple_1

        if 17 in my_tuple:
            print("Minor")
        else:
            print("You're all grown up!")

        my_tuple = ('a', 'b', 'b', 'c', 'f')
        print(my_tuple.count('b')) #How many items are equal to this value
        print(my_tuple.index('c')) #Index of the first item that is equal to that

        my_tuple = ('woman', 'let me be your woman') + ('woman',) * 3
        print(my_tuple)

        dummy_list = ['IMDUM!NAMOW'[::-1][0:6:] + ' I AM SMARTER!']
        smart_tuple = tuple(dummy_list)
        print(smart_tuple)
        del smart_tuple
        del dummy_list

        my_tuple = tuple(range(1,11))
        print("Countdown: " + str(my_tuple[::-1]))

        my_tuple = ("Raph", 17, "Canada")
        name, age, country = my_tuple
        print(name)
        print(age)
        print(country)

        my_tuple = tuple(range(-1,11))
        negative_number, *digits, natural_number = my_tuple
        print(negative_number)
        print(digits)
        print(natural_number)

        my_list = range(1, 11)
        my_tuple = tuple(range(1, 11))
        print(str(sys.getsizeof(my_list)) + " bytes")
        print(str(sys.getsizeof(my_tuple)) + " bytes")

        #Speed test
        print(timeit.timeit(stmt="[0, 1, 2, 3, 4, 5]", number=1000000))
        print(timeit.timeit(stmt="(0, 1, 2, 3, 4, 5)", number=1000000))

    def dicts(self):
        """All about dicts!"""
        #Two main ways of creating dicts
        my_dict = {"name":"Audrey", "age":17, "sex":0}
        my_dict = dict(name="Audrey", age=17, sex=0)
        print(my_dict)
        print(my_dict["name"])
        my_dict["gender"] = "W" #Adding a key is that easy
        print(my_dict)
        del my_dict["gender"]
        my_dict["gender"] = "W"
        print(my_dict.pop("gender"))
        if "gender" in my_dict:
            print(my_dict["gender"])
        else:
            tmp_var = my_dict["name"]
            print(f"Seems like {tmp_var} is non-binary.")
        for key in my_dict:
            print("A key from the dict: " + str(key))
        for value in my_dict.values():
            print(f"A value from the dict: {value}")
        for key,value in my_dict.items():
            print(f"A pair from the dict: {key};{value}")
        
        #Like lists, dict2 = dict 1; dict2 is only a reference to dict1, not a new dict.
        #That's why you can use dict.copy()
        my_dict_copy = my_dict.copy()
        my_dict_copy["copy"] = True
        print(my_dict)
        print(my_dict_copy)

        #Merging
        my_dict.update(dict(city="Montreal", status="single"))
        print(my_dict)

        #You can use numbers as keys, but they will not count as indices
        my_dict = {1:2,3:4,5:6}
        print(my_dict[1])
        #my_dict[0] won't give the first pair

        #dicts only take immutable elements
        #for that reason, you cannot put a list in there
        #you're better off using tuples
        mytuple = 12, 2, 4
        my_dict = {mytuple:"pair"}
        print(my_dict)
        #you can still use dictionnaries in lists however

    def sets(self):
        """Ready? Sets? Go! I'm so funny!"""
        #a set is an unordered data type that is unindexed, mutable and cannot contain duplicate elements
        my_set = {"Yuri", "Monika", "Natsuki", "Sayori"}
        #You can also create a set with set()
        #An empty set must be created with the function, not just {} (or it'll be an empty dict)
        my_set.add("Libitina")
        print(my_set)
        #As you can see, the order varies on each execution. That's because a set is unordered
        my_set.add("Yuri") #Adding an existing item isn't possible
        print(my_set)

        #You can remove an item by two methods
        my_set.remove("Monika") #Raises error if item does not exist
        my_set.discard("Monika") #Does nothing if item does not exist
        #In both cases, it attempts to remove the specified item. lol fuck Monika
        #

_x = main()
_x.sets()
