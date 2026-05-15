# Skills IA Empresariales

Biblioteca modular en castellano de skills IA empresariales reutilizables, auditables y demostrables.

## Objetivo del repositorio

Este repositorio define una base tecnica para construir capacidades IA reutilizables que puedan funcionar de forma independiente o integradas en agentes mayores. No es una coleccion de prompts y no es un agente monolitico.

## Principios tecnicos

- Modularidad por skill con contratos comunes.
- Enfoque free-first y local-first.
- Trazabilidad, validacion y revision humana en acciones sensibles.
- Limites explicitos sobre automatizacion y alcance.
- Compatibilidad con Python 3.11.

## Estado actual

El repositorio se encuentra en estado operativo local-first con las 10 skills previstas implementadas y validadas.

Resumen de avance:

- V0: estructura base, documentacion inicial, contrato comun minimo y test de humo.
- V1: nucleo comun de validacion y trazabilidad reutilizable.
- V2: primera skill funcional con control humano explicito.
- V3: implementacion del catalogo empresarial en modulos independientes.
- V4: demos locales y evidencias reproducibles para validacion tecnica.

Las siguientes iteraciones se gestionan desde V5 en adelante en `ROADMAP.md`.

## Skills previstas

01. Lector Inteligente Documental
02. Radar de Anomalias
03. Forjador de Informes
04. Memoria Contextual de Cliente
05. Pulso de Riesgo
06. Buscador Privado Aumentado
07. Enrutador Inteligente
08. Voz de Marca Inteligente
09. Verificador Normativo
10. Puerta de Aprobacion Humana

## Ejecucion de pruebas

```bash
python -m pytest -q
```

## Nota de seguridad por diseno

La arquitectura aplica seguridad por diseno mediante validacion, trazabilidad y limites explicitos. Las decisiones de alto impacto requieren revision humana.

## Aclaracion profesional

Este proyecto no sustituye revision profesional en ambitos regulados (legal, fiscal, sanitario, financiero o equivalentes).

Publicado bajo licencia Creative Commons CC BY-SA 4.0 International.
(c) 2025 - Txema Rios. Todos los derechos compartidos.
