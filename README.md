# Windows
si no funciona el comando python intentar python3 o python3.7

## Venv (se puede hace desde VisualCode)
``` bash
python -m venv .venv
. ./.venv/Scripts/activate
```
## Dependencies
``` bash
python -m pip install folium
#or
python -m pip install -r requirements.txt

#To save requirements
python -m pip freeze > requirements.txt
```

# Linux/mac

## Venv
``` bash
python3 -m venv .venv
. ./.venv/bin/activate
```

## Dependencies
``` bash
python3 -m pip install folium
#or
python3 -m pip install -r requirements.txt

#To save requirements
python3 -m pip freeze > requirements.txt
```

## Folium
#https://python-visualization.github.io/folium/quickstart.html