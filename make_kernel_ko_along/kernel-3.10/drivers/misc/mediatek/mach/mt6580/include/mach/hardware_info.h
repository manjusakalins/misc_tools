 /* mediatek/platform/mt6577/lk/include/platform/hardware_info.h
  *
  *
  * Copyright (C) 2008,2009 MediaTek <www.mediatek.com>
  * Authors: Infinity Chen <infinity.chen@mediatek.com>  
  *
  * This program is free software; you can redistribute it and/or modify
  * it under the terms of the GNU General Public License as published by
  * the Free Software Foundation; either version 2 of the License, or
  * (at your option) any later version.
  *
  * This program is distributed in the hope that it will be useful,
  * but WITHOUT ANY WARRANTY; without even the implied warranty of
  * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  * GNU General Public License for more details.
  *
  * You should have received a copy of the GNU General Public License
  * along with this program; if not, write to the Free Software
  * Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
  */


#define HW_INFO_OFFSET 252
extern void* mt_get_pro_info_db_addr(void);
//cpu type hw_info[19]
typedef enum
{
    PLAT_MT6577 = 0,
    PLAT_MT6517,
    PLAT_MT6572,
    PLAT_MT6589,
    PLAT_MT8377,
    PLAT_MT8317
} CPU_PLAT;

//mt6577 project item hw_info[0]
typedef enum
{
    ME001 = 0,
    TE711,
    TE820
} PROJECT_77;


//mt6517 project item hw_info[0]
typedef enum
{
    MA001= 0,
    TA780,
    TA761,
} PROJECT_17;

//mt6572 project item hw_info[0]
typedef enum
{
    TD780 = 0,
} PROJECT_72;

//mt6589 project item
typedef enum
{
    TF902 = 0,
} PROJECT_89;


//hw version hw_info[1]
typedef enum
{
    HW_FIRST = 0,
    HW_SECOND,
    HW_THIRD,
} HW_VERSION;


//LCD hw_info[2]
typedef enum
{
    x,
} LCD_TYPE;


//camera hw_info[3]
typedef enum
{
    xx,
} CAMERA_TYPE;


//TP hw_info[4]
typedef enum
{
    xxx,
} TP_TYPE;



//combo hw_info[5]
typedef enum
{
    MT_6628 = 0,
    MT_6620,
} WIFI_CHIP;

//combo hw_info[6]
typedef enum
{
    BT_1800MA = 0,
    BT_2000MA,
	BT_2500MA,
    BT_2400MA,
	BT_2700MA,
    BT_3000MA,
    BT_3200MA,
    BT_2600MA,
    BT_2300MA,
    BT_4500MA,
    BT_1750MA,
    BT_4600MA,
    BT_3500MA,    
    BT_4000MA,
} BATTERY_TYPE;


extern CPU_PLAT get_cpu_type(void);
extern PROJECT_17 get_project_type(void);
extern HW_VERSION get_hw_version(void);
extern LCD_TYPE get_lcd_type(void);
extern LCD_TYPE get_lcd_type(void);
extern CAMERA_TYPE get_camera_type(void);
extern TP_TYPE get_tp_type(void);
extern WIFI_CHIP get_wifi_chip(void);
extern BATTERY_TYPE get_battery_type(void);

