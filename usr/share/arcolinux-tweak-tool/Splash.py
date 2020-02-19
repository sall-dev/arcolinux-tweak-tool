import gi
from Functions import os
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf, Gdk  # noqa

base_dir = os.path.dirname(os.path.realpath(__file__))


class splashScreen():
    def __init__(self):
        super(splashScreen, self).__init__()
        self.window = Gtk.Window(Gtk.WindowType.POPUP)
        self.window.set_decorated(False)
        self.window.set_size_request(400, 150)
        self.window.set_position(Gtk.WindowPosition.CENTER)

        main_vbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=1)
        self.window.add(main_vbox)

        self.image = Gtk.Image()
        self.image.set_name('wind')
        pimage = GdkPixbuf.Pixbuf().new_from_file_at_size(base_dir +
                                                          "/images/splash.png",
                                                          400, 200)
        self.image.set_from_pixbuf(pimage)

        main_vbox.pack_start(self.image, True, True, 0)

        css = b"""
#wind {
    border: 6px solid #196966;
}"""
        style_provider = Gtk.CssProvider()
        style_provider.load_from_data(css)

        Gtk.StyleContext.add_provider_for_screen(
            Gdk.Screen.get_default(),
            style_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )
        self.window.show_all()