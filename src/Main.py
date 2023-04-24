try:
	import sys
	import os
	import shutil
	import subprocess
	import time

	subprocess.call("adb kill-server")
	os.system("cls")
	print("All your files will be backed up to C:\\Android_Backup. New folder will be created if it doesn't exist.")
	print("Connect only one android device during the process.")
	print("Please ensure that your phone has atleast 20GB free storage")

	print("Select the mode of operation:\n1. USB Debugging\n2. Wireless debugging.")
	while True:
		try:
			operation_mode = int(input("Enter your choice(1/2): "))
			break
		except ValueError:
			print("You have to enter either 1 or 2 only.")
			time.sleep(0.5)
	if operation_mode == 1:
		print("Using USB Debugging mode...")
	elif operation_mode == 2:
		print("Using Wireless Debugging mode...")
		while True:
			pairing_status = input("Is your device paired with your PC?: ").lower()
			if pairing_status == "yes":
				ip_address_and_port = input("Now please enter the IP address and port displayed in your wireless debugging options in the above format: ")
				subprocess.run("adb connect " + ip_address_and_port)
				break
			elif pairing_status == "no":
				print("Enable pairing mode in wireless debugging and enter the ip address and port in the following format.")
				print("Example: 127.0.0.2:90008")
				pairing_id = input("Enter your ip address along with port as shown in the above format: ")
				subprocess.run("adb pair " + pairing_id)
				ip_address_and_port = input("Now please enter the IP address and port displayed in your wireless debugging options in the above format: ")
				subprocess.run("adb connect " + ip_address_and_port)
				break
			else:
				print("You have to enter yes or no only.")
				time.sleep(0.5)
	else:
		print("You have to enter either 1 or 2 only.")

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
	try:
		command ="adb shell su -c ls " + source_folder
		output = subprocess.check_output(command)
	except subprocess.CalledProcessError:
		print("Device not connected properly. Please check your device connection.")
		print("The program will now exit.")
		os.system("pause")
		exit()
	# Get a list of files in the source folder on your android device
	file_list = output.decode("utf-8").splitlines()

	#Create a temporary folder on phone to copy the files
	subprocess.call("adb shell rm -r /sdcard/temp_backup")
	subprocess.call("adb shell mkdir /sdcard/temp_backup")
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
except KeyboardInterrupt:
	print("exit.")
	exit()
