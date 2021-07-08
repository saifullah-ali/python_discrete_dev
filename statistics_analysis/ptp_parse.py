import time
import os
import re
import statistics
import csv
from datetime import date

today = date.today()
 

ofm_dict = {}
ofm_list = []
mpd_dict = {}
mpd_list = []
calnex_file = ''
parse_flag = 0
dict_entry = 0
print('Please Specify raw data file name:')
data_file_1 = input()
print('Analyzing File ...' + data_file_1 + '...............')
time.sleep(5)
#f= open("RSG2288(Slave-52)Delay=-2,Thresh=20ms_____4(QA1.1)","r")
f= open(data_file_1,"r")

initial_line = f.readline()
print("Raw file starts with string :: "+ initial_line)
initial_line = initial_line[0:5]
if (initial_line == 'trace'):
	print("Raw file is from ros")
else:
	print("Raw file is from calnex")
f.close()



#f= open("RSG2288(Slave-52)Delay=-2,Thresh=20ms_____4(QA1.1)","r")
f= open(data_file_1,"r")
#print(f.read())
for x in f:
	
	if 'OffsetFromMaster' in x:
		#OffsetFromMaster=17, RemoteTime=1619270062 s, MeanPathDelay=613
		ofm_line = re.search("OffsetFromMaster=(.+), RemoteTime=(.+), MeanPathDelay=(.+)", x)
		print(ofm_line[0] + " with ofm value " + ofm_line[1] + " and MeanPathDelay value " + ofm_line[3])
		dict_entry = dict_entry+1
		ofm_dict[dict_entry] = int(ofm_line[1])
		ofm_list.append(int(ofm_line[1]))
		mpd_dict[dict_entry] = int(ofm_line[3])
		mpd_list.append(int(ofm_line[3]))
		if dict_entry == 28800:
		    break
    
	if 'CF Accuracy:Fwd_CF_Accuracy' in x:
		print("Calnex OFM file detected")
		calnex_file = 'ofm_file'
		

	if 'Measured Link Delay:Peer_Delay_Measured_Link_Delay' in x:
		print("Calnex Peer delay file detected")
		calnex_file = 'mpd_file'
		
	if (calnex_file == "ofm_file" and "#" not in x):
		#print(x)y
		parse_flag = 1
		ofm_line = re.search("(.+),(.+)", x)
		print("OFM Value ::", ofm_line[2])
		dict_entry = dict_entry+1
		ofm_dict[dict_entry] = float(ofm_line[2])
		ofm_list.append(float(ofm_line[2]))
		if dict_entry == 28800:
			break

	if (calnex_file == "mpd_file" and "#" not in x):
		#print(x)y
		parse_flag = 2
		mpd_line = re.search("(.+),(.+)", x)
		print("Peer Delay Value ::", mpd_line[2])
		dict_entry = dict_entry+1
		mpd_dict[dict_entry] = float(mpd_line[2])
		mpd_list.append(float(mpd_line[2]))
		if dict_entry == 28800:
			break

f.close()

#print(ofm_dict)
#print(ofm_list)


dict_entry = 0
if parse_flag == 1:
	print('Please Specify Calnex raw data file for Peer Delay :')
	data_file_2 = input()
	print('Analyzing File ...' + data_file_2 + '...............')
	time.sleep(5)
	f= open(data_file_2,"r")
	for x in f:
		if ("#" not in x):
			mpd_line = re.search("(.+),(.+)", x)
			print("Peer Delay Value ::", mpd_line[2])
			dict_entry = dict_entry+1
			mpd_dict[dict_entry] = float(mpd_line[2])
			mpd_list.append(float(mpd_line[2]))
			if dict_entry == 28800:
				break
	f.close()

if parse_flag == 2:
	print('Please Specify Calnex raw data file for OFM :')
	data_file_2 = input()
	print('Analyzing File ...' + data_file_2 + '...............')
	time.sleep(5)
	f= open(data_file_2,"r")
	for x in f:
		if ("#" not in x):
			ofm_line = re.search("(.+),(.+)", x)
			print("OFM Value ::", ofm_line[2])
			dict_entry = dict_entry+1
			ofm_dict[dict_entry] = float(ofm_line[2])
			ofm_list.append(float(ofm_line[2]))
			if dict_entry == 28800:
				break
	f.close()




#Keymax = max(ofm_dict, key=ofm_dict.get)
#print(ofm_dict[Keymax])

max_ofm_value = max(ofm_list)
min_ofm_value = min(ofm_list)
max_min_ofm_value = max_ofm_value - min_ofm_value
mean_ofm_value = statistics.mean(ofm_list)
stdev_ofm_value = statistics.stdev(ofm_list)
outliers_count_upper = len([i for i in ofm_list if i > 50])
outliers_count_lower = len([i for i in ofm_list if i < -50])
outliers_count = outliers_count_upper + outliers_count_lower
perc_outliers = (outliers_count/28800)*100
perc_inliers = (100 - perc_outliers)
ofm_in_range = list(x for x in ofm_list if -50 <= x <= 50)
max_ofm_without_outlier = max(ofm_in_range)
min_ofm_without_outlier = min(ofm_in_range)



