DATA_FILE = "data/subscribers.csv"


# ---- Tests, written first, before read_subscribers_file() exists below ----

def test_read_returns_string(file_content):
    assert type(file_content) == str


def test_total_emails(file_content):
    lines = file_content.strip().split("\n")
    data_lines = lines[1:]  # drop the header row
    assert len(data_lines) == 24


def test_frequent_travellers_group_count(file_content):
    lines = file_content.strip().split("\n")
    data_lines = lines[1:]  # drop the header row

    count = 0
    for line in data_lines:
        if "frequent-travellers" in line:
            count = count + 1

    assert count == 8


# ---- The actual code, written to satisfy the tests above ----

def read_subscribers_file(path):
    with open(path) as f:
        content = f.read()
    return content


# ---- Run everything ----

def main():
    content = read_subscribers_file(DATA_FILE)

    test_read_returns_string(content)
    test_total_emails(content)
    test_frequent_travellers_group_count(content)

    print("All tests passed!")


if __name__ == "__main__":
    main()
