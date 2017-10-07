
"""
	Given an encoded string, return its corresponding decoded string.

	The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is repeated exactly k times. 
	Note: k is guaranteed to be a positive integer.

	Note that your solution should have linear complexity because this is what you will be asked during an interview.

	For s = "4[ab]", the output should be

	decodeString(s) = "abababab";

	For s = "2[b3[a]]", the output should be

	decodeString(s) = "baaabaaa";

	For s = "z1[y]zzz2[abc]", the output should be

	decodeString(s) = "zyzzzabcabc".
"""

import re

def decodeString(s):
    s_interna = re.findall('[0-9]+[[a-z]+\]', s)
    if s_interna == []:
        return s
    else:
        eval_list = [basic_eval(elemento) for elemento in s_interna]
        for i in range(len(s_interna)):
            s = s.replace(s_interna[i], eval_list[i])
        return decodeString(s)
    
def basic_eval(s):
    regex = r"\[([a-z]+)\]"
    regex_num = r"\d+"
    cadena = re.findall(regex, s)[0]
    num = re.findall(regex_num, s)[0]
    return int(num) * cadena
    
print "4[ab]", decodeString("4[ab]")
print "2[b3[a]]", decodeString("2[b3[a]]")
print "z1[y]zzz2[abc]", decodeString("z1[y]zzz2[abc]")
