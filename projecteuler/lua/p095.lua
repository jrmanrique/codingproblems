local helpers = require('lua/euler/helpers')
local mathtools = require('lua/euler/mathtools')


local ceil = math.ceil
local contains = helpers.contains
local properDivisors = mathtools.properDivisors


function sumDivisors(limit)
  local sieve = {}
  for i = 1, limit do
    sieve[i] = 0
  end

  for i = 1, ceil(limit / 2) do
    for j = 2 * i, limit, i do
      sieve[j] = sieve[j] + i
    end
  end

  return sieve
end

function getIndex(tbl, e)
  for i = 1, #tbl do
    if tbl[i] == e then
      return i
    end
  end
  return 1
end

local limit = 10 ^ 6

local sieve = sumDivisors(limit)
-- helpers.printTable(sieve)

result = 0
chainLength = 0

local seen = {}
for i = 1, limit + 1 do
  seen[i] = false
end

for i = 2, limit do
  if seen[i] then
    goto restart
  end
  
  chain = {}
  n = i
  broken = false

  while not contains(chain, n) do
    chain[#chain + 1] = n
    n = sieve[n]

    if n <= 1 then broken = true; break end
    if n > limit or seen[n] then
      broken = true
      break
    end
  end

  if not broken then
    smallest = math.huge
    first = getIndex(chain, n)

    if #chain - first > chainLength then
      for j = first, #chain do
        if chain[j] < smallest then
          smallest = chain[j]
        end
      end

      chainLength = #chain - first
      result = smallest
    end
  end

  for j = 1, #chain do
    seen[chain[j]] = true
  end
  :: restart ::
end

print('The smallest number in the longest chain is ' .. result .. '.')
