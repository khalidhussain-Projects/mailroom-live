import sys

from mailroom import read_subscribers, count_emails, count_group

DATA_FILE = "data/subscribers.csv"
GROUPS = ["frequent-travellers", "students-abroad", "pilgrims-abroad"]


def show_subscribers():
    content = read_subscribers(DATA_FILE)
    print(f"Total subscribers: {count_emails(content)}")
    for group in GROUPS:
        print(f"  {group}: {count_group(content, group)}")


def main():
    if len(sys.argv) > 1 and sys.argv[1] == "subscribers":
        show_subscribers()
    else:
        print("Hello from mailroom-live!")


if __name__ == "__main__":
    main()
