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
| 07 | Enrutador Inteligente | pendiente | Sin implementación |
| 08 | Voz de Marca Inteligente | pendiente | Sin implementación |
| 09 | Verificador Normativo | pendiente | Sin implementación |
| 10 | Puerta de Aprobación Humana | validada | V2 funcional con CLI, demo y tests locales |

## Nota operativa

Las siguientes skills deben iniciarse reutilizando `src/skillforge/skills/_plantilla_skill.py` para mantener consistencia técnica, trazabilidad y velocidad de desarrollo.

Publicado bajo licencia Creative Commons CC BY-SA 4.0 International.  
© 2025 – Txema Ríos. Todos los derechos compartidos.