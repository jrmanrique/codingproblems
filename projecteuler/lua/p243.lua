local max = math.max
local min = math.min

function gcd(a, b)
  i = max(a, b)
  j = min(a, b)

  while i ~= 0 and j ~= 0 do
    i, j = j, i % j
  end

  if i == 0 then
    return j
  elseif j == 0 then
    return i
  end
end

function phi(n)
  count = 0
  for i = 1, n do
    if gcd(i, n) == 1 then
      count = count + 1
    end
  end
  return count
end

function isPrime(n)
  if n == 2 or n == 3 then return true end
  if n % 2 == 0 or n % 3 == 0 then return false end

  i = 5
  w = 2
  while i * i <= n do
    if n % i == 0 then return false end
    i = i + w
    w = 6 - w
  end
  return true
end

function resilience(n)
  return phi(i) / (i - 1)
end

function solver(limit)
  i = 2
  while resilience(i) >= limit do
    i = i + 1
  end
  return i
end

print(solver(15499 / 94744))
