"""
gff.stats
--------------
Herramienta simple para calcular estadísticas de un archivo GFF.

Características:
- Cuenta el número de features por tipo (columna 3).
- Calcula la distribución por strand (columna 7).
- Calcula la longitud media de los features (end - start + 1).
- Permite filtrar por un tipo de feature concreto mediante el argumento `--feature_type`.

Salida:
Devuelve un JSON con las claves `feature_counts`, `strand_distribution` y `average_length`.

Ejemplo de uso (desde la línea de comandos):
    python gff.stats.py anotaciones.gff --feature_type gene

Notas:
- El programa ignora líneas que empiezan por `#` y líneas mal formateadas con menos de 9 columnas.
- Está pensado como una utilidad pequeña para análisis exploratorio; no valida exhaustivamente el formato GFF.
"""
import json
from collections import defaultdict
import sys
import argparse
def gff_stats(gff_file, feature_type=None):
    """
    Función para calcular estadísticas de un archivo GFF.
    
    Parámetros:
    gff_file (str): Ruta al archivo GFF.
    feature_type (str, opcional): Tipo de feature a analizar. Si es None, se analizan todos los tipos.
    
    Retorna:
    dict: Diccionario con las estadísticas calculadas.
    """
    feature_counts = defaultdict(int)
    strand_distribution = defaultdict(int)
    total_length = 0
    total_features = 0

    with open(gff_file, 'r') as f:
        for line in f:
            if line.startswith('#'):
                continue  # Saltar comentarios
            columns = line.strip().split('\t')
            if len(columns) < 9:
                continue  # Saltar líneas mal formateadas
            
            f_type = columns[2]
            start = int(columns[3])
            end = int(columns[4])
            strand = columns[6]

            if feature_type and f_type != feature_type:
                continue  # Saltar si no es el tipo de feature deseado

            feature_counts[f_type] += 1
            strand_distribution[strand] += 1
            total_length += (end - start + 1)
            total_features += 1

    average_length = total_length / total_features if total_features > 0 else 0

    stats = {
        'feature_counts': dict(feature_counts),
        'strand_distribution': dict(strand_distribution),
        'average_length': average_length
    }

    return stats
def main():
    """
    Punto de entrada para la línea de comandos.

    Analiza los argumentos provistos por el usuario, ejecuta el cálculo de estadísticas
    sobre el archivo GFF especificado y escribe el resultado en formato JSON en
    la salida estándar.

    Argumentos de línea de comandos:
    - `gff_file`: ruta al archivo GFF a procesar.
    - `--feature_type`: (opcional) filtrar por un tipo de feature concreto.

    Ejemplo:
        python gff.stats.py anotaciones.gff --feature_type gene
    """
    parser = argparse.ArgumentParser(description='Calcular estadísticas de un archivo GFF.')
    parser.add_argument('gff_file', help='Ruta al archivo GFF.')
    parser.add_argument('--feature_type', help='Tipo de feature a analizar (opcional).', default=None)
    args = parser.parse_args()

    stats = gff_stats(args.gff_file, args.feature_type)
    print(json.dumps(stats, indent=4))

if __name__ == '__main__':
    main()

