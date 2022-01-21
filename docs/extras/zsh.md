# zsh shell Tipps and Trix

## zsh
[zsh man](https://zsh.sourceforge.io/Doc/zsh_a4.pdf)

## fast cd
To fast cd into often used directories with zsh.

In this case cofigured as the function ```cf```.

### Usage

```
$ pwd
~
$ cf foo
$ pwd
~/path/to/working/dir/foo
```

### Configuration
~/.zshrc:
```
dirs $(< ~/.zshrc_dirs)

cf () {
	cd -$(dirs -v | grep -i $1 | head -1 | cut -f1)
}
```

~/.zshrc_dirs:
```
~/path/to/working/dir/foo
~/path/to/other/dir/bar
``` 




