import keyboard
import time
import platform

def main():
    ostype = platform.system().lower()
    while True:

        if ostype == "windows":
            windows()
            break
        elif ostype == "linux":
            linux()
            break
        elif ostype == "darwin":
            mac()
            break
        else:
            print("Invalid Operating System. Please try again on a differant amchine or controibute to the code on GitHub.")
    
    #Add a menue with options to find location, exit, cheack internet, or rerun the script
def windows():

    keyboard.press_and_release("win+r")
    time.sleep(0.5)
    keyboard.write("powershell")
    keyboard.press_and_release("enter")
    time.sleep(1)
    keyboard.write(""" $debug="$PWD\debug.txt"; "===== SYSTEM DEBUG REPORT ====="|Out-File $debug; systeminfo /fo list|Out-File $debug -Append; "===== HOSTNAME =====`n$(hostname)"|Out-File $debug -Append; "===== CPU =====`n$(Get-CimInstance Win32_Processor | ForEach-Object { "$($_.Name) Cores: $($_.NumberOfCores) Speed: $($_.MaxClockSpeed) MHz" })"|Out-File $debug -Append; "===== MEMORY =====`n$(Get-CimInstance Win32_ComputerSystem | ForEach-Object { "{0:N0} Bytes" -f $_.TotalPhysicalMemory })"|Out-File $debug -Append; "===== NETWORK =====`n$(Get-NetIPAddress | ForEach-Object { "$($_.InterfaceAlias): $($_.IPAddress)" })"|Out-File $debug -Append; "===== WIFI =====`n$(netsh wlan show interfaces)"|Out-File $debug -Append; "===== TOP PROCESSES =====`n$(Get-Process | Sort-Object CPU -Descending | Select-Object -First 10 | ForEach-Object { "$($_.ProcessName) CPU: $($_.CPU)" })"|Out-File $debug -Append; Write-Output "✅ Debug report saved to $debug" """, delay=0.05)
    keyboard.press_and_release("enter")
    time.sleep(10)
    keyboard.press_and_release("ctrl+c")
    keyboard.write("notepad debug.txt")
    keyboard.press_and_release("enter")

def linux():
    keyboard.press_and_release("ctrl+alt+t")
    time.sleep(1)
    keyboard.write("""(echo "===== SYSTEM DEBUG REPORT ====="; echo "===== HOSTNAME ====="; hostname; echo "===== OS ====="; cat /etc/os-release; echo "===== CPU ====="; lscpu | grep 'Model name'; echo "===== MEMORY ====="; free -h; echo "===== DISK INFO ====="; df -h; echo "===== NETWORK ====="; ip addr; echo "===== WIFI ====="; nmcli dev wifi list; echo "===== TOP PROCESSES ====="; ps -Ao pid,comm,%cpu,%mem --sort=-%cpu | head -n 11) > debug.txt""", delay=0.05)
    time.sleep(10)
    keyboard.write("cat debug.txt")
    keyboard.press_and_release("enter")
    
def mac():
    keyboard.press_and_release("cmd+space")
    time.sleep(0.5)
    keyboard.write("Terminal")
    keyboard.press_and_release("enter")
    time.sleep(1)
    keyboard.write("""(echo "===== SYSTEM DEBUG REPORT ====="; echo "===== HOSTNAME ====="; hostname; echo "===== OS ====="; sw_vers; echo "===== CPU ====="; sysctl -n machdep.cpu.brand_string; echo "===== MEMORY ====="; sysctl -n hw.memsize; echo "===== DISK INFO ====="; df -h; echo "===== NETWORK ====="; ifconfig; echo "===== WIFI ====="; /System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -I; echo "===== TOP PROCESSES ====="; ps -Ao pid,comm,%cpu,%mem --sort=-%cpu | head -n 11) > debug.txt""", delay=0.05)
    time.sleep(10)
    keyboard.write("cat debug.txt")
    keyboard.press_and_release("enter")
if __name__ == "__main__":
    main()