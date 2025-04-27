linux boot process

so once we power on the system
and power is shared among diff units, bios(basic ip op system) or uefi(unified extensible firmware interface) is the first
component that is initialized
once bios is in it does the post test zto check the harware, once this is done
it locates the bootable device and loads the bootloader
once bootloader is loaded, bootloader is repso to load the kernel
once kernel is init , it mounts the initial root file system
also does the hadrware intialization
once initramfs is mounted, it has tools and scripts to mount the root file system
then it starts the init process, here all the startup applications starts and we get the user login

kernel is the main com of linix os
it is responsible for MPHDF
kernel is repsonsible to communicate with the harware

kernel space - this is where kernel operates
can directly modify hw, conf, andy files
kernel issues if any wrong address is conf or accessed it can cause kernel panics
userspace - here user applications are present
need to perform system call
no panic issues since this cannot modify the hw

file system
/ root file system
/home user directory
/bin all the user binaries like ls cp are present here
/sbin all the system binaries are present here
/tmp all the temporary files are present here
/boot all the bootable devices are present here
/mount all the mounted devices are present here
/dev all the device drivers are present here
/etc all the configuration files are present here


to add a mounted device
insert ur usb
check if usb is detected using dmesg | tail this will give all kernel info
then create a folder inside mount/usb
# now check for ur device loc using lsblk(since usb is  a block device)
then mount using sudo mount /dev/sdb1 /mount/usb
once the process is done check whether it actually mounted using df -h
this will show all the mounted devices, also freee disk space

there are diff file systems ext4, nfs, xtfs

processor is basically the brain of a comp, it is responsible to execute programs
microprocessor is nothing but  a compact processor, where all units are present on a single chip

microcontroller has processor, io, memory everything, like a mini comp, but here
u can only perform one operation, it is used in washing machines, ac remote, here u cant perform
real time complex operations

risc - reduced ins set comp 
cisc - complex ins set comp
arm - advanced risc
in risc incrustions are simpler, and not excessive comp is required
in cisc a single ins can take multiple operations like in 

arm is just a company that makes risc based processor

harvard here we have diff loc in memory for data and ins, and diff buses for data and ins - arm cortex m7
von neumann here we have same loc in meory for datat and ins so computation speed is more arduido, intel processor


8085 up 
8 bit up
16 bit address bus
genral b,c,d,e,h,l
special pc,sp,ir,a,
40 pin 

instruction cycle - fetch decode execute
during fetch u get the opcode this is svaed in instruction register
then ir gives this opcode to td
then timing and contol unit performs necessary operation and we get the op
once the progrm starts pc is intiali, it will save the address of the prog, and give the address to the address but, add bus will got ot the add, control bus says what to do euther read or write, then data bus will take or put the data, add, data, contol together are system bus
components of a cpu
alu
control unit
registers
bus interface unit
cache unit
id 
ir

how to install linux
download iso
on vm add the iso
install ununtu or whichever disto u need , u download the iso for the specific
when i put iso in vm, the vm treats iso as a virtual cd/dvd usb

normally
u need a device
iso internal organization of standarization is a compact file which contains all contents present in a dvd/usb etc
then mount using rufus tool
f12 bios init
boot from selct the bootable device
then install ubuntu
do the disk part
netwok ini
file system type
ready to use

sudo apt update
sudo yum chekc-update

sudo apt upgrade
sudo yum update

sudo apt full-upgrade
sudo yum upgrade

sudo apt remove pkg
sudo yum remove
sudo apt install pk
sudo yum install


rpm
sudo rpm -ivh pkg-name
sudo rpm -Uvh pkg name
to check for pkg sudo -q pkg-name
to check for all installed packaes - sudo rpm-qa
to verify a package - sudo rpm -V PKG NAME
to list all files in a package - sudo rpm -vl pkg-name
to list dependencies of a package sudo rpm -vR pkg-name
to remove a package sudo rpm -e pkg-name
to list info abt the package sudo -qi pkg-name
# CHECK OTHER COMMANDS 

system commands

to get system info uname -a
uname -r
to get no of mounted devices df -h
to get disk partitioning fdisk -l
to save command op in a variable result = $command
# to check if a command gives proper op - echo $?

to check kernel config
bitbake virtual/kernel -c menuconfig
to rebuild
bitbake -c compile -f virtual/kernel

yocto build system used to create custom linux distro
open source free and has a good commi support

yocto
poky - build system
bitbake - command /tool to build images
image is basically bin files which will help us cretae  a linux os

meta - these are folders/layers which will have source code, recipe files, and conf files
eg meta-bsp meta-kernel
bsp board support package
this will basically help os understand where is the harwarew, whats is the conf, so that we could use it
now bsp will have dtb files, this is harware conf files
eg &gmac {
    status = "okay";
    phy-mode = "rgmii";
    reg = "0x4000 0x100"
    compatibility
    tx-delay = <0x0>
    rx-delay = <0x0>
    interrupts
    clock-speed

}

kernel conf - menuconfig
recipe files are basically inst which will tell bitbake what to do
fetch
compile
execute
menuconfig

device drivers we enable for gmac ethernet com gigabit multimedia access controller mac layer
osi 
application
prese
sessio
tran
netw
data linke mac
hw

protocol to com from mac to hw
# rgmii reduced gigabit media ind interface

uboot conf
uEnv.txt
kernel
dtb
where to boot from based on command
baudrate


gpio, gmac, mdio, pfe

to test
ping tets
iperf3
netstat
ifconfig
dmesg | grep 'eth0'

bsp tests

1. ping tests4
2. ifconfig
# 3. sytemctl to test the services like status, start, stop, 
systemd is the system and service manger
systemctl status app-start
systemctl status bac

memtester 1G 3

cat /etc/os-release
# Check what else commands we have

# eol tests - to check the basic function
can, gpio, ethernet, pmic, adc, sensor_temp, emmc,

xts(we run commands from user space)
diagnostics test, uds(user data gram pro) 
sevice id and the did
target test ip
service which service and data 
next kernel will get the commands
and send us the response

openpyxl
flashign dll voltrcraft pps putty pyserial jinja2 matplotlib pandas seaborn plotly 
artifactory jfrog artifactory meta dat url jfrog_key tftp win32com canoe subprocess.run
configparser config.ini 
argparse 
coloroma 
logging erro, warning, abort, debug
reportslab pdf documents from tex file
cprofile 
vscode for debugging
try except 
filenotfound
valuerror
timeouterror
keywordinterrupt
assertionerror
typerror
ioerror
re.search


gtest
c code
class 
mock_method(funcname, new_functio)

test{
    class_1 obj1

}

jenkiing build is done, then i added a step in the pipeline to save the binrie into jenking workspace


























