local helpers = require('lua.euler.helpers')

local sqrt = math.sqrt
local ceil = math.ceil
local set = helpers.set

local function sieveOfAtkin(limit)
  sieve = {}
  for i = 1, limit do
    sieve[i] = false
  end

  for x = 1, ceil(sqrt(limit)) do
    for y = 1, ceil(sqrt(limit)) do
      n = 4 * x ^ 2 + y ^ 2
      if n <= limit and set({1, 13, 17, 29, 37, 41, 49, 53})[n % 60] then
        sieve[n] = not sieve[n]
      end

      n = 3 * x ^ 2 + y ^ 2
      if n <= limit and set({7, 19, 31, 43})[n % 60] then
        sieve[n] = not sieve[n]
      end

      n = 3 * x ^ 2 - y ^ 2
      if x > y and n <= limit and set({11, 23, 47, 59})[n % 60] then
        sieve[n] = not sieve[n]
      end
    end
  end

  for n = 1, ceil(sqrt(limit)) do 
    if sieve[n] then
      k = 1
      while k * n ^ 2 <= limit do
        sieve[k * n ^ 2] = false
        k = k + 1
      end
    end
  end

  results = {2, 3, 5}
  for n = 1, limit do
    if sieve[n] then
      table.insert(results, n)
    end
  end
  
  return results
end

-- Function index.

local M = {}

M.sieveOfAtkin = sieveOfAtkin

return M
