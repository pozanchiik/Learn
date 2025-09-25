# Ввід значень
x1 = input("x1 = ") == "True"
x2 = input("x2 = ") == "True"
x3 = input("x3 = ") == "True"

# Умови згідно з таблицею 01011100
is_virus_cond_1 = (not x1) and (not x2) and x3
is_virus_cond_2 = (not x1) and x2 and x3
is_virus_cond_3 = x1 and (not x2) and (not x3)
is_virus_cond_4 = x1 and (not x2) and x3

# Перевірка на вірус
has_virus = is_virus_cond_1 or is_virus_cond_2 or is_virus_cond_3 or is_virus_cond_4

print("Файл має вірус:", has_virus)
