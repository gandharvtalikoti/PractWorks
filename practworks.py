import random

def generate_age_question():
    # Names for random selection
    names = ['Raunak', 'Mohini', 'Sushanth', 'Suma', 'Amit', 'Priya', 'John', 'Lily', 'Carlos', 'Maria']
    
    # Randomly picking two different names
    name1, name2 = random.sample(names, 2)
    
    # Randomly picking ratios that are easy to handle (simple fractions)
    ratios = [(2, 1), (3, 2), (4, 3), (5, 3), (6, 1), (7, 5), (8, 3), (9, 4), (10, 3)]
    ratio1, ratio2 = random.choice(ratios)
    
    # Randomly deciding how many years in the future we are considering
    years_after = random.randint(2, 10)
    
    # Generate a base age multiplier x
    x = random.randint(5, 20)  # Base multiplier for ages to ensure ages are integers

    # Calculate the exact ages using ratios
    age1 = ratio1 * x
    age2 = ratio2 * x
    
    # Setting the total future age such that it is a realistic value and fits the equation exactly
    total_future_age = age1 + age2 + 2 * years_after

    question = (f"Question: The ages of {name1} and {name2} are in the ratio of {ratio1}:{ratio2}. "
                f"After {years_after} years, the sum of their ages will be {total_future_age} years. "
                "What is their age now?")
    
    answer = (f"Answer: Since the ages of {name1} and {name2} are in the ratio of {ratio1}:{ratio2} today, let their ages be {age1} and {age2} respectively.\n\n"
              f"Their individual ages after {years_after} years will be $ {ratio1}x+ {years_after} $ and $ {ratio2}x+ {years_after} $."
              f"It is given that the sum of their ages after {years_after} years will be {total_future_age}. Hence we have,\n\n"
              f"\\[ ({ratio1}x + {years_after}) + ({ratio2}x + {years_after}) = {total_future_age} \\]\n"
              f"\\[ {ratio1 + ratio2}x + {2*years_after} = {total_future_age} \\]\n"
              f"\\[ {ratio1 + ratio2}x = {total_future_age - 2*years_after} \\]\n"
              f"\\[ x = \\frac{{{total_future_age - 2 * years_after}}}{{{ratio1 + ratio2}}} \\]\n"
              f"\\[ x = {x} \\]\n\n"
              f"Hence the age of {name1} is $ {ratio1} \\times {x} = {age1} $ and the age of {name2} is $ {ratio2} \\times {x} = {age2} $.")
    
    return question, answer

# Example use of the function
q, a = generate_age_question()
print(q)
print(a)
