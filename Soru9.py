import time


start_time = time.time()



def pythagorean_triplet():
 for a in xrange(1,1000):
  for b in xrange(1,1000):
   c = 1000-a-b
   if (a**2+b**2) == c**2:
    return a*b*c


print pythagorean_triplet()


end_time = time.time()


print end_time - start_time
