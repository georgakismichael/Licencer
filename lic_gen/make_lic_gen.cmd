REM del dist /F /Q
REM del build /F /Q
del lic_gen.spec
REM pyinstaller -F --path C:\Python27\Lib\site-packages\netifaces-0.10.6.dist-info lic_gen.py
pyinstaller -F --path C:\Python27\Lib\site-packages\netifaces-0.10.6.dist-info lic_gen_gui_main.py
.\dist\lic_gen_gui_main.exe