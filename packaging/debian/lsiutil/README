
******************************************************************************
                                 LsiUtil_ReadMe.txt
******************************************************************************

This file presents general information about the LsiUtil utility for Windows,
Linux and Solaris.  

This file is divided into the following sections:
   Introduction
       Features
       LSI Logic Devices Supported
   Description
       Menu Operation
       Command Line Operation



1.0 Introduction
................


LsiUtil is a firmware download and diagnostic utility that can be used with
Windows, Linux, Solaris and DOS environments.  

1.1 Features
............

LsiUtil supports:


o  All SCSI, SAS and Fiobre Channel Host Adapters from LSI NSPG.
o  Identifies and updates the firmware or BIOS images. 
o  Allows Flash to be completely erased.
o  Allows configuration of all HBA and firmware parameters.
o  Provides system level debug tools. 
o  Supports command line execution.

1.2 LSI Logic FC Devices Supported
...................................

o  All LSI MPT Fusion (tm) SCSI chips and HBAs
o  All LSI Fibre Channel chips and HBAs
o  All LSI SAS chips and HBAs


2.0 Description 
...............

LsiUtil supports updating the LSI Logic Fusion-MPT (TM) based Firmware 
and/or BIOS, for chips and HBAs that use FLASH. 

The utility is supported with binaries in several OS environments:

Windows:  lsiutil.exe 
Linux: lsiutil 
Solaris: lsiutil
DOS: lsiutil.exe 

The utility requires the LSI host adapter driver to be installed and 
loaded. 

To run LsiUtil: 

Copy lsiutil to C:\  or /usr/sbin/ Windows or Linux respectively.   

Open and command prompt. 
Command prompt C:\>. 
Type lsiutil and press Enter.  

2.1 Operation
.............

The main window provides a selction of chip/HBA ports. Dual channel cards will 
have two entries (chips) displayed on this screen.  Since both channels of a
dual channel board share a flash part, only one of the paths needs to be 
chosen.  However, no harm will be done if separate updates are done through 
both.  This screen appears as:


C:\>lsiutil

LSI Logic MPT Configuration Utility, Version 1.52, September 7, 2007

6 MPT Ports found

     Port Name         Chip Vendor/Type/Rev    MPT Rev  Firmware Rev  IOC
 1.  Scsi Port 0       LSI Logic 53C1030 B2      102      01032700     0
 2.  Scsi Port 1       LSI Logic 53C1030 B2      102      01032700     1
 3.  Scsi Port 5       LSI Logic FC949E A1       105      01031400     0
 4.  Scsi Port 6       LSI Logic FC949E A1       105      01031400     1
 5.  Scsi Port 7       LSI Logic FC919X A0       103      01021700     0
 6.  Scsi Port 8       LSI Logic SAS1068 B0      105      01160000     0

Select a device:  [1-6 or 0 to quit] 0

    
Once a chip has been chosen, another menu list will be displayed as follows:

 1.  Identify firmware, BIOS, and/or FCode
 2.  Download firmware (update the FLASH)
 4.  Download/erase BIOS and/or FCode (update the FLASH)
 8.  Scan for devices
10.  Change IOC settings (interrupt coalescing, EEDP)
13.  Change FC Port settings
16.  Display logged-in devices
20.  Diagnostics
21.  RAID actions
22.  Reset bus
23.  Reset target
30.  Beacon on
31.  Beacon off
42.  Display operating system names for devices
43.  Diagnostic Buffer actions
60.  Show non-default settings
61.  Restore default settings
69.  Show board manufacturing information
98.  Reset FC link
99.  Reset port
 e   Enable expert mode in menus
 p   Enable paged mode in menus
 w   Enable logging


Main menu, select an option:  [1-99 or e for expert or 0 to quit]
    

- The Identify firmware, BIOS, and/or FCode option displays the version 
  number of the current Fusion-MPT Firmware or the Fusion-MPT BIOS residing on 
  the adapter.  If multiple BIOS images are present (Fusion-MPT BIOS w/EFI BSD 
  or Fusion-MPT BIOS w/FCode), this option will all versions.

- The Download firmware option prompts for a file name to download. 
  
  Example:  "Enter firmware filename: it_1030.fw"
  
  The firmware file to download may be in the same directory as the lsiutil 
  executable, or a full pathname can be provided. 

  Example:  Enter firmware filename: 
  C:\Fusion-MPT_IT_FW10327_BIOS_50703pt_FLASH_10304\it_1030.fw

- The Download BIOS and/or FCode option also prompts for a file name to download.

  Example:

  "Enter x86 BIOS filename: mptbios.rom"  
  "Enter FCode filename: lsi1030f.rom"
  "Enter EFI BIOS filename:lsimpt.rom"

  If no file is entered and there is currently a version on the card, the current
  BIOS version will be displayed.

  Example:  MPTBIOS-x.xx.xx (xxxx.xx.xx)
  Do you want to preserve the current x86 BIOS?  [Yes or No, default is Yes]

  
3.0 Command Line Operation
..........................

The following command line options are supported by this utility and can be 
used to create an automated process to perform the utility's operations. When no 
command line options are specified, the interactive (menu) is displayed.

      -e                Turn on Expert Mode (more menu options).
      -w, -ww, -www     Log internal operations to lsiutil.log, for debug.
      -y                Answer yes to yes/no questions whose default is yes.
      -n                Answer no to yes/no questions whose default is no.
      -j type[,type]    Include just ports of type 'type' (FC, SCSI, SAS).
      -x                Concatenate SAS firmware and NVDATA files.

Display Options

usage:  lsiutil [ -p portNumber ] [ -u ][ -s ] [ -d ] [ -i ] [ -b ]
      -p portNumber     Specify the port number to operate on.
                        If not specified, all ports are used.
      -u                Use untagged, rather than tagged, SCSI commands.
      -s                Scan for and display all targets.
      -d                Dump all config pages.
      -i                Display port settings.
      -b                Show board manufacturing information.
      -m freq[,time]    Monitor port performance, updating the display
                        every 'freq' seconds, for 'time' seconds.

Examples:

1. to display the port settings and targets for port 1:
       lsiutil -p 1 -i -s
2. to display the targets found on all known ports:
       lsiutil -s

Operational Options

usage:  lsiutil -p portNumber [ -l linkSpeed ] [ -t topology ]
                              [ -c timeout,depth ] [ -r ]
      -p portNumber     Specify the port number to operate on.
                        Required parameter for operational options.
      -l linkSpeed      Set link speed.  Valid options for linkSpeed are:
                            'a'     Auto link speed negotiation
                            '1'     Force 1Gb link speed
                            '2'     Force 2Gb link speed
                            '4'     Force 4Gb link speed
      -t topology       Set topology.  Valid options for topology are:
                            'a'     Auto topology negotiation
                            '1'     Force NL_Port topology
                            '2'     Force N_Port topology
      -c timeout,depth  Set interrupt coalescing values.
                        Timeout is a value in microseconds between
                        1 and 1000.  Depth is a value between 1 and 128.
                        Setting either or both values to zero will
                        disable interrupt coalescing for that port.
      -r                Perform a chip reset on the given port.
      -z                Perform an FC link reset on the given port.
NOTE:  In order for linkSpeed, topology, or interrupt coalescing
       settings to take effect, a chip reset is necessary.

Examples:

1. to force linkspeed to 1Gb on port 2:
       lsiutil -p 2 -l 1
2. to set interrupt coalescing to a timeout of 200ms with
   a depth of 9 and to force N_Port topology on port 1:
       lsiutil -p 1 -c 200,9 -t 2




