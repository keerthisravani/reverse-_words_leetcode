def reverseWords( s):
    result=""
    l=s.split()
    for i in l:
            
        result=result+i[::-1]+" "
    result=result[:len(result)-1]
    return result
s="hi hello good morning"
print(reverseWords(s))