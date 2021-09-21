# whats_for_dinner

Chaotic recipe selector for deciding what to make for dinner with the ThermoMix food processor.

Generates 100 random URLs matching the ThermoMix Cookidoo format and tries them all until it finds one that's actually a recipe. 

If the recipe is not in English, returns recipe language. 

If the recipe is in English, returns recipe URL. 

# Example output

```
$ python whats_for_dinner.py 

recipe in fr 
recipe in fr 
recipe in zh 
Strawberry mojito  en    https://cookidoo.thermomix.com/recipes/recipe/en-US/r127630
recipe in pt 
recipe in es 
recipe in de 
recipe in de 
recipe in de 
```


