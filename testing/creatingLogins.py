import pandas as pd

# Definindo os dados básicos
data = {
    "username": [f"{i}s" for i in range(1, 1001)],
    "password": ["moodle"] * 1000,
}

# Criando o DataFrame
df = pd.DataFrame(data)

# Salvando em um arquivo CSV
file_path = "./login.csv"
df.to_csv(file_path, index=False)

file_path
