#!/usr/bin/python3
"""
************************************************************************************************************
FILE:       adder.py
B.O.D.:     2-5-20
AUTHOR:     Russell Cool
TOPIC:      Circuits - Adder Circuits
SUMMARY:    Simulates the creation of adder circuits to find the sum of two binary numbers.
USAGE:      $ python adder.py            
************************************************************************************************************
"""

import re

class Circuit:
    """
    Class to create adder circuit objects.  Variables include logic gates and outputs.
        Constructor inputs:
            in1         - 1st single digit binary 
            in2         - 2nd single digit binary
            carry_in    - carry over binary input from preceding circuit
    """
    def __init__(self, in1=0, in2=0, carry_in=0):
        # CIRCUIT INPUTS
        self.in1 = in1
        self.in2 = in2
        self.carry_in = carry_in
        # LOGIC GATES - OUTPUT STATUS
        self.xor1 = 0
        self.xor2 = 0
        self.or1 = 0
        self.and1 = 0
        self.and2 = 0
        # CIRCUIT OUTPUTS - STATUS
        self.output = 0
        self.carry_out = 0

    def activate_circuit(self):
        # LOGIC GATES:
        # XOR1
        if self.in1 != self.in2:
            self.xor1 = 1
        # AND1
        if self.in1 == self.in2 == 1:
            self.and1 = 1
        # XOR2
        if self.xor1 != self.carry_in:
            self.xor2 = 1
        # AND2
        if self.xor1 == self.carry_in == 1:
            self.and2 = 1
        # OR1
        if self.and1 == 1 or self.and2 == 1:
            self.or1 = 1

        # OUTPUTS:
        if self.xor2 == 1:
            self.output = 1

        if self.or1 == 1:
            self.carry_out = 1


def adder_circuits(d, bin_str1, bin_str2):
    """
    Implements virtual adder circuits to find the sum of two binary inputs.
        Input:
            d        - number of digits within each binary number
            bin_str1 - binary string 
            bin_str2 - binary string
        Output:
            sum - list containing binary digits
    """
    # INITIALIZE A LIST TO STORE ADDER CIRCUIT OBJECTS
    circuit_list = [0]*d
    # START WITH RIGHTMOST DIGITS
    circuit_list[d-1] = Circuit(int(bin_str1[d-1]), int(bin_str2[d-1]))
    circuit_list[d-1].activate_circuit()
    # CONTINUE WITH NEXT RIGHTMOST DIGITS
    for n in range(d-2,-1,-1):
        circuit_list[n] = Circuit(int(bin_str1[n]), int(bin_str2[n]), circuit_list[n+1].carry_out)
        circuit_list[n].activate_circuit()
    circuit_list.insert(0, Circuit(0, 0, circuit_list[0].carry_out))
    circuit_list[0].activate_circuit()
    sum = []
    for c in circuit_list:
        sum.append(c.output)
    #print(sum)
    print(list_to_string(sum).rjust(50))
    return sum
    
def get_binary_str(num_digits):
    """
    Function to obtain a binary string from user.
        Input:
            num_digits  -   length of binary string desired
        Output:
            bnum        -   string of binary numbers
    """
    while True:
        bnum = input(f"Enter a {num_digits} digit binary number: ".rjust(40))
        if not re.match("[01]{10}", bnum):
            print(f"Must be a {num_digits}-digit binary number.  1s and 0s kiddo")
        else:
            break
    return bnum
    
def list_to_string(a_list):   
    new_str = ""     
    for e in a_list:  
        new_str += str(e)   
    return new_str  

def main():
    # use 10-digit binaries
    digits =10
    print("This program simulates adder circuits and returns the sum of 2 binary numbers.")
    n1 = get_binary_str(digits)
    n2 = get_binary_str(digits)
    adder_circuits(digits, n1, n2)

if __name__== "__main__":
    main()

