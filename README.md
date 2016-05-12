# SherlVM
Little VM project in python

With this version of the SherlVM , you can do only the simple functions of the assembly

SUM , SUB , MUL , DIV of values in a stack.
PUSH of values in a stack .
SUM , SUB , MUL , DIV of values in registers.
MOV of value in a register.
PRINT registers

##INSTRUCTION SET : 

**MOV R1 5** --------------> move 5 in the register called R1 <br />
**PUSH 5** ----------------> push 5 at on top of the stack<br />
**POP** -------------------> pop the value of the stack<br />
**ADD** -------------------> sum the 2 values on top of the stack and pop them<br />
**SHOW STACK** ------------> show the value on top of the stack<br />
**SHOW R1** ---------------> show value in the register called R1<br />
**SUB** -------------------> make the difference between the 2 values on top of the stack and pop them<br />
**MUL** -------------------> multiplicate the 2 values on top of the stack and pop them<br />
**DIV** -------------------> make the division between the 2 values on top of the stack and pop them<br />
**RADD R3 R2 R1** ---------> make the sum between R2 and R1 and put the result in R3<br />
**RSUB R3 R2 R1** ---------> subtract R1 from R2 and put the result in R3<br />
**RMUL R3 R2 R1** ---------> multiplicate R1 and R2 and put the result in R3<br />
**RDIV R3 R2 R1** ---------> make the division between R2 and R1 and put the result in R3<br />
**JMP Label** -------------> jump at the label declared into the source<br />
**CMP R3 10** -------------> compare registers and values<br />
**JNZ Label** -------------> jump at the label declared into the source only if the precedent compare got a False result<br />
**JMZ Label** -------------> jump at the label declared into the source only if the precedent compare got a True result<br />
**Label:** ----------------> a label for jumps during the execution of the code<br />
**END** -------------------> END OF PROGRAM<br />

##COMING SOON :
**INC R2** ----------------> increment a register or the stack<br />
**DEC R1** ----------------> decrement a register or the stack<br />


##HOW TO RUN : 
To run the SHERLVM , you have to have python 2.X installed on your computer. <br /><br />
So , from terminal do : <br />
    python sherl.py script.srl <br />
