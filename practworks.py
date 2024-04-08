import random
def generate_question_and_answer():
    # Generating random names
    names = ["Rahul", "Pratik", "Poornima", "Omkar", "Sushant", "Suma"]
    name1, name2 = random.sample(names, 2)

    # Generate random ratios
    numerator = random.randint(2,10)
    denominator = random.randint(2,10)

    #generate random number of years
    years = random.randint(1,10);

    # generate random value sum_of_ages 
    sum_of_ages = random.randint(40,100)

    #calculate x
    x = (sum_of_ages - 2*years)/(numerator+denominator)
