from sys import argv
from os.path import exists

script,from_file,to_file = argv

print "copying from %s to %s " % (from_file,to_file)

# we could do these two on one line too,how?
in_file = open(from_file)
indata = in_file.read()

print "the input file is %d bytes long" % len(indata)

print "does the output file exist? %r" % exists(to_file)
print "ready,hit return to continue,ctrl-c to abort."
raw_input()

out_filt = open(to_file,'w')
out_filt.write(indata)

print "alright,all done."

out_filt.close()
in_file.close()
