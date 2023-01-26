from pywinauto import Application


shortcut = r"C:\Users\Tomh\Desktop\Portal 2 (2).url"

# Set the path to the new icon
icon = r"C:\Users\Public\Desktop\Brave.lnk"

# Launch the application
app = Application().start(shortcut)

# Get the window handle of the shortcut
w_handle = app.window(title="Shortcut Title").handle

# Set the icon
app.window(handle=w_handle).set_icon(icon, index=0)
