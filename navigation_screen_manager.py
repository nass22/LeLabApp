from kivy.uix.screenmanager import ScreenManager

class NavigationScreenManager(ScreenManager):
    screen_stack = [] #on va mettre les noms de screen qu'on afficher et supprimer ceux qu'on enlève afin d'avoir la dernière page sur laquelle on était
    
    def push(self, screen_name): #je push un écran pour l'afficher, prend un paramètre le nom de l'écran
        
        if screen_name not in self.screen_stack:
            self.screen_stack.append(self.current) #on fait un append de l'écran courant -> self.current
            self.transition.direction = "left" #permet de choisir la direction de la transition
            self.current = screen_name;
        
    def pop(self): #je pop un écran pour l'enlever, ne prend pas de prmtrs car on veut revenir sur l'écran précédant
        if len(self.screen_stack) > 0:
            screen_name = self.screen_stack[-1]
            del self.screen_stack[-1]
            self.transition.direction = "right" #permet de choisir la direction de la transition
            self.current = screen_name
        
        