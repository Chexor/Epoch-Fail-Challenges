# 10. Troubleshooting


### Common Issues:

#### Broken Pipe Errors:
- Occur when reader terminates before writer
- Usually harmless in interactive use

#### Permission Denied:
```bash
# Can't write to file
echo "test" > /etc/hosts  # Permission denied

# Solution: use sudo
echo "test" | sudo tee -a /etc/hosts
```

#### No Output from Pipeline:
- Check each command separately
- Use intermediate files for debugging

```bash
# Debug pipeline step by step
command1 > temp1.txt
command2 < temp1.txt > temp2.txt
command3 < temp2.txt
```
---

## Navigation

**Next:** [→ Review Questions](10_Modules/S2%20-%20Introduction%20to%20Linux/Bronnen/IntroToLinux-Repo/04-Redirects-Pipes/11-review-questions.md)  
**Previous:** [← Performance And Best Practices](09-performance-and-best-practices.md)  
**Lesson Home:** [↑ Lesson 4: Redirects & Pipes](../)
**Course Home:** [⌂ Introduction to Linux](10_Modules/S2%20-%20Introduction%20to%20Linux/Bronnen/IntroToLinux-Repo/README.md)
