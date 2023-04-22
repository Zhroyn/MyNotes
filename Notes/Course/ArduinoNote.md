<!-- TOC -->

- [数字I/O](#数字io)
- [模拟I/O](#模拟io)
- [高级I/O](#高级io)
- [串口操作](#串口操作)
- [内置常量](#内置常量)

<!-- /TOC -->






### 数字I/O
- 数字信号有高电平和低电平两种形态
- 输出高电平时，可提供40mA的5V电压
<br>

- 数字接口既可用作输入，又可用作输出
- 使用前需用 `pinMode()` 指定是输入还是输出
<br>

- 引脚13连接到板载的LED指示灯
- 引脚3、5、6、9、10、11具有PWM功能
- 引脚0、1可用作RX和TX串口，进行串口通讯
<br>

- `pinMode(pin, mode)` 设置一个引脚为输入或输出
- `digitalWrite(pin, val)` 给一个数字引脚写入 `HIGH` 或 `LOW`
- `digitalRead(pin)` 从一个数字引脚读取数值，返回 `HIGH` 或 `LOW`


### 模拟I/O
- 模拟端口 `A0~A5` 默认为模拟输入
- 也可用作数字输入、输出端口 `14~19`
<br>

- `analogRead(pin)` 从一个模拟引脚读取数值
- `analogWrite(pin, val)` 从一个引脚输出PWM模拟值


### 高级I/O
- `tone(pin, frequency, duration = 0)` 在一个引脚上产生一个方波（50%占空比）
- `noTone(pin)` 在一个引脚上停止由 `tone()` 产生的波



### 串口操作
- `Serial.begin(baud)` 开启串口并设置波特率
<br>

- `Serial.read()` 读取串口缓存中的一个字符并删除
- `Serial.print(val)` or `Serial.print(val, format)`
  - 写入字符串数据到串口
  - 转换进制
    - `Serial.print(78, BIN)`
    - `Serial.print(78, OCT)`
    - `Serial.print(78, DEC)`
    - `Serial.print(78, HEX)`
  - 四舍五入
    - `Serial.print(1.23456, 4) ==> 1.2346`
- `Serial.println(val)` or `Serial.println(val, format)`
  - 写入字符串数据到串口并换行
<br>




### 内置常量
- 引脚常量：
  - `INPUT` 将该引脚设置为输入引脚
  - `OUTPUT` 将引脚设置为输出引脚
  - `INPUT_PULLUP` 将该引脚设置为内部上拉电阻
<br>

- 电压常量：
  - `HIGH` 高水平的电压，取决于硬件，在3.3V的板子上大于2V，在5V的板子上大于3V
  - `LOW` 低水平的电压，同样取决于所使用的板子
<br>

- 数字常量：
  - `M_PI` 常数pi
  - `M_E` 常数e
  - `M_LN10` 数字10的自然对数
  - `M_LN2` 数字2的自然对数
  - `M_LOG10E` e的对数，以10为底
  - `M_LOG2E` e的对数，以2为底
  - `M_SQRT2` 2的平方根
  - `NAN` NAN（不是一个数字）常数
- 逻辑常量：
  - `true`
  - `false`
<br>


- `LED_BUILTIN` : 13
- `A0` `PIN_A0` : 14
- `A1` `PIN_A1` : 15
- `A2` `PIN_A2` : 16
- `A3` `PIN_A3` : 17
- `A4` `PIN_A4` : 18
- `A5` `PIN_A5` : 19
- `A6` `PIN_A6` : 20
- `A7` `PIN_A7` : 21


