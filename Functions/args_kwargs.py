'''
Example of function with positional and named arguments
'''

def describe_person(*args, **kwargs):
    """
    Function to describe a person with their name, age, and optional additional attributes.

    Args:
    - *args: Positional arguments. The first two arguments should be 'name' (str) and 'age' (int),
      and the rest can be any additional attributes.
    - **kwargs: Keyword arguments to describe extra attributes of the person.
      Possible kwargs include 'occupation', 'location', 'hobbies', etc.
    """
    if len(args) < 2:
        print("Error: At least 'name' and 'age' must be provided as positional arguments.")
        return

    name = args[0]
    age = args[1]

    print(f"Name: {name}")
    print(f"Age: {age}")

    for key, value in kwargs.items():
        print(f"{key.capitalize()}: {value}")


# Using only positional arguments
describe_person("Alice", 30)

# Using a mix of positional and named arguments
describe_person("Bob", 25, occupation="Engineer", hobbies=["Reading", "Hiking"])

# Using only named arguments
describe_person(name="Charlie", age=40, location="New York")
