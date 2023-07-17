# Generat a list of random numbers:
#runif -> 30

random_numbers <- runif(30)

# Plot the random numbers
plot(random_numbers, type = "o", pch = 16, col = "blue",
     xlab = "Index", ylab = "Random Numbers",
     main = "Plot of 30 Random Numbers")

#rnorm -> 30

set.seed(123)  # Set seed for reproducibility
random_numbers <- as.integer(rnorm(30))

# Plot the random numbers
plot(random_numbers, type = "b", pch = 19, col = "red",
     xlab = "Index", ylab = "Value", main = "Random Numbers")

