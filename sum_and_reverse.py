# In string we need to add 'n' is an integer where ever number is present and reverse the number if 'inverse' (boolean) is true.
# string="abcd 24, def 15. n=5 ,inverse= true"
# answer: abcd 92,def 02
res="answer: "
s = input("Enter the string : ").split(".")
s1 = s[0].split(",")
s2 = s[1].split(",")
n = int(s2[0].split('=')[1].strip())
val = s2[1].split('=')[1].strip()
for i in s1:
	i = i.split()
	if val == 'true':
		res += i[0] +" "+str(int(i[1])+n)[::-1] +","
	else:
		res += i[0]+ str(int(i[1])+n)
print(res.strip(","))
