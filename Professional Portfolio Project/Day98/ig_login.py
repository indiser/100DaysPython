import time
import os
import undetected_chromedriver as uc

def generate_persistent_session():
    """Creates a local Chrome profile and gives you 5 minutes to log in manually."""
    
    # 1. Create a dedicated folder inside your project directory to hold the session data
    profile_path = os.path.join(os.getcwd(), "IgBotProfile")
    print(f"Provisioning local browser profile at: {profile_path}")
    
    options = uc.ChromeOptions()
    options.add_argument(f"--user-data-dir={profile_path}")
    
    # 2. Launch the stealth browser with correct Chrome version
    driver = uc.Chrome(options=options, version_main=145)
    
    try:
        print("\n--- INFILTRATION INITIATED ---")
        driver.get("https://www.instagram.com/")
        
        print("\n🚨 HUMAN INTERVENTION REQUIRED 🚨")
        print("1. Log into your Instagram account in the browser window.")
        print("2. When prompted, you MUST click 'Save Your Login Info'.")
        print("3. Dismiss any 'Turn on Notifications' popups.")
        print("You have 5 minutes to complete this before the session locks in...\n")
        
        # Keep the browser open for 300 seconds so you can do the manual work
        time.sleep(300)
        
    finally:
        print("Locking session data and closing browser...")
        driver.quit()
        print("Profile saved. You never have to log in manually again.")

if __name__ == "__main__":
    generate_persistent_session()