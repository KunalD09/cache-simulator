#!/usr/bin/python
from random import randint
import string
import math

print "Note - LRU and FIFO is not implemented for Direct Mapped"
print "-----------------------------------------------------"
print "The size of main memory in bytes is : 128"
print "The size of cache memory in bytes is : 32"
print "The line size is : 1"
print "Cache placement algorithm is : Direct Mapping, Set Associative, Fully Associative"
print "Number of Sets : Depends on the cache placement"
print "Replacement Policy - Random, FIFO, Least Recently Used (LRU)"
print "-----------------------------------------------------"

print "------ Select the cache placement algorithm listed above -------"
print "1. Direct Mapping"
print "2. Fully Associative"
print "3. 4 Way Set Associative"
algo = int(raw_input("Select the cache placement algorithm listed above : "))
print "algo = ",algo

print "Select the Cache Replacement Policy"
print "1. Random replacement policy"
print "2. FIFO replacement policy"
print "3. LRU replacement policy"
rp = int(raw_input("Enter the replacement policy number : "))
print "rp = ",rp
print "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"

if algo is 1:
	print "-----------------------------------------------------"
	print "The size of main memory in bytes is : 128"
	print "The size of cache memory in bytes is : 32"
	print "The line size is : 1"
	print "Cache placement algorithm is : 32 Set 0 Ways"
	print "Number of Sets : 32"
	print "Replacement Policy - Directly mapping"
	print "-----------------------------------------------------"

	cache = []    #tag cache memory
	hit_count = 0
	miss_count = 0
	phyadd = []
	mainmem = []
	

	print "Main Memory size : "
	mainfile = open("main_mem.txt","r")

	for set in range(32):
		cache.append(["xxxxx"])
	
	for row in cache:
		print ' '.join(row)
	#print cache
	################## Open the Physical Address File ###############
	#phyfile = open("phyadd.txt","r")
	pf = open("phyadd.txt","r")
	phy = pf.readlines()
	for line in phy:
		addr = int(line)
		phyadd.append(addr)
	print "Physical Address - ",phyadd
	################## Open Main Memory ###############
	mf = open("main_mem.txt","r")
	main = mf.readlines()
	for line in main:
		inst = int(line)
		mainmem.append(inst)
	print "Main Memory Instructions - ",mainmem
	print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
	print "Cache Simulator Starts"	
	for i in phyadd:
		str = int(i)
		print "Str = ",str
		str1 = int(31)
		print str1
		bits = (str & str1)
		bit = format(bits, 'b').zfill(7) # binary number
		print "bits = ",bit
		num = int(bit,2)     #covert binary to int
		print "Integer num = ",num
		y = mainmem[str]
		print "Instruction = ",y
		if num is 0:
			if cache[num] == y:
				hit_count = hit_count+1
				print "hit_count = ",hit_count
			else:
				cache[num] = y
				miss_count = miss_count+1
				print "miss_count = ",miss_count
			print "Cache Memory = ", cache
		elif num is 1:
			if cache[num] == y:
				hit_count = hit_count+1
				print "hit_count = ",hit_count
			else:
				cache[num] = y
				miss_count = miss_count+1
				print "miss_count = ",miss_count
			print "Cache Memory = ", cache
		elif num is 2:
			if cache[num] == y:
				hit_count = hit_count+1
				print "hit_count = ",hit_count
			else:
				cache[num] = y
				miss_count = miss_count+1
				print "miss_count = ",miss_count
			print "Cache Memory = ", cache
		elif num is 3:
			if cache[num] == y:
				hit_count = hit_count+1
				print "hit_count = ",hit_count
			else:
				cache[num] = y
				miss_count = miss_count+1
				print "miss_count = ",miss_count
			print "Cache Memory = ", cache
		elif num is 4:
			if cache[num] == y:
				hit_count = hit_count+1
				print "hit_count = ",hit_count
			else:
				cache[num] = y
				miss_count = miss_count+1
				print "miss_count = ",miss_count
			print "Cache Memory = ", cache
		elif num is 5:
			if cache[num] == y:
				hit_count = hit_count+1
				print "hit_count = ",hit_count
			else:
				cache[num] = y
				miss_count = miss_count+1
				print "miss_count = ",miss_count
			print "Cache Memory = ", cache
		elif num is 6:
			if cache[num] == y:
				hit_count = hit_count+1
				print "hit_count = ",hit_count
			else:
				cache[num] = y
				miss_count = miss_count+1
				print "miss_count = ",miss_count
			print "Cache Memory = ", cache
		elif num is 7:
			if cache[num] == y:
				hit_count = hit_count+1
				print "hit_count = ",hit_count
			else:
				cache[num] = y
				miss_count = miss_count+1
				print "miss_count = ",miss_count
			print "Cache Memory = ", cache
		elif num is 8:
			if cache[num] == y:
				hit_count = hit_count+1
				print "hit_count = ",hit_count
			else:
				cache[num] = y
				miss_count = miss_count+1
				print "miss_count = ",miss_count
			print "Cache Memory = ", cache
		elif num is 9:
			if cache[num] == y:
				hit_count = hit_count+1
				print "hit_count = ",hit_count
			else:
				cache[num] = y
				miss_count = miss_count+1
				print "miss_count = ",miss_count
			print "Cache Memory = ", cache
		elif num is 10:
			if cache[num] == y:
				hit_count = hit_count+1
				print "hit_count = ",hit_count
			else:
				cache[num] = y
				miss_count = miss_count+1
				print "miss_count = ",miss_count
			print "Cache Memory = ", cache
		elif num is 11:
			if cache[num] == y:
				hit_count = hit_count+1
				print "hit_count = ",hit_count
			else:
				cache[num] = y
				miss_count = miss_count+1
				print "miss_count = ",miss_count
			print "Cache Memory = ", cache
		elif num is 12:
			if cache[num] == y:
				hit_count = hit_count+1
				print "hit_count = ",hit_count
			else:
				cache[num] = y
				miss_count = miss_count+1
				print "miss_count = ",miss_count
			print "Cache Memory = ", cache
		elif num is 13:
			if cache[num] == y:
				hit_count = hit_count+1
				print "hit_count = ",hit_count
			else:
				cache[num] = y
				miss_count = miss_count+1
				print "miss_count = ",miss_count
			print "Cache Memory = ", cache
		elif num is 14:
			if cache[num] == y:
				hit_count = hit_count+1
				print "hit_count = ",hit_count
			else:
				cache[num] = y
				miss_count = miss_count+1
				print "miss_count = ",miss_count
			print "Cache Memory = ", cache
		elif num is 15:
			if cache[num] == y:
				hit_count = hit_count+1
				print "hit_count = ",hit_count
			else:
				cache[num] = y
				miss_count = miss_count+1
				print "miss_count = ",miss_count
			print "Cache Memory = ", cache
		elif num is 16:
			if cache[num] == y:
				hit_count = hit_count+1
				print "hit_count = ",hit_count
			else:
				cache[num] = y
				miss_count = miss_count+1
				print "miss_count = ",miss_count
			print "Cache Memory = ", cache
		elif num is 17:
			if cache[num] == y:
				hit_count = hit_count+1
				print "hit_count = ",hit_count
			else:
				cache[num] = y
				miss_count = miss_count+1
				print "miss_count = ",miss_count
			print "Cache Memory = ", cache
		elif num is 18:
			if cache[num] == y:
				hit_count = hit_count+1
				print "hit_count = ",hit_count
			else:
				cache[num] = y
				miss_count = miss_count+1
				print "miss_count = ",miss_count
			print "Cache Memory = ", cache
		elif num is 19:
			if cache[num] == y:
				hit_count = hit_count+1
				print "hit_count = ",hit_count
			else:
				cache[num] = y
				miss_count = miss_count+1
				print "miss_count = ",miss_count
			print "Cache Memory = ", cache
		elif num is 20:
			if cache[num] == y:
				hit_count = hit_count+1
				print "hit_count = ",hit_count
			else:
				cache[num] = y
				miss_count = miss_count+1
				print "miss_count = ",miss_count
			print "Cache Memory = ", cache
		elif num is 21:
			if cache[num] == y:
				hit_count = hit_count+1
				print "hit_count = ",hit_count
			else:
				cache[num] = y
				miss_count = miss_count+1
				print "miss_count = ",miss_count
			print "Cache Memory = ", cache
		elif num is 22:
			if cache[num] == y:
				hit_count = hit_count+1
				print "hit_count = ",hit_count
			else:
				cache[num] = y
				miss_count = miss_count+1
				print "miss_count = ",miss_count
			print "Cache Memory = ", cache
		elif num is 23:
			if cache[num] == y:
				hit_count = hit_count+1
				print "hit_count = ",hit_count
			else:
				cache[num] = y
				miss_count = miss_count+1
				print "miss_count = ",miss_count
			print "Cache Memory = ", cache
		elif num is 24:
			if cache[num] == y:
				hit_count = hit_count+1
				print "hit_count = ",hit_count
			else:
				cache[num] = y
				miss_count = miss_count+1
				print "miss_count = ",miss_count
			print "Cache Memory = ", cache
		elif num is 25:
			if cache[num] == y:
				hit_count = hit_count+1
				print "hit_count = ",hit_count
			else:
				cache[num] = y
				miss_count = miss_count+1
				print "miss_count = ",miss_count
			print "Cache Memory = ", cache
		elif num is 26:
			if cache[num] == y:
				hit_count = hit_count+1
				print "hit_count = ",hit_count
			else:
				cache[num] = y
				miss_count = miss_count+1
				print "miss_count = ",miss_count
			print "Cache Memory = ", cache
		elif num is 27:
			if cache[num] == y:
				hit_count = hit_count+1
				print "hit_count = ",hit_count
			else:
				cache[num] = y
				miss_count = miss_count+1
				print "miss_count = ",miss_count
			print "Cache Memory = ", cache
		elif num is 28:
			if cache[num] == y:
				hit_count = hit_count+1
				print "hit_count = ",hit_count
			else:
				cache[num] = y
				miss_count = miss_count+1
				print "miss_count = ",miss_count
			print "Cache Memory = ", cache
		elif num is 29:
			if cache[num] == y:
				hit_count = hit_count+1
				print "hit_count = ",hit_count
			else:
				cache[num] = y
				miss_count = miss_count+1
				print "miss_count = ",miss_count
			print "Cache Memory = ", cache
		elif num is 30:
			if cache[num] == y:
				hit_count = hit_count+1
				print "hit_count = ",hit_count
			else:
				cache[num] = y
				miss_count = miss_count+1
				print "miss_count = ",miss_count
			print "Cache Memory = ", cache
		elif num is 31:
			if cache[num] == y:
				hit_count = hit_count+1
				print "hit_count = ",hit_count
			else:
				cache[num] = y
				miss_count = miss_count+1
				print "miss_count = ",miss_count
			print "Cache Memory = ", cache
		print "-------------------------------"
	
	print "-------------------- Final Result of Direct Mapped Cache -------------------------"
	print "Cache Memory = ", cache
	efficiency = (float(hit_count)/(hit_count+miss_count))*100
	print "Hit Rate = ",efficiency

