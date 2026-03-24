# 1. Understanding Standard Streams

Every Linux process has three default streams:

## Visual Overview

```
┌─────────────────────────────────────────────────────────────┐
│                    Linux Process                            │
│                                                             │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐      │
│  │   stdin     │    │   stdout    │    │   stderr    │      │
│  │     (0)     │    │     (1)     │    │     (2)     │      │
│  └─────────────┘    └─────────────┘    └─────────────┘      │
│         ▲                   │                   │           │
└─────────┼───────────────────┼───────────────────┼───────────┘
          │                   │                   │
          │                   ▼                   ▼
    ┌─────────┐         ┌─────────────┐     ┌─────────────┐
    │Keyboard │         │   Terminal  │     │   Terminal  │
    │  Input  │         │   Screen    │     │   Screen    │
    └─────────┘         │  (normal)   │     │  (errors)   │
                        └─────────────┘     └─────────────┘
```

### Standard Input (stdin) - File Descriptor 0

- Where a program reads input
- Default: keyboard
- Can be redirected from files

**Example:**

```bash
# Reading from keyboard (default)
cat                    # Type something, press Ctrl+D to end

# Reading from file
cat < input.txt        # Redirect file to stdin
```

### Standard Output (stdout) - File Descriptor 1

- Where a program writes normal output
- Default: terminal screen
- Can be redirected to files

**Example:**

```bash
# Output to screen (default)
echo "Hello World"

# Output to file
echo "Hello World" > output.txt
```

### Standard Error (stderr) - File Descriptor 2

- Where a program writes error messages
- Default: terminal screen (same as stdout)
- Can be redirected separately from stdout

**Example:**

```bash
# Error to screen (default)
ls /nonexistent

# Error to file
ls /nonexistent 2> error.txt
```

## Stream Redirection Examples

```
Default behavior:
┌─────────┐    stdin     ┌─────────┐    stdout    ┌─────────┐
│Keyboard │ ───────────▶ │Command  │ ───────────▶ │Terminal │
└─────────┘              │         │              │Screen   │
                         │         │    stderr    │         │
                         └─────────┘ ───────────▶ └─────────┘

With redirection:
┌─────────┐    stdin     ┌─────────┐    stdout    ┌─────────┐
│File     │ ───────────▶ │Command  │ ───────────▶ │Output   │
│input.txt│              │         │              │File     │
└─────────┘              │         │    stderr    └─────────┘
                         │         │ ───────────▶ ┌─────────┐
                         └─────────┘              │Error    │
                                                  │File     │
                                                  └─────────┘
```

## ℹ️ Practical Example

```bash
# View file descriptors for current shell
ls -la /proc/$$/fd

# Example output:
# 0 -> /dev/pts/0  (stdin - terminal)
# 1 -> /dev/pts/0  (stdout - terminal)
# 2 -> /dev/pts/0  (stderr - terminal)
```

---

## Navigation

**Next:** [→ Output Redirection](02-output-redirection.md)  
**Previous:** [← Learning Objectives](10_Modules/S2%20-%20Introduction%20to%20Linux/Bronnen/IntroToLinux-Repo/04-Redirects-Pipes/00-learning-objectives.md)  
**Lesson Home:** [↑ Lesson 4: Redirects & Pipes](../)
**Course Home:** [⌂ Introduction to Linux](10_Modules/S2%20-%20Introduction%20to%20Linux/Bronnen/IntroToLinux-Repo/README.md)
