import sys, re, subprocess
from pyudev import Context, Device

ARGDEVICENAMES=sys.argv
ARGDEVICENAMES.pop(0)
if len(ARGDEVICENAMES)<1:
	print "Usage: python mpt2sas-deviceslots.py sdX [sdY sdZ ... ]"
	sys.exit(1)

diskdevices=[]
context = Context()

SAS2IRCU='/usr/sbin/sas2ircu'

# this gets the serial number of the disk
# 	the from_device_file() method only comes in a later version of pyudev
# 	so we can't argue /dev/sdxyz but we can sdxyz to from_name()
for devicename in ARGDEVICENAMES:
	try:
		diskdevices.append(Device.from_name(context, 'block', devicename))
	except:
		diskdevices.append(None)

sas2ircu_output=subprocess.check_output([SAS2IRCU, '0', 'DISPLAY'])
sas2ircu_disks=re.findall("^Device is a Hard disk.*?^\s+Enclosure\s+#\s+:\s+(\d+).*?^\s+Slot\s+#\s+:\s+(\d+).*?^\s+GUID\s+:\s+(\w+).*?^^", sas2ircu_output, re.DOTALL|re.MULTILINE)

for diskdevice in diskdevices:
	if diskdevice==None:
		print None
	else:
        diskwwn=diskdevice.get('ID_WWN')
        # udev shows the WWN with 0x in front and sas2ircu doesn't
        # so we will remove the 0x before comparing it to sas2ircu
        diskwwn=re.sub('^0x', '', diskwwn)
		diskmodel=diskdevice.get('ID_MODEL')
		if diskmodel=="Virtual_Disk":
			print "{}\tis a virtual disk".format(diskdevice.device_node)
			next
		for disk in sas2ircu_disks:
		        if diskwwn==disk[2]:
		                print "{}\tin Enclosure:Slot {}:{}\tis a {}\tWWN: {}".format(diskdevice.device_node, disk[0], disk[1], diskmodel, diskwwn)
