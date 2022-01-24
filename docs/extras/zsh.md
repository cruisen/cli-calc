# zsh shell Tips and Tricks

- zsh [man](https://zsh.sourceforge.io/Doc/zsh_a4.pdf)
  - [guide](https://scriptingosx.com/2019/06/moving-to-zsh/)

## Fast cd

To ```cd``` seaming less into directories in a ```zsh```:

### Example

```
$ pwd
~
$ cf foo
$ pwd
~/path/to/working/dir/foo
$
```

### Explanation

1. Dirs in the file ```~/.zshrc_dirs``` will be placed on the stack when the shell starts
1. All directories which are visited by ```cd``` are pushed on the dir stack as well
1. In this example ```cd``` is re-configured as a zsh function
1. ```cd foo``` will:
  - execute ```builtin cd``` cmd. 
  - When it fails it executes ```cf foo``` instead, and
  - will try to find a matching *foo* dir in ```dirs -v``` with ``grep -i foo`` (case independent).
  - If it finds one, it will ```cd``` into it.
  - If not it will print a final error message and exit.

### Configuration

- Create ~/.zshrc_dirs:

```
~/path/to/working/dir/foo
~/path/to/other/dir/bar
``` 

- Add to ~/.zshrc:

```
setopt autopushd pushdignoredups pushdminus

alias d='dirs -v'

dirs $(< ~/.zshrc_dirs)

cd() {
  builtin cd $1 2> /dev/null || cf $1
}

cf() {
 new=$(dirs -v | grep -i $1 | head -1 | cut -f1)
 if [[ -n $new ]] ; then
   cd -$new
 else
   echo "cd error: dir $1 not found..."
 fi
}
```

## zsh options

- ```setops``` to list all set options
- ```emulate -lLR zsh``` to list all avaiable options
