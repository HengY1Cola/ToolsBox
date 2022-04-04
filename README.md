<p align="center">
  <a href="https://github.com/HengY1Sky/JNU-ToolsBox">
    <img src="https://www.hengy1.top/img/Shin-chan.png" width="200" height="200" alt="portrait">
  </a>
</p>


<div align="center">


# Jnu-ToolsBox

_✨ 由@HengY1发起与维护 ✨_  

</div>

<p align="center">
  <a href="https://github.com/HengY1Sky/JNU-ToolsBox">
    <img src="https://img.shields.io/github/repo-size/HengY1Sky/Jnu-ToolsBox" alt="license">
  </a>
  <a href="https://github.com/HengY1Sky/JNU-ToolsBox">
    <img src="https://img.shields.io/badge/Version-0.0.1-green" alt="license">
  </a>
</p>

## 项目定位 🌍

> 👏欢迎大家成为本项目的参与者，踊跃提交PR与Issue

自己没事喜欢捣鼓，也为了方便大家快速找到所需资源，**避免重复造轮子**。

设计的所有PDF均已经上传到自搭网盘中，**方可有需自取下载**

现在**部分功能源码**已经开源，其余的正在路上（～￣▽￣～）

##  责任说明 🚀

> *最终解释权归作者本人所有，请自觉遵守以下规则

- 允许第三方 / 个人**无偿使用**

- 若产生纠纷等问题，由使用者**自己承担**

- 使用者需要**标注使用来源并且严格遵守开源协议**

- 使用者未经允许**禁止收集用户个人隐私**

- 使用者禁止使用该项目进行**封闭式的引流**

- 使用者禁止**恶意使用接口，第三方有偿售卖/商用等行为**

##  课外拓展 🌟 

> 本分支主要面向面试，相关资料能够助力您冲击大厂

<img src="https://www.hengy1.top/img/code0402.png" alt="" style="width:50%;float:left" />

> 👆以上截图于20220402,路漫漫其修远兮～

|       名称       |                           链接                           | 取件码 |
| :--------------: | :------------------------------------------------------: | :----: |
| 数据结构算法分支 | https://github.com/HengY1Sky/Jnu-ToolsBox/tree/structure |   无   |
|   八股文电子书   |              https://yun.hengy1.top/s/JyFB               | 885ucb |

*以上的电子书本人几乎看完了，最后上传了质量不错的

*在此在线求职**后端Go方向开发**，**收简历**的前辈请在ISSUE中留下邮箱（优先考虑大厂）

##  第三方服务 🤔

> 注意⚠️ 相关事项写在了文档详情中了，注意查收
>
> 部分接口学校服务器作为下游服务器,限定为每5秒请求一次（目前试运行具有保守性）

🦌 接口总路由： https://api.hengy1.top  ｜ 此域名 + 相对路由

🔎 文档详情：https://www.hengy1.top/service/

----

- **宿舍水费预警/充值系统** => https://www.hengy1.top/service/JnuWater.html

😊 注册服务后将会**在每天的 8:00AM 以及 6:00PM 检测余额是否小于30元** (仅番禺校区)

|       描述        |        路由        | 方式 |         参数         |
| :---------------: | :----------------: | :--: | :------------------: |
|  查询余额等信息   | /IBSJnuWeb/balance | GET  |      dormitory       |
| 查询消费记录信息  |  /IBSJnuWeb/stat   | GET  |      dormitory       |
| 注册服务/取消服务 |  /IBSJnuWeb/email  | GET  |   email&dormitory    |
|     验证邮箱      | /IBSJnuWeb/verify  | GET  |        token         |
|     余额充值      | /IBSJnuWeb/charge  | GET  | dormitory&room&money |

- **教务系统** => https://www.hengy1.top/service/school.html

😊 教务系统暂时支持**本科生系统**（研究生没有账号）

😊 教务系统连续错误5次即会锁账号，本服务错误4次即会在1小时内停止服务

|      描述      |       路由       | 方式 |       参数       |
| :------------: | :--------------: | :--: | :--------------: |
|     课程表     |   /school/exam   | POST | account&password |
|    考试安排    | /school/schedule | POST | account&password |
| 总成绩与总绩点 |  /school/score   | POST | account&password |

- **健康每日打卡** => https://github.com/HengY1Sky/Jnu-Stuhealth
- **青年大学习团委完成度** => 本分支下的目录 （填写该团委的账号密码就好了）

##  绩点资料 📖

- 对应分支 👉：https://github.com/HengY1Sky/Jnu-ToolsBox/tree/course

|     学期     |             链接              | 取件码 |
| :----------: | :---------------------------: | :----: |
|     大一     | https://yun.hengy1.top/s/Xlh8 | 8gzf1m |
|    大二上    | https://yun.hengy1.top/s/M2I8 | 07k973 |
| 数据结构期末 | https://yun.hengy1.top/s/YjHp | 7pefni |

##  新兵蛋子 🧪 

> 面向新生提供的建议～ 欢迎大家提交自己的博客链接 为新生提供有效的帮助 包括但不限于 学习 技术
>
> *请提交到ISSUE中：格式：描述---作者---链接
>
> 本人友链：https://www.hengy1.top/link/

----

暂无

##  贡献者 ✨

<table>
  <tr>
    <td align="center"><a href="https://github.com/HengY1Sky/JNU-ToolsBox"><img src="https://avatars.githubusercontent.com/u/98681454?v=4" width="100px;" alt=""/><br /><sub><b>HengY1</b></sub></a><br /><a href="https://github.com/HengY1Sky/JNU-ToolsBox/commits?author=HengY1Sky" title="Tests">⚠️</a> <a href="https://github.com/HengY1Sky/JNU-ToolsBox/commits?author=HengY1Sky" title="Code">💻</a></td>
  </tr>
</table>

> This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!

##  未来计划 ⌛️

- 🏷️ 一键评教（等评教开通）
- 🏷️ 新生图书馆自动答题
- 🏷️ 教务系统增加有效的并发性（目前是试运行具有保守性）
