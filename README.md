# generate_anime_name_combination

Generate a name with random character and item in anime or game.

用随机的动漫角色和物品名称组合得到一个新名称

Although we start writing README in English, but it is not yet done, we will finish it ASAP.

这份README正在用英语进行翻译，欢迎有能力的大佬进行辅助。

## 序

之前虽然也在某些游戏的取名系统见过这样的玩法（例如暴雪的战网随机昵称以及MC代理版的随机昵称），但是我没有见到用动漫的名字和物品进行组合的程序和系统，故自己简单开发了一套。

另外，也是因为觉得docker对于默认容器的命名方式（科学家和物品）很有趣才开发这套系统的。

## Opening

I have seen some name system like Blizzard battle.net default account name which combine a kind of thing and other kind of thing ( like Crazy hat, Happy boot and so on).

and a similar system have been use in docker for default container name, use adjective combine with scientist (like happy_wozniak).

But I don't see such a system with anime character name, so I make one.

## 开发

使用Python3.6.8开发，数据库使用MySQL 5.7.11

代码层反而是最简单的，只需要使用pymysql模块，数据库的数据录入才是最麻烦的

后期数据库录入通过将视频接入弹幕检测系统，匹配符合规则的弹幕（同样使用Python进行弹幕监听）

主程序为douga.py

## Development

Base on Python 3.6.8, use MySQL 5.7.11 for database.

Coding is very simple, just use a  library call "pymysql",but it's hard and tedious to entering a lot of data to database.

Volunteer can input a danmuku conforms to the rules in my video from bilibili, By using Python monitoring, they can entering data to my database in order to make database richer.

Main program is douga.py

## 引用的动漫作品

目前绝大部分使用来自日本和中国的动漫作品（番剧），不会录入未TV化的动漫作品，如果一个角色出场率较低（一般为一集以下），或者官方定义为比较次要的角色，那么ta会被归为不重要角色，这类角色不会被录入数据库，以提高早期开发速度（但是后期可以录入）。

举个例子，《JOJO的奇妙冒险》第三部中大部分反派角色只出场一集或两集，且没有杀死主角团任一角色，那么他们在早期开发就不会被录入。《玉子市场》中兔山商店街大部分拥有店铺的角色因为名字较少提及，他们在早期开发同样不会被录入。

可能存在符合规则但没有录入的情况，如《JOJO的奇妙冒险》第三部和第四部，因为其角色体系较复杂。

早期开发版本（beta v0.1）已经录入213个角色和137个物品，如果在b站的视频有较好播放量会继续更新，当前决定的更新周期为两个星期，且在9月份前确定正式版本。

