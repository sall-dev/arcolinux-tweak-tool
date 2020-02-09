#=================================================================
#=                  Author: Brad Heffernan                       =
#=================================================================

import Functions
from Functions import GLib

def check_lightdm(lists, value):
    pos = Functions._get_position(lists, value)
    val = lists[pos].strip()
    return val
    # comman = Functions.check_lightdm_value(lines[Functions.get_lightdm(lines):], "autologin-user=")
            
def set_lightdm_value(self, lists, value, session, state):
    try:
        pos = Functions._get_position(lists, "autologin-user=")
        pos_session = Functions._get_position(lists, "autologin-session=")
        
        if state:
            lists[pos] = "autologin-user=" + value + "\n"
            lists[pos_session] = "autologin-session=" + session + "\n"
        else:
            if not "#" in lists[pos]:
                lists[pos] = "#" + lists[pos]
                lists[pos_session] = "#" + lists[pos_session]

        with open(Functions.lightdm_conf, "w") as f:
            f.writelines(lists)
            f.close()

        GLib.idle_add(Functions.show_in_app_notification,self, "Settings Saved Successfully")

        # GLib.idle_add(Functions.MessageBox,self, "Success!!", "Settings applied successfully")
    except Exception as e:
        print(e)
        Functions.MessageBox(self, "Failed!!", "There seems to have been a problem in \"set_lightdm_value\"")


def get_lines(files):
    if Functions.os.path.isfile(files):
        with open(files, "r") as f:
            lines = f.readlines()
            f.close()
        return lines

def pop_box(combo):
    coms = []
    for items in Functions.os.listdir("/usr/share/xsessions/"):
        coms.append(items.split(".")[0].lower())
    lines = get_lines(Functions.lightdm_conf)

    # pos = Functions._get_position(lines, "user-session=")
    name = check_lightdm(lines, "autologin-session=").split("=")[1]

    for i in range(len(coms)):
        excludes = ['gnome-classic', 'gnome-xorg', 'i3-with-shmlog', 'openbox-kde']
        if not coms[i] in excludes:
            combo.append_text(coms[i])
            if name in coms[i]:
                combo.set_active(i)
