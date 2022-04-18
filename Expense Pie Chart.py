#CS-175L
#Ryan Basile
#Expense Pie Chart

import matplotlib.pyplot as plt

values =[1000, 250, 350, 200, 375, 800]
slice_labels =['Rent', 'Gas', 'Food', 'Clothing', 'Car Payment', 'Misc']
plt.pie(values, labels=slice_labels)
plt.title('Monthly Expenses')
plt.show()
