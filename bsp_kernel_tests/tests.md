1. cat /etc/os-release check the sw version type, id, meta data
 - What does /etc/os-release contain?
    It contains key-value pairs with information about the Linux distribution, such as name, version, and ID.
    The distro used below is a custom linux distro based on yocto project, for automotive use
    The id is called fsl-auto which is freescale(now nxp) automotive 
    the name is auto linux bsp showing it is a bsp package for automotive systems
    version is kirkstone which is a release of yocto project 
    project indicates it is a custom project for vpc-p hw by Bosch
    the sw release version is 8.0.0


    root@vpc-p-b1:~# cat /etc/os-release
        ID=fsl-auto
        NAME="Auto Linux BSP"
        VERSION="38.0 (kirkstone)"
        PROJECT="HMC VPC-P by Robert Bosch GmbH"
        SW_RELEASE_VER="v8.0.0"
        RB_VER_HARDWARE="VPC-P-B1"
        RB_SW_TYPE="VAL_Git#e3b85d8"

if run on ubuntu machine
NAME="Ubuntu"
VERSION="20.04.6 LTS (Focal Fossa)"
ID=ubuntu
ID_LIKE=debian
PRETTY_NAME="Ubuntu 20.04.6 LTS"
VERSION_ID="20.04"
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
VERSION_CODENAME=focal
UBUNTU_CODENAME=focal

What is the significance of this file?

    It helps identify the Linux distribution and version.

How does this file differ from uname -a?

    /etc/os-release provides distribution-specific information (like OS name and version), while uname -a focuses on the kernel version and system architecture.


2. ifconfig to check all nw interfaces
What does ifconfig do?

    It displays or configures network interfaces on a system.
    Example: ifconfig shows details like IP address, subnet mask, and MAC address.

What are the key fields in the output of ifconfig?

    inet: IP address of the interface.
    netmask: Subnet mask of the interface.
    RX bytes/TX bytes: Received and transmitted bytes.
    HWaddr: Hardware address (MAC address).

How do you enable or disable an interface using ifconfig?

    Enable: ifconfig <interface> up
    Disable: ifconfig <interface> down

How do you assign an IP address to an interface using ifconfig?

    Example: ifconfig eth0 192.168.1.100 netmask 255.255.255.0

Why is ifconfig deprecated?

    ifconfig is considered outdated and replaced by the ip command from the iproute2 suite, which offers more features and better control.
    Example: ip addr show is the modern equivalent of ifconfig.

How do you check the status of all interfaces using ifconfig?

    Run ifconfig -a to list all interfaces, including inactive ones.

How does ifconfig retrieve interface details?

    It reads data from the /proc/net/dev file and interacts with the kernel via ioctl system calls.

What is the difference between ifconfig's inet and inet6 fields?

    inet: Displays IPv4 address.
    inet6: Displays IPv6 address.

Can ifconfig show packet statistics?

    Yes, it displays RX (received) and TX (transmitted) bytes and error statistics.

What happens if you bring down an interface?

    The interface will stop sending or receiving traffic.
    Example: ifconfig eth0 down will disable the eth0 interface.

How would you troubleshoot a network interface using ifconfig?

    Check if the interface is up.
    Verify the IP address and netmask.
    Look for errors in the RX/TX statistics.

What is the MAC address, and why is it shown in ifconfig?

    The MAC address is the hardware address unique to the interface. It’s used for communication within a local network.

How would you accomplish the same tasks as ifconfig using the ip command?

    Show interfaces: ip addr show.
    Bring up/down an interface: ip link set <interface> up/down.
    Assign IP address: ip addr add 192.168.1.100/24 dev eth0.

Where are the network interfaces stored?
The network interfaces and their statistics are exposed in the /proc/ filesystem, specifically in the file /proc/net/dev.
Command - 
cat /proc/net/dev
It displays a table of all network interfaces with statistics like received/transmitted bytes, packet errors, and drops.

Where are the mac addresses and interface configuration stored?
The MAC address and detailed interface configuration for each network interface are exposed in the /sys/ filesystem under /sys/class/net/<interface_name>/.
To view the mac address
cat /sys/class/net/<interface_name>/address
To view the interface state
cat /sys/class/net/<interface>/operstate

How does ifconfig or ip retrieve this information?

    These tools use ioctl system calls or netlink sockets to communicate with the kernel and fetch data from /proc or /sys.

