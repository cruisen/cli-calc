# zsh shell Tips and Tricks

[zsh man](https://zsh.sourceforge.io/Doc/zsh_a4.pdf)

## Fast cd
To cd seaming less into directories in a ```zsh```:

### Example
```
$ pwd
~

$ cf foo
$ pwd
~/path/to/working/dir/foo
```

### Explanation
- In this example configured as the zsh function ```cf```.
- ```cf foo``` will cd into the last dir which it finds with ```grep -i foo``` (case independent)
- However all dirs in the file ```~/.zshrc_dirs``` will be placed on the stack first.
- And all directories which are visited by ```cd``` as well.

### Configuration
~/.zshrc:
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

