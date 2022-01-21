# zsh shell Tips and Tricks

[zsh man](https://zsh.sourceforge.io/Doc/zsh_a4.pdf)

## fast cd
To cd seaming less into directories with zsh:

- In this example configured as the zsh function ```cf```.
- ```cf``` will cd into the last dir which it finds with ```grep -i``` (case indipendant)
- However all dirs in teh file ```~/.zshrc_dirs``` will be palced on teh stack.

```
cf () {
	cd -$(dirs -v | grep -i $1 | head -1 | cut -f1)
}
```

~/.zshrc_dirs:
```
~/path/to/working/dir/foo
~/path/to/other/dir/bar
``` 




