import os
import subprocess

OPTIONS = {
    "1": (
        "Smart Revise Quiz",
        "https://smartrevise.online/student/revise/Question/74",
    ),
    "2": (
        "Smart Revise Terminology",
        "https://smartrevise.online/student/reviseterminology/index/74",
    ),
    "3": (
        "Sparx Maths",
        "https://maths.sparx-learning.com/student/",
    ),
}


def find_chrome():
    """Find chrome.exe in common Windows installation locations."""
    paths = [
        os.path.expandvars(
            r"%ProgramFiles%\Google\Chrome\Application\chrome.exe"
        ),
        os.path.expandvars(
            r"%ProgramFiles(x86)%\Google\Chrome\Application\chrome.exe"
        ),
        os.path.expandvars(
            r"%LocalAppData%\Google\Chrome\Application\chrome.exe"
        ),
    ]

    for path in paths:
        if os.path.isfile(path):
            return path

    return None


def main():
    print()
    print("What would you like to automate today?")
    print()

    for number, (name, _) in OPTIONS.items():
        print(f"{number}. {name}")

    print()

    while True:
        choice = input("Enter your choice (1-3): ").strip()

        if choice in OPTIONS:
            break

        print("Invalid choice. Please enter 1, 2, or 3.")
        print()

    chrome = find_chrome()

    if chrome is None:
        print()
        print("Chrome could not be found on this computer.")
        print("Please make sure Google Chrome is installed.")
        input("\nPress Enter to exit...")
        return

    name, url = OPTIONS[choice]

    print()
    print(f"Opening {name}...")

    subprocess.Popen([
        chrome,
        url
    ])


if __name__ == "__main__":
    main()
