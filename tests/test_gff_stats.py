import importlib.util
from pathlib import Path


def _load_gff_stats_module():
    """Carga el módulo `gff.stats.py` directamente desde la ruta `src/`.

    Usamos carga dinámica para evitar problemas con nombres de módulo que contienen
    puntos en el fichero.
    """
    repo_root = Path(__file__).resolve().parents[1]
    module_path = repo_root / "src" / "gff.stats.py"
    spec = importlib.util.spec_from_file_location("gff_stats_mod", str(module_path))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_gff_stats_basic(tmp_path):
    mod = _load_gff_stats_module()

    gff = tmp_path / "sample.gff"
    gff.write_text(
        """##gff-version 3
chr1\tsource\tgene\t1\t100\t.\t+\t.\tID=gene1
chr1\tsource\texon\t1\t50\t.\t+\t.\tID=exon1;Parent=gene1
chr1\tsource\tgene\t200\t300\t.\t-\t.\tID=gene2
"""
    )

    stats = mod.gff_stats(str(gff))

    assert stats["feature_counts"]["gene"] == 2
    assert stats["feature_counts"]["exon"] == 1
    assert stats["strand_distribution"]["+"] == 2
    assert stats["strand_distribution"]["-"] == 1

    # longitudes: gene1 = 100, exon1 = 50, gene2 = 101 => average = 251/3
    expected_avg = (100 + 50 + 101) / 3
    assert abs(stats["average_length"] - expected_avg) < 1e-8


def test_feature_type_filter(tmp_path):
    mod = _load_gff_stats_module()

    gff = tmp_path / "sample2.gff"
    gff.write_text(
        """chr1\tsource\tgene\t10\t20\t.\t+\t.\tID=gene1
chr1\tsource\texon\t11\t12\t.\t+\t.\tID=exon1
"""
    )

    stats = mod.gff_stats(str(gff), feature_type="exon")

    assert stats["feature_counts"] == {"exon": 1}
    assert stats["strand_distribution"] == {"+": 1}
    assert stats["average_length"] == 2
