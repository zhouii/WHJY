import re

def main ():
	with open('banner.txt','r') as f:
		content=f.read()
	group=[m.group(0) for m in re.finditer(r"(.)\1*", content.replace('\n',''))]
	chars={}
	with open('main.cpp','w') as f:
		f.write('#include <iostream>\n')
		f.write('using namespace std;\n')
		f.write('#define e cout<<"e"<<endl;\n')
		f.write('#define func_(n) cout<<" ";for(int i=0;i<n;i++)cout<<"_";cout<<" ";\n')
		for item in group:
			if item[0] not in chars:
				chars[item[0]]=[]
			if len(item) not in chars[item[0]]:
				chars[item[0]].append(len(item))
		for char in chars:
			if char==' ' or char=='e':
				continue
			func='func'+char
			for num in chars[char]:
				f.write('#define '+char*num+' '+func+'('+str(num)+')\n')
			if char!='_':
				f.write('#define '+func+'(n) for(int i=0;i<n;i++)cout<<"'+char+'";\n')
		f.write('int main () {\n')
		f.write(content)
		f.write('}\n')
		

if __name__=='__main__':
	main()
	