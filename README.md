# NAND-backup-tool
Backup the NAND flash memory of your mobile phone (USERDATA EXCLUDED!!)

# Requirements
1. A windows PC with adb properly installed.
2. Rooted android device.
3. Atleast 20GB of free space in both phone and PC.

# How it works
This application creates a backup of NAND flash memory of your device. This works on both A/B or A only devices.
This backup will be useful in case if you mess up with your device and you are struck in bootloop.
All the backup files will be stored in C:\Android_Backup folder in your PC. If the folder already exist then this app will overwrite it.
If you want to restore the backup, you can simply use fastboot to flash all the images to your phone.
All the data of your partitions is stored in /dev/block/bootdevice/by-name of your device.
This app copies all the data of these partitions in the form of .img files to your PC, so you can restore them back by using fastboot.

# Caution
1. Do not try to downgrade  your phone using this tool because when you try to do so, anti roll-back protection kicks in and your device will get HARDBRICKED. Use it only when your installed OS version and backed up OS version are same.
2. This app cannot backup userdata due to some limitations. When you try to backup using this app, you are actually backing up temporarily /sdcard. These backup images will be temporarily stored in your /sdcard partition. So when you backup userdata partition, the /sdcard partition starts backing up itself and this backup file will be stored in /sdcard partition again which leads to an infinite loop. So backing up userdata using this app is not possible.
3. Connect only 1 Phone during the process.
