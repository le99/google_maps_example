## Venv
``` bash
python3 -m venv .venv
. ./.venv/bin/activate
```

## Dependencies
``` bash
python3 -m pip install folium jupyter
python3 -m pip install ipykernel
python3 -m ipykernel install --user --name=projectname

python3 -m pip install requests

python3 -m pip freeze > requirements.txt
```

## Load if requirements.txt exists
```bash
python3 -m pip install -r requirements.txt
```

## Jupyter plugin

https://stackoverflow.com/questions/58119823/jupyter-notebooks-in-visual-studio-code-does-not-use-the-active-virtual-environm
https://anbasile.github.io/posts/2017-06-25-jupyter-venv/



https://python-visualization.github.io/folium/modules.html#module-folium.vector_layers



## Google Maps
https://developers.google.com/maps/documentation/javascript/adding-a-google-map#maps_add_map-javascript