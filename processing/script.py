import pandas as pd

# Load the CSV file
file_path = 'importing.csv'
df = pd.read_csv(file_path, delimiter=';')

# Remove the columns "Inscrição" e "Oferta"
df = df.drop(columns=["Inscrição", "Oferta"])

# Split the "Nome" column into "firstname" and "lastname"
df[['firstname', 'lastname']] = df['Nome'].str.split(' ', 1, expand=True)
df = df.drop(columns=["Nome"])

# Rearrange and rename the columns
df = df[['CPF', 'firstname', 'lastname', 'Email', 'Senha']]
df.columns = ['username', 'firstname', 'lastname', 'email', 'password']

# Create the new columns
df['course1'] = 'psf'
df['type1'] = 'manual'
df['role1'] = 'student'

# Save the result to a new CSV file
output_path = 'output.csv'
df.to_csv(output_path, index=False)
