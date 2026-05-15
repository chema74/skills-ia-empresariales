import json
import subprocess
import sys
from pathlib import Path


def test_cli_bloquea_accion_sensible_sin_aprobacion() -> None:
    repo = Path(__file__).resolve().parents[1]
    cmd = [
        sys.executable,
        "ejemplos/cli_puerta_aprobacion_humana.py",
        "--accion",
        "aprobar_pago",
        "--descripcion",
        "Pago urgente",
        "--solicitante",
        "finanzas",
    ]

    result = subprocess.run(cmd, cwd=repo, capture_output=True, text=True, check=True)
    salida = json.loads(result.stdout)

    assert salida["estado"] == "advertencia"
    assert salida["salida"]["requiere_aprobador"] is True


def test_cli_habilita_accion_con_aprobacion() -> None:
    repo = Path(__file__).resolve().parents[1]
    cmd = [
        sys.executable,
        "ejemplos/cli_puerta_aprobacion_humana.py",
        "--accion",
        "aprobar_pago",
        "--descripcion",
        "Pago urgente",
        "--solicitante",
        "finanzas",
        "--aprobador",
        "direccion",
        "--rol-aprobador",
        "direccion",
        "--evidencia-id",
        "EV-CLI-001",
        "--aprobada",
    ]

    result = subprocess.run(cmd, cwd=repo, capture_output=True, text=True, check=True)
    salida = json.loads(result.stdout)

    assert salida["estado"] == "ok"
    assert salida["salida"]["aprobador"] == "direccion"
