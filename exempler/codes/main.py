import numpy as np

num_vectors = 1000000
vector_size = 3

# Generate random vectors
random_vectors = np.random.choice([0, 1], size=(num_vectors, vector_size), p=[0.5, 0.5])

# Prob of getting all heads
all_heads = np.sum(random_vectors.all(axis=1))
probability_all_heads = all_heads / num_vectors

print("Probability of getting all ones:", probability_all_heads)

# Prob of getting atleast two heads
at_least_two_heads = np.sum(np.sum(random_vectors, axis=1) >= 2)
probability_at_least_two_heads = at_least_two_heads / num_vectors

print("Probability of getting at least two ones:", probability_at_least_two_heads)