3. ping tests from board to remote setup
ping 192.168.0.2
Why is ping used?

    Purpose:
        To test network connectivity between two devices.
        To measure packet loss and round-trip time (RTT) between the source and destination.

    How it works:
        It sends ICMP Echo Request packets to the target and waits for ICMP Echo Reply packets.
        The results show the time it takes for packets to travel to the destination and back.

What is ICMP?

    Internet Control Message Protocol: Used for diagnostic and error messages in networking.
    ping uses ICMP to send Echo Request and receive Echo Reply.

How do you specify the number of packets to send with ping?

    Use the -c option:

ping -c 4 google.com

Sends 4 packets and stops.

Example
ping 192.168.0.2

Pinging 192.168.0.2 with 32 bytes of data:
Reply from 192.168.0.2: bytes=32 time=1034ms TTL=64
Reply from 192.168.0.2: bytes=32 time=701ms TTL=64
Reply from 192.168.0.2: bytes=32 time=396ms TTL=64
Reply from 192.168.0.2: bytes=32 time=95ms TTL=64

Command Initiated:

    ping 192.168.0.2: This command sends ICMP Echo Request packets to the IP address 192.168.0.2 and waits for ICMP Echo Reply packets.

Line-by-Line Analysis of Replies:

    Reply from 192.168.0.2: bytes=32 time=1034ms TTL=64
        Reply from 192.168.0.2: The destination responded with an ICMP Echo Reply packet.
        bytes=32: Size of the data sent in the ICMP Echo Request (default is 32 bytes on Windows systems).
        time=1034ms: Round-trip time for the ICMP packet to travel to 192.168.0.2 and back.
        TTL=64: The Time-to-Live value decrements with each router hop. The value 64 indicates how many hops were left when the packet was received.

    Subsequent lines show similar information for each packet sent and received, with varying round-trip times.

Ping Statistics:

    Packets Sent = 4, Received = 4, Lost = 0:
        Four ICMP Echo Request packets were sent, and four ICMP Echo Reply packets were received.
        No packet loss (0% loss).
    Round-Trip Times:
        Minimum = 95ms: Fastest round-trip time recorded.
        Maximum = 1034ms: Slowest round-trip time recorded.
        Average = 556ms: Average of all the round-trip times.

Where is ICMP?

    The ICMP Echo Request packets are sent when you run the ping command.
    The ICMP Echo Reply packets are the "Reply from 192.168.0.2" messages you see in the output.
    ICMP is working in the background to test the connectivity, but it is not explicitly mentioned in the output.

What protocol does ping use?

    ping uses the ICMP protocol.

What is TTL in the ping output?

    TTL (Time-to-Live) represents the number of hops a packet can take before being discarded. It decrements by 1 at each router hop. If TTL reaches 0, the packet is dropped.

What happens if the destination does not respond?

    The ping command will indicate "Request timed out," meaning no ICMP Echo Reply was received.

Why do round-trip times (RTTs) vary?

    RTT varies due to network congestion, routing paths, or hardware performance.

iperf3 -s 
What is iperf3?

    Purpose: iperf3 is a tool for testing network bandwidth, latency, and performance between two endpoints.
    How it works:
        One device acts as the server, and the other as the client.
        The client sends data to the server over a specified protocol (TCP, UDP) and measures throughput, packet loss, jitter, etc.

How to Use iperf3

    Start the Server:
        Run the following command on the server:

    iperf3 -s

    The server listens for incoming connections.

Run the Client:

    Run the client command, specifying the server’s IP:

    iperf3 -c <server-ip>

    This initiates the bandwidth test.

UDP Testing:

    Use the -u flag for testing with UDP:

    iperf3 -c <server-ip> -u

Bidirectional Testing:

    Use the --bidir option to test simultaneous upload and download:

        iperf3 -c <server-ip> --bidir

    Common Options:
        -t: Test duration (default: 10 seconds).
        -p: Specify the port (default: 5201).
        -b: Bandwidth limit for UDP (e.g., -b 100M for 100 Mbps).

What is Measured?

    Throughput:
        Measures the data transfer rate (e.g., Mbps, Gbps).

    Packet Loss:
        In UDP tests, shows the percentage of packets lost during transmission.

    Jitter:
        Measures the variation in packet delay, important for real-time applications.

    Latency:
        Indicates the delay between packets, particularly in UDP tests.

