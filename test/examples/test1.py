
# Nested Dictionary
my_details = {'Employee': {'Dave': {'Salary': '2500', 'ID': '001', 'Designation': 'Team Lead'},
                           'Joe': {'Salary': '40000', 'ID': '002', 'Designation': 'Associate'}}}
print(my_details)



import pandas as pd

df = pd.DataFrame(my_details['Employee'])
print(df)


