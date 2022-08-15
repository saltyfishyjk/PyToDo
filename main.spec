# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['main.py', 'mycalendar.py', 'database.py', 'gettime.py', 'home.py', 'login.py', 
    'preresources_rc.py', 'setup.py', 'signup.py', 'task.py', 'mymatrix.py', 'NewTask.py',
    'ui_calendar.py', 'user.py', 'ui_matrix.py', 'ui_newtask.py', 'ui_pic.py',
    'D:\\GitHub_WorkSpace\\BUAA-Python\\PyToDo\\PyToDo\\modules\\__init__.py',
    'D:\\GitHub_WorkSpace\\BUAA-Python\\PyToDo\\PyToDo\\modules\\app_functions.py',
    'D:\\GitHub_WorkSpace\\BUAA-Python\\PyToDo\\PyToDo\\modules\\app_settings.py',
    'D:\\GitHub_WorkSpace\\BUAA-Python\\PyToDo\\PyToDo\\modules\\resources_rc.py',
    'D:\\GitHub_WorkSpace\\BUAA-Python\\PyToDo\\PyToDo\\modules\\ui_functions.py',
    'D:\\GitHub_WorkSpace\\BUAA-Python\\PyToDo\\PyToDo\\modules\\ui_main.py',
    'D:\\GitHub_WorkSpace\\BUAA-Python\\PyToDo\\PyToDo\\widgets\\__init__.py'
    ],
    pathex=[],
    binaries=[],
    datas=[('D:\\GitHub_WorkSpace\\BUAA-Python\\PyToDo\\PyToDo\\images', 'images'),
            ('D:\\GitHub_WorkSpace\\BUAA-Python\\PyToDo\\PyToDo\\img', 'img'),
            ('D:\\GitHub_WorkSpace\\BUAA-Python\\PyToDo\\PyToDo\\log', 'log'),
            ('D:\\GitHub_WorkSpace\\BUAA-Python\\PyToDo\\PyToDo\\themes', 'themes')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='D:\\GitHub_WorkSpace\\BUAA-Python\\PyToDo\\PyToDo\\images\\images\\inboxtodo.png'
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='main',
)
