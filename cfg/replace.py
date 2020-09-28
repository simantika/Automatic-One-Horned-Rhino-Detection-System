#input file
fin = open("/home/sccaec2/Documents/yolov3/cfg/cd53s-yolov3.cfg", "rt")
#output file to write the result to
fout = open("/home/sccaec2/Documents/yolov3/cfg/cd53s-yolov3-mish.cfg", "wt")
#for each line in the input file
for line in fin:
	#read replace the string and write to output file
	fout.write(line.replace('leaky', 'mish'))
#close input and output files
fin.close()
fout.close()
