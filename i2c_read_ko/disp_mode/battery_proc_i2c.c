#include <linux/module.h>
#include <linux/kernel.h>
#include <linux/i2c.h>
#include <mach/mt_gpio.h>
#include <linux/xlog.h>

#include <asm/io.h>
#include <mach/mt_typedefs.h>
#include "ddp_matrix_para.h"

#include <linux/kernel.h> 
#include <linux/mm.h>
#include <linux/mm_types.h>
#include <linux/module.h>
#include <generated/autoconf.h>
#include <linux/init.h>
#include <linux/types.h>
#include <linux/cdev.h>
#include <linux/kdev_t.h>
#include <linux/delay.h>
#include <linux/ioport.h>
#include <linux/platform_device.h>
#include <linux/dma-mapping.h>
#include <linux/device.h>
#include <linux/fs.h>
#include <linux/interrupt.h>
#include <linux/wait.h>
#include <linux/spinlock.h>
#include <linux/param.h>
#include <linux/uaccess.h>
#include <linux/sched.h>
#include <linux/slab.h>
#include <linux/aee.h>

#include <linux/xlog.h>

#include <asm/io.h>
#include <mach/mt_typedefs.h>
#include "ddp_matrix_para.h"

#include "ddp_reg.h"
#include "ddp_rdma.h"
#include "ddp_hal.h"
#include "ddp_debug.h"
#include "ddp_drv.h"

#include <mach/sync_write.h>

#define DISP_REG_GET(reg32) (*(volatile unsigned int*)(reg32))

#define DISP_REG_GET_FIELD(field, reg32, out) \
        do{                           \
              out = ((*(volatile unsigned int*)(reg32) & REG_FLD_MASK(field)) >> REG_FLD_SHIFT(field)); \
          } while(0)  


#define REG_FLD(width, shift) \
    ((unsigned int)((((width) & 0xFF) << 16) | ((shift) & 0xFF)))
#define GLOBAL_CON_FLD_MODE_SEL                                REG_FLD(1, 1)
#define DISP_INDEX_OFFSET 0x0  // must be consistent with ddp_rdma.c



#define DDP_REG_BASE_DISP_RDMA	   0xf4008000
#define DISPSYS_RDMA1_BASE      DDP_REG_BASE_DISP_RDMA			
#define DISP_REG_RDMA_GLOBAL_CON              (DISPSYS_RDMA1_BASE + 0x10)

extern void DISP_HalfVsync(bool enable);
static int __init i2c_rw_init(void)
{
    unsigned int ret = 0;
    DISP_REG_GET_FIELD(GLOBAL_CON_FLD_MODE_SEL, 0 * DISP_INDEX_OFFSET + DISP_REG_RDMA_GLOBAL_CON, ret);;

    printk("%s %d =========== %d\n", __func__, __LINE__, ret);
    return 0;
}

static void __exit i2c_rw_exit(void)
{


}

module_init(i2c_rw_init);
module_exit(i2c_rw_exit);

MODULE_DESCRIPTION("v4l2 driver module for cx2388x based TV cards");
MODULE_AUTHOR("Gerd Knorr <kraxel@bytesex.org> [SuSE Labs]");
MODULE_LICENSE("GPL");
