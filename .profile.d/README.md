# My profile.d


## Usage

    [[ ! -L "${HOME}/.profile.d" ]] && ln -s `pwd` ~/.profile.d
    [[ ! `grep 'for f in ~/.profile.d/\*; do source $f; done' ~/.zshrc` ]] && echo 'for f in ~/.profile.d/*; do source $f; done' >> ~/.zshrc

