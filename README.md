# SherlVM
Little VM project in python

With this version of the SherlVM , you can do only the simple functions of the assembly

SUM , SUB , MUL , DIV of values in a stack.
PUSH of values in a stack .
SUM , SUB , MUL , DIV of values in registers.
MOV of value in a register.
PRINT registers

INSTRUCTION SET : 

MOV R1 5 --------------> move 5 in the register called R1
PUSH 5 ----------------> push 5 at on top of the stack
POP -------------------> pop the value of the stack
ADD -------------------> sum the 2 values on top of the stack and pop them
SHOW STACK ------------> show the value on top of the stack
SHOW R1 ---------------> show value in the register called R1
SUB -------------------> make the difference between the 2 values on top of the stack and pop them
MUL -------------------> multiplicate the 2 values on top of the stack and pop them
DIV -------------------> make the division between the 2 values on top of the stack and pop them
RADD R3 R2 R1 ---------> make the sum between R2 and R1 and put the result in R3
RSUB R3 R2 R1 ---------> subtract R1 from R2 and put the result in R3
RMUL R3 R2 R1 ---------> multiplicate R1 and R2 and put the result in R3
RDIV R3 R2 R1 ---------> make the division between R2 and R1 and put the result in R3
END -------------------> END OF PROGRAM

To run the SHERLVM , you have to have python 2.X installed on your computer. 
So , from terminal do :
    python sherl.py script.srl
