function fib(n)
  local cache = {}
  
  local function _fib(m)
    if m < 2 then
      return m
    end

    if cache[m] then 
      return cache[m]
    else
      local r = _fib(m - 1) + _fib(m - 2)
      cache[m] = r
      return r
    end
  end

  return _fib(n)
end

maxima = 4 * 10^6

sigma = 0
i = 0
while fib(i) < maxima do
  if fib(i) % 2 == 0 then
    sigma = sigma + fib(i)
  end
  i = i + 1
end
print(sigma)