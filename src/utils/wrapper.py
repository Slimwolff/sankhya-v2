import os
import tomllib

# Diretório base do projeto (assumindo que 'wrapper.py' está em 'src/utils/')
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Sobe para 'src/'

print(BASE_DIR)

# Caminho absoluto do arquivo TOML
CONFIG_PATH = os.path.join(BASE_DIR, "config", "config.toml")

# Abre o arquivo
# with open(CONFIG_PATH, mode="rb") as fp:
#     config = tomllib.load(fp)

# print(config)