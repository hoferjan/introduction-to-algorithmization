def permute(s):
  out = []
  if len(s) == 1:
    return s
  else:
    for i,let in enumerate(s):
      for perm in permute(s[:i] + s[i+1:]):
        out.append([let + [perm]])
  return out

print(permute([1,2,3]))