# pyenv (Python Version Manager)

## What is pyenv?
`pyenv` is a tool used to install, manage, and switch between multiple Python versions on the same machine.

It allows:
- Installing any Python version
- Switching between versions globally or per project
- Keeping system Python untouched and safe
- Ensuring each project uses the correct Python version



## Why use pyenv?
- Avoid "version mismatch" issues
- Different projects need different Python versions
- System Python should not be modified


## How pyenv works (Simple Explanation)
When you run `python`, pyenv changes your PATH so that:
- Instead of using system Python
- It uses a Python version installed and selected via pyenv

It also:
- Creates a `.python-version` file for local version settings
- Manages all installed Pythons inside `~/.pyenv/versions/`



## pyenv Installation (macOS)

### Install pyenv (Homebrew)
```
brew install pyenv
```

### Add pyenv to shell (zsh)
Add the following lines at the END of `~/.zshrc`:


```
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
```

Reload shell:

```
source ~/.zshrc
```

### Install required dependencies

```
brew install openssl readline sqlite3 xz zlib tcl-tk
```



## Common pyenv Commands

### Check installed versions

```
pyenv versions
```

### Install a Python version

```
pyenv install 3.10.12
pyenv install 3.11.6
```

### Set global Python version

```
pyenv global 3.11.6
```

### Set local (per-project) Python version
Inside a project folder:

```
pyenv local 3.10.12
```

### Check current Python version

```
python --version
```

### Uninstall a Python version
```
pyenv uninstall 3.12.0
```