import pandas as pd

# Definindo os dados básicos
data = {
    "username": [f"{i}s" for i in range(1, 1001)],
    "firstname": ["student"] * 1000,
    "lastname": [str(i) for i in range(1, 1001)],
    "email": [f"{i}email@uni.com" for i in range(1, 1001)],
    "password": ["moodle"] * 1000,
    "course1": ["m1"] * 1000,
    "type1": ["manual"] * 1000,
    "role1": ["student"] * 1000
}

# Criando o DataFrame
df = pd.DataFrame(data)

# Salvando em um arquivo CSV
file_path = "./usuarios.csv"
df.to_csv(file_path, index=False)

file_path
