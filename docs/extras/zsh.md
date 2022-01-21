# zsh shell Tips and Tricks

[zsh man](https://zsh.sourceforge.io/Doc/zsh_a4.pdf)

## Fast cd

To ```cd``` seaming less into directories in a ```zsh```:

### Example

```
$ pwd
~

$ cf foo
$ pwd
~/path/to/working/dir/foo
```

### Explanation

1. Dirs in the file ```~/.zshrc_dirs``` will be placed on the stack when the shell starts
1. All directories which are visited by ```cd``` are pushed on the dir stack as well
1. In this example ```cf``` is configured as a zsh function
1. ```cf foo``` will cd into the latest vistited dir which it finds with ```grep -i foo``` (case independent)

### Configuration

- ~/.zshrc_dirs:
```
~/path/to/working/dir/foo
~/path/to/other/dir/bar
``` 

- ~/.zshrc:
```
dirs $(< ~/.zshrc_dirs)

cf () {
	cd -$(dirs -v | grep -i $1 | head -1 | cut -f1)
}
```

