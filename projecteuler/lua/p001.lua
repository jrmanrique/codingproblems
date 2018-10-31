function sum35(n)
  sigma = 0
  for i = 1, n - 1 do
    if i % 3 == 0 or i % 5 == 0 then
      sigma = sigma + i
    end
  end
  return sigma
end

print(sum35(1000))