# This is the code to get the Subsequences of a string
res = []
def getSubsequences(s, output, res):
    if (len(s)) == 0:
        res.append(output)
        return
    getSubsequences(s[1:],  output + s[0], res)
    getSubsequences(s[1:], output, res)
    return res

s = "abcd"
print(getSubsequences(s, "", res))
