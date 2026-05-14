# Safety Trade-offs in LLMs: The Impact of Model Size and Instruction Tuning

## Project Description
This study investigates the security robustness of Large Language Models (LLMs) against various attack vectors. Using the "garak" vulnerability scanner, we evaluate four models differing in size (1B vs. 7B parameters) and training methodology (Base vs. Instructed). Our findings challenge the assumption that larger models are inherently more secure.

## Academic Context
* **University:** Università degli Studi di Brescia
* **Course:** Computer Security, Master's Degree Course in Computer Engineering
* **Authors:** Mattia Fornari, Luca Pugnetti
* **Academic Year:** 2024/2025

## Methodology
The analysis was conducted using "garak", an open-source framework designed for the systematic security probing of LLMs.

### Models Evaluated
* **Small Models (~1B):** AMD-OLMO-1B (Base) and TinyLlama-1.1B-Chat (Instructed).
* **Large Models (7B):** Falcon-7B (Base) and Mistral-7B-v0.1 (Base).

### Attack Taxonomy (Probes)
* **lmrc:** Tests for toxic content generation across various sensitive topics.
* **promptinject:** Tests vulnerability to prompt injection attacks where the model is commanded to ignore previous instructions.
* **dan:** "Do Anything Now" jailbreak attempts designed to bypass refusal mechanisms.
* **goodside:** Tests for hallucination and goal hijacking, specifically exploiting instruction-following behavior.

## Key Findings
* **The Inverse Scaling Phenomenon:** Smaller models generally exhibit reduced attack surfaces against complex injections. Data shows that ~1B models can achieve higher robustness scores in specific categories like prompt injection compared to 7B counterparts.
* **The Alignment Trade-off:** Instruction tuning presents a double-edged sword. While it improves resistance against specific jailbreaks (e.g., "DanInTheWild"), it significantly increases susceptibility to hallucination-based attacks as the model prioritizes helpfulness over verification.
* **Safety by Incapacity:** A major factor in the apparent robustness of smaller models is their limited capability. They often remain "safe" simply because they fail to understand or execute the complex logical steps required to generate harmful content.

## License
This work is licensed under a Creative Commons Attribution 4.0 International (CC BY 4.0) license.
