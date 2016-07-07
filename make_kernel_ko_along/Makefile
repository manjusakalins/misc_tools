obj-m := test.o
#KERNELDIR := /lib/modules/$(shell uname -r)/build
#KERNELDIR := /mnt/data/all_codes/mtk_codes/exocet_jb_6577/kernel
#KERNELDIR := /home/manjusaka/all_codes/ll80/kernel-3.10
KERNELDIR := ./kernel-3.10
CROSS_COMPILE_R :="/home/manjusaka/all_codes/my_codes/kernel_ko/arm-eabi-4.8/bin/arm-eabi-"
PWD := $(shell pwd)
default:
	$(MAKE) -C $(KERNELDIR) M=$(PWD)  CROSS_COMPILE=$(CROSS_COMPILE_R) ARCH=arm modules
clean:
	rm -f *.ko *.mod.c *.mod.o *.o
