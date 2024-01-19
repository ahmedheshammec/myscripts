
<!-- Add the following to the .zshrc file -->

quote_double() {
    LBUFFER+='""'
    CURSOR=$((CURSOR-1))
}
zle -N quote_double

quote_single() {
    LBUFFER+="''"
    CURSOR=$((CURSOR-1))
}
zle -N quote_single

bindkey '"' quote_double
bindkey "'" quote_single
