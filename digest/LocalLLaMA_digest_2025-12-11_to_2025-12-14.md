# r/LocalLLaMA Reading Digest

**Period:** 2025-12-11 to 2025-12-14
**Posts Summarized:** 10
**Total Posts Analyzed:** 16

---

## 1. [Someone from NVIDIA made a big mistake and uploaded the parent folder of their upcoming model on Hugging Face](https://reddit.com/r/LocalLLaMA/comments/1pkpxss/someone_from_nvidia_made_a_big_mistake_and/)

**Author:** u/Nunki08 | **Upvotes:** 1278 | **Comments:** 149 | **Date:** 2025-12-12

**Summary:** A NVIDIA employee accidentally uploaded the parent folder of an upcoming model on Hugging Face, sparking discussions about the potential leak of sensitive information and the urgency to save the data before it gets taken down.

**Key Points:**
- NVIDIA employee uploaded the parent folder of an upcoming model on Hugging Face
- The post gained significant attention with 1278 upvotes and 149 comments
- Users expressed concern about the data being taken down and urged others to save it
- The Nemotron lineup was mentioned as promising
- There was a sense of urgency to grab the data before full censoring

**Discussion Highlights:** The discussion highlighted the community's interest in the leaked data, with many users emphasizing the need to save the information before it gets removed. There was also appreciation for the Nemotron lineup and the potential of the projects mentioned.

---

## 2. [Training an LLM only on 1800s London texts - 90GB dataset](https://reddit.com/r/LocalLLaMA/comments/1pkpsee/training_an_llm_only_on_1800s_london_texts_90gb/)

**Author:** u/Remarkable-Trick-177 | **Upvotes:** 660 | **Comments:** 71 | **Date:** 2025-12-12

**Summary:** The post discusses the TimeCapsuleLLM project, which involves training an LLM on a 90GB dataset of 1800s London texts. The author has conducted a bias report and trained a small evaluation model to assess the dataset before scaling up.

**Key Points:**
- Project name: TimeCapsuleLLM
- Dataset size: 90GB with 135,000 documents
- Bias report covering temporal, gender/pronoun, and geographic bias
- Evaluation model trained on a 15GB subset
- Community appreciation and technical suggestions in comments

**Discussion Highlights:** The community shows strong support for the project, with comments highlighting its uniqueness and offering technical advice, such as considering Mixture of Experts (MoE) models for better compute efficiency.

---

## 3. [8x RTX Pro 6000 server complete](https://reddit.com/r/LocalLLaMA/comments/1plwgun/8x_rtx_pro_6000_server_complete/)

**Author:** u/koushd | **Upvotes:** 597 | **Comments:** 262 | **Date:** 2025-12-13

**Summary:** The user detailed their multi-year journey upgrading a GPU server, culminating in a system with 8x RTX Pro 6000 GPUs (768 GB VRAM), a Threadripper PRO 9955WX CPU, and 384 GB RAM. They faced challenges with heat management, power consumption, and hardware compatibility, ultimately resolving issues with a larger case and server-grade motherboard. Key points include the final configuration, challenges like overheating and power distribution, and community reactions ranging from admiration to criticism of the setup's practicality. The discussion highlighted the juxtaposition of high-end hardware with a basic setup and focused on power supply risks and cooling solutions.

---

## 4. [OpenAI's flagship model, ChatGPT-5.2 Thinking, ranks  most censored AI on Sansa benchmark.](https://reddit.com/r/LocalLLaMA/comments/1plnuqu/openais_flagship_model_chatgpt52_thinking_ranks/)

**Author:** u/Difficult-Cap-7527 | **Upvotes:** 593 | **Comments:** 105 | **Date:** 2025-12-13

**Summary:** The Reddit post discusses OpenAI's ChatGPT-5.2 model, highlighting its high censorship levels on the Sansa benchmark and perceived performance issues compared to previous versions.

**Key Points:**
- ChatGPT-5.2 is ranked as the most censored AI on the Sansa benchmark.
- Users report that the model performs poorly on follow-up questions and research tasks compared to version 5.1.
- The model frequently denies requests for evaluating QA models, which was not an issue with previous versions.
- There is curiosity about the testing criteria used in the benchmark, especially given Grok's low ranking.
- Gemini is noted to be less censored than other open models, including Mistral.

**Discussion Highlights:** The discussion highlights user dissatisfaction with ChatGPT-5.2's performance and censorship levels. Users compare it unfavorably to previous versions and express curiosity about the benchmark's testing criteria. There is also a notable observation about Gemini's relatively lower censorship levels.

---

## 5. [The new monster-server](https://reddit.com/r/LocalLLaMA/comments/1pl0ojb/the_new_monsterserver/)

**Author:** u/eribob | **Upvotes:** 573 | **Comments:** 116 | **Date:** 2025-12-12

**Summary:** The user shares their upgraded 'Monster Server' setup, featuring a Ryzen 3950x CPU, 128GB RAM, and three GPUs (2x RTX 3090 and 1x RTX 4090). The server runs local LLMs like GPT-OSS-120B and is used for research and coding. The post highlights the hardware configuration and performance details.

**Key Points:**
- Server setup includes Ryzen 3950x, 128GB RAM, and three GPUs (2x RTX 3090, 1x RTX 4090)
- Uses a 10GB fiber internet connection for $50/month
- Runs GPT-OSS-120B fully in VRAM with high performance
- Discussion includes feedback on GPU setup efficiency and heat management
- Users express envy and curiosity about the setup and performance

