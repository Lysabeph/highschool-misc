# The upper range limit constant
CON = 20000

# Returns the sum of the factors of any whole number, n.
def get_factor_sum(n):
    factors = [1] # Includes 1.
    f = 2
    # Stops looping once n is divided by itself. (n/n = 1)
    while n/f > 1:
        # When n is divided by a, if the remainder is 0, a is a factor (n MOD a).
        if n%f == 0:
            factors.append(f) # Adds f to the list of factors.
        f += 1 # Increaments f to find all factors of n.
    return sum(factors) # Adds all the factors together.

fact_sum = {}

# Loops through the range and populates a dictionary with keys of the integers
# and values of the sum of the factors.
for i in range(2, CON):
    summ = get_factor_sum(i) # The sum of the factors of i.
    
    if summ < CON: # If sum of the factors is greater than CON, it isn't needed.
        fact_sum[i] = int(summ) # Adds the sum to the dictionary with its key.
        
    else:
        fact_sum[i] = 0 # Populates the integers with sums greater than 20000.

pairs = []

# Finds all dictionary keys with the same value as anther key's value.
for i in range(2, CON):
    for j in range(2, CON):
        if fact_sum[j] == i:
            pairs.append([i, fact_sum[i], j, fact_sum[j]])

# Removes false pairs
for pair in pairs:
    if len(set(pair)) == 2:
            #if pair.count(list(set(pair))[0]) == 2:
            print(pair)
