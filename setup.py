from distutils.core import setup
import platform
sys_type = platform.system()

if sys_type == "Windows":
    """For windows system, add auto run service."""
    import os
    import sys
    import win32api
    import win32con

    def add_python_to_autorun(pyfile):
        print('Add to auto-run.')
        runpath = "Software\\Microsoft\\Windows\\CurrentVersion\\Run"
        hKey = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER, runpath, 0, win32con.KEY_SET_VALUE)
        path = os.path.abspath(pyfile)
        if os.path.isfile(path):
            cmd = '{}\\pythonw.exe {}'.format(sys.prefix, path)
            win32api.RegSetValueEx(hKey, 'MessageNotifierService', 0, win32con.REG_SZ, cmd)
            import subprocess
            subprocess.Popen('{}\\pythonw.exe MessageNotifier.py'.format(sys.prefix))   # run service
        win32api.RegCloseKey(hKey)

    def remove_python_to_autorun():
        print('remove auto-run.')
        runpath = "Software\\Microsoft\\Windows\\CurrentVersion\\Run"
        hKey = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER, runpath, 0, win32con.KEY_ALL_ACCESS)
        try:
            win32api.RegDeleteValue(hKey, 'MessageNotifierService')
        except:
            pass
        win32api.RegCloseKey(hKey)

    attrs = sys.argv[1:]
    if 'remove' in attrs:
        remove_python_to_autorun()
        exit(0)
    elif 'install' in attrs:
        add_python_to_autorun('{}\\Lib\\site-packages\\MessageNotifier.py'.format(sys.prefix))


# setup
setup(name='MessageNotifier',
      version='1.0',
      py_modules=['MessageNotifier'],
      )

