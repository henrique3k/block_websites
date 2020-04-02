# block-website
Bloqueador de website simples em python.

O objetivo desse script é bloquear websites para você produzir mais ainda, como estudar, trabalhar e manter o seu foco e concentração


É recomendado executar o script com privilégios administrativos para correto funcionamento.

Para rodar: 
```python3 block.py block```
```python3 block.py unblock```

LINUX EXTRA:

Você pode criar uma função em seu `.bashrc` ou no `.zshrc` dependendo do seu setup para chamar o script mais facilmente]

```
bloquear-sites(){
  sudo python3 $HOME/dev/block-website/block.py $1
}
```

inspirado pelo trabalho do [@CyberSecurityUP](https://github.com/CyberSecurityUP/block-website)
