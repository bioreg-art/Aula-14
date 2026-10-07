import pandas as pd

df = pd.read_csv(r"C:\Users\regina.alvarenga\Downloads\funcionarios.csv")

print(df.iloc[0:5, 0:3])

salario = df.query("salario > 3000 and ativo== True")

print(salario)

