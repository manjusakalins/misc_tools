

#include <linux/kernel.h>
#include <linux/device.h>
#include <linux/module.h>


static int __init test_init(void)
{
	printk("%s %d\n", __func__, __LINE__);
	return 0;
}

static void __exit test_exit(void)
{
	printk("%s %d\n", __func__, __LINE__);;
}

module_init(test_init);
module_exit(test_exit);
MODULE_LICENSE("GPL");
MODULE_DESCRIPTION("jlink");
MODULE_AUTHOR("jlink test");






