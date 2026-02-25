"""Exercise 3
Retrieve and operate on tasks from https://jsonplaceholder.typicode.com/todos.
Get the task list as JSON from the preceding API URL.
Save the data to two local files, one that contains completed tasks and another one that contains incomplete tasks.
The JSON data written to the files should be formatted as minimally as possible (no spaces, newlines, etc).
The program should display the number of tasks we have completed. Sample output:
90 of 200 tasks are done"""

import requests
import json

url = "https://jsonplaceholder.typicode.com/todos"
resposta = requests.get(url) #vai no site e coleta os dados JSON e a variavel(resposta) recebe esses dados

lista_de_tarefas = resposta.json() #O comando json() transforma tudo coletado e coloca nessa lista, que contém dicionarios com cada um tendo pares-valores

completas = []
incompletas = []

for tarefa in lista_de_tarefas: #tarefa é o indíce do dicionario naquela posição ex: 0 = {chave:valor}
    
    if tarefa["completed"] == True:
        completas.append(tarefa)
    else:
        incompletas.append(tarefa)

with open("completas.json","w") as completajs:
    json.dump(completas,completajs,separators=(',', ':'))  
    
with open("incompletas.json","w") as incompletasjs:
    json.dump(incompletas,incompletasjs,indent="\t")

print(f"O numero de tarefas concluidas é {len(completas)} de {len(completas) + len(incompletas)}")