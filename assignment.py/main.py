from greet import greet
from functions import services
from calc import consultation
hello=greet()
total=services()
consult=consultation()
final_total=total+consult
print("TOTAL:", final_total)



