import sys

"""

ACTUALLY THE VM HAS A STACK AND THE 4 OPERATIONS

ADD SUB MUL DIV 
ADDED PRINT FUNCTION

TO RUN FILES USE FORMAT '.srl' 
BUT IT ISN'T IMPORTANT 


EOP  - End of program
PUSH - Push
POP  - Pop
SHOW - Print
ADD  - Add
SUB  - Subtract
MUL  - Multiplicate
DIV  - Divide

Registers
R1   - General Purpose register 1
R2   - General Purpose register 2
R3   - General Purpose register 3
R4   - General Purpose register 4
"""
l = ''
i = 0
stack = [] #stack which will contains the values
label = [] #array of labels

 #################################
 #        REGISTERS GENERAL      #
 #            PURPOSE            #
 #################################


registers = {'R1':'1','R2':'22','R3':'32','R4':'4'}
cmp_val = True

OP_EOP = 'END'           #############################################
OP_PUSH = 'PUSH'         #              INSTRUCTION SET              #
OP_POP = 'POP'           #############################################
OP_PRINT = 'SHOW'        # MOV : MOV A VALUE IN A REGISTER;          #
OP_ADD = 'ADD'           # MUL : MUL IN STACK ; DIV : DIV IN STACK ; #
OP_SUB = 'SUB'           # END : END OF PROGRAM ; PUSH : PUSH STACK ;#
OP_MUL = 'MUL'           # POP : POP STACK ; SHOW : PRINT ;          #
OP_DIV = 'DIV'           # ADD : ADD IN STACK ; SUB : SUB IN STACK ; #
OP_MOV = 'MOV'           # RADD: SUM REGISTER ; RSUB : SUB REGISTER ;#
OP_RADD = 'RADD'         # RMUL: MUL REGISTER ; RDIV : DIV REGISTER ;#
OP_RSUB = 'RSUB'         #############################################
OP_RMUL = 'RMUL'
OP_RDIV = 'RDIV'
OP_CMP = 'CMP'
OP_JMP = 'JMP'
OP_JNZ = 'JNZ'
OP_JMZ = 'JMZ'

###################################
#          LOAD FUNCTION          #
###################################
#   THIS FUNCTION WILL FETCH THE  #
#   SOURCE CODE , WHICH WILL BE   #
#   DECODED AND EXECUTED LATER .  #
###################################

def load(argv):
  #open the file from argv
  f=open(argv)
  #replace all \n with a space
  #then it remove all spaces
  lines = f.read().replace('\n',' ')
  lines = lines.split(' ')
  f.close()
  return lines

##################
# PUSH  FUNCTION #
##################
#  PUSH A VALUE  #
# INTO THE STACK #
##################

def do_PUSH():
  global l
  global i
  topush = int(l[i+1])
  stack.append(topush)

##################
#  POP FUNCTION  #
##################
#  POP THE FIRST #
# VALUE FROM THE #
#     STACK      #
##################

def do_POP():
  stack.pop()


#############################
#       SHOW FUNCTION       #
#############################
#        IT PRINT OUT       #
#   THE PARAMETER WHICH IS  #
#      PASSED AFTER THE     #
#        INSTRUCTION        #
#############################

def make_SHOW(toshow):
  global l
  global i
  if toshow == "STACK": return stack[-1] 
  #IF THE NEXT PAR IN THE SOURCE IS
  #STACK, PRINT THE LAST VALUE IN THE STACK
  elif toshow == "R1": return registers['R1']
  #THE SAME IS APPLIED FOR THE REGISTERS
  elif toshow == "R2": return registers['R2']
  elif toshow == "R3": return registers['R3']
  elif toshow == "R4": return registers['R4']
  #IF NOTHING OF THE PARS ALLOWED
  else : 
    #NEXT INSTRUCTION WILL BE REPLACED BY END OF PROGRAM
    try : l[i+2] = "END"
    except : pass
    #AND RETURN ERROR
    return "ERROR , NOTHING TO SHOW "

##############################
#     PRINT  FUNCTION        #
##############################
#   IT'LL PRINT THE RESULT   #
##############################

