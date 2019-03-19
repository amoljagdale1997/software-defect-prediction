f=open("string1.java",'r')
a=f.read()
import javalang
count1=0
# to find dunction definition we find keywords first
keys=["long",'short','boolean','int','float','double','char','byte','void']

#to find if,else in function
ifelse=["if","else","while","elseif",'for']
tokens = list(javalang.tokenizer.tokenize(a))
complexity =[]
for i in range(0,len(tokens)):
	#print(type(tokens[i]))
	if tokens[i].value in keys:
		#print(1)
		if str(type(tokens[i+1]))=="<class 'javalang.tokenizer.Identifier'>":
			#print(2)
			if tokens[i+2].value=="(":
				i=i+2
				while(tokens[i].value!=')'):
					
					i=i+1
				i=i+1
				#print(tokens[i].value)
				if tokens[i].value=='{':
					a=["{"]
					#print(tokens[i].position)
					count=0
					while len(a)!=0:
						#print(1)
						i=i+1
						if tokens[i].value=='{':
							a.append("{")
						if tokens[i].value=='}':
							if a[-1]=='{':
								a.pop()
							else :
								a.append("}")
						if tokens[i].value in ifelse:
							count=count+1
					complexity.append(count)
print(complexity)
'''print("abstract_count ---> ",abstract_count)
print("assert_count ---> ",assert_count)
print("boolean_count ---> ",boolean_count)
print("break_count ---> ",break_count)
print("byte_count ---> ",byte_count)
print("case_count ---> ",case_count)
print("catch_count ---> ",catch_count)
print("char_count ---> ",char_count)
print("class_count ---> ",class_count)
print("continue_count ---> ",continue_count)
print("default_count ---> ",default_count)
print("do_count ---> ",do_count)
print("double_count ---> ",double_count)
print("else_count ---> ",else_count)
print("enum_count ---> ",enum_count)
print("final_count ---> ",final_count)
print("finally_count ---> ",finally_count)
print("float_count ---> ",float_count)
print("for_count ---> ",for_count)
print("if_count ---> ",if_count)
print("implements_count ---> ",implements_count)
print("instanceof_count ---> ",instanceof_count)
print("import_count ---> ",import_count)
print("int_count ---> ",int_count)
print("interface_count ---> ",interface_count)
print("long_count ---> ",long_count)
print("native_count ---> ",native_count)
print("new_count ---> ",new_count)
print("null_count ---> ",package_count)
print("private_count ---> ",private_count)
print("protected_count ---> ",protected_count)
print("public_count ---> ",public_count)
print("return_count ---> ",return_count)
print("short_count ---> ",short_count)
print("static_count ---> ",static_count)
print("strictfp_count ---> ",strictfp_count)
print("super_count ---> ",super_count)
print("switch_count ---> ",switch_count)
print("synchronized_count ---> ",synchronized_count)
print("this_count ---> ",this_count)
print("throw_count ---> ",throw_count)
print("throws_count ---> ",throws_count)
print("transient_count ---> ",transient_count)
print("try_count ---> ",try_count)
print("void_count ---> ",void_count)
print("volatile_count ---> ",volatile_count)
print("while_count ---> ",while_count)
print("const_count ---> ",const_count)
print("true_count ---> ",true_count)
print("false_count ---> ",false_count)'''
