cmd_arch/arm/boot/dts/K960.dtb := /home/manjusaka/all_codes/ll80/prebuilts/gcc/linux-x86/arm/arm-eabi-4.8/bin/arm-eabi-gcc -E -Wp,-MD,arch/arm/boot/dts/.K960.dtb.d.pre.tmp -nostdinc -I/media/2Tdata/souce_code/6580l1_vf/kernel-3.10/arch/arm/boot/dts -I/media/2Tdata/souce_code/6580l1_vf/kernel-3.10/arch/arm/boot/dts/include -undef -D__DTS__ -x assembler-with-cpp -o arch/arm/boot/dts/.K960.dtb.dts.tmp arch/arm/boot/dts/K960.dts ; /media/2Tdata/souce_code/6580l1_vf/kernel-3.10/scripts/dtc/dtc -O dtb -o arch/arm/boot/dts/K960.dtb -b 0 -i arch/arm/boot/dts/ -i /media/2Tdata/souce_code/6580l1_vf/kernel-3.10/drivers/misc/mediatek/mach/mt6580/K960/dct/dct/ -d arch/arm/boot/dts/.K960.dtb.d.dtc.tmp arch/arm/boot/dts/.K960.dtb.dts.tmp ; cat arch/arm/boot/dts/.K960.dtb.d.pre.tmp arch/arm/boot/dts/.K960.dtb.d.dtc.tmp > arch/arm/boot/dts/.K960.dtb.d

source_arch/arm/boot/dts/K960.dtb := arch/arm/boot/dts/K960.dts

deps_arch/arm/boot/dts/K960.dtb := \
  arch/arm/boot/dts/mt6580.dtsi \
    $(wildcard include/config/base.h) \
    $(wildcard include/config/addr.h) \
  /media/2Tdata/souce_code/6580l1_vf/kernel-3.10/drivers/misc/mediatek/mach/mt6580/K960/dct/dct/cust_i2c.dtsi \
  /media/2Tdata/souce_code/6580l1_vf/kernel-3.10/drivers/misc/mediatek/mach/mt6580/K960/dct/dct/cust_eint.dtsi \

arch/arm/boot/dts/K960.dtb: $(deps_arch/arm/boot/dts/K960.dtb)

$(deps_arch/arm/boot/dts/K960.dtb):
