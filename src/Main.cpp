#include "helper.hpp"

int main() {
    adb *a = new usbD;
    a->display_devices();
    a->connect();
    return 0;
}