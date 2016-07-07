#include <linux/module.h>
#include <linux/kernel.h>
#include <linux/i2c.h>
#include <mach/mt_gpio.h>

//#include <asm/uaccess.h>
//for battery
extern int mt_set_gpio_out(unsigned long pin, unsigned long output);
extern int mt_set_gpio_mode(unsigned long pin, unsigned long mode);
extern int mt_set_gpio_dir(unsigned long pin, unsigned long dir);

void lcm_gpio_set(int num, int enable)
{
    mt_set_gpio_mode(num, GPIO_MODE_00);
    mt_set_gpio_dir(num, GPIO_DIR_OUT);
    if (enable)
		mt_set_gpio_out(num, GPIO_OUT_ONE);
	else
		mt_set_gpio_out(num, GPIO_OUT_ZERO);
}
extern void mt_usb_set_vbus(struct musb *musb, int is_on);
static struct delayed_work battery_up_work;
static int index=0;

static void battery_wake_up_work(struct work_struct *work)
{
#define MOD_INT (2)
    if (index%MOD_INT==0 ) {
        printk("%s %d:========== pwr up target\n", __func__, __LINE__);
        lcm_gpio_set(118, 1);
        schedule_delayed_work(&battery_up_work, msecs_to_jiffies(4000));
    } else if(index%MOD_INT == 1){
        printk("%s %d:========== pwr down target\n", __func__, __LINE__);
        lcm_gpio_set(118, 0);
        printk("%s %d:========== sleep to calm down battery\n", __func__, __LINE__);
        schedule_delayed_work(&battery_up_work, msecs_to_jiffies(15*60*1000));
    }
    index++;

    return;
}


#define I2C_RW_NAME "i2c_rw_entry"
static struct i2c_board_info __initdata i2c_rw_dev = {
	I2C_BOARD_INFO(I2C_RW_NAME, 0xfd>>1)
};
static struct i2c_client *i2c_rw_clients[4];
static const struct i2c_device_id i2c_rw_id[] = {{I2C_RW_NAME,0},{}};



/*******************************************************************************
* i2c relative end
********************************************************************************/
static int i2c_rw_probe(struct i2c_client *client, const struct i2c_device_id *id)
{
	printk("============================%s %d, line: %d\n", __func__, __LINE__, client->adapter->nr);

	return 0;
}
static int i2c_rw_remove(struct i2c_client *client)
{
	return 0;
}

struct i2c_driver i2c_rw_driver = {
    .probe = i2c_rw_probe,
    .remove = i2c_rw_remove,
    .driver.name = I2C_RW_NAME,
    .id_table = i2c_rw_id,
};


/*******************************************************************************
* CAMERA_HW_remove
********************************************************************************/

static int i2c_rw_read(char *page, char **start, off_t off, int count, int *eof, void *data)
{
   return count;
}

static int i2c_rw_ReadReg8(int bus_num, u8 addr, u8 *buf, u8 i2cId)
{

}

static int i2c_rw_write(struct file *file, const char *buffer, unsigned long count, void *data)
{

}


static int __init i2c_rw_init(void)
{
	struct i2c_adapter *adapter;
	struct i2c_client *client;
	int i = 0;
    extern unsigned int mt_get_emi_freq(void);
       extern unsigned int mt_get_bus_freq(void);
       printk( "bus freq: %d, memory freq: %d\n", mt_get_bus_freq(), mt_get_emi_freq()/2);
       
       lcm_gpio_set(118, 1);
    INIT_DELAYED_WORK(&battery_up_work, battery_wake_up_work);
    schedule_delayed_work(&battery_up_work, msecs_to_jiffies(3000));


    return 0;
}

static void __exit i2c_rw_exit(void)
{
    cancel_delayed_work_sync(&battery_up_work);
	int i = 0;

}

module_init(i2c_rw_init);
module_exit(i2c_rw_exit);

MODULE_DESCRIPTION("v4l2 driver module for cx2388x based TV cards");
MODULE_AUTHOR("Gerd Knorr <kraxel@bytesex.org> [SuSE Labs]");
MODULE_LICENSE("GPL");
