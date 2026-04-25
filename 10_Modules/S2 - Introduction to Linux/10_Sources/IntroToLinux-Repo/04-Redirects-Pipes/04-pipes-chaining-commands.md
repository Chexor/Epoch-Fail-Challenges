# 4. Pipes: Chaining Commands

## What Are Pipes?

Pipes (`|`) connect the output of one command to the input of another command, creating powerful command chains.

```
┌─────────┐    stdout   ┌─────────┐    stdout   ┌─────────┐
│Command 1│ ─────────▶  │Command 2│ ─────────▶  │Command 3│
└─────────┘             └─────────┘             └─────────┘
     │                       ▲                       │
     │                       │                       ▼
     ▼                   stdin from                Terminal
  Terminal                command1                  Screen
 (ignored)                                         (final)

Flow: cmd1 | cmd2 | cmd3
```

### Basic Pipe Syntax:

```bash
command1 | command2
command1 | command2 | command3

# Examples
ls | wc -l                    # Count files in directory
ps aux | grep firefox         # Find Firefox processes
cat /etc/passwd | head -5     # Show first 5 users
history | tail -10            # Show last 10 commands
```

## Pipe Chain Visualization

```
Example: ls -la | grep "txt" | wc -l

┌─────────┐   │   ┌─────────┐   │   ┌─────────┐
│ ls -la  │───┼──▶│grep txt │───┼──▶│ wc -l   │
└─────────┘   │   └─────────┘   │   └─────────┘
              │                 │
    All files │   Only .txt     │   Count of
    listed    │   files         │   .txt files
              ▼                 ▼
        -rw-r--r-- file1.txt    │
        drwxr-xr-x mydir   ──── │ ───▶ 3
        -rw-r--r-- file2.txt    │
        -rw-r--r-- script.sh    │
        -rw-r--r-- notes.txt    │
```

### Powerful Pipe Examples:

```bash
# Find largest files
ls -la | sort -k5 -nr | head -10

# Count unique users currently logged in
who | cut -d' ' -f1 | sort | uniq | wc -l

# Show memory usage sorted by usage
ps aux | sort -k4 -nr | head -10

# Find most used commands in history
history | awk '{print $2}' | sort | uniq -c | sort -nr | head -10

# Show directory sizes sorted
du -sh */ | sort -hr
```

## Complex Pipeline Example

```
Command: ps aux | grep -v grep | sort -k4 -nr | head -5

┌─────────┐   ┌─────────────┐   ┌─────────────┐   ┌─────────┐
│ ps aux  │──▶│grep -v grep │──▶│sort -k4 -nr │──▶│ head -5 │
└─────────┘   └─────────────┘   └─────────────┘   └─────────┘
     │              │                   │              │
     ▼              ▼                   ▼              ▼
All processes   Remove grep      Sort by memory    Top 5 by
running         from results     (highest first)   memory usage

USER  PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root    1  0.0  0.8  22528  8804 ?        Ss   Oct01   0:02 systemd
user  1234 1.2  4.5 123456 45678 ?        Sl   Oct01   1:23 firefox
user  5678 0.5  2.1  87654 21098 ?        S    Oct01   0:45 chrome
...
```

## Pipeline Best Practices

```
Good Practice:
┌─────────┐   ┌─────────┐   ┌─────────┐   ┌─────────┐
│ Input   │──▶│ Filter  │──▶│  Sort   │──▶│ Format  │
│ Source  │   │ Data    │   │ Data    │   │ Output  │
└─────────┘   └─────────┘   └─────────┘   └─────────┘

Example: cat data.txt | grep "error" | sort | uniq -c

Bad Practice:
┌─────────┐   ┌─────────┐   ┌─────────┐
│ cat     │──▶│ cat     │──▶│ cat     │  ← Unnecessary cats!
│ file    │   │ again   │   │ again   │
└─────────┘   └─────────┘   └─────────┘

Better: grep "error" data.txt | sort | uniq -c
```

## Pipe vs Redirection

```
Pipes (|):           Redirection (>, <):
Data flows between   Data flows to/from files
commands in memory   
                     
cmd1 | cmd2          cmd > file
  ▲─────▼               ▼
Memory buffer      ┌─────────┐
(temporary)        │ File on │
                   │ Disk    │
                   └─────────┘
```

---

## Navigation

**Next:** [→ Text Processing Commands](05-text-processing-commands.md)  
**Previous:** [← Input Redirection](03-input-redirection.md)  
**Lesson Home:** [↑ Lesson 4: Redirects & Pipes](../)
**Course Home:** [⌂ Introduction to Linux](10_Modules/S2%20-%20Introduction%20to%20Linux/10_Sources/IntroToLinux-Repo/README.md)
