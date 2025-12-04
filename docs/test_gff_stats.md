# Pruebas para gff.stats

Este documento describe las pruebas unitarias creadas para `gff.stats.py` y cómo
ejecutarlas con `pytest`.

Archivos añadidos:
- `tests/test_gff_stats.py`: contiene dos pruebas que cubren el cómputo de estadísticas
  básico y el filtrado por tipo de feature.

Cómo ejecutar las pruebas (desde la raíz del repositorio):

```powershell
python -m pip install pytest  # si no tiene pytest
pytest -q
```

Qué comprueban las pruebas:
- `test_gff_stats_basic`: crea un GFF pequeño en tiempo de ejecución y comprueba:
  - conteo de features por tipo
  - distribución por strand
  - cálculo de la longitud media
- `test_feature_type_filter`: comprueba que el filtrado por `feature_type` devuelve
  únicamente las estadísticas del tipo solicitado.

Notas:
- Las pruebas cargan dinámicamente `gff.stats.py` desde `src/` para evitar problemas
  con nombres de módulos que contienen puntos en el nombre de fichero.
