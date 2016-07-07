cmd_arch/arm/lib/io-readsw-armv4.o := /home/manjusaka/all_codes/ll80/prebuilts/gcc/linux-x86/arm/arm-eabi-4.8/bin/arm-eabi-gcc -Wp,-MD,arch/arm/lib/.io-readsw-armv4.o.d  -nostdinc -isystem /media/2Tdata/souce_code/6580l1_vf/prebuilts/gcc/linux-x86/arm/arm-eabi-4.8/bin/../lib/gcc/arm-eabi/4.8/include -I/media/2Tdata/souce_code/6580l1_vf/kernel-3.10/arch/arm/include -Iarch/arm/include/generated  -Iinclude -I/media/2Tdata/souce_code/6580l1_vf/kernel-3.10/arch/arm/include/uapi -Iarch/arm/include/generated/uapi -I/media/2Tdata/souce_code/6580l1_vf/kernel-3.10/include/uapi -Iinclude/generated/uapi -include /media/2Tdata/souce_code/6580l1_vf/kernel-3.10/include/linux/kconfig.h -D__KERNEL__ -mlittle-endian  -I/media/2Tdata/souce_code/6580l1_vf/kernel-3.10/drivers/misc/mediatek/mach/mt6580/include  -D__ASSEMBLY__ -mabi=aapcs-linux -mno-thumb-interwork -marm -D__LINUX_ARM_ARCH__=7 -march=armv7-a  -include asm/unified.h -msoft-float -gdwarf-2         -c -o arch/arm/lib/io-readsw-armv4.o arch/arm/lib/io-readsw-armv4.S

source_arch/arm/lib/io-readsw-armv4.o := arch/arm/lib/io-readsw-armv4.S

deps_arch/arm/lib/io-readsw-armv4.o := \
  /media/2Tdata/souce_code/6580l1_vf/kernel-3.10/arch/arm/include/asm/unified.h \
    $(wildcard include/config/arm/asm/unified.h) \
    $(wildcard include/config/thumb2/kernel.h) \
  include/linux/linkage.h \
  include/linux/compiler.h \
    $(wildcard include/config/sparse/rcu/pointer.h) \
    $(wildcard include/config/trace/branch/profiling.h) \
    $(wildcard include/config/profile/all/branches.h) \
    $(wildcard include/config/enable/must/check.h) \
    $(wildcard include/config/enable/warn/deprecated.h) \
    $(wildcard include/config/kprobes.h) \
  include/linux/stringify.h \
  include/linux/export.h \
    $(wildcard include/config/have/underscore/symbol/prefix.h) \
    $(wildcard include/config/modules.h) \
    $(wildcard include/config/modversions.h) \
    $(wildcard include/config/unused/symbols.h) \
  /media/2Tdata/souce_code/6580l1_vf/kernel-3.10/arch/arm/include/asm/linkage.h \
  /media/2Tdata/souce_code/6580l1_vf/kernel-3.10/arch/arm/include/asm/assembler.h \
    $(wildcard include/config/cpu/feroceon.h) \
    $(wildcard include/config/trace/irqflags.h) \
    $(wildcard include/config/smp.h) \
    $(wildcard include/config/cpu/use/domains.h) \
  /media/2Tdata/souce_code/6580l1_vf/kernel-3.10/arch/arm/include/asm/ptrace.h \
    $(wildcard include/config/arm/thumb.h) \
  /media/2Tdata/souce_code/6580l1_vf/kernel-3.10/arch/arm/include/uapi/asm/ptrace.h \
    $(wildcard include/config/cpu/endian/be8.h) \
  /media/2Tdata/souce_code/6580l1_vf/kernel-3.10/arch/arm/include/asm/hwcap.h \
  /media/2Tdata/souce_code/6580l1_vf/kernel-3.10/arch/arm/include/uapi/asm/hwcap.h \
  /media/2Tdata/souce_code/6580l1_vf/kernel-3.10/arch/arm/include/asm/domain.h \
    $(wildcard include/config/io/36.h) \
  /media/2Tdata/souce_code/6580l1_vf/kernel-3.10/arch/arm/include/asm/opcodes-virt.h \
  /media/2Tdata/souce_code/6580l1_vf/kernel-3.10/arch/arm/include/asm/opcodes.h \
    $(wildcard include/config/cpu/endian/be32.h) \

arch/arm/lib/io-readsw-armv4.o: $(deps_arch/arm/lib/io-readsw-armv4.o)

$(deps_arch/arm/lib/io-readsw-armv4.o):
