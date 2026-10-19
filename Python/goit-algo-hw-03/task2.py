import random

def get_numbers_ticket(min, max, quantity):
  if min<1 or max>1000 or min>max:
    return []

  # if not (min<=quantity<=max):
  #   return []

  numbers_pool = range(min, max + 1)
  res = random.sample(numbers_pool, quantity)
  return sorted(res)

print(get_numbers_ticket(1, 49, 6))