引用的动漫/动漫系列/游戏系列如下（角色引用资料来自[萌娘百科](https://zh.moegirl.org.cn/)）：

	• 《轻音少女》系列（基本全覆盖）
	
	• 《玉子市场》系列（仅玉子紧密相关角色）
	
	• 《JOJO的奇妙冒险》系列 (主角团基本全覆盖，以及主要反派角色)
	
	• 《擅长作弄的高木同学》系列（基本全覆盖）
	
	• 《辉夜大小姐想让我告白》系列（学生会全覆盖）
	
	• 《某科学的超电磁炮》系列（《魔法禁书目录》未录入）
	
	• 《LoveLive！》与《LoveLive！Sunshine！》（除了μ's和Aqours所有主角团，还包含了非主角团和其它角色）
	
	• 《狐妖小红娘》（部分角色）
	
	• 《境界的彼方》（仅两角色）
	
	• 《笨女孩》（基本全覆盖）
	
	• 《鬼灭之刃》 (部分角色)
	
	• 《未闻花名》（仅主要角色）
	
	• 《小林家的龙女仆》（仅登场的龙和小林）
	
	• 《我们无法一起学习》系列（仅主角团）
	
	• 《猫和老鼠》（MGM旧版上镜率较高角色，而非现在的华纳版）
	
	• 《天使降临到我身边》（基本全覆盖）
	
	• 《中二病也要谈恋爱》系列（基本全覆盖）
	
	• 《青春猪头少年不会梦到兔女郎学姐》（仅与咲太紧密相关角色）
	
	• 《女高中生的虚度日常》（三人组加萝莉）
	
	• 《干物妹小埋》系列（基本全覆盖）
	
	• 《Re：从零开始的异世界生活》（仅部分爱蜜莉雅阵营角色）
	
	• 《公主连结RE:DIVE》（仅主角团）
	
	• 《Overlord》系列（部分安兹·乌尔·恭阵营角色）
	
	• 《新世纪福音战士》（仅部分驾驶员和指挥官）
	
	• 《冰菓》(仅两个角色)
	
	• 《我想吃掉你的胰脏》(仅两个角色)
	
	• 《我的妹妹不可能那么可爱》(仅三个角色)
	
	• 《理科生坠入情网，故尝试证明。》(研究生全覆盖)
	
	• 《游戏人生》(仅两个角色)
	
	• 《书店里的骷髅店员本田》(全覆盖)
	
	• 《Urara迷路帖》(基本全覆盖)
	
	• 《马达加斯加》系列 (四个主角动物，企鹅阵营和朱利安阵营)
	
	• 《全职高手》(主角团及其游戏内昵称)
	
	• 《紫罗兰永恒花园》(部分主要角色)
	
	• 《夏目友人帐》(基本全覆盖)
	
	• 《女神异闻录5》(主角团)
	
	• 《齐木楠雄的灾难》(基本全覆盖)
	
	• 《塞尔达传说:旷野之息》(全覆盖)
	
	• 《心跳文学部》（全覆盖）
	
	• ... ...

由于上次更新（2020-08-08）的番剧和游戏过多，下次更新将一并合并到一个单独文件，此README中的名称保留
	
## Included anime series

Most of anime series is from Japan and China, and all are anime drama.

If a character appearance rate is low ( 1 episode or lower), they won't be entering to database in early development, but we can add it later.

For example,  In JoJo's Bizarre Adventure Season 3，most of negative character did not kill or cause a lot of damage to main character, so they won't be entering to database in early development. In Tamako Market, most of character have their own shop in Usagiyama Shopping District(うさぎ山商店街), but their name are rarely mentioned, so they also won't be entering to database in early development.

But there may be special circumstances, such as some drama  with complex role system like JoJo's Bizarre Adventure Season 3 and 4.

Early development version( beta v0.1 ) had entered 213 characters name and 137 items name, I may update it in the future. ALL characters names and items are in Chinese for now.

All drama name is here, refer to [萌娘百科](https://zh.moegirl.org.cn/):

	• K-On! (Basically full cover)
	
	• Tamako Market ( Close to Kitashirakawa Tamako only )
	
	• JoJo's Bizarre Adventure ( Main charatcers basically full cover, and some main negative character)
	
	• Teasing Master Takagi-san ( Basically full cover )
	
	• Kaguya-sama: Love Is War ( Student union full cover only )
	
	• A Certain Scientific Railgun ( A little, but A Certain Magical Index is not includied )
	
	• LoveLive! and LoveLive! Sunshine! ( Contain μ's and Aqours, and other charatcers )
	
	• Enmusubi no Youko-chan/Huyao Xiao Hongniang (A little)
	
	• Beyond the Boundary( Just two charatcers )
	
	• Aho Girl ( Basically full cover )
	
	• Kimetsu no Yaiba (A little)
	
	• Anohana/The Flower We Saw That Day ( Main charatcers only )
	
	• Miss Kobayashi's Dragon Maid ( 5 main dragon charatcers and Kobayashi )
	
	• We Never Learn ( Main charatcers only )
	
	• Tom and Jerry( MGM ver. from 20 century, not  Warner Bros. ver. )
	
	• Wataten!: An Angel Flew Down to Me ( Basically full cover )
	
	• Love, Chunibyo & Other Delusions ( Basically full cover )
	
	• Rascal Does Not Dream of Bunny Girl Senpai  ( Close to Azusagawa Sakuta only )
	
	• Wasteful Days of High School Girls ( Main charatcers and Saku Momoi/LOLI )
	
	• Himouto! Umaru-chan ( Basically full cover )
	
	• Re:Zero − Starting Life in Another World  ( A little from Emilia's side )
	
	• Princess Connect! Re:Dive ( Main charatcers only )
	
	• Overlord ( A little from Ainz Ooal Gown's side )
	
	• Neon Genesis Evangelion（Some pliot and commander）
	
	• Hyouka (Just 2 characters)
	
	• I want to eat your pancreas ( Just 2 characters )
	
	• My Little Sister Can't Be This Cute! ( Just 3 characters )

	• Science Fell in Love, So I Tried to Prove It ( Student full cover )

	• NO GAME NO LIFE ( Just two character )

	• Skull-face Bookseller Honda-san ( Full cover )

	• Urara Meirocho ( Basically full cover )

	• Madagascar ( 4 main animal character, Penguin side and King Julien side )

	• The King's Avatar ( Main charatcers and their nickname in game )

	• Violet Evergarden ( Some main charatcers )

	• Natsume's Book of Friends ( Basically full cover )

	• Persona 5 ( Main charatcers only )

	• The Disastrous Life of Saiki K ( Basically full cover )

	• The Legend of Zelda: Breath of the Wild ( Full cover )

	• Doki Doki Literature Club! ( Full cover )
	
	• ... ...
	

Last upgrade (2020-08-08) we pull too many anime drama and game, we will list them in another file in next upgrade, but we won't delete the list in README.

## 组合

默认情况下，在物品数据库和人物数据库随机挑出后组合即为结果，类似“姓名的物品”格式。

早期开发时，物品基本与人物绑定，或为人物标志物以加快开发速度，有些人物可能没有对应物品，同样在后期录入时可以进行添加

## Combination

douga.py will output a combination name with a random character name and a a random item by default.

In early development , when we record a character ,we may record a item about this character , but  some character will not , Also can be updated in the future.

## 数据库

数据库默认叫anime_name，如果你从GitHub下载了完整的代码和数据库文件，请注意这一点

数据库使用UTF-8编码

该数据库含有两个表，ITEM表和NAME表，分别为物品表和角色名表。

	• 角色名表
	
	该表含四个列
	
		a. 编号（NO，主键，非空，5位int）
		
		已经编写好数据库录入程序，如果你仍然手动录入，请注意编号也需要手动录入
		
		b. 姓（FAMILY，非空，10位varchar）
		
		无论是哪种姓名规则这里都应该输入姓，复姓只输入非名字部分
		
		c. 名（NAME，非空，8位varchar）
		
		无论是哪种姓名规则这里都应该输入名
		
		d. 反转值（REVERSE，1位tinyint，默认值为0）
		
		对于非日本/中国姓名命名规则情况等，调整此数值，以告知程序这个姓名该如何输出，详细规则见下文“反转值”
		
	• 物品表
	
	该表含一个列
	
		a. 物品（ITEM，主键，非空，15位varchar）
		
		目前仍在考虑是否使用更长位的varchar

## Database

Default database call 'anime_name', pay attention if you download the full code or table file from GitHub. 

Coding with UTF-8.

The database contains 2 tables, 'ITEM' table with item and 'NAME' table with character name.

	• 'NAME' table with character name
	
	This table contains 4 columns.
	
		a. Number( NO, Primary key, Not null, int(5) )
		
		Now with auto-record code, if you record manually, you must enter number manually , too.
		
		b. Family name(FAMILY, Not null, varchar(10) )
		
		Input family name here. ( No matter family name is the first or the last )
		
		For compound surname, input non-last-name part.
		
		c. Last name( NAME, Not null, varchar(8) )
		
		Input last name here. ( No matter last name is the first or the last )
		
		d. Reverse value( REVERSE, tinyint(1)，default is 0 )
	
		For some charatcer that family name isn't the first like China and Japan, input the value in order to tell Python code how to output the name or short name. See 'Reverse value' below.
		
	• 'ITEM' table with item
	
	This table contains 1 column.
	
		a. Item ( ITEM,Primary key, Not null, varchar(15) )
		
		We may set varchar(25) ever longer in the future.


## 反转值

一开始，由于角色的姓名规则均为日本/中国的姓名规则（姓在前），但后来遇到了欧美姓名的情况(名在前)，特此引入一个解决方法-反转值

    0
    
    角色姓名符合日本/中国的姓名规则，短名字模式输出名字
    
    这是数据库的默认值
    
    e.g.平泽**唯**，涂山**苏苏**
  
  
    
    1
    
    角色姓名符合欧美的姓名规则，短名字模式输出名字
    
    e.g.**德拉**·莫奇马兹，**乔瑟夫**·乔斯达
    
    

    2
    
    角色仅有名，无姓（或官方没有说明姓）
    
    e.g.丹尼，伊奇
    
    
    或者角色只有姓（或官方没有说明名字）
    
    e.g.高木同学，西片
    
    
    或者角色虽然有姓名，但其别称更耳熟/不适合进行姓名拆分
    
    e.g.胖重，面玛，苏沐橙
    
    注意，仅有姓的角色也应该被录入到“名字”列
    
    
    
    
    100
    
    角色姓名符合日本/中国的姓名规则，但短名字模式输出姓
    
    e.g.**花京院**典明，**白银**御行
    
    

    101
    
    角色姓名符合欧美的姓名规则，但短名字模式输出姓
    
    e.g.穆罕默德·**阿布德尔**，简·皮耶尔·**波鲁纳雷夫**

短名字开关（short_name）以布尔值形式存在，真时不会输出姓（角色只有姓除外）

反转值不适用于复姓名字的一些情况，例如惣流·明日香·兰格雷（短名字为明日香），目前没有办法解决，请使用反转值2录入

## 后期录入

后期数据库录入通过将视频接入弹幕检测系统，匹配符合规则的弹幕。

发送弹幕不会返回任何内容到发送者。

为了防止数据库被注入攻击，所有弹幕内容被严格过滤，请不要尝试提交以下值：

	• 空值
	
	• SQL/Linux bash/Windows CMD等命令
	
	• Python代码
	
	• 在Github/Bilibili简介已经出现的例子
	
	• 含空格的字符串
	
	• 转义字符（\）
	
	• 颜文字（可能存在转义字符）
	
	• 其它不能正确录入的值或可能影响代码和数据库正常运行的值
	
由于违规操作会造成代码和数据库的崩溃或不稳定，所有违规操作或疑似违规操作将记录UID，如果用户在视频发送违规格式的数据库录入型弹幕超过三次，将自动拉入黑名单，故意录入违规值（如颜文字）的用户将直接拉黑

默认情况下，用户如果提交的是纯中文值，会被自动录入，如果是以下任何情况，将转为人工审核：

	• 名字含大小写字母
	
	• 名字含数字
	
	• 名字含特殊符号或疑似正则表达式符号
	
	• 其它可能影响代码和数据库正常运行的值
	
我们鼓励大家尽可能提交纯中文值，即使这是国外作品的角色，目前没有考虑开发其它语言的版本，且纯中文录入能有效防止数据库被攻击

后期录入除继续录入日本/中国动漫角色以外，同时接受游戏角色和欧美动漫角色等，甚至鬼畜全明星或三次元人物（例如田所浩二）

但是三次元人物我们建议尽量提交昵称（如giao哥）而不是一个已经存在的人物名字（如某站CEO）

对于物品，类型不限制，可以是现实存在的，也可以是虚构的，也可以是小场景（例如花店）或其它未归类的物品或概念（如AT立场）等，但是它不能是：

	• 不可被感知或看见的物品、抽象的概念（例如相对论）
	
	• 人物或人物概念（例如保镖，老婆）
	
	• 大场景或大区域（例如常盘台中学，东京都，兔山商店街）
	
	• 宗教和政治相关物品或概念（即使剧中出现也不允许）
	
	• 严重色情，严重违法物品或概念（在已过审剧中出现的物品或概念则不算，例如枪）
	
	• 其它认为不合适或违反相关法律法规的物品或概念
	
虽然录入不合法的物品不会被拉入黑名单，但我们仍然不鼓励这样做


## 版权

所有源代码和数据库在GitHub上开源发布，欢迎所有人对数据库和源代码进行优化和完善

由于所有引用动漫作品没有得到官方许可，所以仅做娱乐和个人用途

请不要用于商业等盈利场景!

## Copyright

All code and database tables is open source on GitHub, we welcome everyone to improve the source code and enrich the tables.

All anime charatcers are not officially authorized, entertainment and personal use only.

DO NOT USE IT IN BUSINESS PURPOSES! 


