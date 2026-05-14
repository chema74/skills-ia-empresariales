# Catálogo Técnico de Skills

## Estado de implementación

- `pendiente`: no iniciada.
- `en_progreso`: con esqueleto o desarrollo parcial.
- `validada`: con tests locales en verde y contrato común cumplido.

## Criterio de aceptación mínimo por skill

- Ejecuta en local sin Internet ni APIs externas para validación base.
- Usa `EntradaSkill` y devuelve `ResultadoSkill`.
- Incluye trazabilidad local y advertencias explícitas cuando aplique.
- Añade tests de comportamiento principal y casos de error.
- Documenta ejemplo de ejecución y evidencia reproducible.

## Matriz de skills

| ID | Skill | Estado | Criterio actual |
|---|---|---|---|
| 01 | Lector Inteligente Documental | validada | V1 local con demo, evidencia y tests |
| 02 | Radar de Anomalías | validada | V1 local con umbral estadístico, demo y tests |
| 03 | Forjador de Informes | validada | V1 local con informe markdown, demo y tests |
| 04 | Memoria Contextual de Cliente | validada | V1 local con timeline, conflictos y tests |
| 05 | Pulso de Riesgo | validada | V1 local con scoring, umbrales y tests |
| 06 | Buscador Privado Aumentado | validada | V1 local con ranking y citas internas |
| 07 | Enrutador Inteligente | validada | V1 local con reglas de ruteo y plan de ejecución |
| 08 | Voz de Marca Inteligente | validada | V1 local con ajuste de tono y checklist |
| 09 | Verificador Normativo | validada | V1 local con reglas y no conformidades |
| 10 | Puerta de Aprobación Humana | validada | V2 funcional con CLI, demo y tests locales |

## Cierre operativo actual

El repositorio queda en estado operativo base: las 10 skills previstas están implementadas en versión local validada con tests automáticos y evidencias reproducibles.

## Nota operativa

Las siguientes iteraciones deben mantener el contrato común (`EntradaSkill` y `ResultadoSkill`), seguridad por diseño, trazabilidad y revisión humana para acciones sensibles.

Publicado bajo licencia Creative Commons CC BY-SA 4.0 International.  
© 2025 – Txema Ríos. Todos los derechos compartidos.