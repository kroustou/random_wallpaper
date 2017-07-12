# Random wallpaper
get_wallpaper is a python script that fetches a random wallpaper from
`https://unsplash.com/'` and can be used from feh in order to be set as
a background.

How to use:

1. Create API token from unsplash
2. run:

    feh --bg-scale `UNSPLASH_CLIENT_ID='<client_id>' ./get_wallpaper.py`

3. profit

this only works in non gnome desktop environments. For gnome you need
to use gconftool.

#### command to be used for cronjob

	#!/bin/bash
	source /home/staurosk/.virtualenvs/random_wallpaper/bin/activate
	LINK="$(/usr/local/bin/get_wallpaper.py)"
	DISPLAY=:0 /usr/bin/feh --bg-scale ${LINK}




