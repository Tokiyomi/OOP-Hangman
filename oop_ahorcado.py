# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 08:07:56 2019

@author: monic
"""
import random

class Game:
    
    #Initializer / Instance Attributes
    def __init__(self):
        
        self.flag = True
        
        print("...Bienvenido, vamos a jugar ahorcado...")
        print("\nLas reglas son:\n\tIntroducir un caracter a la vez.\n\tDebe ser una letra del alfabeto.\n\tDe no cumplir alguna de estas reglas, se te restará 1 de vida.")
        
        word_list = ["Awkward","Bagpipes","Banjo","Bungler","Croquet","Crypt","Dwarves","Fervid","Fishhook","Fjord","Gazebo","Gypsy","Haiku","Haphazard","Hyphen","Ivory","Jazzy","Jiffy","Jinx","Jukebox","Kayak","Kiosk","Klutz","Memento","Mystify","Numbskull","Ostracize","Oxygen","Pajama","Phlegm","Pixel","Polka","Quad","Quip","Rhythmic","Rogue","Sphinx","Squawk","Swivel","Toady","Twelfth","Unzip","Waxy","Wildebeest","Yacht","Zealous","Zigzag","Zippy","Zombie"]
       
        self.word_list = [item.lower() for item in word_list]#Poner todo a minúscula
        
        self.descubiertas = []
        
        self.vidas = 5
        
        return None
    
    #Instance method
    def random_word(self):
        
        palabra= random.choice(self.word_list)
        self.palabra=palabra
            
    
    #Instance method
    def init_asteriscos(self):
        """
        Prints a string of '*' with the same lenght of the secret word
        
        Arg:
            palabra: a word string from the secret words list
            
        Returns:
            lista: a list of '*' with the same length of palabra
        """
        lista=['*' for i in range(len(self.palabra))]
        print("\nTu palabra tiene {0} letras".format(len(self.palabra)))
        print(''.join(lista))
        self.lista=lista
        return None
    
    def life_counter_status(self):
        """
        Prints the current life counter status
        
        Arg:
            life_counter: an integer which represents your number of lives
            
        Returns:
            A printed life_counter status
        """
        if (self.vidas)!=1:
            print("\nTienes {0} vidas".format(self.vidas))
        else:
            print("\nTienes {0} vida".format(self.vidas))

        return self.vidas
    
    def letter(self):
        """
        Gets a letter from the user.
        
        Returns:
            letra: an alphabetic character
        """
        #Pedir la letra
        letra=str(input("Escribe una letra: "))
        letra=letra.lower() #Pasarla a minuscula por cualquier cosa
        self.letra=letra
        
        return None
    
    def play(self):
        """
        It's the game stage, evaluates if the introduced character is in a correct format
        
        Args:
            life_counter: an integer which represents your current number of lifes
            palabra: a word string from the secret words list
            lista: a list of '*' with the same leght of palabra
            letra: a character from the user
            
        Returns:
            life_counter: an integer which represents the new current life after evaluating
            if the introduced letter was in a correct format
            
        """
        #Evaluar si efectivamente es un solo caracter alfabético
        if  len(self.letra)>1 or len(self.letra)==0:
            print("\t\nOJO. Introduciste más de un caracter o ninguno.\nDebes escribir un caracter a la vez. (-1 de vida)\n")
            self.vidas=self.vidas - 1
        elif (self.letra).isalpha()==False:
            print("\t\nOJO. Introduciste un caracter que no pertenece al alfabeto. (-1 de vida)\n")
            self.vidas=self.vidas - 1
        elif self.letra not in self.palabra:
            print("Esa letra no está en la palabra. (-1 de vida)\n")
            self.vidas=self.vidas - 1
        else:
            print("¡Bien!") #Si acierta, imprime esto y no quita vida
            #Reemplazar los asteriscos por los caracteres ya hallados que esten en la palabra
            for index in range(len(self.palabra)):
                if self.letra==self.palabra[index]:
                    self.lista[index]=self.letra
                    
        print(''.join(self.lista)) #Imprimir el avance
        return None
    
    def win(self):
        """
        Asigns a boolean value of True if the user guess the secret word
        
        Args:
            lista: a list of '*'
            palabra: a word string from the secret words list
            descubiertas: a list of previewed discovered words if the user played before
        Returns:
            True: if the user guess before lossing all his lives
        """
        if '*' not in self.lista: #Si adivina antes de gastar sus oportunidades, gana
            print("\n\nHaz ganado, la palabra es: {0}\n¡Felicidades!".format(self.palabra))
            if self.palabra not in self.descubiertas:
                (self.descubiertas).append(self.palabra) #Si es la primera vez que la descubre, añadirla a la lista
            return True #Si ya ganó, salir del loop
   
    def loss(self):
        """
        Prints a message if in "lista" remains '*'
        
        Args:
            lista: a list of '*'
            
        Returns:
            a printed message of defeat
        """
        if '*' in self.lista:
            print("\n\nPerdiste. :c")
        return None
    
    def descubierta(self):
        """
        Prints clues if the user have guessed the secret word before
        
        Args:
            lista_descubiertas: an empty or not guessed word list
            palabra: a word from the secret words list
            
        Returns:
            lista_descubiertas: the same list with a new, or any, word 
        """
        if self.palabra in self.descubiertas:
               print("\n\t>>PISTA. Ya has adivinado antes esta palabra<<") #Si ya la descubrió anteriormente, darle una pista
        if len(self.descubiertas)>0:
                print("\nTus palabras descubiertas hasta el momento son las siguientes:\n{0}".format(' '.join(self.descubiertas)))
        return None
    
    def goodbye():
        """
        Asks to the user if he wants to keep playing
        
        Returns:
            True: if the user wants to keep playing
            False: if the user does not want to play any more
        """
        try:
            status=int(input("Jugar de nuevo?\t\nSI:presiona 1\t\nNO:presiona 0\n"))
            if status==1:
                return True
            elif status==0:
                print("\nHasta pronto...")
                return False
            else:
                print("No entendí tu respuesta, hazlo de nuevo:")
                return Game.goodbye()
        except:
            print("No entendí tu respuesta, hazlo de nuevo:")
            return Game.goodbye()
        
    def status(self):
        
        self.flag= Game.goodbye()
        
        return self.flag
    
#MAIN

juego=Game()
#statuss=juego.flag

while juego.flag==True:
    
    juego.random_word()
    juego.descubierta()
    juego.init_asteriscos()
    juego.life_counter_status()
    
    while (juego.vidas) > 0:
        
        juego.letter()
        juego.play()
        juego.life_counter_status()
        
        if juego.win()==True:
            break
        
    juego.loss()
    
    juego.status()
    
    