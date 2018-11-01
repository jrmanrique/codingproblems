local function set(list)
  local s = {}
  for _, l in ipairs(list) do s[l] = true end
  return s
end

local function contains(tbl, e)
  for _, l in ipairs(tbl) do
    if l == e then return true end
  end
  return false
end

local function printTable(tbl)
  for i, v in ipairs(tbl) do
    print(i, v)
  end
end

local function printMatrix(tbl)
  for _, v in ipairs(tbl) do
    print(table.concat(v, '\t'))
  end
end

-- Function Index

local M = {}

M.set = set
M.contains = contains
M.printTable = printTable
M.printMatrix = printMatrix

return M
