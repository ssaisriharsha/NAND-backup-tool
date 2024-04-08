#include "helper.hpp"
#include "error_handler.hpp"

int main() {
    int method = 0;
    std::string serial;
    adb *bridge = nullptr;
    std::cout << "Welcome to NAND backup tool." << std::endl;
    std::cout << "Select the connection method: " << std::endl;
    std::cout << "1. USB Debugging (Recommended)" << std::endl;
    std::cout << "2. Wireless Debugging" << std::endl;
    std::cout << "Enter your preferred method(1/2): " << std::endl;
    std::cin >> method;
    if (method == 1) {
        bridge = new usbD;
        
    }
    else if (method == 2) {
        int pairing_status = 0;
        bridge = new wirelessD;
        std::cout << "Is your device paired with wireless debugging? " << std::endl;
        std::cout << "1. Yes" << std::endl;
        std::cout << "2. No" << std::endl;
        std::cin >> pairing_status;
        if(pairing_status == 1) {
        }
        else if (pairing_status == 2) {
            bridge->pair();
        }
    }
    else {
        abort();
    }
    adb::display_devices();
    bridge->connect();
    bridge->escalate();
    bridge->pull();
    bridge->cleanup();
}