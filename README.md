# Skills IA Empresariales

Biblioteca modular en castellano de skills IA empresariales reutilizables, auditables y demostrables.

## Objetivo del repositorio

Este repositorio define una base técnica para construir capacidades IA reutilizables que puedan funcionar de forma independiente o integradas en agentes mayores. No es una colección de prompts y no es un agente monolítico.

## Principios técnicos

- Modularidad por skill con contratos comunes.
- Enfoque free-first y local-first.
- Trazabilidad, validación y revisión humana en acciones sensibles.
- Límites explícitos sobre automatización y alcance.
- Compatibilidad con Python 3.11.

## Estado V0

La versión V0 crea estructura base, documentación inicial, contrato común mínimo y test de humo. No implementa todavía la lógica completa de las 10 skills.

## Skills previstas

01. Lector Inteligente Documental
02. Radar de Anomalías
03. Forjador de Informes
04. Memoria Contextual de Cliente
05. Pulso de Riesgo
06. Buscador Privado Aumentado
07. Enrutador Inteligente
08. Voz de Marca Inteligente
09. Verificador Normativo
10. Puerta de Aprobación Humana

## Ejecución de pruebas

```bash
python -m pytest -q
```

## Nota de seguridad por diseño

La arquitectura aplica seguridad por diseño mediante validación, trazabilidad y límites explícitos. Las decisiones de alto impacto requieren revisión humana.

## Aclaración profesional

Este proyecto no sustituye revisión profesional en ámbitos regulados (legal, fiscal, sanitario, financiero o equivalentes).
Publicado bajo licencia Creative Commons CC BY-SA 4.0 International.  
© 2025 – Txema Ríos. Todos los derechos compartidos.
