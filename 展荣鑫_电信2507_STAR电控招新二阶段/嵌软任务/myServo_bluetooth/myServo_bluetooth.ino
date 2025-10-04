#include <SoftwareSerial.h>
#include <Servo.h>
//引入软件串口库和舵机库

SoftwareSerial BTserial(2,3);
//建立对象，令引脚2为RX，引脚3为TX
Servo myServo;
//创建舵机
char Data=0;
//创建接受的字符变量
int angle=90;
//创建角度变量
String temp="";
//创建字符串变量作为缓存

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  //开启串口通讯
  BTserial.begin(9600);
  //蓝牙默认波特率
  BTserial.print("AT");
  //通讯测试
  myServo.attach(9);
  myServo.write(angle);
  //令舵机初始角度为90°
  delay(1000);

}

void loop() {
  // put your main code here, to run repeatedly:
  while(BTserial.available()>0){    
    //检查是否接收到数据
    Data=BTserial.read();
    //将接收到的一个字符赋予Data
    temp+=Data;
    //用“缓存”暂时存储输入的字符串
  }
if(temp!=""){
  angle=temp.toInt();
  //将“字符串”转换为整型变量并赋予给angle
  Serial.println(angle);
  //输出角度值
}
temp="";
//清空缓存，准备下一次接收
myServo.write(angle);
//舵机作出回应
delay(50);
}