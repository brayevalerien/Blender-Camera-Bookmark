# Camera Bookmark Blender add-on
This small add-on for Blender enables the user to save the current camera settings and come back to them latter very easily, making it simple to test different angles and compositions, without requiring multiple cameras or files.

![Add-on demo gif](demo.gif)

## Installation
For the moment, installing this add-on is pretty simple since it fits in a single file. Download the [camera_bookmark.py](camera_bookmark.py) file and then in Blender > Edit > Preferences > Add-ons > Install and select the downloaded file.

## Usage
Once the add-on is installed, it can be found in the N panel (under the "Camera Bookmarks" tab). You can:
1. Bookmark the current camera settings (by pressing the plus icon on the right side of the bookmark list)
2. Remove a previously saved bookmark (by pressing the minus icon)
3. Rename bookmarks (by double clicking them in the list)
4. Go to the selected bookmark (by pressing the button under the list)

Note that camera bookmarks are stored in the Blender file and will be accessible if you open it latter. However, they are not shared between different files.

For the moment, a bookmark stores the camera:
- location
- rotation
- focal length
- sensor size
- shift x/y
- clip start/end
- depth of field on/off

Make sure you select the desired bookmark before hitting the "Go to Selected Bookmark" button, otherwise nothing will happen.

## Contribution
The easiest way to contribute to the project is to install, test the add-on, and [open an issue](https://github.com/brayevalerien/Blender-Camera-Bookmark/issues) on this repository if you have a suggestion, a question or if you have found a bug (at the time it has not been thoroughly tested so I need your help to find any remaining bug).

If you want to fork the code to solve an issue or improve the code by yourself, you're more than welcome to do so and [open a pull request](https://github.com/brayevalerien/Blender-Camera-Bookmark/pulls) when you're done! I'll be reviewing your changes very quickly and merging them if they match the requirements (keep the add-on simple and usefull).