
a = str(input())

if a.isalpha():
  print("kata")
elif int(a) > 0:
  print("bilangan bulat positif")
elif int(a) < 0:
  print("bilangan bulat negatif")
else:
  print("nol")