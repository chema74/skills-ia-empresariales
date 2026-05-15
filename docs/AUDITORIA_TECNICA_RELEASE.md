# Auditoria Tecnica por Release

## Objetivo

Definir una checklist minima y repetible para auditoria tecnica antes de publicar una version.

## Checklist obligatoria

1. Calidad estatica en verde
- `python -m ruff check src tests`
- `python -m mypy src`

2. Pruebas en verde
- `python -m pytest -q`

3. Validacion de gobernanza
- Politicas versionadas disponibles en `configs/gobernanza/politicas_aprobacion_v1.json`
- Registro de cambios actualizado en `configs/gobernanza/registro_cambios_gobernanza.json`

4. Evidencias de demos
- Evidencias de flujos V6 y V7 presentes en `evidencias/salidas/`

5. Consistencia documental
- `ROADMAP.md` y `CHANGELOG.md` actualizados
- Checklist de release disponible en `RELEASE_CHECKLIST.md`

## Plantilla de acta de auditoria

```json
{
  "release": "vX.Y.Z",
  "fecha": "YYYY-MM-DD",
  "estado": "aprobada|rechazada",
  "resultados": {
    "ruff": true,
    "mypy": true,
    "pytest": true,
    "gobernanza_versionada": true,
    "registro_cambios_gobernanza": true,
    "evidencias_demo": true,
    "documentacion_actualizada": true
  },
  "observaciones": []
}
```
