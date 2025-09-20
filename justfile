MY_IP := "$(ip addr show enp0s1 | rg 'inet ([\\d\\.]+)' -o --replace '$1')"

install:
    brew install zola

check:
    dprint check --config ~/.config/dprint/dprint.json

format:
    dprint fmt --config ~/.config/dprint/dprint.json

run:
    zola serve --interface 0.0.0.0 --base-url http://{{MY_IP}}
