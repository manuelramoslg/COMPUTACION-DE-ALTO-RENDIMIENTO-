#  SPARQL

En la primera query ejecutada en wikidata consultamos los datos de los países, sus jefes de estado como también la fecha en que se fundó el país, con los datos de la fecha en que se fundó el país calculamos cuántos años tiene el país desde que se fundó.

La query ejecutada para extraer estos datos es la siguiente:

```
# PRIMERA QUERY
SELECT DISTINCT ?country ?countryLabel ?hgovernment ?hgovernmentLabel (?inception AS ?fundation) ?yearsOfFundation WHERE {
  ?country wdt:P31 wd:Q3624078.
  ?country p:P6 ?statement.
  ?statement ps:P6 ?hgovernment.
  ?country wdt:P6 ?hgovernment.
  ?country wdt:P571 ?inception.
  BIND((YEAR(NOW())) - (YEAR(?inception)) AS ?yearsOfFundation)
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
}
ORDER BY ?countryLabel
```

Para optimizar los resultados del test T se p agregaron valores a la búsqueda, estos son:
género o sexo del jefe de estado y el continente al cual pertenece el país

```
# SE AGREGÓ GENERO DEL PRESIDENTE Y CONTINENTE AL QUE PERTENECE EL PAIS
SELECT DISTINCT ?country ?countryLabel ?hgovernment ?hgovernmentLabel ?yearsOfFundation ?continentLabel ?sex_or_genderLabel WHERE {
  ?country wdt:P31 wd:Q3624078.
  ?country p:P6 ?statement.
  ?statement ps:P6 ?hgovernment.
  ?country wdt:P6 ?hgovernment.
  ?country wdt:P571 ?inception.
  BIND((YEAR(NOW())) - (YEAR(?inception)) AS ?yearsOfFundation)
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
  OPTIONAL { ?country wdt:P30 ?continent. }
  OPTIONAL { ?hgovernment wdt:P21 ?sex_or_gender. }
}
ORDER BY ?countryLabel
```

![captura de pantalla 2018-05-06 a la s 11 24 19](https://user-images.githubusercontent.com/4138880/39674494-271170bc-5123-11e8-8002-b668e1d0663b.png)
