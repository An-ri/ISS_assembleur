import numpy as np 
from annexe import bin2dec
global NB_REGISTER #nombre de registre définit en variable globale
NB_REGISTER = 5
n = 1 # varaible utile pour le scall 

"""
classe Register dans laquelle on définit les registres, la liste des instructions et leur numéro

"""

class Register :
    
    def __init__(self):
        
        self.pc = 0
        self.running = 1
        self.regs = np.zeros(NB_REGISTER)
        self.r1 = 0
        self.r2 = 0
        self.r3 = 0
        self.r4 = 0
        self.r5 = 0
        self.imm = 0
        self.instrNum = 0
        self.addr = 0
        self.prog = []
        self.bitImm = 0 #valeur du bit qui définit si on a une valuer constante ou un registre 
        self.call = 0

reg = Register()

# lecture du fichier renvoyé par l'assembleur 

fichier = open('codeasm.txt','r')
lignes = fichier.readlines()
for ligne in lignes:
    ligne = ligne.replace("\n","")
    reg.prog.append(ligne)  #on remplit la liste des instructions 


"""
focntion fetch qui va chercher l'instruction en cours dans la liste des instructions 

"""
def fetch():
    return reg.prog[reg.pc]

"""
fonction decode qui permet de traduire le binaire envoyé par l'assembleur

""" 
def decode(instr) :
    
    reg.instrNum = bin2dec(instr[0:5])
    if reg.instrNum<15:
        reg.r1 = bin2dec(instr[5:10])
        reg.bitImm = int(instr[10])
        if (instr[10] == '0'):
            reg.r2 = bin2dec(instr[11:27])
        else :
            reg.imm = bin2dec(instr[11:27]) 
        reg.r3 = bin2dec(instr[27:32])
    elif reg.instrNum == 15:
        reg.bitImm= int(instr[5])
        reg.imm=bin2dec(instr[6:27])
        reg.r1=bin2dec(instr[27:32])
    elif reg.instrNum == 18:
        reg.call=bin2dec(instr[5:32])
    else:
        reg.r1 = bin2dec(instr[5:10])
        reg.imm = bin2dec(instr[11:32])
