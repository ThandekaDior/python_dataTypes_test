def create_squares_of_evens():
    """
    Task:
    - Create a list of squares for all even numbers from 1 to 20 using list comprehension.
    
    Return:
    - The list of squares of even numbers.
    """
    squares = []
    for i in range(1,20):
        if i % 2 == 0:
            x = i ** 2
            squares.append(x)
    return squares[:5]
    #pass


def convert_to_dict(students):
    """
    Task:
    - Convert the list of student tuples into a dictionary where the name is the key and the grade is the value.
    
    Return:
    - The dictionary created from the list of students.
    """
    students_dict = dict(students)
    return students_dict
    #pass


def access_value_x(nested):
    """
    Task:
    - Access the value of 'x' from the nested dictionary `nested = {'a': [1, 2, 3], 'b': (4, 5), 'c': {'x': 10, 'y': 20}}`.
    
    Return:
    - The value of 'x' (which is 10).
    """
    return nested['c']['x']
    #pass


def append_to_list_in_dict(nested):
    """
    Task:
    - Append the value 6 to the list under key 'a' in the nested dictionary `nested = {'a': [1, 2, 3], 'b': (4, 5), 'c': {'x': 10, 'y': 20}}`.
    
    Return:
    - The updated dictionary.
    """
    nested['a'].append(6)
    return nested
    #pass


def convert_tuple_to_list_and_append(nested):
    """
    Task:
    - Convert the tuple under key 'b' in the nested dictionary into a list and add the value 6 at the end.
    
    Return:
    - The updated dictionary.
    """
    to_list = list(nested['b'])
    to_list.append(6)
    nested['b'] = to_list
    return nested
print(convert_tuple_to_list_and_append({'a': [1, 2, 3], 'b': (4, 5), 'c': {'x': 10, 'y': 20}}))
    #pass