elif algo is 2:
	cache = []    #tag cache memory
	instr_data = []    #instruction cache memory
	hit_count = 0
	miss_count = 0
	k = 0
	flag = 0
	phyadd = []
	mainmem = []

	print "-----------------------------------------------------"
	print "The size of main memory in bytes is : 64"
	print "The size of cache memory in bytes is : 16"
	print "The line size is : 1"
	print "Cache placement algorithm is : Fully Set Associative"
	print "Number of Sets : 1"
	print "Replacement Policy - FIFO, Random and LRU"
	print "Write Policy is Write Back"
	print "-----------------------------------------------------"
	########## Fully Associative Cache #############
	for j in range(32):
		cache.append(["xxxxx"])
	
	print cache
	for m in range(32):
		instr_data.append(["xxxxx"])
	
	print instr_data

	################ Access Physical Address ###############
	pf = open("phyadd.txt","r")
	phy = pf.readlines()
	for line in phy:
		addr = int(line)
		phyadd.append(addr)
	print "Physical Address - ",phyadd

	################ Access Instructions ##################
	mf = open("main_mem.txt","r")
	main = mf.readlines()
	for line in main:
		inst = int(line)
		mainmem.append(inst)
	print "Main Memory Instructions - ",mainmem

	################# Random Replacement Policy ###########
	if rp is 1:
		for i in phyadd:
			str = int(i)
			print "pa = ",str
			str1 = int(31)
			print "str1 = ",str1
			bits = (str & str1)
			bit = format(bits, 'b').zfill(7) # binary number
			print "bits = ",bit
			num = int(bit,2)     #covert binary to int
			print "setnumber = ",num
			if cache[num] != str:
				instr_data[num] = mainmem[str]
				print "Instruction = ",instr_data
				cache[num] = str
				miss_count = miss_count + 1
				print "miss_count = ",miss_count
			elif cache[num] == str:
				hit_count = hit_count+1
				print "hit_count = ",hit_count
			print "Cache = ",cache
			print "------------------------------------"
	elif rp is 2:
		for i in phyadd:
			print "Physical Address = ",i
			for j in cache:
				if j == i:
					flag = 0
					hit_count = hit_count+1
					print "hit_count = ",hit_count
					k = k
					print "k = ",k
					break
				elif j != i:
					flag = 1
			
			if flag is 1:	
				cache[k] = i
				instr_data[k] = mainmem[i]
				miss_count = miss_count+1
				print "miss_count = ",miss_count
				if k < 32:
					k = k+1
					print "k = ",k
				else:
					k = 0
			print "Cache = ",cache
			print "Instruction = ",instr_data
			print "------------------------------------"
		
	########################## Final Result #########################
	print "-------------------- Final Result of fully associative Cache -------------------------"
	print "Cache Memory = ", cache
	efficiency = (float(hit_count)/(hit_count+miss_count))*100
	print "Hit Rate = ",efficiency

	pf.close()
	mf.close()
	
