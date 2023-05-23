import os
f=open('list.dic','r')

for i in f:
	i=i.replace('\n',"")
	result=os.popen(f"./script {i}").read()
	if "Incorrect" not in result:
		print(result)
		break


f.close()
