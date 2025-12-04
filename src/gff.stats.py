# Ejercicio 3: estadísticas de un archivo GFF
# El objetivo de este programa es contar el número de features por tipo en un archivo GFF, contar el average lenght
# y la distribución por strand
# Para contar el número de features
# Podemos usar un diccionario donde las keys son los tipos de features y los values son los contadores
# Podemos eliminar los comentarios con el método startswith('#')
# Podemos usar el método split('\t') para separar las columnas
# Para contar el average length
# Podemos restar la columna 5 (end) menos la columna 4 (start) para obtener la longitud de cada feature
# Sumamos todas las longitudes y dividimos por el número total de features
# Para contar la distribución por strand
# Podemos usar otro diccionario donde las keys son los strands ('+', '-') y los values son los contadores
# Haga el archivo para enviarlo json
# Añadir documentación al código
# Añadir la función para que el usuario pueda escoger el tipo de feature (si así lo requiere) para analizar
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
    parser = argparse.ArgumentParser(description='Calcular estadísticas de un archivo GFF.')
    parser.add_argument('gff_file', help='Ruta al archivo GFF.')
    parser.add_argument('--feature_type', help='Tipo de feature a analizar (opcional).', default=None)
    args = parser.parse_args()

    stats = gff_stats(args.gff_file, args.feature_type)
    print(json.dumps(stats, indent=4))

