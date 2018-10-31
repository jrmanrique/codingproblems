local mathtools = require('lua.euler.mathtools')
local helpers = require('lua.euler.helpers')

limit = 10 ^ 6
primes = mathtools.sieveOfAtkin(limit)
primeSet = helpers.set(primes)

maxima = 0
while #primes > 0 do
  sigma = 0
  count = 0
  for _, p in ipairs(primes) do
    sigma = sigma + p
    count = count + 1
    if primeSet[sigma] and count > maxima then
      maxima = count
      print(sigma)
    end
    if sigma >= limit then
      break
    end
  end
  table.remove(primes, 1)
end
