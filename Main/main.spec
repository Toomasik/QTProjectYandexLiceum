# -*- mode: python ; coding: utf-8 -*-

import os

base_dir = os.getcwd()
root_dir = os.path.abspath(os.path.join(base_dir, '..'))

datas = [
    (os.path.join(root_dir, 'products.db'), '.'),
    (os.path.join(root_dir, 'Main', 'main.ui'), '.'),
    (os.path.join(root_dir, 'AdminFncs', 'addProduct', 'addProduct.ui'), 'AdminFncs/addProduct'),
    (os.path.join(root_dir, 'AdminFncs', 'changeInfo', 'changeInfo.ui'), 'AdminFncs/changeInfo'),
    (os.path.join(root_dir, 'AdminFncs', 'deleteProduct', 'deleteProduct.ui'), 'AdminFncs/deleteProduct'),
    (os.path.join(root_dir, 'AdminFncs', 'isAdmin.txt'), 'AdminFncs'),
    (os.path.join(root_dir, 'Card', 'card.ui'), 'Card'),
    (os.path.join(root_dir, 'Card', 'card_info.ui'), 'Card'),
    (os.path.join(root_dir, 'Cart', 'cart.ui'), 'Cart'),
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
    noarchive=False
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='main',
    console=False
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='main'
)
