#task1
from datetime import datetime, timedelta
    
x = datetime.now()
print(x - timedelta(days = 5))

#task2
from datetime import datetime, timedelta
    
print(datetime.now() - timedelta(days = 1))
print(datetime.now())
print(datetime.now() + timedelta(days = 1))

#task3
from datetime import datetime

x = datetime.now()
print(x.replace(microsecond = 0))

#task4
from datetime import datetime

d1 = datetime(2023, 5, 10, 8, 45, 0)
d2 = datetime(2022, 5, 10, 8, 45, 0)

difference = d1 - d2

result = difference.total_seconds()

print("Difference:", result)