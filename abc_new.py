import re
def mpq(s):
		f=open(s,"r")
		no_of_line=0
		for line in f:
			no_of_line+=1
		#print (no_of_line)
		public="public"
		public_count= 0
		operator_counter=0
		operand_counter=0
		public_count=0
		abstract_count=0
		assert_count=0
		boolean_count=0
		break_count=0
		byte_count=0
		case_count=0
		switch_count=0
		default_count=0
		catch_count=0
		try_count=0
		finally_count=0
		char_count=0
		class_count=0
		continue_count=0
		do_count=0
		while_count=0
		double_count=0
		else_count=0
		enum_count=0
		exports_count=0
		extends_count=0
		final_count=0
		finally_count=0
		float_count=0
		for_count=0
		if_count=0
		implements_count=0
		import_count=0
		instanceof=0
		int_count=0
		interface_count=0
		instanceof_count=0
		static_count=0
		long_count=0
		module_count=0
		native_count=0
		new_count=0
		package_count=0
		private_count=0
		protected_count=0
		requires_count=0
		return_count=0
		short_count=0
		strictfp_count=0
		super_count=0
		synchronized_count=0
		this_count=0
		throw_count=0
		throws_count=0
		transient_count=0
		void_count=0
		volatile_count=0
		true_count=0
		null_count=0
		false_count=0
		var_count=0
		const_count=0
		goto_count=0
		plus_count=0
		minus_count=0
		division_count=0
		multiplication_count=0
		equal_count=0 # == count
		pp_count=0 # ++ count
		mm_count=0 #-- count
		not_equal_count=0
		remainder_count=0
		assignment_count=0 # = count
		greater_count=0
		less_count=0
		greater_equal_count=0
		lesser_equal_count=0
		conditional_and_count=0
		conditional_or_count=0
		shorthand_its_count=0
		left_shift_count=0
		right_shift_count=0
		minusequal_count=0
		plusequal_count=0
		dplus_count=0
		unique_operator=0
		comment=0
		
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
		complexity1=sum(complexity)/len(complexity)

		
		keyword=["abstract","assert","boolean","break","byte","case","catch","char","class","const","continue","default","do","double","else","enum","extends","final","finally","float","for","goto","if","implements","import","instanceof","int","interface","long","native","new","package","private","protected","public","return","short","static","strictfp","super","switch","synchronized","this","throw","throws","transient","try","void","volatile","while","true","false","null"]
		operator = 0
		d=[]
		id=0
		id1=0
		blank=0
		operand = []
		total_operands=0
		key_operator=0
		keywords=["long",'short','boolean','int','float','double','char','byte']

		with open(s, 'r') as f:
				for line in f :
					line = re.sub(r'".*"',"1",line)
					if not line:
						blank+=1
					
					#to find one line comment
					if (id==1):
						d=re.findall('\*/|^\*',line)
						if not d:
							no=0
						else:
							print(1)
							for i in d:
								if(i=="*"):
									line=""
								if(i=="*/"):
									id=0
									comment+=1
									line=""
					if (id1==1)	:
						d=re.findall('\*/|^\*',line)
						if "*/" in d:
							id1=0
							line=""
							comment+=1
					b=re.findall('^/\*\*|\//|\*/|^\*|^/\*',line)
					if not b:
						no=0
					else:	
						for i in b :

							if i=="/**":
								id=1
								line=""
							if i=="/*":
								id1=1
								line=""
							if i=="//":
								#print(line)
								m=line.split("//")
								print(m)
								line=line.replace(m[1],'')
								
								comment+=1
					#find operands
					#print (line)
					
					c=re.findall("\w+",line)
					#print(c)
					m=re.split("\w|\n|\=|\+|\-|;",line)
					#print(m)
					brackets=["[","]","{","}","(",")","[]","()"]
					for i in m :
						if i in brackets:
							operator+=1
					
					for i in c:
						if i in keywords:
							for i in c:
								if i not in keywords:
									if not i.isdigit():
										if i not in operand:
											operand.append(i)
					for i in c:
						if i in operand:
							total_operands=total_operands+1

		'''print("comment",comment)					
		print("unique",operand)
		print("total_operands",total_operands)'''
		 
		#find operator
		#print("unique OPerands = ", len(operand))
		with open(s, 'r') as f:
				for line in f:
					words = line.split()
					x=re.split("\w+|\[|\]|\(|\)|\{|\}|;| ",line)
					#print(x)
					for i in x:
						i.replace(" ","")
						if (i=="+"):
							plus_count=1
							operator+=1
						if (i=="++"):
							dplus_count=1
							operator+=1
						if (i=="-"):
							minus_count=1
							operator+=1
						if(i=="*"):
							multiplication_count=1
							operator+=1
						if (i=="/"):
							division_count=1
							operator+=1
						if (i=="%"):
							remainder_count=1
							operator+=1
						if (i=="=="):
							equal_count=1	
							operator+=1
						if (i=="+="):
							plusequal_count=1	
							operator+=1
						if (i=="-="):
							minusequal_count=1	
							operator+=1
						if (i=="!="):
							not_equal_count=1
							operator+=1
						if (i=="="):
							assignment_count=1
							operator+=1
						if (i==">"):
							greater_count=1
							operator+=1
						if (i=="<"):
							less_count=1
							operator+=1
						if (i==">="):
							greater_equal_count=1
							operator+=1
						if (i=="<="):
							lesser_equal_count=1
							operator+=1
						if(i=="&&"):
							conditional_and_count=1
							operator+=1
						if (i=="||"):
							conditional_or_count=1
							operator+=1
						if (i=="?"):
							if(x[x.index(i)+1]==":"):
									shorthand_its_count=1
									operator+=1
						if (i=="<<"):
							left_shift_count=1
							operator+=1
						if (i==">>"):
							right_shift_count=1
							operator+=1
							
							
					for i in words:	
						if(i=="public"):
							public_count=public_count+1
							key_operator+=1
						if (i=="abstract"):
							abstract_countunt+=1
							key_operator+=1
						if (i=="assert"):
							assert_count+=1
							key_operator+=1
						if (i=="boolean"):
							boolean_count+=1
							key_operator+=1
						if (i=="break;"):
							break_count+=1
							key_operator+=1
						if (i=="byte"):
							byte_count+=1
							key_operator+=1
						if (i=="case"):
							case_count+=1
							key_operator+=1
						if (i=="switch"):
							switch_count+=1
							key_operator+=1
						if (i=="default"):
							default_count+=1
							key_operator+=1
						if (i=="catch"):
							catch_count+=1
							key_operator+=1
						if (i=="try"):
							true_count+=1
							key_operator+=1
						if (i=="finally"):
							finally_count+=1
							key_operator+=1
						if (i=="finally"):
							finally_count+=1
							key_operator+=1
						if (i=="for"):
							for_count+=1
							key_operator+=1
						if (i=="if"):
							if_count+=1
							key_operator+=1
						if (i=="else"):
							else_count+=1
							key_operator+=1
						if (i=="implements"):
							implements_count+=1
							key_operator+=1
						if (i=="import"):
							import_count+=1
							key_operator+=1
						if (i=="instanceof"):
							instanceof_count+=1
							key_operator+=1
						if (i=="int"):
							int_count+=1
							key_operator+=1
						if (i=="interface"):
							interface_count+=1
							key_operator+=1
						if (i=="continue"):
							continue_count+=1
							key_operator+=1
						if (i=="char"):
							char_count+=1	
							key_operator+=1
						if (i=="do"):
							do_count+=1
							key_operator+=1
						if (i=="class"):
							class_count+=1
							key_operator+=1
						if (i=="static"):
							static_count+=1	
							key_operator+=1
						if (i=="long"):
							long_count+=1
							key_operator+=1
						if (i=="module"):
							module_count+=1
							key_operator+=1
						if (i=="new"):
							new_count+=1
							key_operator+=1
						if (i=="package"):
							package_count+=1
							key_operator+=1
						if (i=="private"):
							private_count+=1
							key_operator+=1
						if (i=="protected"):
							protected_count+=1
							key_operator+=1
						if (i=="requires"):
							requires_count+=1
							key_operator+=1
						if (i=="return"):
							return_count+=1
							key_operator+=1
						if (i=="short"):
							short_count+=1
							key_operator+=1
						if (i=="strictfp"):
							strictfp_count+=1
							key_operator+=1
						if (i=="super"):
							super_count+=1
							key_operator+=1
						if (i=="synchronized"):
							synchronized_count+=1
							key_operator+=1
						if (i=="float"):
							float_count+=1
							key_operator+=1
						if (i=="this"):
							this_count+=1
							key_operator+=1
						if (i=="throw"):
							throw_count+=1
							key_operator+=1
						if (i=="throws"):
							throws_count+=1
							key_operator+=1
						if (i=="transient"):
							transient_count+=1
							key_operator+=1
						if (i=="void"):
							void_count+=1
							key_operator+=1
						if (i=="volatile"):
							volatile_count+=1
							key_operator+=1
						if (i=="true"):
							true_count+=1
							key_operator+=1
						if (i=="null"):
							null_count+=1
							key_operator+=1
						if (i=="false"):
							false_count+=1
							key_operator+=1
						if (i=="var"):
							var_count+=1
							key_operator+=1
						if (i=="const"):
							const_count+=1
							key_operator+=1
						if (i=="goto"):
							goto_count+=1
							key_operator+=1
						if (i=="extends"):
							extends_count+=1
							key_operator+=1
		unique_operator=plus_count+left_shift_count+right_shift_count+shorthand_its_count+conditional_or_count+lesser_equal_count+greater_equal_count+less_count+greater_count+assignment_count+not_equal_count+equal_count+division_count+multiplication_count+minus_count+dplus_count+plus_count+minusequal_count+plusequal_count
		'''print(operator)					
		print("Total_operator--->",operator)
		print("key_operator--->",key_operator)'''
		operator=key_operator+operator
		n=len(operand)+unique_operator
		#print("vocab",n)
		N=total_operands+operator
		#print("size",N)
		import math
		V=N*math.log2(n)
		#print("v",V)
		D=(unique_operator/2)*(total_operands/2)
		#print("D",D)
		E=V*D
		#print("E",E)
		B=V/3000
		#print("B",B)
		T=E/18
		#print("T",T)
		listofvalues=[no_of_line,complexity1,N,V,D,E,T,no_of_line,comment,blank,unique_operator,len(operand),total_operands,operator]
		
		print(listofvalues)
		return listofvalues

if __name__=='__main__':
	mpq('string1.java')	