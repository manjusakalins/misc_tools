#include <stdio.h>
#include <fcntl.h>
#include <time.h>
#include <linux/input.h>
#include <sys/wait.h>
#include <errno.h>

#define PWR_INPUT_FILE "/dev/input/event0"
#define PANEL_INPUT_FILE "/sys/class/leds/lcd-backlight/brightness"
enum point_state {
	POINT_MOVE,
	POINT_ON,
	POINT_OFF,
};
int pwr_fd;
int panel_fd;

int write_file(int fd, int type, int code, int value)
{
	struct input_event ev;
	int ret;

	//gettimeofday(&ev.time, NULL);
	ev.type = type;
	ev.code = code;
	ev.value = value;

	ret = write(fd, &ev, sizeof(ev));
	if(ret <= 0) {
		printf("write error fd: %d, ret: %d, (%d,%d,%d)\n", fd, ret, type, code, value);
		return ret;
	}
	return 0;
}
int pwr_onoff(int on)
{
	struct input_event ev;
	int ret;

	write_file(pwr_fd, EV_KEY, KEY_END, on?1:0);
	write_file(pwr_fd, EV_SYN, SYN_REPORT, 0);

	return 0;
}

int panel_input_point(int x, int y, int state)
{
	struct input_event ev;
	int ret;

	write_file(panel_fd, EV_ABS, ABS_MT_POSITION_X, x);
	write_file(panel_fd, EV_ABS, ABS_MT_POSITION_Y, y);
	write_file(panel_fd, EV_ABS, ABS_MT_WIDTH_MAJOR, 1);
	//write_file(panel_fd, EV_ABS, ABS_MT_TRACKING_ID, 0);

	if (state == POINT_ON) {
		write_file(panel_fd, EV_KEY, BTN_TOUCH, 1);
	}/* else if (state == POINT_OFF) {
	    write_file(panel_fd, EV_KEY, BTN_TOUCH, 0);
	    }*/
	write_file(panel_fd, EV_SYN, SYN_MT_REPORT, 0);
	write_file(panel_fd, EV_SYN, SYN_REPORT, 0);
	usleep(100000);
	return 0;
}
int main(void)
{
	int ret;
	struct input_event ev;
	pwr_fd = open(PWR_INPUT_FILE, O_RDWR);
	if (pwr_fd < 0) {
		printf("open file failed %d, errno: %d, %s\n", pwr_fd, errno, PWR_INPUT_FILE);
		return -1;
	}

	panel_fd = open(PANEL_INPUT_FILE, O_RDWR);
	if (panel_fd < 0) {
		close(pwr_fd);
		printf("error file open %d, errno: %d, %s\n", panel_fd, errno, PANEL_INPUT_FILE);
		return -1;
	}
	//ret = write(pwr_fd, &ret, sizeof(ret));
	if (ret < 0) {
		close(pwr_fd);
		close(panel_fd);
		printf("error file open %d, ret: %d, errno: %d, %d\n", panel_fd, ret, errno, __LINE__);
		return -1;
	}
	char *buf[256];
	memset(buf,0,256);
	read(panel_fd, buf, 256);
	printf("%s \n", buf);
	while(0) {
		//pwr_onoff(0);
		//pwr_onoff(1);
		//usleep(600000);
	

	}
	close(pwr_fd);
	close(panel_fd);
	return 0;

}
