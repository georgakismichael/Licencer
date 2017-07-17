REM del dist /F /Q
REM del build /F /Q
del lic_gen.spec
pyinstaller -F --path C:\Python27\Lib\site-packages\netifaces-0.10.6.dist-info lic_gen.py