# ISS_assembleur

the assembleur reads a FILE.txt in ASCII format as in: 

load r0,2000,0
load r1,0,r0
sub r0,1,r0
mult r1,r0,r1
branz r0,2
stop

and creates or overwrites 'codeasm.txt' in his repository which is a binary translation of the instructions

the ISS contains 32 registers, it uses the codeasm.txt and follows the instructions
