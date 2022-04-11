import math
import datetime
from decimal import Decimal
start=datetime.datetime.now()
for i in range(450,460+1):
    print(Decimal(i).ln() /Decimal(10).ln())
end=datetime.datetime.now()
print("Total time taken is: ",end-start," milli seconds")
