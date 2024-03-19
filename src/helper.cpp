#include "helper.hpp"
#include <string>

void adb::display_devices() {
    system("adb devices");
}

void usbD::connect() {
    std::cout << "Enter the serial number of the device you want to connect to: " << std::endl;
    std::string s;
    std::cin >> s;
    setSerial(s);
}

void adb::setSerial(std::string s) {
    serial = s;
}

void adb::pull() {
    system("mkdir androidBackup");
    system("adb root");
    system("adb pull /dev/block/bootdevice/by-name/* androidBackup/");
}

void adb::cleanup() {
    std::cout << "Cleaning up" << std::endl;
    system("adb kill-server");
    system("pause");
}

std::string adb::getSerial() {
    return serial;
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
