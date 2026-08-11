#WAP to work with random package and print different random numbers using random(), choice(), randrange(), seed().
import random as r

nums = r.random()
print(nums)

list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

print("Random choice from list:", r.choice(list))

print("Random choice from another list:",
      r.choice((1, 2, 3, 4, 5, 6)))

print("Random number using randrange:",
      r.randrange(10, 50, 3))

print("Another number:", r.random())

r.seed(5)

print("After seed:", r.random())