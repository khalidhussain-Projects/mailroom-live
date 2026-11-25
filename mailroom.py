def read_subscribers(path):
    with open(path) as f:
        content = f.read()
    return content


def count_emails(content):
    lines = content.strip().split("\n")
    data_lines = lines[1:]  # drop the header row
    return len(data_lines)


def count_group(content, group_name):
    lines = content.strip().split("\n")
    data_lines = lines[1:]  # drop the header row

    count = 0
    for line in data_lines:
        if group_name in line:
            count = count + 1
    return count
