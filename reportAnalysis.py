import os, sys, subprocess, json
from string import split

eventInterval = ['288,288','200,200','168,168','86,86','56,56','43,43','28,29']
#eventInterval = ['576,576','400,400','336,336','168,168','112,112','86,86','56,58]
endTime = [86400,172800]
nrofCopies = [8]
rngSeed = [1,2,3,4,5,6]
node = []
nodeID = ''
temp = ''
op = open("finalReportAnalysis.txt","w")
for ei in eventInterval:
  for e in endTime:
		for n in nrofCopies:
			msgload = 0
			a_spray = 0
			a_focus = 0
			dectime = 0.0
			delprob = 0
			for r in rngSeed:
				op1 = open( p + "/sortedAnalysis_" + str(ei) +"_" + str(e) +"_" + str(n) + "_" + str(r) + ".txt",'w')
				op2 = open( q + "/nodeID_" + str(ei) +"_" + str(e) +"_" + str(n) + "_" + str(r) + ".txt","w")
				
				directory = str(ei) +"/" + str(e) +"/" + str(n) + "/" + str(r)
				spray = 0
				stime = 0.0
				focus = 0
				ftime = 0.0
				dprob = 0.0
				for files in os.listdir(directory):
					if files.startswith("default_scenario_MaliciousDetectDataReport"):
						ip = open(directory+"/"+files)
						for eachline in ip:
							if "m_s" in eachline:
								spray+=1
								stime = float(split(eachline)[0])
							elif "m_f" in eachline:
								focus+=1
								ftime = float(split(eachline)[0])
						
							
						op.write("------------------------------------------------------------\n")
						op.write("Details for Simulation with E:" + str(e)+" load:" + str(ei) + " C:" + str(n) + " R:" + str(r) + "\n")
						op.write("------------------------------------------------------------\n")
						op.write("Number of spray malicious detected = "+str(spray)+"\n")
						op.write("Number of focus malicious detected = "+str(focus)+"\n")
						op.write("Time taken to detect = "+str(max(stime,ftime)) + "\n")
						ip.close()
						a_spray+=spray
						a_focus+=focus
						dectime+=max(stime,ftime)
					
					if files.startswith("default_scenario_MaliciousDetectDataReport"):
						ip = open(directory+"/"+files)
						for eachline in ip:
							if "m_" not in eachline:
								falseDetection = str(split(eachline)[1])
								op.write("False malicious node detected : " + str(falseDetection) + "\n")
			
					
					if files.startswith("default_scenario_MessageStatsReport"):
						ip = open(directory+"/"+files)
						for eachline in ip:
							if "created" in eachline:
								load = float(split(eachline)[1])
							if "delivery_prob" in eachline:
								dprob = float(split(eachline)[1])
							if "relayed:" in eachline:
								relay = float(split(eachline)[1])
						op.write("Number of messages = "+str(load)+"\n")
						op.write("Delivery Probablity = " + str(dprob)+"\n")
						op.write("Relayed =" str(relay) + "\n")

						ip.close()
						delprob+=dprob
						tlRelay+=relay
                        
                        
					if files.startswith("default_scenario_EventLogReport"):
						ip = open(directory+"/"+files)
						for eachline in ip:
							if "m_f" in str(split(eachline)[2]):
								if "R" in str(split(eachline)[1]):
									stime = str(split(eachline)[0])
									nodeid = str(split(eachline)[2])
									x = str(nodeid + stime)
									nodeid,IDtime = x.split('m_f')
									wiki = json.loads(IDtime)
									node.append(wiki)					
									node.sort()
									
						for i in node:
							kai = str(i)
							y = kai[:3]
							z = kai[3:]
							op1.write("m_f" + str(y) + " " + str(z) + "\n")
							
						ip2 = open(p + "/sortedAnalysis_" + str(ei) +"_" + str(e) +"_" + str(n) + "_" + str(r) + ".txt","r")
						for eachline in ip2:
							if "m_f" in eachline:
								temp = str(nodeID)
								nodeID = str(split(eachline)[0])
								if (str(temp) != str(nodeID)):
									op2.write( str(nodeID) + "\n")
						
					
					
				op1.close()
				op2.close()
				os.system('./relay.sh '"sortedAnalysis/sortedAnalysis_" + str(ei) +"_" + str(e) +"_" + str(n) + "_" + str(r) + ".txt"' '"nodeID/nodeID_" + str(ei) +"_" + str(e) +"_" + str(n) + "_" + str(r) + ".txt"' > '"relayReport/relayReport" + str(ei) +"_" + str(e) +"_" + str(n) + "_" + str(r) + ".txt"'')
				os.system('sort -k2 '"relayReport/relayReport" + str(ei) +"_" + str(e) +"_" + str(n) + "_" + str(r) + ".txt"' | uniq > '"finalRelayReport/finalRelayReport" + str(ei) +"_" + str(e) +"_" + str(n) + "_" + str(r) + ".txt"'')			
							
									
			op.write("############################################################\n")
			op.write("------------------------------------------------------------\n")
			op.write("Average Transfer Details for Simulation with E:"+ str(e)+ " load:" + str(ei) + " C:" + str(n) + "\n")
			op.write("------------------------------------------------------------\n")
			op.write("Number of messages = "+str(load)+"\n")
			op.write("Number of spray malicious detected = "+str(a_spray/6)+"\n")
			op.write("Number of focus malicious detected =  = "+str(a_focus/6)+"\n")
			op.write("Time taken to detect = "+str(dectime/6) + "\n")
			op.write("message relayed = "+str(tlRelay/6)+"\n")
			op.write("Delivery Probablity = " + str(delprob/6)+"\n")
			op.write("------------------------------------------------------------\n")
			op.write("############################################################\n")
