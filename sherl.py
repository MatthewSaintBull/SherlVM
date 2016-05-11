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

stack = [] #stack which will contains the values

 #################################
 #        REGISTERS GENERAL      #
 #            PURPOSE            #
 #################################


registers = {'R1':'1','R2':'22','R3':'32','R4':'4'}


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

def do_PUSH(i,l):
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

def make_SHOW(toshow, i, l):
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

def do_PRINT(i, l):
  toshow = l[i + 1]
  result = make_SHOW(toshow, i, l)
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

def do_RADD(i,l):
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

def do_RSUB(i,l):
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

def do_RMUL(i,l):
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

def do_RDIV(i,l):
  reg_div =  l[i + 1] 
  reg_1 = l[i + 2]
  reg_2 = l[i + 3]
  registers[reg_div] = int(registers[reg_1]) /  int(registers[reg_2])

##########################
#      MOV FUNCTION      #
##########################
# IT ALLOCATE THE VALUE  #
# INTO A REGISTER (R1)   #
##########################

def make_MOV(register, val, i, l):
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


def do_MOV(i,l):
  register = l[i + 1] #PICK REGISTER FROM INSTRUCTION LIST
  val = l[i + 2] #PICK THE VALUE
  make_MOV(register, val, i, l) #PASS THEM AT THE MAKE MOV
  
################################
#       EXECUTE FUNCTION       #
################################
#    THIS FUNCTION EXECUTE     #  
#  INSTRUCTIONS CALLING OTHER  #
#    FUNCTIONS OF THE SCRIPT   #
################################

def execute(l):
  i=0

  while i < len(l): #WHILE THERE IS AN INSTRUCTION INTO THE TOKEN
    instruction = l[i] #PICK THE INSTRUCTION
    #CHECK WHAT THE INSTRUCTION IS
    if instruction == OP_EOP: 
      break
    elif instruction == OP_PUSH:
      do_PUSH(i,l)
    elif instruction == OP_POP:
      do_POP()
    elif instruction == OP_PRINT:
      do_PRINT(i,l)
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
      do_MOV(i,l)
      i += 1
    elif instruction == OP_RADD:
      do_RADD(i,l)
    elif instruction == OP_RSUB:
      do_RSUB(i,l)
    elif instruction == OP_RMUL:
      do_RMUL(i,l)
    elif instruction == OP_RDIV:
      do_RDIV(i,l)

    i += 1

####################
#   RUN FUNCTION   #
####################
# FETCH 'N EXECUTE #
####################


def run_program(argv):
  l = load(argv)
  execute(l)

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