**Discussion Highlights:** The discussion includes positive feedback on the setup, with users expressing envy and curiosity. Some comments highlight potential issues with the 3-GPU setup being slower compared to 2 or 4 GPUs due to Tensor Parallel vs. Pipeline Parallel. Users also ask about heat management and the second PSU setup.

---

## 6. [New in llama.cpp: Live Model Switching](https://reddit.com/r/LocalLLaMA/comments/1pk0ubn/new_in_llamacpp_live_model_switching/)

**Author:** u/paf1138 | **Upvotes:** 459 | **Comments:** 83 | **Date:** 2025-12-11

**Summary:** The Reddit post announces a new feature in llama.cpp called 'Live Model Switching'. The community response highlights its popularity, mentions related tools like 'llamaswap', and expresses appreciation for recent UX improvements.

**Key Points:**
- Introduction of 'Live Model Switching' in llama.cpp
- Post gained significant attention with 459 upvotes
- Community mentions tools like 'llamaswap' and UX improvements
- User expresses intention to switch from 'ollama'

**Discussion Highlights:** The discussion reflects positive sentiment around the new feature and recent improvements in llama.cpp, with users showing enthusiasm for switching to this tool.

---

## 7. [Mistral’s Vibe CLI now supports a 200K token context window (previously 100K)](https://reddit.com/r/LocalLLaMA/comments/1pjw7rj/mistrals_vibe_cli_now_supports_a_200k_token/)

**Author:** u/Dear-Success-1441 | **Upvotes:** 438 | **Comments:** 36 | **Date:** 2025-12-11

**Summary:** Mistral’s Vibe CLI has doubled its context window support from 100K to 200K tokens, a change achieved with a simple configuration update. The community discussed the practical implications and challenges of large context windows.

**Key Points:**
- Context window increased from 100K to 200K tokens
- Change implemented via a single-line config update
- Community reactions highlight both enthusiasm and skepticism about practical utility
- Large context windows may struggle with usefulness beyond a certain threshold

**Discussion Highlights:** The discussion emphasized the simplicity of the change (a single config line) and debated the real-world utility of such large context windows, with some users noting that models often struggle with context beyond 100K tokens.

---

## 8. [What is the smartest uncensored nsfw LLM you can run with 12GB VRAM and 32GB RAM?](https://reddit.com/r/LocalLLaMA/comments/1pkidf6/what_is_the_smartest_uncensored_nsfw_llm_you_can/)

**Author:** u/Dex921 | **Upvotes:** 395 | **Comments:** 146 | **Date:** 2025-12-11

**Summary:** The post asks for recommendations on the smartest uncensored NSFW LLM that can run with 12GB VRAM and 32GB RAM, including both local and closed-source options. The discussion highlights a few models and their performance in NSFW contexts.

**Key Points:**
- The post seeks uncensored NSFW LLMs suitable for specific hardware constraints.
- TheDrummer_Cydonia-24B is mentioned as a truly uncensored local model.
- Qwen3 32B is noted for good NSFW roleplay results on similar hardware.
- The discussion includes both local and closed-source LLM options.

**Discussion Highlights:** The discussion focuses on models like TheDrummer_Cydonia-24B and Qwen3 32B, with users sharing their experiences and recommendations for NSFW use cases. There is a consensus that these models perform well in uncensored contexts.

---

## 9. [Qwen3 Next generation optimization](https://reddit.com/r/LocalLLaMA/comments/1plng6f/qwen3_next_generation_optimization/)

**Author:** u/ilintar | **Upvotes:** 356 | **Comments:** 39 | **Date:** 2025-12-13

**Summary:** The post discusses optimizations for Qwen3 Next generation, highlighting a 40% generation speed upgrade achieved through optimized autoregressive delta net computation. The community has responded positively, appreciating the contribution.

**Key Points:**
- Optimized autoregressive delta net computation for Qwen3 Next generation
- 40% generation speed upgrade reported
- Community appreciation and engagement
- Questions about compatibility with ROCm/Vulkan
- Author's continuous contributions recognized

**Discussion Highlights:** The community has shown strong appreciation for the optimization work, with questions about compatibility with other platforms like ROCm/Vulkan. The author's continuous contributions are recognized and celebrated.

---

## 10. [NVIDIA gpt-oss-120b Eagle Throughput model](https://reddit.com/r/LocalLLaMA/comments/1plewrk/nvidia_gptoss120b_eagle_throughput_model/)

**Author:** u/Dear-Success-1441 | **Upvotes:** 236 | **Comments:** 53 | **Date:** 2025-12-13

**Summary:** The post discusses NVIDIA's GPT-OSS-120B-Eagle3-throughput model, an optimized speculative decoding module designed to improve throughput during text generation using Eagle3 speculative decoding. It is licensed for both commercial and non-commercial use.

**Key Points:**
- Optimized speculative decoding module for improved throughput
- Uses NVIDIA’s Eagle3 speculative decoding approach
- Licensed under nvidia-open-model-license for commercial and non-commercial use
- Intended for AI agents, chatbots, RAG systems, and instruction-following tasks
- Not supported in llama.cpp, limiting its usability in some contexts

**Discussion Highlights:** The discussion highlights interest in making the model derestricted and its potential benefits for CPU inference. There is also mention of its lack of support in llama.cpp, which limits its usability in certain environments.

---

