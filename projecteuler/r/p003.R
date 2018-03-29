primefactors <- function(num) {
  factors <- numeric()
  while (num > 1) {
    for (div in 2:num) {
      if (num %% div == 0) {
        num <- num %/% div
        factors <- c(factors, div)
        break
      }
    }
  }
  return(factors)
}

# Full input '600851475143' to large to be vectorized.
ans <- primefactors(600851475)
print(ans)