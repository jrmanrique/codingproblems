fibonacci <- function(n) {
  if (n == 1 || n == 2) {
    return(1)
  }
  
  cache <- integer(n)
  cache[1:2] <- 1

  calc <- function(n) {
    if (cache[n] != 0) {
      return(cache[n])
    }
    cache[n] <<- calc(n - 1) + calc(n - 2)
    cache[n]
  }

  calc(n)
}

fibs <- numeric()

total <- 0
i <- 1
while (fibonacci(i) < 4000000) {
  if (fibonacci(i) %% 2 == 0) {
    total <- total + fibonacci(i)
  }
  i <- i + 1
}

print(total)
