# Guía Demo Local

## Instalación de dependencias de desarrollo

```bash
python -m pip install -e ".[dev]"
```

## Ejecución de tests

```bash
python -m pytest -q
```

## Criterio de demos futuras

Las demos deberán funcionar en local sin depender de APIs externas para su validación básica.

## Proveedor LLM opcional en fases futuras

Groq podrá añadirse como proveedor LLM opcional en iteraciones posteriores, sin romper el flujo local-first.

## Alcance V0

La V0 valida estructura de repositorio, documentación base y contrato común mínimo con test de humo.
Publicado bajo licencia Creative Commons CC BY-SA 4.0 International.  
© 2025 – Txema Ríos. Todos los derechos compartidos.
