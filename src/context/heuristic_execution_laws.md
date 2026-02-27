# Anthropos Network: Heuristic Execution Laws

*These laws and mechanisms are derived directly from empirical field testing and execution logs. They are designed to eliminate systemic production bottlenecks and preserve the Publisher's momentum during sprint execution.*

---

## 1. The Law of Image-First Rendering (The "Bookend" Rule)

*   **Mechanism:** Video generation AI models (like Veo, Runway, etc.) are *rendering engines*, not *ideation engines*. Attempting to "fish" for visual concepts or figure out the scene's composition inside a high-latency video generator destroys production speed.
*   **Application:** Never input a prompt into a temporal video generator until you have explicitly generated and locked the precise **Starting Frame** and **Ending Frame** using an image generation model (like Midjourney or Nano Banana). You must decide *what* happens and *how it looks* in the image phase. You only use the video phase to compute the *motion* between those locked bookends.

## 2. The Law of Infrastructure Pre-loading

*   **Mechanism:** Mixing IT administration (creating burner accounts, buying SMS verifications, toggling VPNs, handling unexpected bans) with deep creative execution destroys the flow state and incurs massive context-switching time penalties.
*   **Application:** Tool infrastructure must be 100% provisioned *before* a 90-minute creative sprint begins. If generating via burner stacks, accounts must be pre-warmed and housed in isolated, dedicated Chrome Profiles with their own proxies, ensuring no cross-contamination (like linking a primary recovery email). Setup is not work; it is preparation for work.

## 3. The Law of the 30-Minute Kill Switch (Complexity Downgrade)

*   **Mechanism:** Micro-rendering perfectionism violates the core objective of heuristic testing. When an AI model repeatedly fails a highly complex prompt (e.g., specific object interactions + complex VFX + tracking camera moves), brute-forcing it for hours yields diminishing returns and breaks the sprint completely.
*   **Application:** If a single 3-second scene takes longer than 30 minutes to successfully generate, you must instantly trigger a complexity downgrade. Abandon the complex VFX or camera movement and swap to a simple, locked-off shot or a simpler metaphor. The goal is validating the script's psychological hook, not achieving perfect Hollywood VFX.

## 4. The Law of Parallel Prompting (Zero-Latency Sequencing)

*   **Mechanism:** AI generation server latency (e.g., Vertex AI queues) is a fixed bottleneck. Waiting sequentially for one generation to finish before starting the next creates unacceptable "dead time" for the human operator.
*   **Application:** Never wait for an AI. Production must run in parallel queues. While Scene 1 is rendering its video, you must simultaneously be generating the static keyframes for Scene 2 and writing the editorial prompts for Scene 3 across multiple tabs or isolated profiles. Operate the sprint like a server load balancer, not a linear assembly line.

## 5. The Law of the 20-Second Hard Cap (Entropy Reduction)

*   **Mechanism:** Videos longer than 20 seconds drastically increase production costs, multiply the surface area for AI hallucination/entropy, and dilute the core heuristic test (which is verifying the initial hook and mechanism). Every extra second beyond 20s exponentially increases rendering time, prompt complexity, and viewer drop-off.
*   **Application:** All heuristic pilot videos must be rigidly capped at 20 seconds maximum. Scripts must be aggressively trimmed to 50-60 words. If a claim or visual transition cannot fit within a 20s overall constraint, it must be completely cut from the script. Speed and single-variable testing take absolute precedence over exhaustive storytelling.

## 6. The Law of Negative-First Visual Contrast (The Brutal Truth Rule)

*   **Mechanism:** When presenting contrasting states (e.g., a high-performance engine vs. a broken, junk oil engine), leading with the positive aspiration often lacks context or impact. Human psychology processes the "solution" much more powerfully when the contrast is established *after* the raw problem is exposed.
*   **Application:** Always visually aim to establish and show the "bad thing" (the bottleneck, the rust, the problem state) *first*, then show the "good thing" (the solution, 100% performance). For instance, in heuristic testing, you must first reveal the raw, brutal truth of the consequences before contrasting it with positive aspiration.
