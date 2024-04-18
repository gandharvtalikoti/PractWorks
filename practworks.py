import random

def generate_age_question():
    # Names for random selection
    names = ['Raunak', 'Mohini', 'Sushanth', 'Suma', 'Amit', 'Priya', 'John', 'Lily', 'Carlos', 'Maria']
    
    # Randomly picking two different names
    name1, name2 = random.sample(names, 2)
    
    # Randomly picking a reasonable multiplier for x (the base age unit)
    x = random.randint(5, 20)  # x is the multiplier, ensuring that ages are integers
    
    # Randomly picking ratios that are easy to handle (simple fractions)
    ratios = [(2, 1), (3, 2), (4, 3), (5, 3), (6, 1), (7, 5), (8, 3), (9, 4), (10, 3)]
    ratio1, ratio2 = random.choice(ratios)
    
    # Age calculation is based on these ratios
    age1 = ratio1 * x
    age2 = ratio2 * x
    
    # Randomly deciding how many years in the future we are considering
    years_after = random.randint(2, 10)
    
    # Calculating the sum of their ages after these years
    total_future_age = random.randint(40, 100)  # Total age in years_after years, ensures it is realistic and manageable
    # Making sure the sum after years results in an integer solution
    total_future_age -= (total_future_age - (age1 + age2 + 2 * years_after)) % (ratio1 + ratio2)

    question = (f"Question: The ages of {name1} and {name2} are in the ratio of {ratio1}:{ratio2}. "
                f"After {years_after} years, the sum of their ages will be {total_future_age} years. "
                "What is their age now?")
    
    # Calculating x from the future ages equation
    future_sum_equation = ratio1 * x + ratio2 * x + 2 * years_after
    # Ensuring the sum of future ages matches the given total future age
    x = (total_future_age - 2 * years_after) / (ratio1 + ratio2)
    
    # Recalculate exact ages based on new x
    age1 = ratio1 * x
    age2 = ratio2 * x
    
    answer = (f"Answer: Since the ages of {name1} and {name2} are in the ratio of {ratio1}:{ratio2} today, let their ages be {int(age1)} and {int(age2)} respectively.\n\n"
              f"Their individual ages after {years_after} years will be $ {int(age1)} + {years_after} $ and $ {int(age2)} + {years_after} $. "
              "It is given that the sum of their ages after {years_after} years will be {total_future_age}. Hence we have,\n\n"
              f"\\[ ({ratio1}x + {years_after}) + ({ratio2}x + {years_after}) = {total_future_age} \\]\n"
              f"\\[ {ratio1}x + {ratio2}x + {2*years_after} = {total_future_age} \\]\n"
              f"\\[ {ratio1 + ratio2}x = {total_future_age - 2 * years_after} \\]\n"
              f"\\[ x = \\frac{{{total_future_age - 2 * years_after}}}{{{ratio1 + ratio2}}} \\]\n"
              f"\\[ x = {x} \\]\n\n"
              f"Hence the age of {name1} is $ {ratio1} \\times {x} = {int(age1)} $ and the age of {name2} is $ {ratio2} \\times {x} = {int(age2)} $.")
    
    return question, answer

# Example use of the function
q, a = generate_age_question()
print(q)
print(a)
