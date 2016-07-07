cmd_arch/arm/kernel/mt_cache_v7.o := /home/manjusaka/all_codes/ll80/prebuilts/gcc/linux-x86/arm/arm-eabi-4.8/bin/arm-eabi-gcc -Wp,-MD,arch/arm/kernel/.mt_cache_v7.o.d  -nostdinc -isystem /media/2Tdata/souce_code/6580l1_vf/prebuilts/gcc/linux-x86/arm/arm-eabi-4.8/bin/../lib/gcc/arm-eabi/4.8/include -I/media/2Tdata/souce_code/6580l1_vf/kernel-3.10/arch/arm/include -Iarch/arm/include/generated  -Iinclude -I/media/2Tdata/souce_code/6580l1_vf/kernel-3.10/arch/arm/include/uapi -Iarch/arm/include/generated/uapi -I/media/2Tdata/souce_code/6580l1_vf/kernel-3.10/include/uapi -Iinclude/generated/uapi -include /media/2Tdata/souce_code/6580l1_vf/kernel-3.10/include/linux/kconfig.h -D__KERNEL__ -mlittle-endian  -I/media/2Tdata/souce_code/6580l1_vf/kernel-3.10/drivers/misc/mediatek/mach/mt6580/include  -D__ASSEMBLY__ -mabi=aapcs-linux -mno-thumb-interwork -marm -D__LINUX_ARM_ARCH__=7 -march=armv7-a  -include asm/unified.h -msoft-float -gdwarf-2         -c -o arch/arm/kernel/mt_cache_v7.o arch/arm/kernel/mt_cache_v7.S

source_arch/arm/kernel/mt_cache_v7.o := arch/arm/kernel/mt_cache_v7.S

deps_arch/arm/kernel/mt_cache_v7.o := \
    $(wildcard include/config/l1c/opt.h) \
  /media/2Tdata/souce_code/6580l1_vf/kernel-3.10/arch/arm/include/asm/unified.h \
    $(wildcard include/config/arm/asm/unified.h) \
    $(wildcard include/config/thumb2/kernel.h) \

arch/arm/kernel/mt_cache_v7.o: $(deps_arch/arm/kernel/mt_cache_v7.o)

$(deps_arch/arm/kernel/mt_cache_v7.o):
