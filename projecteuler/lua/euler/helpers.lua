local function set(list)
  local _set = {}
  for _, l in ipairs(list) do _set[l] = true end
  return _set
end

local function printTable(tbl)
  for i, v in ipairs(tbl) do
    print(i, v)
  end
end

-- Function index.

local M = {}

M.set = set
M.printTable = printTable

return M
