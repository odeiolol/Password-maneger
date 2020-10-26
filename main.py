while True:
    number=0
    #Loggin
    print("Chose one")
    initialQ=input('Loggins or Register?')

    #Register
    if initialQ == 'register':
        platformR=input("Which platform is it for ? ")
        logginR=input("What is your loggin? ")
        passwordR=input("What password do you wanna use? ")

        openfile=(logginR+".txt")
        file=open(openfile,'x')
        #processing data

        data="loggin:"+logginR+','+" Password:"+passwordR+','+" Platform:"+platformR
        file.write(data)
        print("Registered with success!")
    else:
        number+=1

    #loggin
    if initialQ =="loggins":
        l1=input('loggin: ')
        l2=input('key: ')
        ll1=l1+'.txt'

        if l2 == 'café':
            try:
                r1=open(ll1,'r')
                for i in r1:
                    print(i)
            except:
                print("Your loggin was not found")
    else:
        if number== 1:
            print("ESCREVE CERTO CEQUELADO")


