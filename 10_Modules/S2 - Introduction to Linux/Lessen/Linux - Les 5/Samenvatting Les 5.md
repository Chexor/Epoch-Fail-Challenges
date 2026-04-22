# Samenvatting Les 5 - Echo, Alias en Operators

#linux

## Kernidee

Deze les gaat over hoe de shell jouw input interpreteert en hoe je commando's sneller en slimmer gebruikt.

- quotes bepalen hoe tekst gelezen wordt
- `echo` toont tekst en escape sequences
- aliases maken shortcuts
- control operators koppelen commando's aan elkaar

## Quotes en whitespace

- spaties splitsen argumenten op, tenzij je quotes of escaping gebruikt
- single quotes `'...'` houden alles letterlijk
- double quotes `"..."` laten variabelen en command substitution toe
- backslash `\` kan een speciaal teken escapen

```bash
touch "my file.txt"
echo 'Hello $NAME'
echo "Hello $NAME"
touch my\ file.txt
```

## `echo` en special characters

- `echo` print tekst naar de terminal
- `echo -e` interpreteert escapes zoals `\n` en `\t`
- `echo -n` voegt geen newline toe
- speciale tekens zoals `$`, `"` en `\` moet je soms escapen

```bash
echo "Hello World"
echo -e "Line 1\nLine 2"
echo -n "No newline"
echo "The price is \$10"
```

## Command types en discovery

- een commando kan een builtin, external command, alias of function zijn
- `type` toont wat een commando precies is
- `type -a` toont alle varianten
- `which` en `command -v` helpen een commando terugvinden

```bash
type cd
type -a echo
which ls
command -v git
```

## Aliases

- een alias is een eigen shortcut voor een commando
- handig om sneller te werken en typfouten te vermijden
- `alias` toont bestaande aliases
- `unalias` verwijdert een alias
- permanente aliases zet je in `~/.bashrc`

```bash
alias ll='ls -la'
alias grep='grep --color=auto'
unalias ll
source ~/.bashrc
```

## Control operators

- `;` voert commando's na elkaar uit
- `&&` voert het volgende commando enkel uit bij succes
- `||` voert het volgende commando enkel uit bij fout
- `&` start een commando in de achtergrond
- `$?` toont de exit status van het laatste commando

```bash
pwd; ls; date
cd /tmp && ls
cd /bestaat-niet || echo "Directory not found"
sleep 30 &
echo $?
```

## Line continuation en escaping

- een backslash op het einde van een lijn laat een lang commando doorlopen
- escaping is nodig voor speciale tekens of bestandsnamen met spaties

```bash
find /home \
    -name "*.txt" \
    -type f

echo "Quote: \"Hello\""
touch file\ with\ spaces.txt
```

## Onthouden voor examen

- verschil tussen single quotes, double quotes en escaping
- verschil tussen builtin, external command en alias
- betekenis van `;`, `&&`, `||` en `&`
- nut van `type`, `which` en `command -v`
- files by inode vinden is examengericht
