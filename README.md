# giftdraw1000

simple, web server based program for random drawing of who should be given a gift for e.g. christmas 

---

## configuration

in `config.py`:
- set `seed` that will be used for the random generator
- set `participants` as list of string

## running

just run the command:

```
python server.py
```

server will be available at `localhost:8080` and will generate `participants.txt` with with the 'keys' of each participant

## usage

to see who has been chosen for you visit `localhost:8080/chuj/<your key>`
