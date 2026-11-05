#!/usr/bin/env python3
"""Block Claude Code from touching .env files. Template files like .env.example stay allowed."""
import json
import re
import sys

SAFE_SUFFIXES = (".example", ".sample", ".template")
ENV_FILE = re.compile(r"(?<![\w.-])\.env(\.[\w-]+)?(?![\w-])")


def touches_env(text):
    return any(not match.group().endswith(SAFE_SUFFIXES) for match in ENV_FILE.finditer(text))


def main():
    event = json.load(sys.stdin)
    tool_input = event.get("tool_input", {})
    target = tool_input.get("command") or tool_input.get("file_path") or ""
    if touches_env(target):
        print("Blocked: .env files hold secrets. Ask the user to do this by hand.", file=sys.stderr)
        sys.exit(2)


if __name__ == "__main__":
    main()
