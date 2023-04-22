
# x = int(input("Enter a 5 digit integer: "))
# digits = [int(n) for n in str(x)]
# rows = max(digits)
# bar_graph = []
# for row in range(rows, 0, -1):
#     bar_graph.append(['x' if digit >= row else ' ' for digit in digits])
# for row in bar_graph:
#     print(' '.join(row))
# print('-'*(2*len(digits)+3))

import os
import csv
print(os.getcwd()) 
folder = os.getcwd()
def importSalesData():
    fileName = folder + "\\matpattheory\\"+"sales.csv"

    sales_data=[]        
    with open(fileName, 'r') as rf:
        salesData = csv.reader(rf, delimiter=',')
        for row in salesData:
            sales_data.append(row[1])
    sales_data.remove('Sales')
    print(sales_data)
importSalesData()

    
importSalesData()
#	log10(n + 1) - log10(n)# possible ways to access column 2 


