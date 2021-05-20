# Windows
si no funciona el comando python intentar python3 o python3.7

## Venv (se puede hace desde VisualCode)
``` bash
python -m venv .venv
. ./.venv/Scripts/activate
```
## Dependencies
``` bash
python -m pip install folium jupyter ipykernel requests
#or
python -m pip install -r requirements.txt

#To save requirements
python -m pip freeze > requirements.txt
```

## Jupyter standalone
```bash
python -m ipykernel install --user --name=projectname
jupyter notebook
```

# Linux/mac

## Venv
``` bash
python3 -m venv .venv
. ./.venv/bin/activate
```

## Dependencies
``` bash
python3 -m pip install folium jupyter ipykernel requests
#or
python3 -m pip install -r requirements.txt

#To save requirements
python3 -m pip freeze > requirements.txt
```

## Jupyter plugin

https://stackoverflow.com/questions/58119823/jupyter-notebooks-in-visual-studio-code-does-not-use-the-active-virtual-environm
https://anbasile.github.io/posts/2017-06-25-jupyter-venv/
https://python-visualization.github.io/folium/modules.html#module-folium.vector_layers


## Jupiter standalone
```bash
python3 -m ipykernel install --user --name=projectname
jupyter notebook
```

## Google Maps
https://developers.google.com/maps/documentation/javascript/adding-a-google-map#maps_add_map-javascript