import random
def generate_question_and_answer():
    """to handle the situation in line number 22 i have adjusted the problem parameters until the ages can be expressed as whole numbers.
        For instance, you could try different ratios, different numbers of years, or different sums of ages after those years until you find a combination that results in whole numbers for the ages.
        So i have used while loop till i get correct set of random values so that it computes upto to a whole number result
        """
    while True:
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
        """intiution: 
        Age is typically considered as a whole number, and it doesnt make sense for someones age 
        to be in fractions
        """
        if x.is_integer(): # check if x is a whole number
            break

    age1_now = int(numerator*x)
    age2_now = int(denominator*x)

    # printing formatted question
    question = f"The ages of {name1} and {name2} are in the ratio of {numerator}:{denominator}. After {
        years} years, the sum of their ages will be {sum_of_ages} years. What is their age now?"
    
    # print(question)
    # Printing formatted answer
    answer = f"Since the ages of {name1} and {name2} are in the ratio of {numerator}:{
        denominator} today, let their ages be {numerator}x and {denominator}x respectively.\n"
    answer += f"Their individual ages after {years} years will be $ {
        numerator}x + {years} $ and $ {denominator}x + {years} $.\n"
    answer += f"It is given that the sum of their ages after {
        years} years will be {sum_of_ages}. Hence we have,\n"
    answer += f"\\[ {numerator}x + {years} + {denominator}x + {years} = {sum_of_ages} \\]\n"
    answer += f"\\[ {numerator + denominator}x + {2 *
                                                  years} = {sum_of_ages} \\]\n"
    answer += f"\\[ {numerator +
                     denominator}x = {sum_of_ages} - {2*years} \\]\n"
    answer += f"\\[ {numerator + denominator}x = {sum_of_ages - 2*years} \\]\n"
    answer += f"\\[ x = \\frac{{{sum_of_ages - 2 *
                                 years}}}{{{numerator + denominator}}} \\]\n"
    answer += f"\\[ x = {x} \\]\n"
    answer += f"\nHence the age of {name1} is $ {int(numerator)} \\times {int(x)} = {
        age1_now} $ and the age of {name2} is $ {int(denominator)} \\times {int(x)} = {age2_now} $."
    
    return question, answer


question, answer = generate_question_and_answer()
print("Question: ", question)
print("Answer: ", answer)