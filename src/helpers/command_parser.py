def parse_input(content: str):
    cmd, *args = content.split()
    cmd = cmd.strip().lower()
    return cmd, *args
