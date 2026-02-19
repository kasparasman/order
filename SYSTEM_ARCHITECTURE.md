# SYSTEM ARCHITECTURE: THE ORDER ENGINE

This document serves as the single source of truth for the **Anthropos Order** CrewAI implementation. It bridges the strategic "Anthropos Network" vision with the technical Multi-Agent execution.

## 1. STRATEGIC MISSION
The Order is an "Intelligence vs. Execution" engine designed to bypass algorithmic spam filters by separating high-level strategic "Recipes" from **AI-Native Execution**.

- **The Goal:** Turn viral marketing into an engineering problem.
- **The Moat:** Data Velocity and Volume.
- **The Core Mechanic:** "Open Loops" and "Laws of Short-Form Physics."
- **AI Context:** All content is designed for 100% AI-generated video (e.g., via Kling/Veo). No biological filming or cameras are used by the Ambassadors.

## 2. THE 10-PHASE PIPELINE (Logic Flow)
The engine executes a sequential 10-phase pipeline to transform raw product data into an AI-native script skeleton.

1.  **Phase 1: Product Scrape** — Extracts key facts and "mandatory anchors" from Amazon/URL.
2.  **Phase 2: Visual Signal Extraction** — Analyzes product images for "Gold" details.
3.  **Phase 3: Intelligence Install** — Translates expert input into "One-Size Bites" of value.
4.  **Phase 4: Value Finalization** — Polishes strategic value for clinical, authoritative status.
5.  **Phase 5: Physics Guardrails** — Enforces non-negotiable conversion laws (3s Rule, 5s Beat).
6.  **Phase 6: Visual DNA** — Injects aesthetic directives (Digital Brutalism, Clinical High-Perf).
7.  **Phase 7: Execution Arc** — Synthesizes all intelligence into an 80% script skeleton.
8.  **Phase 8: Persona Modulation** — Dynamically refines tone (e.g., Venora) without altering structure.
9.  **Phase 9: Physics Audit** — Final check for "Text Clog" and engagement gaps.
10. **Phase 10: Final Assembly** — Assembles the finalized **5-Section** "Field Manual" in Markdown.

## 3. THE AGENT STACK
Defined in [agents.yaml](file:///c:/Users/Kasparas/The%20order/anthropos_order/src/anthropos_order/config/agents.yaml) and [crew.py](file:///c:/Users/Kasparas/The%20order/anthropos_order/src/anthropos_order/crew.py).

| Agent | Role | Focus |
| :--- | :--- | :--- |
| **Manager** | Manual Curator | Assembly & Tone Integrity |
| **Product Agent** | Source Truth Lead | Fact Extraction & Image Analysis |
| **Value Agent** | Insights Specialist | Strategy-to-Talking-Point Translation (Persona-aware) |
| **Physics Agent** | Conversion Coach | Guardrail Enforcement & Audit (Human Language) |
| **Marketing Agent** | Psychological Strategist | Synthesis & Roadmap (Persona-aware) |
| **Visual DNA Agent** | Vibe Architect | Aesthetic & Haptic Cues |
| **Persona Agent** | Tone Specialist | Dynamic Tone Modulation (Venora/Custom) |

## 4. LAWS OF PHYSICS (Non-Negotiable)
As detailed in [NewLogic.md](file:///c:/Users/Kasparas/The%20order/src/logic/NewLogic.md):
- **Law of Pattern Interrupt (0-2s):** First frame must look like action in progress.
- **Law of Information Density:** 130-150 Words Per Minute; re-hook every 2s.
- **Law of Retention Curve:** No value at the start; reveal "Truth" at the end.
- **Law of Native Integration:** Content must stay within the "Safe Zone" central 60%.

## 5. OUTPUT PROTOCOL (The 5 Sections)
1. **SECTION 1 — Core Lever**: Problem/Mechanism/Win.
2. **SECTION 2 — Execution Map**: Psychological roadmap (Hook, Body, Close).
3. **SECTION 3 — Persona**: Active persona name and vibe description.
4. **SECTION 4 — Execution Laws**: Zero-friction posting rules.
5. **SECTION 5 — Creative Freedom**: Boundary declaration.

## 5. TECHNICAL IMPLEMENTATION
- **Framework:** [crewAI](https://crewai.com)
- **Primary Logic:** [crew.py](file:///c:/Users/Kasparas/The%20order/anthropos_order/src/anthropos_order/crew.py)
- **Task Definitions:** [tasks.yaml](file:///c:/Users/Kasparas/The%20order/anthropos_order/src/anthropos_order/config/tasks.yaml)
- **Entry Point:** [main.py](file:///c:/Users/Kasparas/The%20order/anthropos_order/src/anthropos_order/main.py)

---
> *"Solo is addition. The Network is multiplication."*
