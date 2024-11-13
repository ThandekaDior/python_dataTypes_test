def int_division():
    """
    Task:
    - Perform integer division of 7 by 2.
    
    Return:
    - The result of the division (integer).
    """
    a = 7
    b = 2
    return a // b


def float_multiplication():
    """
    Task:
    - Multiply 3.0 by 2.
    
    Return:
    - The result of the multiplication (float).
    """
    a = 3.0
    b = 2
    return a * b


def combine_operations():
    """
    Task:
    - Add the result of integer division and multiplication.
    
    Return:
    - The combined result (float).
    """
    division = int_division()
    multiplication = float_multiplication()
    result = division + multiplication/2
    return result


def extract_word():
    """
    Task:
    - Extract the word 'awesome' from the string 'Python is awesome!'.
    
    Return:
    - The extracted word ('awesome').
    """
    string = 'Python is awesome !'
    string2 = string.split(' ')
    return string2[2]


def to_lowercase():
    """
    Task:
    - Convert the string 'Python is awesome!' to lowercase.
    
    Return:
    - The lowercase version of the string.
    """
    string = 'Python is awesome!'
    return string.lower()


def count_o():
    """
    Task:
    - Count how many times the letter 'o' appears in the string 'Python is awesome!'.
    
    Return:
    - The count of the letter 'o'.
    """
    string = 'Python is awesome!'
    count = 1
    if 'o' in string:
        count += 1
    return count

def evaluate_boolean():
    """
    Task:
    - Evaluate the expression 'not (5 > 3) and (10 == 5 * 2)'.
    
    Return:
    - The boolean result of the expression.
    """
    if not (5 > 3) and (10 == 5 * 2) is True:
        return True
    else:
        return False
