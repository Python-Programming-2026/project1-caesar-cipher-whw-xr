[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/fPQK30A4)<br>
[成员 **王浩玮 2243211064 许睿 2243211067**]<br>
<span style="color: red;">**第一段** `caesar_encrypt` 也就是凯撒密码加密函数：</span><br>
--就是把明文按偏移量 shift 变成密文
遍历每一个字符，ord(char) - 65 把 A到Z 变成 0到25，加上偏移量 shift<br>
--%26 防止超出字母范围,再加 65 转回大写字母。小写字母同理，用 97（a 的 ASCII）,空格、数字、符号直接保留不变。<br>
**第二段**`caesar_decrypt`也就是凯撒密码解密函数：就是减去偏移量即可。<br>
**第三段**则是暴力破解的功能，因为只有26种可能，把每种可能全都翻译一下然后交由用户判断。<br>
**第四段**是制作的简易界面，便于得到输入反馈。<br>


![演示视频](https://github.com/user-attachments/assets/08598496-c275-4588-b9b5-160223f97b24)

