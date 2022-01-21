# zsh shell Tipps and Trix

## zsh
[zsh man](https://zsh.sourceforge.io/Doc/zsh_a4.pdf)

## fast cd
~/.zshrc:
```dirs $(< ~/.zshrc_dirs)

cf () {
	cd -$(dirs -v | grep -i $1 | head -1 | cut -f1)
}
```


~/.zshrc_dirs:
```~/path/to/working/dir
~/path/to/other/dir
``` 




