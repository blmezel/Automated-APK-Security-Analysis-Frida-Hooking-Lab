/*
 * Module: Root Detection Bypass Payload
 * Course: Reverse Engineering (BGT210)
 * Description: Hooks file system checks to hide root binaries (su, Superuser.apk).
 */

Java.perform(function() {
    console.log("[*] Injecting Root Detection Bypass payload...");

    var File = Java.use("java.io.File");

    // List of common root files to hide from the application
    var rootPaths = [
        "/system/app/Superuser.apk",
        "/sbin/su",
        "/system/bin/su",
        "/system/xbin/su",
        "/data/local/xbin/su",
        "/data/local/bin/su",
        "/system/sd/xbin/su",
        "/system/bin/failsafe/su",
        "/data/local/su"
    ];

    // Hooking the exists() method of java.io.File
    File.exists.implementation = function() {
        var filePath = this.getAbsolutePath();
        
        // Check if the app is looking for a root binary
        for (var i = 0; i < rootPaths.length; i++) {
            if (filePath == rootPaths[i]) {
                console.log("[+] Intercepted root check for: " + filePath + " -> Returning false.");
                return false; // Lie to the app, pretend the root file doesn't exist
            }
        }
        
        // If it's a normal file, return the real result
        return this.exists();
    };

    console.log("[+] Root Detection Bypass payload successfully injected and active.");
});