def do_PRINT():
  global l
  global i
  toshow = l[i + 1]
  result = make_SHOW(toshow)
  print result

##########################
#      ADD FUNCTION      #
##########################
#   MAKE SUM WITH THE    #
#  TWO VALUES INTO THE   #
#        STACK           #
##########################

def do_ADD():
  num1 = stack[-1]
  num2 = stack[-2]
  total = num1 + num2
  stack.pop()
  stack.pop()
  stack.append(total)


##########################
#      SUB FUNCTION      #
##########################
#   MAKE SUB WITH THE    #
#  TWO VALUES INTO THE   #
#        STACK           #
##########################

def do_SUB():
  num1 = stack[-1]
  num2 = stack[-2]
  total = num2 - num1
  stack.pop()
  stack.pop()
  stack.append(total)


##########################
#      MUL FUNCTION      #
##########################
#   MAKE MUL WITH THE    #
#  TWO VALUES INTO THE   #
#        STACK           #
##########################


def do_MUL():
  num1 = stack[-1]
  num2 = stack[-2]
  total = num1 * num2
  stack.pop()
  stack.pop()
  stack.append(total)

##########################
#      DIV FUNCTION      #
##########################
#   MAKE DIV WITH THE    #
#  TWO VALUES INTO THE   #
#        STACK           #
##########################

def do_DIV():
  num1 = stack[-1]
  num2 = stack[-2]
  total = num2 / num1
  stack.pop()
  stack.pop()
  stack.append(total)

##########################
#      RADD FUNCTION     #
##########################
#   MAKE SUM BETWEEN     #
#     TWO REGISTERS      #
##########################

def do_RADD():
  global l
  global i
  reg_sum =  l[i + 1] #PICK FROM INSTRUCTIONS , THE REGISTERS WHICH ARE USED FOR
  reg_1 = l[i + 2]    #RADD. 
  reg_2 = l[i + 3]
  #PUT THE SUM OF THE REGISTERS IN THE DICTIONARY
  #INTO THE REG_SUM KEY OF THE DICTIONARY
  registers[reg_sum] = int(registers[reg_1]) + int(registers[reg_2])

##########################
#      RSUB FUNCTION     #
##########################
#   MAKE SUB BETWEEN     #
#     TWO REGISTERS      #
##########################

def do_RSUB():
  global l
  global i
  reg_sub =  l[i + 1] 
  reg_1 = l[i + 2]
  reg_2 = l[i + 3]
  registers[reg_sub] = int(registers[reg_1]) - int(registers[reg_2])

##########################
#      RMUL FUNCTION     #
##########################
#   MAKE MUL BETWEEN     #
#     TWO REGISTERS      #
##########################

def do_RMUL():
  global l
  global i
  reg_mul =  l[i + 1] 
  reg_1 = l[i + 2]
  reg_2 = l[i + 3]
  registers[reg_mul] = int(registers[reg_1]) *  int(registers[reg_2])



##########################
#      RDIV FUNCTION     #
##########################
#   MAKE DIV BETWEEN     #
#     TWO REGISTERS      #
##########################

def do_RDIV():
  global l
  global i
  reg_div =  l[i + 1] 
  reg_1 = l[i + 2]
  reg_2 = l[i + 3]
  registers[reg_div] = int(registers[reg_1]) /  int(registers[reg_2])

#########################
#    COMPARE FUNCTION   #
#########################
#  DO COMPARE BETWEEN   # 
#  REGISTERS AND VALS   #
#########################

def do_CMP():
  global l
  global i
  global cmp_val
  #IF NUM AND NUM
  if l[i+1].isdigit() and l[i+2].isdigit():
    try:
      if l[i+1]  == l[i+2] : 
        cmp_val =  True
      else : cmp_val =  False
    except : 
      print "ERROR COMPARE"
      l[i+1] = 'END'

  #IF NUM AND REGISTER
  elif l[i+1].isdigit() and not(l[i+2].isdigit()):
    try:
      if l[i+1] == registers[l[i+2]]:
        cmp_val = True
      else : cmp_val =  False
    except : 
      print "ERROR COMPARE"
      l[i+1] = 'END'

  #IF REGISTER AND NUM  
  elif not(l[i+1].isdigit()) and l[i+2].isdigit():
    try:
      if registers[l[i+1]] == l[i+2]:
        cmp_val = True
      else: cmp_val = False
    except : 
      print "ERROR COMPARE"
      l[i+1] = 'END'

  #IF REGISTER AND REGISTER
  else :
    try:
      if registers[l[i+1]] == registers[l[i+2]]:
        cmp_val =  True
      else: cmp_val =  False
    except: 
      print "ERROR COMPARE"
      l[i+1] = 'END'

