from tkinter import *
import random

root = Tk()
root.geometry('400x400')
root.resizable(0,0)
root.title('DataFlair-Rock,Paper,Scissors')
root.config(bg ='seashell3')

Label(root, text = 'Rock, Paper ,Scissors' , font='arial 20 bold', bg = 'light sky blue').pack()

user_take = StringVar()
Label(root, text = 'choose any one: rock, paper ,scissors' , font='arial 15 bold', bg =  "light blue").place(x = 20,y=70)
Entry(root, font = 'arial 15', textvariable = user_take , bg = 'sky blue').place(x=90 , y = 130)


computer_choice= random.randint(1,3)
if computer_choice == 1:
    computer_choice = 'rock'
elif computer_choice ==2:
    computer_choice = 'paper'
else:
    computer_choice = 'scissors'

Result = StringVar()

def play():

    while True:
        player_choice = input('What do you pick? (rock, paper, scissors)')
        player_choice.strip()
        random_move = random.randint(1, 3)
        moves = ['rock', 'paper', 'scissors']
        computer_choice =[random_move]
        if player_choice == computer_choice:
            Label('both player choise paper. its a draw!')
        elif player_choice == 'rock'or computer_choice == 'scissors':
            Label("rock smashes scissors! congratulations you are win!")
        elif  player_choice== 'paper' or computer_choice== 'scissors':
            Label("scissors cuts paper! you miss this chance you are lose!")
        elif player_choice == 'scissors' or computer_choice == 'paper':
            Label("scissors cuts paper! congratulations you are win!")
        elif player_choice == 'scissors' or computer_choice == 'rock':
            Label("rock smashes scissors! you miss this chance you are lose.")
        elif player_choice == 'paper' or computer_choice == 'rock':
            Label("paper cover rock! congratulations you are win!")
        elif player_choice =="rock" or computer_choice == "scissors":
            Label("rock smashes scissors! you miss this chance you are win!")
        aGain = input('Do you want to play again? (y or n)').strip()
        if aGain== 'n':
            break
    
        
def Reset():
    Result.set("") 
    user_take.set("")

def Exit():
    root.destroy()

Entry(root, font = 'arial 10 bold', textvariable = Label, bg ='light blue',width = 50,).place(x=25, y = 250)

Button(root, font = 'arial 13 bold', text = 'PLAY'  ,padx =5,bg ='sky blue' ,command = play).place(x=150,y=190)

Button(root, font = 'arial 13 bold', text = 'RESET'  ,padx =5,bg ='light pink' ,command = Reset).place(x=70,y=310)

Button(root, font = 'arial 13 bold', text = 'EXIT'  ,padx =5,bg ='light pink' ,command = Exit).place(x=230,y=310)