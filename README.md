# pytest框架封装
- 改造pytest插件
- 生成allure测试报告

### 写在前面的话
拥有简单python与pytest基础后即可使用该项目，强烈建议使用于Test目录下命令行（cmd）运行pytest。
- 链接[pycharm运行参数化teardown的坑](https://blog.csdn.net/m0_46493851/article/details/113564004)

## 环境准备
- 安装 java
- 安装 allure
- 安装 python
- 以上软件安装完之后均需要配置环境变量
- 系统 windows
- ide pycharm
- chrome 88.0.4324.104（正式版本） （64 位）



## 目录文件
- \Test\conftest           : 改造pytest中setup与teardown方法
- \Test\pytest.ini         : 初始化pytest,自动生成allure报告
- \Test\result             : 存放allure报告文件
- \Test\bin\openReport.bat : 自动打开allure服务批处理文件
- \Tset\driver             : 存放selenium浏览器驱动
- \Test\dist               : 存放python打包文件及setup.py模板文件
  
