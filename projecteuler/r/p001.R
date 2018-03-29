total <- 0
i <- 0
while (i < 1000) {
  i <- i + 1
  if (i %% 3 == 0 | i %% 5 == 0) {
    total <- total + i
  }
}
print(total)