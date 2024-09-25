# p1
import nltk
from nltk.tokenize import RegexpTokenizer
tk = RegexpTokenizer('\s+', gaps=True)
input = "I love to study Compiler code in Python"
tokens = tk.tokenize(input)
print(tokens)

#  postfix and regex
import re

def infix_to_postfix(regex):
    if not regex:
        return ""
    if '(' in regex:
        left = regex.index('(')
        right = regex.index(')', left)
        inner = regex[left + 1:right]
        return regex[:left] + infix_to_postfix(inner) + regex[right + 1:]
    return ''.join(char for char in regex if char.isalnum())
regex = input("Enter a regular expression: ")
string = input("Enter a string to match: ")
postfix = infix_to_postfix(regex)
match_result = "ACCEPTED" if re.fullmatch(regex, string) else "REJECTED"
print("Postfix form:", postfix)
print("Match:", match_result)

# Quadruples

import pandas as pd
def generate_quadruples(ae):
    quadruples = []
    for i in ae:  
        if '=' in i and ('+' in i or '-' in i or '*' in i or '/' in i):
            result, expression = i.split('=')
            left, operator, right = expression.split()
            quadruples.append([result.strip(), left.strip(), operator.strip(), right.strip()])
        elif '=' in i:
            result, right = i.split('=')
            quadruples.append([result.strip(), '', '=', right.strip()])    
    return quadruples
ae = [ 
    "a = b + c",  # First entry
    "d = e"       # Second entry
]
quadruples = generate_quadruples(ae)
df = pd.DataFrame(quadruples, columns=['Result', 'Left', 'Operator', 'Right'])
print("\nQuadruples:")
print(df)

# time

import time
n = int(input("enter number"))
t1 = time.time()
for i in range (1, n+1):
    print(i, end=" ")
t2 = time.time()
t3 = time.time()
for i in range (1, n+1):
    print(i, end=" ")
    if (i % 5 == 0):
        print()
t4 = time.time()
print(f" time1 {t2-t1:.6f} sec")
print(f" time2 {t4-t3:.6f} sec")

#Accept and reject

def FA(s):
    if len(s) < 3:  # Ensure the string has at least 3 characters
        return "Rejected"
    if s[0] == '1':
        if s[1] == '0':
            if s[2] == '1':
                for i in range(3, len(s)):  # Check from the 4th character onward
                    if s[i] != '1':
                        return "Rejected"
                return "Accepted"
            return "Rejected"
        return "Rejected"
    return "Rejected"
input_list = ['101', '1110', '11111', '10111', '0101', '0000']
for i in input_list:
    print(f"Input: {i}, Result: {FA(i)}")
