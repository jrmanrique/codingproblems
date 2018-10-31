local sqrt = math.sqrt
local ceil = math.ceil

table.sum = function(list)
  sigma = 0
  for _, v in ipairs(list) do
    sigma = sigma + v
  end
  return sigma
end

function set(list)
  local _set = {}
  for _, v in ipairs(list) do _set[v] = true end
  return _set
end

function getDivisors(n)
  divisors = {}
  for i = 1, n - 1 do
    if n % i == 0 then
      divisors[#divisors + 1] = i
    end
  end
  return divisors
end

function isAbundant(n)
  return table.sum(getDivisors(n)) > n
end

limit = 28123

abundants = {}
for i = 1, limit do
  if isAbundant(i) then
    abundants[#abundants + 1] = i
  end
end

abundantSum = {}
check = set(abundants)
for j = 1, limit do
  for _, v in ipairs(abundants) do
    if check[j - v] then
      abundantSum[#abundantSum + 1] = j
      break
    end
  end
end

allSums = table.sum(abundantSum)
allNums = (limit * (limit + 1)) * (1 / 2)
print(allNums - allSums)
