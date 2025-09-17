# -*- mode: python ; coding: utf-8 -*-
# Advanced Image Processor Application Spec File
# Created for legitimate image processing software with adaptive overlay system
# Features: Smart sizing, adaptive light/dark overlays, offline operation

app_analysis = Analysis(
    ['image_processor_app.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[
        # PIL Core Components
        'PIL._tkinter_finder',
        'PIL.ImageTk',
        'PIL.Image',
        'PIL.ImageFile',
        'PIL.ImageOps',
        'PIL.ImageStat',
        'PIL.ImageFilter',
        
        # Image Format Plugins
        'PIL.JpegImagePlugin',
        'PIL.PngImagePlugin',
        'PIL.GifImagePlugin',
        'PIL.BmpImagePlugin',
        'PIL.WebPImagePlugin',
        'PIL.TiffImagePlugin',
        
        # Tkinter Components
        'tkinter.filedialog',
        'tkinter.messagebox',
        'tkinter.ttk',
        'tkinter.font',
        
        # Python Standard Library
        'concurrent.futures',
        'json',
        'tempfile',
        'shutil'
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        'tkinter.test', 
        '_tkinter_test',
        'test',
        'tests',
        'unittest'
    ],
    noarchive=False,
    optimize=2,
)

app_pyz = PYZ(app_analysis.pure, app_analysis.zipped_data)

app_exe = EXE(
    app_pyz,
    app_analysis.scripts,
    app_analysis.binaries,
    app_analysis.datas,
    [],
    name='AdvancedImageProcessor',
    debug=False,
    bootloader_ignore_signals=False,
    strip=True,
    upx=False,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=None,
    version_info=None,
    # Additional security and performance settings
    manifest=None,
    uac_admin=False,
    uac_uiaccess=False
)
