income=45000
print(f"The income given is given as: {income}.")
print("The first 10,000 is tax free.")
print("The next 10,000 is taxed at 10%.")
print("The remaining income is taxed at 20%.")
print()
print("From the income of 45000, the first income of 10,000 is tax free while the next income of 10,000 is taxed at 10% and the final 25,000 is taxed at 20%.")
second_income=(10*10000)/(100)
last_income=(20*25000)/(100)
total_income=second_income+last_income
print(f"The total amount from tax is given as: " , total_income)