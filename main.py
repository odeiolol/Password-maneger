import PySimpleGUI as sg    
import time
rr1=[]
layout = [  [sg.Text("Loggin or register ?            ")],
            [sg.Button('Loggin         ')],
            [sg.Button('Register       ')] ]
            
window = sg.Window('Gerenciador de senhas', layout)      
event, values = window.read()

#Register
if event == 'Register       ':
    window.close()

    
    layout = [  [sg.Text("Which platform is it for ? ")],    
                [sg.Input()],
                [sg.Text("What is your loggin? ")],
                [sg.Input()],
                [sg.Text("What's your password ? ")],
                [sg.Input()],
                [sg.Button('registrar')] ]

    window = sg.Window('Gerenciador de senhas', layout)      
    event, values = window.read()   

   

    openfile=(values[1]+".txt")
    file=open(openfile,'x')


    data="Platform:"+values[0]+"  loggin:"+values[1]+"  Password:"+values[2]
    file.write(data)
    time.sleep(1)
    file.close()
    window.close()


#loggin
if event == 'Loggin         ':
    
    layout = [  [sg.Text("What's your loggin ? ")],    
                [sg.Input()],
                [sg.Text("What's your MAIN password ? ")],
                [sg.Input()],
                [sg.Button('Loggin')] ]


    window = sg.Window('Gerenciador de senhas', layout)      
    event, values = window.read()
    l1=values[0] 
    l2=values[1]     
                
    window.close()

    ll1=l1+'.txt'

    if l2 == 'café':
        try:
            r1=open(ll1,'r')
            for i in r1:
                rr1.append(i)
            
            layout =[  
            [sg.Text("This is your data :D  :")],
            [sg.Text(rr1)],
            [sg.Button('Quit')] ]
            
            window = sg.Window('Gerenciador de senhas', layout)      
            event, values = window.read()
    
            window.close()


        except:
            print("Your loggin was not found")



