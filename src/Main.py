import os
import shutil
import subprocess

print("All your files will be backed up to C:\\Android_Backup. New folder will be created if it doesn't exist.")
print("Connect only one android device during the process.")
print("Please ensure that your phone has atleast 20GB free storage")

# Set the destination folder on your computer
backup_folder = "C:\\Android_Backup"

try:
	shutil.rmtree("C:\\Android_Backup")
except FileNotFoundError:
	pass

os.mkdir("C:\\Android_Backup")

# Set the source folder on your Android device
source_folder = "/dev/block/bootdevice/by-name/"

# Connect to your Android device using adb
command ="adb shell su -c ls " + source_folder
output = subprocess.check_output(command, shell=True)

# Get a list of files in the source folder on your android device
file_list = output.decode("utf-8").splitlines()

#Create a temporary folder on phone to copy the files
os.system("adb shell rm -r /sdcard/temp_backup")
os.system("adb shell mkdir /sdcard/temp_backup")
destination_file_temp = "/sdcard/temp_backup/"
# Copy the files from source_folder to temporary folder

for file_name in file_list:
	if file_name != "userdata":
		source_file = source_folder + file_name
		destination_file_temp_for_print = "/sdcard/temp-backup/" + file_name + ".img"
		print("Copying", source_file, "to", destination_file_temp_for_print)
		subprocess.call("adb shell su -c cp " + source_file+ " " + destination_file_temp, shell=True) 
		subprocess.call("adb shell su -c rename /sdcard/temp_backup/" + file_name + " " + "/sdcard/temp_backup/" + file_name + ".img")

# Copy each file from the temporary backup folder to the backup folder on your computer
print("Copying", destination_file_temp, "to", backup_folder)
print("This step may take a while...")
subprocess.call("adb pull " + destination_file_temp + " " + backup_folder, shell=True)

# delete the temoporary folders
print("Cleaning up the temporary files and directories...")
print("This may take a while...")
subprocess.call("adb shell rm -r /sdcard/temp_backup")


print("Done.")
os.system("pause")
