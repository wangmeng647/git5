import re
text = 'qwedas qweqwasd rqweq'
res = re.findall(r"[a-zA-Z0-9]+", text)
print(list(res))
ls = [1,2,3,4]
se = {1,2}
res = list(filter(lambda x: x in se, ls))
print(res)