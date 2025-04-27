yocto - build system customized linux os

board - ecu(electronic control unit) desktop

we have to enable linux on the board

yocto will help us enable linux os on out board

yocto
 - poky(build system - open source)
 conf, meta folders
 meta - folder/ layer which has source code, conf and recipe file
 this entire folder is responsible for some conf
 meta-bsp
 meta-kernel 
 meta-connectivity

 -  build we use bitbake , tool used to build the recipe files
 recipe files are files which have instructions which helps bitbake understand what to do

 in recipe files we have diff commands
 fetch - used to fetch some source code
 compile - used to compile the source code
 execute - used to execute the source code
 menuconfig - menu used to configure kernel


 board - u have a lot of hw components
 usb to my pc, then it detects it because it has a device drivers installed, but when u are creating your own linux distro, this should be done manually

 gpio, ethernet, mdio

 bsp - board support package

it helps os(linux) to understand the hw

most of the conf is already given to us by manufactur
meta-nxp
meta-freescale

ethernet - 
o/p i should be able to perform ping test

in board - gmac(gigabit media access controller) operates on mac layer/data link layer of the osi model(layer2)

meta-bsp >>  dts files

1. dts (device tree source file) this will tell the os where the hardware is present

.dts
&gmac {
    status = "okay";
    phy-mode = "rgmii";
    reg = <0x4000 0x100> base add size
    clockspeed
    interrupts
    rx-delay
    tx-delay

}

2. kernel configuration - enable the drivers required for the hardware


menuconfig

bitbake virtual/kernel -c menuconfig

device drivers
shared memory
virtualization
boot 
file system

bitbake -c compile -f virtual/kernel

u get new images, kernel.bin
now u reflash it using trace32 or tftp

3. uboot configuration

here u basically provide address, baudrate, offset values, boot devices, 

4. flash the images on the board

ifconfig
ping tests
iperf3
kernel logs
dmesg | grep -i "eth0"



