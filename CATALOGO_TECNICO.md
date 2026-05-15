# Catalogo Tecnico de Skills

## Estado de implementacion

- `pendiente`: no iniciada.
- `en_progreso`: con esqueleto o desarrollo parcial.
- `validada`: con tests locales en verde y contrato comun cumplido.

## Criterio de aceptacion minimo por skill

- Ejecuta en local sin Internet ni APIs externas para validacion base.
- Usa `EntradaSkill` y devuelve `ResultadoSkill`.
- Incluye trazabilidad local y advertencias explicitas cuando aplique.
- Anade tests de comportamiento principal y casos de error.
- Documenta ejemplo de ejecucion y evidencia reproducible.

## Matriz de skills

| ID | Skill | Estado | Criterio actual |
|---|---|---|---|
| 01 | Lector Inteligente Documental | validada | V1 local con demo, evidencia y tests |
| 02 | Radar de Anomalias | validada | V1 local con umbral estadistico, demo y tests |
| 03 | Forjador de Informes | validada | V1 local con informe markdown, demo y tests |
| 04 | Memoria Contextual de Cliente | validada | V1 local con timeline, conflictos y tests |
| 05 | Pulso de Riesgo | validada | V1 local con scoring, umbrales y tests |
| 06 | Buscador Privado Aumentado | validada | V1 local con ranking y citas internas |
| 07 | Enrutador Inteligente | validada | V1 local con reglas de ruteo y plan de ejecucion |
| 08 | Voz de Marca Inteligente | validada | V1 local con ajuste de tono y checklist |
| 09 | Verificador Normativo | validada | V1 local con reglas y no conformidades |
| 10 | Puerta de Aprobacion Humana | validada | V2 funcional con CLI, demo y tests locales |

## Cierre operativo actual

El repositorio queda en estado operativo base: las 10 skills previstas estan implementadas en version local validada con tests automaticos y evidencias reproducibles.

## Nota operativa

Las siguientes iteraciones deben mantener el contrato comun (`EntradaSkill` y `ResultadoSkill`), seguridad por diseno, trazabilidad y revision humana para acciones sensibles.

Publicado bajo licencia Creative Commons CC BY-SA 4.0 International.
(c) 2025 - Txema Rios. Todos los derechos compartidos.
