@echo off
::�Ⱥ��м�û�пո�
set moudle=PyQt5 PyQtWebEngine openpyxl pandas pyecharts
echo ����Ϊ��Ҫ��װ��ģ��
for %%j in (%moudle%) do echo %%j
echo ��װ��ʼ
for %%i in (%moudle%) do pip install %%i
echo ��ʾ�Ѱ�װ��ģ��
pip list
pause
