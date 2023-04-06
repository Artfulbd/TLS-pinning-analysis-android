1. Install fida on machine pip install frida-tools
2. Download frida server for android for emulator it is x86_64
- check architecture by adb shell getprop ro.product.cpu.abi 
path E:\GIT\TLS-pinning-analysis-android\Hooking\frida-server-16.0.11-android-x86_64

3. Push it to the emulator (first start emulator as usually)
adb push E:\GIT\TLS-pinning-analysis-android\Hooking\frida-server-16.0.11-android-x86_64 /data/local/tmp/frida-server

4. Enable root access to the device
adb root

5. Make the server binary executable
adb shell "chmod 755 /data/local/tmp/frida-server"

6. Start the server on your device
adb shell "/data/local/tmp/frida-server &"

7. Install frida on PC -> pip install frida-tools

8. Now hook

frida -U -l E:\GIT\TLS-pinning-analysis-android\Hooking\frida-script.js -f com.walmart.android

9. Kill Frida
adb shell ps -e | findstr frida-server
adb shell kill 4476 pid