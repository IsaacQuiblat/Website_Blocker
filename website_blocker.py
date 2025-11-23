from datetime import datetime
import time

hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"

def block(sites):
    with open(hosts_path, 'r+') as hostsfile:
        hosts_content = hostsfile.read()
        for site in sites:
            if site not in hosts_content:
                hostsfile.write(redirect + " " + site + "\n")

def unblock(sites):
    with open(hosts_path, 'r+') as hostsfile:
        lines = hostsfile.readlines()
        hostsfile.seek(0)
        for line in lines:
            if not any(site in line for site in sites):
                hostsfile.write(line)
        hostsfile.truncate()

def run_blocker():
    print("------------------WEBSITE BLOCKER------------------")
    print("Enter website(s) to block (separate with comma ',')")
    sites_input = input("Sites: ")
    sites_to_block = [site.strip() for site in sites_input.split(",")]

    print("Set the end time (format: YYYY-MM-DD HH:MM)")
    user_input = input("End time: ")
    end_time = datetime.strptime(user_input, "%Y-%m-%d %H:%M")

    print(f"Blocking enabled until: {end_time}. Press Ctrl+C to unblock instantly.")

    try:
        while True:
            now = datetime.now()
            if now < end_time:
                print(f"[{now}] Blocking sites...")
                block(sites_to_block)
            else:
                print(f"[{now}] Time is up! Unblocking sites...")
                unblock(sites_to_block)
                break
            time.sleep(5)
    except KeyboardInterrupt:
        print("Sites Unblocked!")
    finally:
        unblock(sites_to_block)

    # After unblocking, ask user if they want to block again
    choice = input("Do you want to block another website? (y/n): ").lower()
    if choice == "y":
        print()
        run_blocker()
    else:
        print("Program ended. Thank You!")


run_blocker()
