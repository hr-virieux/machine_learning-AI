# create the initial variables below
age = 28
sex = 0  # 0 for female, 1 for male
bmi = 26.2
num_of_children = 3
smoker = 0  # 0 for non-smoker, 1 for smoker

# Add insurance estimate formula below
insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
#print("This person's insurance cost is " + str(insurance_cost) + " dollars")

# Age Factor
age += 4

new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
change_in_insurance_cost = new_insurance_cost - insurance_cost
#print("The change in cost of insurance after increating the age by 4 years is "+str(change_in_insurance_cost) + " dollars")

# BMI Factor
age -= 4
bmi += 3.1

new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
change_in_insurance_cost = new_insurance_cost - insurance_cost
#print("The change in cost of insurance after increating BMI by 3.1 is "+str(change_in_insurance_cost) + " dollars")

# Male vs. Female Factor
bmi -= 3.1
sex = 1

new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
change_in_insurance_cost = new_insurance_cost - insurance_cost
#print("The change in estimated cost for being male instead of female is "+str(change_in_insurance_cost) + " dollars")
