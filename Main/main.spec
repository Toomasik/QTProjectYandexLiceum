# -*- mode: python ; coding: utf-8 -*-

import os
from PyInstaller.utils.hooks import collect_data_files

# Безопасное определение базовой директории
base_dir = os.getcwd()  # вместо os.path.dirname(__file__)
root_dir = os.path.abspath(os.path.join(base_dir, '..'))

# Добавляем ресурсы
datas = [
    (os.path.join(root_dir, 'products.db'), '.'),
    (os.path.join(root_dir, 'Main', 'main.ui'), '.'),
    (os.path.join(root_dir, 'AdminFncs', 'addProduct', 'addProduct.ui'), 'AdminFncs/addProduct'),
    (os.path.join(root_dir, 'AdminFncs', 'changeInfo', 'changeInfo.ui'), 'AdminFncs/changeInfo'),
    (os.path.join(root_dir, 'AdminFncs', 'deleteProduct', 'deleteProduct.ui'), 'AdminFncs/deleteProduct'),
    (os.path.join(root_dir, 'AdminFncs', 'isAdmin.txt'), 'AdminFncs'),
    (os.path.join(root_dir, 'Card', 'card.ui'), 'Card'),
    (os.path.join(root_dir, 'Card', 'card_info.ui'), 'Card'),
    (os.path.join(root_dir, 'Cart', 'profile.ui'), 'Cart'),
    (os.path.join(root_dir, 'Images'), 'Images'),
]

a = Analysis(
    ['main.py'],
    pathex=[base_dir],
    binaries=[],
    datas=datas,
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
)