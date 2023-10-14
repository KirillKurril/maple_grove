 org $8000
 psha
 pshb

 andb #%01010101
 stab $9000
 anda #%10101010
 oraa $9000
 staa $9000  

 pulb
 pula

 psha
 pshb
 andb #%10101010
 stab $9001
 anda #%01010101
 oraa $9001

 tab
 ldaa $9000
 
 xgdx
 pulb
 pula