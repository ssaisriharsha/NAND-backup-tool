#include "helper.hpp"
#include <string>

void adb::display_devices() {
    system("adb devices");
}

void adb::setSerial(std::string s) {
    serial = s;
}

void adb::pair(){}

std::string adb::getSerial() {
    return serial;
}

void adb::escalate() {
    std::string cmd = "adb -s " + getSerial() + " root";
    system(cmd.c_str());
    std::cout << "privilages escalated successfully." << std::endl;
}

void usbD::connect() {
    std::cout << "Enter the serial number of the device you want to connect to: " << std::endl;
    std::string s;
    std::cin >> s;
    setSerial(s);
}

void adb::pull() {
    system("mkdir androidBackup");
    std::string pull_m = "adb -s " + getSerial() +  " pull /dev/block/bootdevice/by-name androidBackup/";
    system(pull_m.c_str());
}

void adb::cleanup() {
    std::cout << "Cleaning up" << std::endl;
    system("adb kill-server");
    std::cout << "Thanks for using this app :)!" << std::endl;
    system("pause");
}



void wirelessD::pair() {
    std::string ip;
    std::string port;
    std::cout << "Enter the ip address: " << std::endl;
    std::cin >> ip;
    std::cout << "Enter the port number: " << std::endl;
    std::string connection = "adb pair " + ip + ":" + port;
    system(connection.c_str());
}

void wirelessD::connect() {
    std::string ip;
    std::string port;
    std::cout << "Enter the ip address: " << std::endl;
    std::cin >> ip;
    std::cout << "Enter the port number: " << std::endl;
    std::string connection = "adb connect " + ip + ":" + port;
    system(connection.c_str());
}
