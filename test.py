import re

s = "Nota(s) com frete incluso.Não é possível vincular o CT-e com esta(s) nota(s) Nro(s) Únicos(s): 149692, 157279, 157694, 157695, 157696, 157706, 158233, 158231, 158302"

x = re.search(r":\s*7[0-9]", s)

print(x.group())