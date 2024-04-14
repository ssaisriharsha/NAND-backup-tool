# NAND-backup-tool
Backup the NAND flash memory of your mobile phone.

---

# Requirements
1. Android devices rooted with magisk.
2. Atleast as much free space in your PC as the space occupied by your internal storage.
3. Either of the following magisk modules/apps:
    1. adb_root_enabler (Magisk module) (Recommended) : [Link](https://github.com/anasfanani/Adb-Root-Enabler)
    2. adb_root (Magisk module) (Android 11+) (Not working) : [Link](https://github.com/tiann/adb_root)
    3. adb_root (Magisk module) (Android 9/10) (Not working) : [Link](https://github.com/evdenis/adb_root)
    4. adbd_insecure (App) (Android 6+) (Will not work after Android 10) : [Link](https://github.com/wuxianlin/android_tools/blob/master/adbd-Insecure-v2.00.apk)

---

# How it works
This application creates a backup of NAND flash memory of your device. This works on both A/B or A only devices.
This backup will be useful in case if you mess up with your device and you are struck in bootloop.
All the backup files will be stored in androidBackup folder in your PC. If the folder already exist then this app will NOT overwrite it.
If you want to restore the backup, you can simply use fastboot to flash all the images to your phone.
This app copies all the data in the form of .img files to your PC, so you can restore them back by using fastboot.

---

# Caution
1. Do not try to downgrade  your phone using this tool because when you try to do so, anti roll-back protection kicks in and your device will get HARDBRICKED. Use it only when your installed OS version and backed up OS version are same.
2. Cannot be used with SAMSUNG phones because they do not contain fastboot mode. 

---

**TESTED ON POCO X5 PRO ROOTED WITH MAGISK AND ADB_ROOT_ENABLER INSTALLED**

# Credits

Thanks to [@anasfanani](https://github.com/anasfanani/), [@tiann](https://github.com/tiann/), [@evdenis](https://github.com/evdenis/adb_root), [@wuxianlin](https://github.com/wuxianlin) :)

