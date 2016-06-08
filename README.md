# Random wallpaper
get_wallpaper is a python script that fetches a random wallpaper from
`https://unsplash.com/'` and can be used from feh in order to be set as
a background:

    feh --bg-scale `./get_wallpaper.py`

this only works in non gnome desktop environments. For gnome you need
to use gconftool.

#### installing as a command

    sudo ln -s get_wallpaper.py /usr/local/bin/get_wallpaper.py


