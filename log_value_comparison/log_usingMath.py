import math
import datetime
from decimal import Decimal
start=datetime.datetime.now()
for i in range(1,1000000):
    #print(i ," - ",
    math.log(i,10)
end=datetime.datetime.now()
print("Total time taken is: ",end-start," milli seconds")