Questions That Could Be Asked
Basic Questions

    What is the difference between iperf and iperf3?
        iperf3 is the updated version with improved features like JSON output and support for bidirectional testing.
        iperf3 is not backward-compatible with iperf.

    How do you start an iperf3 test?
        Start a server with iperf3 -s and a client with iperf3 -c <server-ip>.

    What are the default settings in iperf3?
        Protocol: TCP.
        Test duration: 10 seconds.
        Port: 5201.

Intermediate Questions

    How do you test network bandwidth using UDP?
        Use the -u flag with iperf3 -c <server-ip> -u.

    What is jitter, and why is it important?
        Jitter measures the variation in packet delay. It’s critical for real-time applications like VoIP or video streaming.

    How do you set bandwidth limits in an iperf3 test?
        Use the -b flag (for UDP):

    iperf3 -c <server-ip> -u -b 50M

What does the server output show?

    Data sent/received, throughput (Mbps), and additional stats like packet loss and jitter (for UDP).


iperf3 -c 192.168.0.2 > output.txt 2>&1
Yes, the 2 and 1 in 2>&1 have specific meanings in the context of shell I/O redirection. They refer to file descriptors,
 which are used to manage input and output streams in Unix-like operating systems, including Linux.
iperf3 -c 192.168.0.2 > output.txt 2>&1

    > output.txt:
        >: Redirects stdout (file descriptor 1) to the specified file (output.txt in this case).
        By default, stderr (file descriptor 2) is not redirected and will still appear in the terminal.
        Any normal output of the iperf3 command will be written to this file.

    2>&1:
        Redirects stderr (standard error) to the same location as stdout.
        Since stdout is already redirected to output.txt, this ensures that both normal output and error messages go into output.txt.

Example
iperf3 -s
-----------------------------------------------------------
Server listening on 5201
-----------------------------------------------------------
Accepted connection from 192.168.0.2, port 49532
[  5] local 192.168.0.1 port 5201 connected to 192.168.0.2 port 49532
[ ID] Interval           Transfer     Bandwidth
[  5]   0.00-1.00   sec  1.10 MBytes  9.21 Mbits/sec
[  5]   1.00-2.00   sec  1.18 MBytes  9.90 Mbits/sec
[  5]   2.00-3.00   sec  1.15 MBytes  9.67 Mbits/sec
[  5]   3.00-4.00   sec  1.14 MBytes  9.56 Mbits/sec
[  5]   4.00-5.00   sec  1.12 MBytes  9.42 Mbits/sec
[  5]   5.00-6.00   sec  1.13 MBytes  9.49 Mbits/sec
[  5]   6.00-7.00   sec  1.16 MBytes  9.72 Mbits/sec
[  5]   7.00-8.00   sec  1.15 MBytes  9.65 Mbits/sec
[  5]   8.00-9.00   sec  1.17 MBytes  9.82 Mbits/sec
[  5]   9.00-10.00  sec  1.13 MBytes  9.49 Mbits/sec
[  5]  10.00-10.00  sec  0.00 Bytes   0.00 bits/sec
-----------------------------------------------------------
Test Complete. Summary:
[ ID] Interval           Transfer     Bandwidth
[  5]   0.00-10.00  sec  11.5 MBytes  9.63 Mbits/sec                  sender
[  5]   0.00-10.00  sec  11.4 MBytes  9.60 Mbits/sec                  receiver
-----------------------------------------------------------

iperf3 -c 192.168.0.1

Connecting to host 192.168.0.1, port 5201
[  5] local 192.168.0.2 port 49532 connected to 192.168.0.1 port 5201
[ ID] Interval           Transfer     Bandwidth
[  5]   0.00-1.00   sec  1.10 MBytes  9.21 Mbits/sec
[  5]   1.00-2.00   sec  1.18 MBytes  9.90 Mbits/sec
[  5]   2.00-3.00   sec  1.15 MBytes  9.67 Mbits/sec
[  5]   3.00-4.00   sec  1.14 MBytes  9.56 Mbits/sec
[  5]   4.00-5.00   sec  1.12 MBytes  9.42 Mbits/sec
[  5]   5.00-6.00   sec  1.13 MBytes  9.49 Mbits/sec
[  5]   6.00-7.00   sec  1.16 MBytes  9.72 Mbits/sec
[  5]   7.00-8.00   sec  1.15 MBytes  9.65 Mbits/sec
[  5]   8.00-9.00   sec  1.17 MBytes  9.82 Mbits/sec
[  5]   9.00-10.00  sec  1.13 MBytes  9.49 Mbits/sec
-----------------------------------------------------------
Test Complete. Summary:
[ ID] Interval           Transfer     Bandwidth
[  5]   0.00-10.00  sec  11.5 MBytes  9.63 Mbits/sec                  sender
[  5]   0.00-10.00  sec  11.4 MBytes  9.60 Mbits/sec                  receiver
-----------------------------------------------------------

