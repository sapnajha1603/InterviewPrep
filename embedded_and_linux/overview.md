1. Overview of the Process

The VPC-P/VCU-P project involves generating Linux images for the S32G2 VPC-P board. This is achieved using Yocto, a widely used build system for creating Linux distributions tailored to specific hardware. The process involves cloning repositories, configuring the build environment, and generating the necessary binaries and images.
2. Pre-Requisite Setup

Before starting the build process:

    Install Ubuntu 20.04 or a compatible OSD 6 Linux environment.
    Ensure all necessary Yocto dependencies are installed:

    sudo apt-get install gawk wget git-core diffstat unzip texinfo gcc-multilib build-essential chrpath socat cpio python3 python3-pip python3-pexpect xz-utils debianutils iputils-ping python3-git python3-jinja2 libegl1-mesa libsdl1.2-dev pylint3 xterm python3-subunit mesa-common-dev

3. Repository Setup

Clone the project repository:

git clone https://sourcecode.socialcoding.bosch.com/scm/pavc_mp_dev/vpc-p_up.git

This will fetch the necessary base elements, including:

    Poky: The Yocto Project’s reference distribution.
    meta-openembedded: Provides additional layers for extended functionality.
    meta-alb: Contains SoC-specific elements for the S32G2 hardware.
    meta-bosch: Contains Bosch-specific hardware adaptations and configurations.

4. Running the Setup Script

To set up the build environment and fetch dependencies, run:

./meta-bosch/scripts/Setup_build.sh -i base -m vpc-p-b1 -fcp

Explanation of options:

    -m vpc-p-b1: Specifies the machine type for the S32G2 board.
    -i base: Specifies the type of image to build (e.g., base, eol, val, app).
    -f: Fetches dependencies, such as cloning poky and meta-openembedded.
    -c: Checks out a temporary local branch after cloning.
    -p: Applies any available patches to the fetched repositories.

5. Building the Image

After the initial setup, perform the build:

./meta-bosch/scripts/Setup_build.sh -m vpc-p-b1 -i app -b

This step compiles the source code, integrates the necessary layers, and generates the Linux binaries and images.
6. Role of DTS Files

The Device Tree Source (DTS) files describe the hardware configuration for the kernel. This includes defining peripherals, memory mappings, and clock settings.
During the Yocto build:

    DTS files specific to the S32G2 board are included in the build process.
    These files are essential for the kernel to interact with the hardware components correctly.
    Any modifications to hardware configurations require updates to the DTS files before rebuilding.

7. Yocto Layers and Metadata

Yocto uses a layered architecture:

    Poky: Core build system.
    meta-openembedded: Provides extended functionality like networking tools and utilities.
    meta-bosch: Adds Bosch-specific configurations and hardware adaptations.
    Bitbake Recipes: These are the scripts that Yocto uses to build specific components, such as the kernel, bootloader, or root filesystem.

8. Bitbake Command

Yocto uses bitbake to build the images. When running the Setup_build.sh script with the -b option, it internally triggers bitbake. For example:

bitbake core-image-minimal

This command builds a minimal Linux image for the target hardware.
9. Uploading Conan Images

After building, the binaries and images are uploaded to Artifactory to support project integration:

    Conan packages ensure dependencies are managed and available for the project.
    Automating the upload process simplifies integration with downstream tools.

10. Outputs

Once the build is complete, the output includes:

    Bootloader (e.g., U-Boot): Facilitates the initial hardware setup and kernel boot.
    Kernel Image: The Linux kernel tailored to the hardware.
    Root Filesystem (initramfs): Contains all the necessary binaries, libraries, and configurations for the OS.
    Device Tree Blob (DTB): Compiled DTS file defining hardware configuration.

These files are then flashed to the S32G2 board using flashing scripts (e.g., via Trace32 or Lauterbach tools).
11. Example Build Workflow

    Initial Setup:

./meta-bosch/scripts/Setup_build.sh -i base -m vpc-p-b1 -fcp

Building the Image:

    ./meta-bosch/scripts/Setup_build.sh -m vpc-p-b1 -i app -b

    Uploading Artifacts:
        The build process uploads generated artifacts (e.g., images and binaries) to Artifactory for integration.

12. Flashing to the Board

Once the images are generated:

    Use a flashing script or tool (e.g., Trace32) to flash the binaries and DTB onto the hardware.
    Verify the boot process using UART logs and ensure all peripherals are initialized as per the DTS configuration.

This step-by-step explanation provides an overview of the entire process, from setting up the Yocto environment to generating and flashing Linux images for the S32G2 VPC-P board. Let me know if you need more details or adjustments!