print("\n******************************************\n")
print("Maximum ofm value  :",max_ofm_value)
print("Minimum ofm value  :",min_ofm_value)
print("Max -Min ofm value  :",max_min_ofm_value)
print("Mean ofm value  : %.4f" %mean_ofm_value)
print("Standard Deviation of ofm value  : %.4f" %stdev_ofm_value)
print("Number of Samples greater than 50ns (OFM)  :", outliers_count_upper)
print("Number of Samples less than -50ns (OFM)  :", outliers_count_lower)
print("Number of outliers  :", outliers_count)
print("Percentage of outliers  : %.4f" %perc_outliers)
print("Percentage witin 50ns  : %.4f" %perc_inliers)
print("Max OFM without Outlier  :",max_ofm_without_outlier)
print("Min OFM without Outlier  :",min_ofm_without_outlier)


max_mpd_value = max(mpd_list)
min_mpd_value = min(mpd_list)

print("Maximum Mean Path Delay value  :",max_mpd_value)
print("Minimum Mean Path Delay value  :",min_mpd_value)

if perc_inliers > 99.7:
    print("Power Profile Compliance:: YES")
    power_comp = "YES"	
else:
    print("Power Profile Compliance:: NO")
    power_comp = "NO"	
print("\n******************************************\n")
mean_ofm_value = format(mean_ofm_value, '.4f')
stdev_ofm_value = format(stdev_ofm_value, '.4f')
perc_outliers = format(perc_outliers, '.4f')
perc_inliers = format(perc_inliers, '.4f')

def slidingwindow(init_value,step_size):
	end_value = init_value + step_size
	count = 0
	ofm_outof_range = {}
	for n in range(init_value,end_value):
		value = ofm_dict[n]
		if value > 50 or value < -50:
			#print("Outlier value "+ str(value))
			ofm_outof_range[n] = value
			count = count + 1
	if count > 3:
		print("More than 3 outliers in range " + str(init_value) + " to " + str(end_value))	
		print("values are (sample number vs value) :")
		print(ofm_outof_range)
		print("Total Count ::", count)	
	return count

print_string = ""
if power_comp == 'YES':
	print("\nChecking with Sliding window technique......")
	time.sleep(2)
	max_iter = 27800
	if len(ofm_list) < 28800:
		max_iter = (len(ofm_list) - 1000)
	else:
		max_iter = 27800
	for m in range(1,max_iter):
	
		out_value = slidingwindow(m,999)
		if out_value > 3:
			print_string = print_string + "Range " + str(m) + "-" + str(m+ 1000) + " :: " + str(out_value) +"\n"
			print("Range " + str(m) + "-" + str(m+ 1000) + " :: " + str(out_value))
	if print_string == "":
		print("\nNo more than three outliers found between the ranges")
		print_string = "No more than three outliers found between the ranges"
else:
	print("====> No need to check with Sliding window technique.")



sample = 0
if len(ofm_list) < 28800:
	sample = len(ofm_list)
	print("*****Caution:: Less than 28800 samples found*****")
else:
	sample = 28800

date_string = today.strftime("%b-%d-%Y")
data_file_1 = data_file_1.replace(".csv", "")
file_name = data_file_1 +  "output" + ".csv"
with open(file_name, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Test Duration", "8hrs"])
    writer.writerow(["Total Number of Samples", sample])
    writer.writerow(["Max OFM Value", max_ofm_value])
    writer.writerow(["Min OFM Value", min_ofm_value])
    writer.writerow(["Max-Min OFM", max_min_ofm_value])
    writer.writerow(["Max OFM without Outlier", max_ofm_without_outlier])
    writer.writerow(["Min OFM without Outlier", min_ofm_without_outlier])
    writer.writerow(["Mean OFM Value", mean_ofm_value])
    writer.writerow(["Standard Deviation", stdev_ofm_value])
    writer.writerow(["Max Peer Delay", max_mpd_value])
    writer.writerow(["Min Peer Delay", min_mpd_value])
    writer.writerow(["Number of samples greater than 50ns (OFM)", outliers_count_upper])
    writer.writerow(["Number of samples less than -50ns (OFM)", outliers_count_lower])
    writer.writerow(["Number of Outliers", outliers_count])
    writer.writerow(["Percentage of outliers", perc_outliers])
    writer.writerow(["Percentage withing 50ns", perc_inliers])
    writer.writerow(["Power Profile Compliance", power_comp])
    writer.writerow(["", ""])
    
    if print_string != "":
    	writer.writerow(["Sliding Window - Range vs Outliers", print_string])

print("\n\nOutput Saved on file : " + file_name)