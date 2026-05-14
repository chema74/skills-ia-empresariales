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
| 01 | Lector Inteligente Documental | pendiente | Sin implementación |
| 02 | Radar de Anomalías | pendiente | Sin implementación |
| 03 | Forjador de Informes | pendiente | Sin implementación |
| 04 | Memoria Contextual de Cliente | pendiente | Sin implementación |
| 05 | Pulso de Riesgo | pendiente | Sin implementación |
| 06 | Buscador Privado Aumentado | pendiente | Sin implementación |
| 07 | Enrutador Inteligente | pendiente | Sin implementación |
| 08 | Voz de Marca Inteligente | pendiente | Sin implementación |
| 09 | Verificador Normativo | pendiente | Sin implementación |
| 10 | Puerta de Aprobación Humana | validada | V2 funcional con CLI, demo y tests locales |

## Nota operativa

Las siguientes skills deben iniciarse reutilizando `src/skillforge/skills/_plantilla_skill.py` para mantener consistencia técnica, trazabilidad y velocidad de desarrollo.

Publicado bajo licencia Creative Commons CC BY-SA 4.0 International.  
© 2025 – Txema Ríos. Todos los derechos compartidos.