X = 18
print(f"jeremias tem %d anos" %X)

X = 18
print("[%d]"% X)
print("[%03d]" % X)
print("[%3d]" % X)
print("[%-3d]" % X)
print("[%-3d]" % X)

print("%5f" % X)
print("%5.2f" % X)
print("%10.52f"% X)

nome = "jeremias"
idade = 18
Salário = 90.31
print("%s tem %d anos e R$%f no bolso." % (nome, idade, Salário))
print("%-12s tem %-3d anos e R$%-5.2f no bolso." % (nome, idade, Salário))