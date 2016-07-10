#!/usr/bin/env python3
#   Arquivo principal do trabalho final de CPD
#   E: Arquivo de texto com links do youtube 
#   S: Arquivos binario com dados e um arquivo de texto 

import os
from CSV_ import *
from open_csv import *
from write_bin_file import *
#===============================
#   functions
#===============================
# switch => selecao dos comandos existentes
# executa funcoes a partir da selecao
########################################

def switch(menu, handler,exit,registros):
    while menu != 99:
        if menu == 1:
            print("Listagem de videos.\n")
            exit.write("Listagem de videos.\n")
            listar_videos(registros)
            break
        elif menu == 2:
            print ("Busca por palavras chaves.\n")
            exit.write("Busca por palavras chaves.\n")
            #video_name(handler,input("Digite: "), exit)
            break
        else:
            print ("Valor invalido, tente novamente\n")
            return 0
    if menu == 99:
        print("Fim\n")
        exit.write("Arquivo Fechado.\n")
        exit.close()
        
    return 0
#####################################################
def listar_videos(Registros):
    for i in Registros:
        r = i.__repr__()
        exit.write(r + "\n\n")

#####################################################
def video_name(name_archive, word, exit):
    # Busca palvra consultada
    # Imprime todos videos com a palavra consultada
    list_vid = []

    f = open(name_archive + "data_name_videos_index.bin",'rb')

    tree = pickle.load(f)

    word = word.lower()

    list_vid = list_video(word,tree,name_archive)

    print_list(list_vid)

    if list_vid != None:
        for i in list_vid:
            r = i.__repr__()
            exit.write(r + "\n\n")

    f.close()

#####################################################
# verify_entry => verifica se tem um arquivo com mesmo nome
# ou nao
####################################################
def verify_entry(nomedaentrada):
    try:
        entrada = open(nomedaentrada+"data_name_videos_index.bin",'wb')
        print("\nArquivo ja processado anteriormente\n")
        entrada.close()
        return True
    except:
        print("\nArquivo novo.\nVamos processar o arquivo pela primeira vez.\nAguarde\n")
        return False
#####################################################
def create_register(offset,video,link,registers):
    for i in range(0,offset):
        Element = Register(i,info=[link[i],video[i]])
        registers.append(Element)
############################################################   
# open_csv => substituida por open_csv_and_return_data
####################################################
# Main
####################################################
Registers = []
files = []
# Chamo a funcao do arquivo open_csv e retorna uma lista com os objetos das colunas
a = open_csv_and_return_data("MCPD.csv")
_vid = a[0] # parametro 0 da lista=> nome dos videos
_links = a[1] # parametro 1 da lista=> nome dos links
# processamento de arquivo 
offset = 698 # numero de dados do csv
# .values do panda eh a lista com o conteudo valido dos dados
lista_v = (_vid.values)
lista_l = (_links.values)

# create bin fara com que escreva cada arquivo com os dados necessarios
create_bin(lista_v,"videos")
create_bin(lista_l,"links")

create_register(offset,lista_v,lista_l,Registers)

handler = "MCPD"
# Criacao de um arquivo txt para visualizar o que foi acessado, uma especie de log 
arquivo_de_saida = input("Para melhor visualizacao de dados, um arquivo txt sera criado. Digite o nome dele: ")
arquivo_de_saida = arquivo_de_saida + ".txt"
print(arquivo_de_saida + "criado\n")
saida = open(arquivo_de_saida,"w")
##############################
# A seguir o menu ira mostrar as opcoes
# Usuario seleciona uma delas
# 1,2 ou 99=> caso contrario invalido
##############################
menu = 1
while menu != 99:
    print(""".___  ___.      ___   .___________. __    __       _______. _______     ___      .______        ______  __    __  
|   \/   |     /   \  |           ||  |  |  |     /       ||   ____|   /   \     |   _  \      /      ||  |  |  | 
|  \  /  |    /  ^  \ `---|  |----`|  |__|  |    |   (----`|  |__     /  ^  \    |  |_)  |    |  ,----'|  |__|  | 
|  |\/|  |   /  /_\  \    |  |     |   __   |     \   \    |   __|   /  /_\  \   |      /     |  |     |   __   | 
|  |  |  |  /  _____  \   |  |     |  |  |  | .----)   |   |  |____ /  _____  \  |  |\  \----.|  `----.|  |  |  | 
|__|  |__| /__/     \__\  |__|     |__|  |__| |_______/    |_______/__/     \__\ | _| `._____| \______||__|  |__| """)
    print ("Bem-vindo ao MATH_SEARCH\n")
    print ("[1] - Listagem de todos videos\n")
    print ("[2] - Busca por palavra-chave\n")
    print ("[99] - Saida do programa\n")
    menu=int(input())
    switch(menu,handler,saida,Registers) # chama a funcao de selecionamento
    input()
