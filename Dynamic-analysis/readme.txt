1. Install android studio cli (required java>=11 as it needs class fomate version 55)
2. unzip it and open terminal on bin folder
3. run-> sdkmanager "platform-tools" "platforms;android-30" "build-tools;30.0.2"
4. add to env_var_path -> some_loc\Android\platform-tools
5. run -> sdkmanager "system-images;android-33;google_apis_playstore;x86_64"
6. run -> avdmanager create avd --name "Custom_pxl_7_pro_API_33" --package "system-images;android-33;google_apis_playstore;x86_64"
7. change in _>C:\Users\Admin\.android\avd\Custom_pxl_7_pro_API_33.avd\config.ini

/* replicate Pixel Pro 7 */
PlayStore.enabled = yes
hw.keyboard = yes
hw.lcd.density = 560
hw.lcd.height = 3120
hw.lcd.width = 1440
vm.heapSize = 64M
hw.ramSize = 4096



adb shell pm uninstall com.instagram.android
Failure [DELETE_FAILED_INTERNAL_ERROR]

adb shell pm disable-user --user 0 com.android.vending       <--disabling play store
Package package_name new state: disabled  

adb shell pm enable com.android.vending                      <--anabling play store
Package com.android.vending new state: enabled





adb shell pm list packages -f                         <--see installed packages

list packages [-f] [-d] [-e] [-s] [-3] [-i] [-l] [-u] [-U] [--uid UID] [--user USER_ID] [FILTER]
Prints all packages; optionally only those whose name contains
the text in FILTER.
Options:
-f: see their associated file
-d: filter to only show disabled packages
-e: filter to only show enabled packages
-s: filter to only show system packages
-3: filter to only show third party packages
-i: see the installer for the packages
-l: ignored (used for compatibility with older releases)
-U: also show the package UID
-u: also include uninstalled packages
--uid UID: filter to only show packages with the given UID
--user USER_ID: only list packages belonging to the given user