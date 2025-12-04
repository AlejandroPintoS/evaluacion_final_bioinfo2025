# Evaluación Final - Bioinformática 2025

Proyecto de ejemplo para el ejercicio final de la asignatura de Bioinformática.
Incluye una pequeña utilidad para calcular estadísticas sobre archivos GFF,
pruebas unitarias con `pytest` y documentación mínima.

## Estructura

- `src/` - código fuente del proyecto.
  - `gff.stats.py` - script principal que calcula estadísticas de un archivo GFF.
- `tests/` - pruebas automáticas (`pytest`).
- `docs/` - documentación y notas de las pruebas.

## Objetivo

Calcular estadísticas básicas sobre un archivo GFF (conteo por tipo de feature,
distribución por strand y longitud media). Permite filtrar por tipo de feature
con el argumento `--feature_type`.

## Requisitos

- Python 3.8+
- (Opcional) `pytest` para ejecutar las pruebas.

Instale `pytest` si aún no lo tiene:

```powershell
python -m pip install pytest
```

## Uso

Ejecutar el script pasando un archivo GFF como argumento:

```powershell
python src\gff.stats.py ruta/al/archivo.gff
```

Filtrar por tipo de feature (por ejemplo `gene`):

```powershell
python src\gff.stats.py ruta/al/archivo.gff --feature_type gene
```

El script imprime un JSON en la salida estándar con las claves:

- `feature_counts`: conteo de features por tipo.
- `strand_distribution`: conteo por strand (`+` / `-`).
- `average_length`: longitud media de los features (end - start + 1).

## Pruebas

Se han añadido pruebas con `pytest` en `tests/test_gff_stats.py`.
Para ejecutar las pruebas desde la raíz del repositorio:

```powershell
pytest -q
```

Debería ver las pruebas ejecutarse y pasar (en el entorno donde ya ejecuté las
pruebas localmente obtuve `2 passed`).

## Notas

- El script ignora líneas que comienzan con `#` y líneas con menos de 9 columnas.
- Está pensado como una utilidad de análisis exploratorio; no valida
  exhaustivamente todas las variaciones del formato GFF.

## Contacto / Autor

Autor: Alejandro Pinto S.

Si quieres que añada un `requirements.txt`, un archivo de configuración para
`pytest` o que haga un commit con estos cambios, dímelo y lo hago.
