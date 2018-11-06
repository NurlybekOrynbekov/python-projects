import cx_Freeze
executables = [cx_Freeze.Executable("main.py")]

cx_Freeze.setup(
    name="Space Invaders",
    version = "1",
    options={"build_exe": {"packages":["pyglet", "cocos", "pygame", "collections", "random"]}},
    executables = executables
    )