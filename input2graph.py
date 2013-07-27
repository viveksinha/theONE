import os, string

dir1 = ["1.2", "2.1", "2.2"]
#os.makedirs("DelProb")
#os.makedirs("DetectTime")
for dirs in dir1:
  dirlist = os.listdir(dirs + "_Results")
	op1 = open(dirs+"delprobReport.txt","w")
	op2 = open(dirs + "dectimeReport.txt", "w")
	op1.write("case time" + "\n")
	op2.write("case time" + "\n")
	for alldir in dirlist:
		for allfiles in os.listdir(dirs + "_Results/" + alldir):
			ip = open(dirs + "_Results/" + alldir + "/" + allfiles)
						
			if allfiles.startswith("default_scenario_DeliveryProbReport"):
				op = open("DelProb/"+ dirs + "_" + alldir + "i2g.txt","w")
				line = 0
				for eachline in ip:
					if eachline.startswith("M"):
						break
					if line % 5 == 0:
						l1 = string.split(eachline)
						time = str(float(l1[0])/60.0)
						delProb = l1[1]
						op.write(time + " " + delProb+"\n")
					line += 1
				op.close()
			
			if allfiles.startswith("default_scenario_Malicious"):
				op = open("DetectTime/"+ dirs + "_" + alldir + "i2g.txt","w")
				for eachline in ip:
					l1 = string.split(eachline)
					time = str(float(l1[0])/60.0)
					nodenum = l1[2]
					op.write(nodenum + " " + time+"\n")
				op.close()
			'''
			if allfiles.startswith("default_scenario_MessageStatsReport"):
				delprob = ''
				for eachline in ip:
					if "delivery_prob" in eachline:
						delprob = string.split(eachline)[1]
						print alldir, delprob
				op1.write(alldir + " " + delprob + "\n")
			
			if allfiles.startswith("default_scenario_MaliciousDetect"):
				detectionTime = ''
				for eachline in ip:
					if "m_f" in eachline or "m_s" in eachline:
						detectionTime = str(float(string.split(eachline)[0])/60.0)
				op2.write(alldir + " " + detectionTime + "\n")
			'''
			ip.close()
