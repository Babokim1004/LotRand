# -*- coding: utf-8 -*-
import random
import sys
import time

match=[]
mlist=[]
tc1=time.time()
sc2=[1,0,1]
sc1=[0,1,0]
sc7=[0,1]

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])
num3 = int(sys.argv[3])
num4 = int(sys.argv[4])
num5 = int(sys.argv[5])
num6 = int(sys.argv[6])
lnum = int(sys.argv[7])
line=0

for i in xrange(lnum):
	line=line+1
	def num_com(a):
		global s1; global s2; global s3; global s4; global s5; global s6
		if a >= 32:
			a = a-32
			s1=sc1
		else:
			s1=sc2
		if a >= 16:
			a = a-16
			s2=sc1
		else:
			s2=sc2
	
		if a >= 8:
			a = a-8
			s3=sc1
		else:
			s3=sc2
	
		if a >= 4:
			a = a-4
			s4=sc1
		else:
			s4=sc2
		if a >= 2:
			a = a-2
			s5=sc1
		else:
			s5=sc2

		if a >= 1:
			a = a-1
			s6=sc1
		else:
			s6=sc2




	def ans_make():
		global ansp; global anshop
		a1=random.choice(s1)*32
		a2=random.choice(s2)*16
		a3=random.choice(s3)*8
		a4=random.choice(s4)*4
		a5=random.choice(s5)*2
		a6=random.choice(s6)*1
		a7=random.choice(sc7)*64
		anshap = a1+a2+a3+a4+a5+a6+a7
		if anshap <= 45:
			ansp = anshap
		else:
			ansp=0
	ans1=[]
	num_com(num1)
	ans_make()
	ans1=[ansp]


	def ans2_make():
		global ans2
		num_com(num2)
		ans_make()
		ans2 = [ansp]
		if ans1 == ans2:
			ans2=[0]

	
	ans2_make()

	def ans3_make():
		global ans3
		num_com(num3)
		ans_make()
		ans3=[ansp]
		if ans1 == ans3 or ans2 == ans3:
			ans3=[0]

	
	ans3_make()

	def ans4_make():
		global ans4
		num_com(num4)
		ans_make()
		ans4=[ansp]
		if ans1 == ans4 or ans2 == ans4 or ans3 == ans4:
			ans4=[0]

		
	
	ans4_make()

	def ans5_make():
		global ans5
		num_com(num5)
		ans_make()
		ans5=[ansp]
		if ans1 == ans5 or ans2 == ans5 or ans3 == ans5 or ans4 == ans5:
			ans5=[0]


	ans5_make()

	def ans6_make():
		global ans6
		num_com(num6)
		ans_make()
		ans6=[ansp]
		if ans1 == ans6 or ans2 == ans6 or ans3 == ans6 or ans4 == ans6 or ans5 == ans6:
			ans6=[0]

		

	ans6_make()
	match= [ans1 + ans2 + ans3 + ans4 + ans5 + ans6]
	match.sort()
	mlist = mlist+match

	
clist=random.choice(mlist)
tc2=time.time()
tc=tc2-tc1

print clist

print "종료 되었습니다. 총 걸린 시간은", tc, "초 이며 총",line,"번 수행 하였습니다."



