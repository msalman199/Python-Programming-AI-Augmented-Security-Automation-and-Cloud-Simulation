from safe_runner import SafeSubprocessRunner

runner = SafeSubprocessRunner()

# These should all fail safely
dangerous_commands = [
    "ls; rm -rf /tmp/test",
    "cat /etc/passwd && echo 'hacked'",
    "echo test | grep test",
    "rm -rf /",
    "cat /etc/passwd"
]

for cmd in dangerous_commands:
    result = runner.execute(cmd)
    print(f"Command: {cmd}")
    print(f"Blocked: {not result['success']}\n")
