#include <linux/module.h>
#include <linux/kernel.h>
#include <linux/i2c.h>
#include <linux/proc_fs.h>   //proc file use
#include <linux/spinlock.h>
#include <asm/uaccess.h>


#define I2C_RW_NAME "i2c_rw_entry"
static struct i2c_board_info __initdata i2c_rw_dev = {
	I2C_BOARD_INFO(I2C_RW_NAME, 0xfd>>1)
};
static struct i2c_client *i2c_rw_clients[4];
static const struct i2c_device_id i2c_rw_id[] = {{I2C_RW_NAME,0},{}};
static DEFINE_SPINLOCK(i2c_rw_drv_lock);
static struct proc_dir_entry *prEntry;

/*******************************************************************************
* i2c relative end
********************************************************************************/
static int i2c_rw_probe(struct i2c_client *client, const struct i2c_device_id *id)
{
	printk("============================%s %d, line: %d\n", __func__, __LINE__, client->adapter->nr);
	i2c_rw_clients[client->adapter->nr] = client;
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
	struct i2c_client *client = i2c_rw_clients[bus_num];
    int  i4RetValue = 0;
    char puReadCmd[1] = {(char)(addr & 0xFF)};

	if (!client)
		return -1;

	spin_lock(&i2c_rw_drv_lock);

    client->addr = (i2cId >> 1);

	spin_unlock(&i2c_rw_drv_lock);

    //
    i4RetValue = i2c_master_send(client, puReadCmd, 1);
    if (i4RetValue != 1) {
        printk("[i2c_rw_ReadReg8] I2C send failed, addr = 0x%x, data = 0x%x !! \n", addr,  *buf );
        return i4RetValue;
    }
    //
    i4RetValue = i2c_master_recv(client, (char *)buf, 1);
    if (i4RetValue != 1) {
        printk("[i2c_rw_ReadReg8] I2C read failed!! \n");
        return i4RetValue;
    }

    return 0;
}

static int i2c_rw_write(struct file *file, const char *buffer, unsigned long count, void *data)
{
	u8 in_data[64];
	int in_count;
	int bus_idx;
	int client_addr;
	int read_addr;
	int res;

	//printk("%s %d\n", __func__, count);
	in_count = count > sizeof(in_data)?sizeof(in_data)-1:count;
	if (copy_from_user(in_data, buffer, in_count))
		return 0;
	in_data[in_count] = '\0';
	printk("%s\n", in_data);

	if (3 == sscanf(in_data, "%d,0x%x,0x%x", &bus_idx, &client_addr, &read_addr)) {
		printk("%d, 0x%x, 0x%x\n", bus_idx, client_addr&0xff, read_addr&0xff);
		res = i2c_rw_ReadReg8(bus_idx, read_addr&0xff, in_data, client_addr&0xff);
		if (res < 0)
			printk("%s: read error: %d\n", __func__, res);
		else
			printk("=============read out:0x%02x:0x%02x=============\n", read_addr&0xff, in_data[0]);
	}
	return count;
}


static int __init i2c_rw_init(void)
{
	struct i2c_adapter *adapter;
	struct i2c_client *client;
	int i = 0;
    extern unsigned int mt_get_emi_freq(void);
       extern unsigned int mt_get_bus_freq(void);
       sprintf(buf+strlen(buf), "bus freq: %d, memory freq: %d\n", mt_get_bus_freq(), mt_get_emi_freq()/2);
	for (; i < 4; i++) {
		adapter = i2c_get_adapter(i);
		if (adapter == NULL)
			continue;
		client = i2c_new_device(adapter,&i2c_rw_dev);
		i2c_put_adapter(adapter);
	}

	i2c_add_driver(&i2c_rw_driver);
	prEntry = create_proc_entry("i2c_rw", 0, NULL);
    if (prEntry) {
        //prEntry->read_proc  = SYSRAM_read_flag;
        prEntry->write_proc = i2c_rw_write;
    }

    return 0;
}

static void __exit i2c_rw_exit(void)
{
	struct i2c_client *client;
	int i = 0;

	if (prEntry != NULL)
		remove_proc_entry("i2c_rw", NULL);
	i2c_del_driver(&i2c_rw_driver);


	for (; i < 4; i++) {
		client = i2c_rw_clients[i];
		if (client != NULL)
			i2c_unregister_device(client);
	}
}

module_init(i2c_rw_init);
module_exit(i2c_rw_exit);

MODULE_DESCRIPTION("v4l2 driver module for cx2388x based TV cards");
MODULE_AUTHOR("Gerd Knorr <kraxel@bytesex.org> [SuSE Labs]");
MODULE_LICENSE("GPL");
