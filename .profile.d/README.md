# My profile.d


## Usage

    [[ "$0" == "${HOME}/.profile.d/README.md" ]] && return 0
    ln -s `pwd` ~/.profile.d
    [[ ! `grep '. ~/.profile.d/\*' ~/.zshrc` ]] && echo '. ~/.profile.d/*' >> ~/.zshrc
    [[ ! `grep '. ~/.profile.d/alias' ~/.zshrc` ]] && echo '. ~/.profile.d/alias*' >> ~/.zshrc

