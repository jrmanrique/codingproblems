function reverseSum(n)
  return n + string.reverse(n)
end

function isAllOdd(n)
  for digit in string.gmatch(math.floor(n), '%d') do
    if digit % 2 == 0 then
      return false
    end
  end
  return true
end

count = 0
for i = 1, 10 ^ 9 do
  if i % 10 ~= 0 and isAllOdd(reverseSum(i)) then
    count = count + 1
  end
end
print(count)