def do_JMP():
  global i
  global l
  lab = l[i+1] + ':'
  if not(lab in label):
    print "UNKNOWN LABEL"
    l[i+1] = 'END'
  else : 
    i = l.index(lab)

######################
#    JNZ FUNCTION    #
######################
#  IT MAKES JUMP IF  #
#    CMP IS False    #
######################

def do_JNZ():
  global i 
  global l
  global cmp_val

  lab = l[i+1] + ':'
  #DA CANELLARE
  print cmp_val
  try:
    if cmp_val == False:
      i = l.index(lab)
    else: i = i+1
  except:
    print "UNKNOWN LABEL"
    l[i+1] = 'END'

##########################
#      MOV FUNCTION      #
##########################
# IT ALLOCATE THE VALUE  #
# INTO A REGISTER (R1)   #
##########################

def make_MOV(register, val):
  global i 
  global l
  try : 
    registers[register] = val
  except :  
    print ("ERROR , UNKNOWN REGISTER FOR ALLOCATING " + val) 
    try:
      #NEXT INSTRUCTION WILL BE REPLACED BY END INSTRUCTION#
      l[i + 3] = "END"
    except: pass



#####################
#   MOV EXECUTION   #
#####################
#    IT'LL PICK     #
# THE PARS AND IT   #
# WILL PASS AT THE  # 
# MAKE MOV FUNCTION #
#####################


def do_MOV():
  global i
  global l
  register = l[i + 1] #PICK REGISTER FROM INSTRUCTION LIST
  val = l[i + 2] #PICK THE VALUE
  make_MOV(register, val) #PASS THEM AT THE MAKE MOV
  
################################
#       EXECUTE FUNCTION       #
################################
#    THIS FUNCTION EXECUTE     #  
#  INSTRUCTIONS CALLING OTHER  #
#    FUNCTIONS OF THE SCRIPT   #
################################

def execute():
  global i
  global l 
  c = 0
  while c < len(l):
    if ':' in l[c]:
      label.append(l[c])
    c+=1

  while i < len(l): #WHILE THERE IS AN INSTRUCTION INTO THE TOKEN
    instruction = l[i] #PICK THE INSTRUCTION
    #CHECK WHAT THE INSTRUCTION IS
    if instruction == OP_EOP: 
      break
    elif instruction == OP_PUSH:
      do_PUSH()
    elif instruction == OP_POP:
      do_POP()
    elif instruction == OP_PRINT:
      do_PRINT()
      i += 1
    elif instruction == OP_ADD:
      do_ADD()
    elif instruction == OP_SUB:
      do_SUB()
    elif instruction == OP_MUL:
      do_MUL()
    elif instruction == OP_DIV:
      do_DIV()
    elif instruction == OP_MOV:
      do_MOV()
      i += 1
    elif instruction == OP_RADD:
      do_RADD()
    elif instruction == OP_RSUB:
      do_RSUB()
    elif instruction == OP_RMUL:
      do_RMUL()
    elif instruction == OP_RDIV:
      do_RDIV()
    elif instruction == OP_CMP:
      do_CMP()
    elif instruction == OP_JMP:
      do_JMP()
    elif instruction == OP_JNZ:
      do_JNZ()
    i += 1

####################
#   RUN FUNCTION   #
####################
# FETCH 'N EXECUTE #
####################


def run_program(argv):
  global l
  l = load(argv)
  execute()

#################
# MAIN FUNCTION #
#################

def main(argv):
  run_program(argv[1])
  return 0

#####################
# PICK THE ARGUMENT #
#####################

def target(*args):
  return main, None

if __name__ == '__main__':
  main(sys.argv)
