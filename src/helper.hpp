#ifndef _HELPER_HPP_
#define _HELPER_HPP_
#include <iostream>

class adb {
    private:
    std::string serial;
    public:
    std::string getSerial();
    void setSerial(std::string);
    static void display_devices();
    virtual void connect() = 0;
    virtual void pull() final;
    virtual void cleanup() final;
    virtual void escalate() final;
    virtual void pair();
};

class usbD: public adb {
    public:
    virtual void connect() final;
};

class wirelessD: public adb {
    public:
    virtual void pair() final;
    virtual void connect() final;
};

#endif