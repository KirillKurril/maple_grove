 org $fff6
 jmp ih

 org $8000
gen_int ldaa #$55
 swi 
 coma
 swi
 coma
 swi
 coma
 swi
done bra *
ih ldx #$1f04
 staa 0,x
 ldy #$500

delay dey
 bne delay
 rti