elif algo is 3:
	if rp is 1:
		board1 = []    #tag cache memory
		board2 = []    #instruction cache memory
		hit_count = 0
		miss_count = 0
		phyadd = []
		mainmem = []

		#initializing tag memory with 0's
		for j in range(8):
			board1.append(["xxxxx"] * 4)
	
		#initializing instruction memory with 0's
		for i in range(8):
			board2.append(["xxxxx"] * 4)
	
		#function for tag memory
		def tag(board1):
			for row in board1:
				print " ".join(row)
		
		#function for instruction memory		
		def instr(board2):
			for row in board2:
				print " ".join(row)

		print "Let's begin Cache Simulator : "
		################ Cache Memory Initialize ###################
		print "Tag Memory"
		tag(board1)
		print "------------------------"
		print "Instruction Memory"
		instr(board2)
		print "-----------------------------------------"
		print "Access Physical Address and main memory"
		################ Access Physical Address from CPU ###############
		pf = open("phyadd.txt","r")
		phy = pf.readlines()
		for line in phy:
			addr = int(line)
			phyadd.append(addr)
		print "Physical Address - ",phyadd

		mf = open("main_mem.txt","r")
		main = mf.readlines()
		for line in main:
			inst = int(line)
			mainmem.append(inst)
		print "Main Memory Instructions - ",mainmem

		################### Start Cache #######################
		for i in phyadd:
			str = i
			print "pa = ",str
			str1 = 12
			print "str1 = ",str1
			str2 = 3
			print "str2 = ",str2
			bits = (str & str1) >> 2
			bit = format(bits, 'b').zfill(8) # binary number
			print "bits = ",bit
			num = int(bit,2)     #covert binary to int
			print "setnumber = ",num
			num1 = (str & str2)
			print "way number = ",num1
			y = mainmem[str]
			print "Instruction = ",y
			if board1[num][num1] != str:
				board1[num][num1] = str
				board2[num][num1] = mainmem[str] 
				miss_count = miss_count+1
				print board1[num][num1]
				print "miss_count = ",miss_count
			elif board1[num][num1] == str:
				hit_count = hit_count + 1
				print "hit_count = ", hit_count
			print "Tag = ",board1
			print "Instruction = ",board2
			print "###########"
	
		print "--------------------------------Final Cache Results-----------------------------"
		print "Tag = ",board1
		print "Instruction = ",board2
		efficiency = (float(hit_count)/(hit_count+miss_count))*100.0
		print "Hit Rate = ",efficiency,"%"