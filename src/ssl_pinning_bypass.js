/*
 * Module: SSL Pinning Bypass Payload
 * Course: Reverse Engineering (BGT210)
 * Description: Hooks into Android's TrustManager to bypass SSL Certificate Pinning.
 */

Java.perform(function() {
    console.log("[*] Injecting SSL Pinning Bypass payload...");

    var TrustManagerImpl = Java.use('com.android.org.conscrypt.TrustManagerImpl');
    var ArrayList = Java.use("java.util.ArrayList");

    // Hooking the checkTrustedRecursive method to bypass certification checks
    TrustManagerImpl.checkTrustedRecursive.implementation = function(certs, host, clientAuth, untrustedChain, trustAnchorChain, used) {
        console.log("[+] Intercepted TrustManagerImpl.checkTrustedRecursive() for host: " + host);
        console.log("[!] Bypassing SSL Pinning mechanism. All certificates are now trusted!");
        return ArrayList.$new();
    };

    console.log("[+] SSL Pinning Bypass payload successfully injected and active.");
});
