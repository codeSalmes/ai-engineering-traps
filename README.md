# AI Engineering Traps: Testing LLMs on Real-World Hardware Design

## 📌 Overview
Frontier AI models (like Claude Opus, Qwen, and Kimi) are incredibly good at writing code and answering textbook questions. However, when tasked with real-world hardware engineering, they often fail. 

They suffer from the **"Nominal Value Trap"**. They assume ideal components, ignore datasheet derating, and fail to reverse-engineer undocumented protocols when a strict standard isn't provided. 

This repository contains a series of hardware design challenges built to separate "textbook AI" from "real engineers".

## 🧠 The Methodology
Every task in this repository is designed with a specific **trap**:
1.  **The Prompt:** A realistic engineering request with no formulas or hand-holding. The AI must figure out the math itself.
2.  **The Environment:** Realistic datasheets, oscilloscope captures, and component inventories.
3.  **The Trap:** A "naive" solution that looks correct on the surface but fails under worst-case conditions.
4.  **The Grader:** A strict Python-based verification suite that checks the math, the output format, and the engineering logic step-by-step.

---

## 🛠️ The Tasks

### [Task 1: SPI Reverse-Engineering](./task-1-spi-reverse-engineering/)
**The Challenge:** The AI is given raw SPI byte captures from a sensor. It must deduce the bit layout, byte order, scaling factors, and implement a CRC-8 check from scratch.
*   **The Trap:** The AI must parse the reference data to figure out the scaling, and identify that packet `202` has a corrupted CRC. 
*   **The Results:** **Claude Opus failed 6/6 times.** Qwen3.8 Max timed out on 30-minute limits multiple times trying to figure out the byte order. 
*   *(See the [evaluation results](./task-1-spi-reverse-engineering/results/spi_eval_results.png) for proof).*


---

## 🏆 Summary of Results
| Model | SPI Reverse-Eng |
| :--- | :--- |
| **Claude Opus** | **0/6 Passes** (Mean: 0.07) |
| **Qwen 3.8 Max** | **0/6 Passes** (Mean: 0.53) |
| **Kimi K3** | **0/2 Passes** (Mean: 0.10) |

## 🚀 How to Run the Traps
If you want to test these prompts on your own local models:
1. Copy the `PROMPT.md` into your AI interface.
2. Load the files from the `environment/` folder.
3. Check the AI's output against the `solutions/gold_engineer.py` script.
