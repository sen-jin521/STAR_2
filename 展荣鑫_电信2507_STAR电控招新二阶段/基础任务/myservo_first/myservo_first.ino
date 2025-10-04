#include <Servo.h>
Servo myservo;
//创建舵机对象
int p=0;
int ang[]={0,30,45,90,135};
//定义变量与数组


void setup() {
  // put your setup code here, to run once:
  myservo.attach(9);
  //舵机信号线接入PWM的9号引脚
  Serial.begin(9600);
  myservo.write(p);
  //设置初始角度为0
  delay(1000);
}

void loop() {
  // put your main code here, to run repeatedly: 
 for(int i=0;i<5;i++){
    myservo.write(ang[i]);
    //依次输出角度
    Serial.print("当前的角度为");
    Serial.println(ang[i]);
    delay(1000);
 }

  
}
