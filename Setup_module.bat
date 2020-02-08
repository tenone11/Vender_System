@echo off
::等号中间没有空格
set moudle=PyQt5 PyQtWebEngine openpyxl pandas pyecharts
echo 以下为将要安装的模块
for %%j in (%moudle%) do echo %%j
echo 安装开始
for %%i in (%moudle%) do pip install %%i
echo 显示已安装的模块
pip list
pause
