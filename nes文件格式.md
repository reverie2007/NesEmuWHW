# nes 文件格式

.nes 文件可能是iNES文件或者NES2.0文件

资料来源：

http://wiki.nesdev.com/w/index.php/INES

http://wiki.nesdev.com/w/index.php/NES_2.0



## iNES文件格式

### 类型判定

推荐检测顺序：

    If byte 7 AND $0C = $08, and the size taking into account byte 9 does not exceed the actual size of the ROM image, then NES 2.0.
    If byte 7 AND $0C = $00, and bytes 12-15 are all 0, then iNES.
    Otherwise, archaic iNES.

### 文件结构

iNES包含以下部分, 按顺序有:
    
     一、文件头 (16 bytes)
     二、Trainer, if present (0 or 512 bytes)
     三、PRG ROM data (16384 * x bytes)
     四、CHR ROM data, if present (8192 * y bytes)
     五、PlayChoice INST-ROM, if present (0 or 8192 bytes)
     六、PlayChoice PROM, if present (16 bytes Data, 16 bytes CounterOut)
      (this is often missing, see PC10 ROM-Images for details)
     七、Some ROM-Images additionally contain a 128-byte (or sometimes 127-byte) title at the end of the file.

### 文件头:


    0-3: string    "NES"<EOF>
    4: byte      以16384(0x4000)字节作为单位的PRG-ROM大小数量
    5: byte      以 8192(0x2000)字节作为单位的CHR-ROM大小数量
    6: bitfield  Mapper, mirroring, battery, trainer
    7: bitfield  Mapper, VS/Playchoice, NES 2.0
    8: Flags 8 - PRG-RAM size (rarely used extension)
    9: Flags 9 - TV system (rarely used extension)
    10: Flags 10 - TV system, PRG-RAM presence (unofficial, rarely used extension)
    11-15: ines中未使用 (应该填充0，但有些ripper使用7-15字节保存自己的名字)
   
    Flags 6:
    7       0
    ---------
    NNNN FTBM
    N: Mapper编号低4位
    F: 4屏标志位. (如果该位被设置, 则忽略M标志)
    T: Trainer标志位.  1表示 $7000-$71FF加载 Trainer
    B: SRAM标志位 $6000-$7FFF拥有电池供电的SRAM.
    M: 镜像标志位.  0 = 水平, 1 = 垂直.
    Byte 7 (Flags 7):
    7       0
    ---------
    NNNN xxPV
     
    N: Mapper编号高4位
    P: Playchoice 10标志位. 被设置则表示为PC-10游戏
    V: Vs. Unisystem标志位. 被设置则表示为Vs.  游戏
    x: nes2.0 标志 10表示是nes2.0格式，如果等于2，8-15字节按照2.0格式解析

### 读取方法
    
## nes2.0