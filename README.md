# extensions

A collection of folders (because at the time I didn't know submodules were a thing) of browser extensions that all do one very minute job questionably well.

The idea was inspired after completing my senior capstone course during the spring semester of 2018 and realizing that browser extensions were a lot of fun to make :)

## General instructions unless stated otherwise:

1. Clone the repository


**Chrome**:

1. Go to the Chrome extension page at `chrome://extensions`
2. Toggle "Developer Mode" if it isn't already toggled
3. Select "Load Unpacked", and select the appropriate subfolder within this repository that contains the extension you want to install
4. The extension should be enabled by default, but if it isn't, enable it with the little toggle button.
5. Browse the internet with your newfound power

**Firefox**:
1. Go to the Firefox debugging page at `about:debugging`
2. Check the `Enable add-on` debugging box
3. Click `Load Temporary Add-on`
  * Note you'll need to do this every time you reopen the browser
  * You can avoid this by using the Firefox developer browser instead
4. Select a file *within* the subfolder corresponding to the extension you want to install; as you won't be able to select just the folder itself.
