# Custom exception class for ListDivide
class ListDivideException(Exception):
    pass

# Function to count elements in a list that are divisible by 'divide'
def list_divide(numbers, divide = 2):
    """
    Count the number of elements in the 'numbers' list that are divisible by 'divide'.

    :param numbers: A list of integers
    :param divide: An integer (default is 2)
    :return: Number of elements in the list divisible by 'divide'
    """
    
    count = 0 # Initialize a count variable to store the number of divisible elements

    for num in numbers:
        if num % divide == 0:
            count += 1  #Increment count if the element is divisible by 'divide'.
    return count

# Function to perform tests on list_divide
def test_List_divide():
    try:
        # Test 1: list_divide([1,2,3,4,5]) should return 2
        result = list_divide([1,2,3,4,5])
        print(f"Test 1 Passed: {result ==2}")

                # Test 2: list_divide([2,4,6,8,10]) should return 5
        result = list_divide([2, 4, 6, 8, 10])
        print(f"Test 2 Passed: {result == 5}")

        # Test 3: list_divide([30, 54, 63, 98, 100], divide=10) should return 2
        result = list_divide([30, 54, 63, 98, 100], divide=10)
        print(f"Test 3 Passed: {result == 2}")

        # Test 4: list_divide([]) should return 0
        result = list_divide([])
        print(f"Test 4 Passed: {result == 0}")

        # Test 5: list_divide([1,2,3,4,5], 1) should return 5
        result = list_divide([1, 2, 3, 4, 5], 1)
        print(f"Test 5 Passed: {result == 5}")
    except ListDivideException:
        print("A ListDivideException occurred!")

# Run the test function
test_List_divide()