上海大学自动每日一报


1、配置Python环境:

	selenium、tkinter、bs4


2、进入界面先输入账号密码，点击添加账号。信息会加密储存在login_info中，如果密码输入错误请在login_info中删除对应一行，不要留下换行符。

   可以储存多个账号密码，顺序打卡。


3、界面右边可选打卡完自动关机，以及0点后自动打卡，延迟打卡等。会自动将历史未打卡的打完。


4、准备好后就点击开始每日一报吧，使用前请一定记得连接校园网。正确使用姿势：全宿舍用一个电脑自动打卡，每天晚上睡前配置好， 会自动将当天晨报和昨天晚报打卡。


5、小脚本有很多问题，但就本人目前使用帮十个同学打卡一个月没出现大的bug，欢迎大家改进、指导、斧正。邮箱：silicon@shu.edu.cn


6、每次打卡界面更换后旧版本就不能用了，本人会在两天内更新新版本，各位有能力的可以自己修改一下。


7、此脚本仅可用于学习用途，其余做法产生的结果本人概不负责。

8、  可以先尝试看能否使用，如果不能使用再进行以下配置。

  请先安装谷歌浏览器chrome和配置chrome的chromedriver

  chromedriver下载地址http://npm.taobao.org/mirrors/chromedriver/

  请按照浏览器版本下载，下载好后请将其放到谷歌浏览器根目录和python根目录下

  将webdriver在浏览器目录中的绝对地址复制到login_info第一行，覆盖掉之前存在的示例地址

