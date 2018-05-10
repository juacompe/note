# My profile.d


## Usage

    [[ "$0" == "${HOME}/.profile.d/README.md" ]] && return 0
    ln -s `pwd` ~/.profile.d
    [[ ! `grep 'for f in ~/.profile.d/\*; do source $f; done' ~/.zshrc` ]] && echo 'for f in ~/.profile.d/*; do source $f; done' >> ~/.zshrc