Q. why is iperf3 test even needed
Modern vehicles use Ethernet for in car communication.
Testing bandwidth ensures that infotainment systems, cameras, sensors, and ECU (Electronic Control Unit) 
communications work without bottlenecks.
Vehicle-to-Vehicle (V2V) and Vehicle-to-Everything (V2X) Communication:

Automotive systems often rely on real-time communication between vehicles or with infrastructure (e.g., traffic lights, road sensors).
Knowing the bandwidth ensures that these systems can handle the required data transmission rates without delays or packet loss, which is critical for safety.

Q. What is bandwidth
Bandwidth is the maximum amount of data that can be transmitted over a network connection in a given amount of time.
 It is usually measured in bits per second (bps), such as Mbps (Megabits per second) or Gbps (Gigabits per second). 
Bandwidth is often confused with network speed. While bandwidth is the maximum data transfer rate, 
speed refers to how quickly data actually travels through the network.

Q. How to increase the bandwidth is increased
Use routers, switches, and NICs (Network Interface Cards) that support higher bandwidth, such as Gigabit Ethernet or 10-Gigabit Ethernet.
Example: Upgrading from a 100 Mbps switch to a 1 Gbps switch increases available bandwidth.
Use network monitoring tools like Wireshark to identify bottlenecks and high-usage devices.

4. to test the services
systemctl is a command-line utility to control and inspect the systemd system and service manager.
It’s used to manage system services, check their statuses, and control their lifecycle (start, stop, restart, enable, disable, etc.).
systemctl list-units --type=service
Purpose: Lists all active services (units of type service) currently loaded by systemd.

systemctl start <service-name>
Purpose: Starts the specified service immediately.
Example:

systemctl start nginx

    Starts the nginx service.

Key Note:

    This does not enable the service at boot. It only starts the service for the current session.

systemctl stop <service-name>
 systemctl stop <service-name>

    Purpose: Stops the specified service immediately.
    Example:

systemctl stop nginx

    Stops the nginx service.

systemctl status <service-name>

    Purpose: Displays detailed information about the current status of a service.

    Example:

systemctl status nginx

Output Includes:

    Whether the service is active, inactive, or failed.
    The main process ID (PID) of the service (if running).
    Logs from the service.

Example Output:

● nginx.service - A high performance web server
   Loaded: loaded (/lib/systemd/system/nginx.service; enabled)
   Active: active (running) since Tue 2025-01-27 10:00:00 IST; 3min ago
  Main PID: 1234 (nginx)
     Tasks: 3
   Memory: 10.1M
      CPU: 200ms


Status can be used for debugging purpose, say i want to test a certain service, but then i get an error saying the service is not available, or a timeout error
then i can use status command to check whether it is enabled or not
And if it is not enabled, then we can use start to start the service
Now stop will be used, when say a certain service is using to much cpu load, to free up some memory, 
Now we have systemctl start service, and systemctl enable service, the difference between the 2 is that, when you run start service it will start the service at that time, but 
when you enable a service that service will be enabled in boot process, even if you do multiple reboots the service will still be available, but with start it is only valid for that
timebeing, once you do reboot that service is again disabled
similarly stop will stop the service for one boot, disable will stop the service for all boots

5. to get system info
uname -a

6. kernel info
uname -r

7. memory test
memtester 1G 3

8. fdisk -l 
to check the disk partioning

9. cpu info and memory info
cat /proc/cpuinfo
cat /proc/meminfo

10. to check mounted devices
df -h

11. list the kernel modules
lsmod

12. list the block devices
lsblk

13. disk usage 
du -sh <fol_name>

can send can0 123#5665352738
candump can0

gpio detect
can detect


14. eol testing
uds ip sid did

userspace

