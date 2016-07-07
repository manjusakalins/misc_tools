#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <typeinfo>
#include <unistd.h>

#include "RefBase.h"

namespace android {

class Object : public RefBase {
public:
    Object();
    ~Object(); //must be public
    Object(int num);
    int getNumber();
    void setNumber(int num);
                    
private:
    int m_num;           
};

Object::Object() {
	printf("%s %d\n", __func__, __LINE__);

    m_num = 0;
}
Object::~Object() {
		printf("%s %d\n", __func__, __LINE__);

}
Object::Object(int num) {
    m_num = num;
}

int Object::getNumber() {
    return m_num;
}

void Object::setNumber(int num) {
     m_num = num;
}





};
int main(int argc, char *argv[])
{
	android::sp<class android::Object> sdp = new android::Object();
	printf("%s %d %d\n", __func__, __LINE__,sdp->getNumber());
	printf("%s %d\n", __func__, __LINE__);
}