"""
fonction eval dans laquelle on code toutes les instructions que l'on peut écrire en assembleur

"""
def eval():
    a = reg.instrNum
    b = reg.bitImm
    if (a == 0):
        print("stop\n")
        reg.running = 0
        
    if (a == 13):
        if (b == 1):
            print("load (r" + str(reg.r1) + ", #" + str(reg.imm) + ", r" + str(reg.r3) + ")\n")
            reg.regs[reg.r1] = reg.imm + reg.regs[reg.r3]
        else : 
            print("load (r" + str(reg.r1) + ", r" + str(reg.r2) + ", r" + str(reg.r3) + ")\n")
            reg.regs[reg.r1] = reg.regs[reg.r2] + reg.regs[reg.r3]
                  
    
    if (a == 1):
        if (b == 1):
            print("add (r" + str(reg.r1) + ", #" + str(reg.imm) + ", r" + str(reg.r3) + ")\n")
            reg.regs[reg.r1] = reg.imm + reg.r3
        else :
            print("add (r" + str(reg.r1) + ", r" + str(reg.r2) + ", r" + str(reg.r3) + ")\n")
            reg.regs[reg.r1] = reg.regs[reg.r2] + reg.regs[reg.r3]
    
    if (a == 2):
        if (b == 1):
            print("sub (r" + str(reg.r1) + ", #" + str(reg.imm) + ", r" + str(reg.r3) + ")\n")
            reg.regs[reg.r1] = reg.regs[reg.r3] - reg.imm
        else :
            print("sub (r" + str(reg.r1) + ", r" + str(reg.r2) + ", r" + str(reg.r3) + ")\n")
            reg.regs[reg.r1] = reg.regs[reg.r2] - reg.regs[reg.r3]
        
    
    if (a == 3):
        if (b == 1):
            print("mult (r" + str(reg.r1) + ", #" + str(reg.imm) + ", r" + str(reg.r3) + ")\n")
            reg.regs[reg.r1] = reg.imm * reg.regs[reg.r3]
        else :
            print("mult (r" + str(reg.r1) + ", r" + str(reg.r2) + ", r" + str(reg.r3) + ")\n")
            reg.regs[reg.r1] = reg.regs[reg.r2] * reg.regs[reg.r3]
    
    if (a == 4):
        if (b == 1):
            print("div (r" + str(reg.r1) + ", #" + str(reg.imm) + ", r" + str(reg.r3) + ")\n")
            reg.regs[reg.r1] = reg.imm / reg.r3
        else :     
            print("div (r" + str(reg.r1) + ", r" + str(reg.r2) + ", r" + str(reg.r3) + ")\n")
            reg.regs[reg.r1] = reg.regs[reg.r2] / reg.regs[reg.r3]
        
    if (a == 5):
        print("and (r" + str(reg.r1) + ", r" + str(reg.r2) + ", r" + str(reg.r3) + ")\n")
        reg.regs[reg.r1] = reg.regs[reg.r2] & reg.regs[reg.r3]
    
    if (a == 6):
        print("or (r" + str(reg.r1) + ", r" + str(reg.r2) + ", r" + str(reg.r3) + ")\n")
        reg.regs[reg.r1] = reg.regs[reg.r2] | reg.regs[reg.r3]
    
    if (a == 7):
        print("xor (r" + str(reg.r1) + ", r" + str(reg.r2) + ", r" + str(reg.r3) + ")\n")
        reg.regs[reg.r1] = reg.regs[reg.r2] ^ reg.regs[reg.r3]
        
    if (a == 8):
        print("shl (r" + str(reg.r1) + ", r" + str(reg.r2) + ", r" + str(reg.r3) + ")\n")
        reg.regs[reg.r1] = reg.regs[reg.r2] << reg.regs[reg.r3]
        
    if (a == 9):
        print("shr (r" + str(reg.r1) + ", r" + str(reg.r2) + ", r" + str(reg.r3) + ")\n")
        reg.regs[reg.r1] = reg.regs[reg.r2] >> reg.regs[reg.r3]
    
    if (a == 10):
        print("slt (r" + str(reg.r1) + ", r" + str(reg.r2) + ", r" + str(reg.r3) + ")\n")
        if (reg.r2 < reg.r3):
            reg.regs[reg.r1] = 1
        else :
            reg.regs[reg.r1] = 0
    
    if (a == 11): 
        print("sle (r" + str(reg.r1) + ", r" + str(reg.r2) + ", r" + str(reg.r3) + ")\n")
        if (reg.r2 <= reg.r3):
            reg.regs[reg.r1] = 1
        else :
            reg.regs[reg.r1] = 0
    
    if (a == 12):
        print("seq (r" + str(reg.r1) + ", r" + str(reg.r2) + ", r" + str(reg.r3) + ")\n")
        if (reg.r2 == reg.r3):
            reg.regs[reg.r1] = 1
        else :
            reg.regs[reg.r1] = 0
    
    if (a == 14):
        print("store r" + str(reg.r1) + " #" + str(reg.imm) + "\n")
        reg.imm = reg.regs[reg.r1]
        
    if (a == 15):
        print("jmp (r" + str(reg.r3) + ", r" + str(reg.r1) + ")\n")
        # à compléter
        
    if (a == 16):
        print("braz (r" + str(reg.r1) +str(reg.addr)+ ")\n")
        if (reg.regs[reg.r1] == 0):
            reg.pc = reg.imm
    
    if (a == 17):
        print("branz (r" + str(reg.r1) +' #'+str(reg.imm)+ ")\n")
        if (reg.regs[reg.r1] != 0):
            reg.pc = reg.imm
    
    if (a == 18):
        print("scall (" + str(n) + ")\n")
        #appelle le système n 
    
    

"""
fonction showReg qui permet d'afficher les registres en temps réel 

"""        
       
def showRegs():
    for i in range(NB_REGISTER):
        print('%04x' % int(reg.regs[i]) + " " , end='')
        
        
        
        
"""
fonction run qui permet d'exécuter les instructions décodées 

"""       
def run():
    while (reg.running != 0):
        showRegs()
        print("\n")
        instr = fetch()
        reg.pc +=1
        decode (instr)
        eval()
        
       
if __name__ == '__main__':
    run()


# coder un script qui convertit les instructions écrites en assembleur en hexadécimal  
#print(hex(int('1000001100100',2)))  
    #convertit une chaine de carac en de binaire en hexa

        
        
              
