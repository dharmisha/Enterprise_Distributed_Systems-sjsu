import psutil
import csv
import collections
from operator import itemgetter,attrgetter

netstat=psutil.net_connections(kind='tcp')  				# network socket monitoring tool that can check how many TCP sockets are being created by a web application
groupingPID=sorted(netstat,key=attrgetter('pid'))			# Grouped PID together
counts= collections.Counter(t[6] for t in groupingPID)			# using counter to count the same PIDs
datasorted=sorted(groupingPID,key=lambda t:counts[t[6]],reverse=True)   # sort the output in descending order,by the number of the connections per process
#datasorted=sorted(groupingPID,key=lambda t:counts[t[6]])		# uncomment this line to sort the output in ascending order, by the number of the connections per process
with open('output_socket_monitoring.csv', 'w') as f:			# writing data to csv
    w = csv.writer(f)
    w.writerow(('pid', 'laddr', 'raddr', 'status'))    			# field header
    for data in datasorted:
	if (len(data.laddr)!=0 and len(data.raddr)!=0):			# writing only those rows for which laddr and raddr values exist
    		w.writerows([(data.pid,data.laddr,data.raddr,data.status)]) #writing field values in csv


