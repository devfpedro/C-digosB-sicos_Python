#Faça um programa em python que abra e reproduza o áudio de um arquivo MP3.

from pygame import mixer

mixer.init()
mixer.music.load("") #Aqui é colocado o nome do arquivo da música mp3 (é importante que o arquivo esteja na mesma pasta do código)
mixer.music.play()
parar= str(input("Digite algo para parar a reprodução de áudio: \033[1m"))
