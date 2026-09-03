# DSD canonical renumbering map

Date: 2026-09-03
Status: **AUTHORITATIVE CROSSWALK FOR LEGACY M5-481+**

Legacy files are retained. Canonical IDs below are used for all future references.

| Canonical module | Legacy range | Canonical range | Conversion |
|---|---:|---:|---|
| M5 | M5-481~502 | M5-001~022 | canonical local = legacy - 480 |
| M6 | M5-503~508 | M6-001~006 | canonical local = legacy - 502 |
| M7 | M5-509~522 | M7-001~014 | canonical local = legacy - 508 |
| M8 | M5-523~540 | M8-001~018 | canonical local = legacy - 522 |
| M9 | M5-541~558 | M9-001~018 | canonical local = legacy - 540 |
| M10 | M5-559~588 | M10-001~030 | canonical local = legacy - 558 |
| M11 | M5-589~598 | M11-001~010 | canonical local = legacy - 588 |
| M12 | M5-599~619 | M12-001~021 | canonical local = legacy - 598 |
| M13 | M5-620~646 | M13-001~027 | canonical local = legacy - 619 |
| M14 | M5-647~666 | M14-001~020 | canonical local = legacy - 646 |
| M15 | M5-667~676 | M15-001~010 | canonical local = legacy - 666 |
| M16 | M5-677~688 | M16-001~012 | canonical local = legacy - 676 |

## Boundary examples

- Legacy `M5-481` -> canonical `M5-001`.
- Legacy `M5-502` -> canonical `M5-022`.
- Legacy `M5-503` -> canonical `M6-001`.
- Legacy `M5-508` -> canonical `M6-006`.
- Legacy `M5-559` -> canonical `M10-001`.
- Legacy `M5-588` -> canonical `M10-030`.
- Legacy `M5-599` -> canonical `M12-001`.
- Legacy `M5-619` -> canonical `M12-021`.
- Legacy `M5-620` -> canonical `M13-001`.
- Legacy `M5-646` -> canonical `M13-027`.
- Legacy `M5-647` -> canonical `M14-001`.
- Legacy `M5-666` -> canonical `M14-020`.
- Legacy `M5-667` -> canonical `M15-001`.
- Legacy `M5-676` -> canonical `M15-010`.
- Legacy `M5-677` -> canonical `M16-001`.
- Legacy `M5-685` -> canonical `M16-009`.
- Legacy `M5-686` -> canonical `M16-010`.
- Legacy `M5-687` -> canonical `M16-011`.
- Legacy `M5-688` -> canonical `M16-012`.

## Reference rule

New documents use the canonical identifier in title and body. When referring to a legacy calculation for the first time in a document, use for example:

`M16-009 (Legacy M5-685)`.

After that, canonical ID alone is sufficient.

## Scope firewall

This map deliberately does **not** renumber legacy `M5-001~480`; that range requires its own topic-level inventory before any canonical reassignment.
