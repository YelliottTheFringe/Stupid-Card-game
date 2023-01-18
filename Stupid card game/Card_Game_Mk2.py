#card game the second.
from random import randint

from time import sleep

def round():
    def betcheck(bet):
        if bet<bankAcc and bet>0:
            pass
        elif bet == 115111115:
            print("RIP. You folded.")
            sleep(2)
            print("Seriously?")
            sleep(5)
            print("Ok")
            sleep(2)
            quit()
        else:
            print("Your balance is:",bankAcc)
            bet1=input("You must bet less then your bank account. New bet: " )
    def findDouble(pcval,c1val,c2val,c3val,c4val,c5val,c6val,c7val):
        score=2
        if pcval==c1val:
            score+=2
        if pcval==c2val:
            score+=2
        if pcval==c3val:
            score+=2
        if pcval==c4val:
            score+=2
        if pcval==c5val:
            score+=2
        if pcval==c6val:
            score+=2
        if pcval==c7val:
            score+=2
        return score
    def checkFlush(pctp,c1tp,c2tp,c3tp,c4tp,c5tp,c6tp,c7tp,score):
        if pctp==c1tp==c2tp==c3tp==c4tp:
            score=score*4
        if pctp==c2tp==c3tp==c4tp==c5tp:
            score=score*4
        if pctp==c3tp==c4tp==c5tp==c6tp:
            score=score*4
        if pctp==c4tp==c5tp==c6tp==c7tp:
            score=score*4
        if pctp==c3tp==c5tp==c6tp==c7tp:
            score=score*4
        if pctp==c2tp==c5tp==c6tp==c7tp:
            score=score*4
        else:
            score+=randint(10,15)
        return score
    def open_bankAccount():
        file=open("bank.txt","r")
        v=file.readlines()
        print(v)
        print(int(v[0]))
        bankAcc=int(v[0])
        file.close()
        return(bankAcc)
    bankAcc=open_bankAccount()
    print("Your bank account has:",bankAcc)
    randomCardClass=["Diamonds","Spades","Clubs","Hearts"]
    cardvalue      =[1,2,3,4,5,6,7,8,9,10,11,12,13]
    randomCardtype=["1","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
    def randomCard():
        cardvaluerandomizer=randint(0,12)
        return cardvaluerandomizer
    cr=randomCard()
    #player cards
    pc1=[randomCardClass[(randint(0,3))],cardvalue[cr],randomCardtype[cr]]
    cr=randomCard()
    pc2=[randomCardClass[(randint(0,3))],cardvalue[cr],randomCardtype[cr]]
    pbt=0
    cbt=0
    #computer cards
    cr=randomCard()
    cc1=[randomCardClass[(randint(0,3))],cardvalue[cr],randomCardtype[cr]]
    cr=randomCard()
    cc2=[randomCardClass[(randint(0,3))],cardvalue[cr],randomCardtype[cr]]
    print("\n","  your cards              ",pc1,"\n","                          ",pc2)
    if input("Fold by typing 115111115. Begin Game? y/n ")=='y':
        # prebeting
        print("First round. Your bank account has:",bankAcc)
        sleep(0.5)
        print("First round of betting. Computer first.")
        cbet=randint(1,10)
        sleep(1)
        print("Computer bet ",cbet)
        cbt+=cbet
        sleep(1)
        pbet=int(input("Your bet?"))
        while pbet<0 or pbet> bankAcc:
            betcheck(pbet)
        bankAcc-=pbet
        pbt+=pbet
        sleep(1)
        print("\nHere comes the Flop.")
        sleep(1)
        # table cards
        cr=randomCard()
        tcrd1=[randomCardClass[(randint(0,3))],cardvalue[cr],randomCardtype[cr]]
        cr=randomCard()
        tcrd2=[randomCardClass[(randint(0,3))],cardvalue[cr],randomCardtype[cr]]
        print(tcrd1,"\n",tcrd2)
        sleep(1)
        cbet+=findDouble(cc1[1],tcrd1[1],tcrd2[1],0,0,0,0,cbet)+findDouble(cc2[1],tcrd1[1],tcrd2[1],0,0,0,0,cbet)
        print("Your account holds ",bankAcc)
        sleep(1)
        pbet=int(input("Your bet?"))
        sleep(1)
        while pbet <0 or pbet>bankAcc:
            betcheck(pbet)
        bankAcc-=pbet
        pbt+=pbet
        print("The computer bet",cbet)
        cbt+=cbet
        sleep(1)
        print("\nHere comes the turn.")
        sleep(1)
        # table cards
        cr=randomCard()
        tcrd3=[randomCardClass[(randint(0,3))],cardvalue[cr],randomCardtype[cr]]
        cr=randomCard()
        tcrd4=[randomCardClass[(randint(0,3))],cardvalue[cr],randomCardtype[cr]]
        print(tcrd1,"\n",tcrd2,"\n ",tcrd3,"\n  ",tcrd4)
        sleep(1)
        cbet+=findDouble(cc1[1],tcrd1[1],tcrd2[1],tcrd3[1],tcrd4[1],0,0,cbet)+findDouble(cc2[1],tcrd1[1],tcrd2[1],tcrd3[1],tcrd4[1],0,0,cbet)
        print("Your account holds ",bankAcc)
        sleep(1)
        pbet=int(input("Your bet?"))
        sleep(1)
        while pbet <0 or pbet>bankAcc:
            betcheck(pbet)
        bankAcc-=pbet
        pbt+=pbet
        print("The computer bet",cbet)
        cbt+=cbet
        sleep(1)
        print("\n")
        print("Here comes the River,")
        sleep(1)
        # table cards
        cr=randomCard()
        tcrd5=[randomCardClass[(randint(0,3))],cardvalue[cr],randomCardtype[cr]]
        cr=randomCard()
        tcrd6=[randomCardClass[(randint(0,3))],cardvalue[cr],randomCardtype[cr]]
        print(tcrd1,"\n",tcrd2,"\n ",tcrd3,"\n  ",tcrd4,"\n   ",tcrd5,"\n    ",tcrd6)
        sleep(1)
        cbet+=findDouble(cc1[1],tcrd1[1],tcrd2[1],tcrd3[1],tcrd4[1],tcrd5[1],tcrd6[1],0)+findDouble(cc2[1],tcrd1[1],tcrd2[1],tcrd3[1],tcrd4[1],tcrd5[1],tcrd6[1],0)
        print("Your account holds ",bankAcc)
        sleep(1)
        pbet=int(input("Your bet?"))
        sleep(1)
        while pbet <0 or pbet>bankAcc:
            betcheck(pbet)
        bankAcc-=pbet
        pbt+=pbet
        print("The computer bet",cbet)
        cbt+=cbet
        sleep(1)
        # Final round
        if randint(5,10)==9:
            print("I dont like you very much.")
            input("")
            quit()
        print("\n")
        print("Here comes the extra!")
        sleep(1)
        # table cards
        cr=randomCard()
        tcrd7=[randomCardClass[(randint(0,3))],cardvalue[cr],randomCardtype[cr]]
        print(tcrd1,"\n",tcrd2,"\n ",tcrd3,"\n  ",tcrd4,"\n   ",tcrd5,"\n    ",tcrd6,"\n      ",tcrd7)
        sleep(1)
        cbet=checkFlush(cc1[0],tcrd1[0],tcrd2[0],tcrd3[0],tcrd4[0],tcrd5[0],tcrd6[0],tcrd7[0],randint(5,12))
        cbet+=checkFlush(cc2[0],tcrd1[0],tcrd2[0],tcrd3[0],tcrd4[0],tcrd5[0],tcrd6[0],tcrd7[0],randint(5,12))
        cbet+=findDouble(cc1[1],tcrd1[1],tcrd2[1],tcrd3[1],tcrd4[1],tcrd5[1],tcrd6[1],tcrd7[1])+findDouble(cc2[1],tcrd1[1],tcrd2[1],tcrd3[1],tcrd4[1],tcrd5[1],tcrd6[1],tcrd7[1])
        print("Your account holds ",bankAcc)
        sleep(1)
        pbet=int(input("Your bet?"))
        sleep(1)
        while pbet <0 or pbet>bankAcc:
            betcheck(pbet)
        print("The computer bet",cbet)
        cbt+=cbet
        bankAcc-=pbet
        pbt+=pbet
        sleep(1)
        print("\nBet checking Time!")
        endScoreThingies=[]
        
        computerFindbet=findDouble(cc1[1],tcrd1[1],tcrd2[1],tcrd3[1],tcrd4[1],tcrd5[1],tcrd6[1],tcrd7[1])+findDouble(cc1[1],tcrd1[1],tcrd2[1],tcrd3[1],tcrd4[1],tcrd5[1],tcrd6[1],tcrd7[1])
        computerFindbet=checkFlush(cc2[0],tcrd1[0],tcrd2[0],tcrd3[0],tcrd4[0],tcrd5[0],tcrd6[0],tcrd7[0],computerFindbet)
        computerFindbet=checkFlush(cc1[0],tcrd1[0],tcrd2[0],tcrd3[0],tcrd4[0],tcrd5[0],tcrd6[0],tcrd7[0],computerFindbet)
        print("The computer score is ",computerFindbet)
        sleep(1)
        playerBF=findDouble(pc1[1],tcrd1[1],tcrd2[1],tcrd3[1],tcrd4[1],tcrd5[1],tcrd6[1],tcrd7[1])+findDouble(pc1[1],tcrd1[1],tcrd2[1],tcrd3[1],tcrd4[1],tcrd5[1],tcrd6[1],tcrd7[1])
        playerBF=checkFlush(pc2[0],tcrd1[0],tcrd2[0],tcrd3[0],tcrd4[0],tcrd5[0],tcrd6[0],tcrd7[0],playerBF)
        playerBF=checkFlush(pc1[0],tcrd1[0],tcrd2[0],tcrd3[0],tcrd4[0],tcrd5[0],tcrd6[0],tcrd7[0],playerBF)
        print("Your score is ",playerBF)
        sleep(1)
        endScore=cbt+pbt
        if playerBF>computerFindbet:
            print("You win.")
            print("Winner takes all.")
        
            print("You get ",endScore)
            with open("bank.txt","w") as f:
                f.write(str(bankAcc+endScore*2))
                f.close()
        elif computerFindbet>playerBF:
            print("Computer wins.")
            print("Winner takes all.")
            sleep(1)
            print("Computer gets ",endScore)
            with open("bank.txt","w") as f:
            
                f.write(str(bankAcc-100))
                f.close()
        elif computerFindbet==playerBF:
            print("Its down to the high cards!")
            crdvlaueP=[pc1[1],pc2[1]]
            playerHigh=max(crdvlaueP)
            crdvalueC=[cc1[1],cc2[1]]
            compHigh = max(crdvalueC)
            if compHigh>playerHigh:
                print("Computer wins highcard.")
                sleep(1)
                print("Computer gets ",endScore)
                with open("bank.txt","w") as f:
                    f.write(str(bankAcc-100))
                    f.close()
            elif compHigh<playerHigh:
                print("You win.")
                sleep(1)
                print("You get ",endScore)
                with open("bank.txt","w") as f:
                    f.write(str(bankAcc+endScore*2))
                    f.close()
            else:
                print("You've tied. Computer beats ties.")
                sleep(1)
                print("Computer gets ",endScore)
                with open("bank.txt","w") as f:
                    f.write(str(bankAcc-100))
                    f.close()
    else:
        pass

round()
if input("End Game? Play again is again. ")=="again":
    round()
print("\n")
print("\n")
print("Thanks for playing! Let me know what you think.")
print("\n")
sleep(3)
