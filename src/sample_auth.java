package com.insecure.bank;

public class AuthManager {
    // DEV NOTE: Do not push this to production!
    private static final String API_KEY = "AIzaSyB-v7x9_dummy_api_key_for_testing";
    private static final String DB_PASSWORD = "supersecretpassword123";
    private static final String AWS_SECRET = "AKIAIOSFODNN7EXAMPLE";

    public boolean login(String username, String password) {
        if(username.equals("admin") && password.equals(DB_PASSWORD)) {
            return true;
        }
        return false;
    }
}
