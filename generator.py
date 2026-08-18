import random
import string

n=int(input("how long do you want your password to be"))

random_string="".join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=n))

print(random_string)
