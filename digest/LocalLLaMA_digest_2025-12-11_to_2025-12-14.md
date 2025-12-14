# r/LocalLLaMA Reading Digest

**Period:** 2025-12-11 to 2025-12-14
**Posts Summarized:** 16
**Total Posts Analyzed:** 16

---

## 1. [Someone from NVIDIA made a big mistake and uploaded the parent folder of their upcoming model on Hugging Face](https://reddit.com/r/LocalLLaMA/comments/1pkpxss/someone_from_nvidia_made_a_big_mistake_and/)

**Author:** u/Nunki08 | **Upvotes:** 1264 | **Comments:** 149 | **Date:** 2025-12-12

**Summary:** An NVIDIA employee accidentally uploaded the parent folder of their upcoming model on Hugging Face, sparking interest and urgency among users to save the files before potential removal.

**Key Points:**
- Accidental upload of NVIDIA's upcoming model files on Hugging Face
- Urgency among users to save the files before they are taken down
- Mentions of specific models like Nano and 30B-A3B
- Positive sentiment towards the Nemotron lineup
- Concerns about potential censoring of the uploaded content

**Discussion Highlights:** The discussion highlights a sense of urgency to preserve the accidentally uploaded files, with users expressing interest in specific models and concerns about potential censorship. There is also appreciation for the Nemotron lineup and the potential of these projects.

---

## 2. [Training an LLM only on 1800s London texts - 90GB dataset](https://reddit.com/r/LocalLLaMA/comments/1pkpsee/training_an_llm_only_on_1800s_london_texts_90gb/)

**Author:** u/Remarkable-Trick-177 | **Upvotes:** 655 | **Comments:** 70 | **Date:** 2025-12-12

**Summary:** The post discusses an open-source project called TimeCapsuleLLM, which involves training LLMs using a 90GB dataset of 1800-1875 London texts. The author has conducted bias analysis and trained a small evaluation model to assess the dataset before scaling up.

**Key Points:**
- The project, TimeCapsuleLLM, focuses on training LLMs using texts from 1800-1875 London.
- The dataset is 90GB with 135,000 documents, sourced from the Internet Archive.
- A bias report covering temporal, gender/pronoun, and geographic bias has been generated and is available on GitHub.
- A small evaluation model (300M parameters) was trained on a 15GB subset to evaluate the dataset.
- The community appreciates the detailed work and suggests considering Mixture of Experts (MoE) for better compute efficiency.

**Discussion Highlights:** The community shows strong support for the project, with suggestions for improvement such as using MoE for better compute efficiency. There is also interest in the methodology and the potential for further exploration of historical text datasets.

---

## 3. [OpenAI's flagship model, ChatGPT-5.2 Thinking, ranks  most censored AI on Sansa benchmark.](https://reddit.com/r/LocalLLaMA/comments/1plnuqu/openais_flagship_model_chatgpt52_thinking_ranks/)

**Author:** u/Difficult-Cap-7527 | **Upvotes:** 575 | **Comments:** 104 | **Date:** 2025-12-13

**Summary:** The Reddit post discusses OpenAI's ChatGPT-5.2 model being ranked as the most censored AI on the Sansa benchmark, with users reporting issues in follow-up questions, research capabilities, and processing clinical notes for QA evaluation.

**Key Points:**
- ChatGPT-5.2 is ranked as the most censored AI on the Sansa benchmark.
- Users report the model performs poorly on follow-up questions and research tasks compared to previous versions.
- The model frequently denies processing made-up clinical notes for QA evaluation, which was not an issue with earlier models.
- Questions arise about the testing criteria used in the Sansa benchmark, especially given Grok's low ranking.
- Observations note that Gemini appears less censored than other models, including Mistral.

**Discussion Highlights:** The discussion highlights concerns about ChatGPT-5.2's performance degradation in specific tasks and questions about the benchmark's evaluation criteria. Users express frustration with increased censorship and reduced functionality in certain use cases.

---

## 4. [The new monster-server](https://reddit.com/r/LocalLLaMA/comments/1pl0ojb/the_new_monsterserver/)

**Author:** u/eribob | **Upvotes:** 569 | **Comments:** 116 | **Date:** 2025-12-12

**Summary:** The Reddit post details a user's upgraded 'monster-server' built for running local LLMs, featuring a Ryzen 3950x CPU, three GPUs (including an RTX 4090), and extensive storage. The user expresses satisfaction with the setup's performance and cost-effectiveness.

**Key Points:**
- The server uses a Ryzen 3950x CPU and three GPUs (2x RTX 3090, 1x RTX 4090) for running local LLMs.
- The setup includes 128GB RAM, 10GBe networking, and a mix of NVMe and HDD storage.
- The user runs GPT-OSS-120B fully in VRAM and uses the server for research and coding.
- Community feedback includes nostalgia for early 2000s overclocking and questions about the 3-GPU setup's efficiency.
- The post gained significant attention, with 569 upvotes and 116 comments.

**Discussion Highlights:** The community showed strong interest in the server's specifications and performance, with some users reminiscing about early overclocking days. Technical discussions included questions about the efficiency of a 3-GPU setup and the heat management in the cramped case. The post was well-received, earning a special flair and being featured on Discord.

---

## 5. [8x RTX Pro 6000 server complete](https://reddit.com/r/LocalLLaMA/comments/1plwgun/8x_rtx_pro_6000_server_complete/)

**Author:** u/koushd | **Upvotes:** 568 | **Comments:** 256 | **Date:** 2025-12-13

**Summary:** The author details their journey upgrading a GPU server, culminating in an 8x RTX Pro 6000 setup with 768 GB VRAM, a Threadripper PRO 9955WX, and 384 GB RAM. They faced challenges with heat, power, and hardware compatibility, ultimately achieving a high-performance system for training vision models and local LLMs.

**Key Points:**
- The server features 8x RTX Pro 6000 GPUs (4 Workstation, 4 Max-Q), providing 768 GB VRAM.
- The build includes a Threadripper PRO 9955WX CPU and 384 GB RAM.
- The author faced issues with heat, power consumption, and hardware compatibility during upgrades.
- The discussion highlights concerns about the build's physical setup and power management.
- The community appreciates the build's scale but questions its practicality and safety.

**Discussion Highlights:** The discussion includes praise for the build's scale and power, but also criticism regarding its physical setup, power management, and the use of a 'shitty aluminum frame.' Some users share concerns about power supply reliability and the practicality of such a high-end setup.

---

## 6. [New in llama.cpp: Live Model Switching](https://reddit.com/r/LocalLLaMA/comments/1pk0ubn/new_in_llamacpp_live_model_switching/)

**Author:** u/paf1138 | **Upvotes:** 456 | **Comments:** 83 | **Date:** 2025-12-11

**Summary:** The Reddit post announces a new feature in llama.cpp called Live Model Switching, which has gained significant attention and positive feedback from the community.

**Key Points:**
- Live Model Switching is a new feature in llama.cpp
- The post has gained popularity with 456 upvotes and 83 comments
- Community appreciates the UX improvements and progress
- Users express preference for llama.cpp over alternatives like ollama

**Discussion Highlights:** The community is enthusiastic about the new feature, with comments highlighting its popularity, UX improvements, and user preference for llama.cpp over other tools.

---

## 7. [Mistral’s Vibe CLI now supports a 200K token context window (previously 100K)](https://reddit.com/r/LocalLLaMA/comments/1pjw7rj/mistrals_vibe_cli_now_supports_a_200k_token/)

**Author:** u/Dear-Success-1441 | **Upvotes:** 434 | **Comments:** 36 | **Date:** 2025-12-11

**Summary:** Mistral’s Vibe CLI has doubled its context window from 100K to 200K tokens, a change achieved with a simple configuration update. The community discusses its practical utility and implications.

**Key Points:**
- Context window increased from 100K to 200K tokens
- Change implemented via a single line config update
- Community notes potential vs. practical utility of large context windows
- Some models struggle with context beyond 100K tokens
- Feature appreciated for summarizing long sessions

**Discussion Highlights:** The community acknowledges the technical achievement but debates its real-world usefulness, with some pointing out that many models struggle with context beyond 100K tokens. The simplicity of the implementation was also highlighted.

---

## 8. [What is the smartest uncensored nsfw LLM you can run with 12GB VRAM and 32GB RAM?](https://reddit.com/r/LocalLLaMA/comments/1pkidf6/what_is_the_smartest_uncensored_nsfw_llm_you_can/)

**Author:** u/Dex921 | **Upvotes:** 400 | **Comments:** 146 | **Date:** 2025-12-11

**Summary:** The post asks for recommendations on uncensored NSFW LLMs that can run with 12GB VRAM and 32GB RAM, including both local and closed-source options. Users discuss various models and their experiences.

**Key Points:**
- The post seeks uncensored NSFW LLMs compatible with 12GB VRAM and 32GB RAM.
- Users mention models like TheDrummer_Cydonia-24B and Qwen3 32B.
- Specific prompts and settings are discussed for better NSFW roleplay results.
- The discussion highlights the importance of the right prompt for effective NSFW interactions.

**Discussion Highlights:** The discussion focuses on specific model recommendations and the importance of proper prompting for NSFW interactions. TheDrummer_Cydonia-24B and Qwen3 32B are mentioned as viable options, with users sharing their experiences and settings for optimal performance.

---

## 9. [Qwen3 Next generation optimization](https://reddit.com/r/LocalLLaMA/comments/1plng6f/qwen3_next_generation_optimization/)

**Author:** u/ilintar | **Upvotes:** 343 | **Comments:** 39 | **Date:** 2025-12-13

**Summary:** The post discusses optimizations made to Qwen3, resulting in a 40% generation speed upgrade. The author implemented an optimized autoregressive delta net computation and removed unnecessary operations.

**Key Points:**
- Optimized autoregressive delta net computation for faster performance
- Removed unnecessary reshapes and operations
- Reported 40% generation speed improvement
- Community appreciation and recognition for the contribution
- Questions about compatibility with ROCm/Vulkan

**Discussion Highlights:** The community showed strong appreciation for the optimization work, with comments highlighting the author's frequent contributions and expressing interest in further improvements. There was also a question about whether the speedup would apply to ROCm/Vulkan in addition to CUDA.

---

## 10. [Leaked footage from Meta's post-training strategy meeting.](https://reddit.com/r/LocalLLaMA/comments/1pjvtgn/leaked_footage_from_metas_posttraining_strategy/)

**Author:** u/YouCanMake1t | **Upvotes:** 306 | **Comments:** 80 | **Date:** 2025-12-11

**Summary:** The Reddit post discusses Meta's post-training strategy, with comments highlighting concerns about data usage, leadership, and comparisons to other AI models.

**Key Points:**
- Meta allegedly downloaded a large number of videos but did not use them for training.
- Questions about the expertise of Meta's AI leadership.
- Comparisons to other AI models like GLM and Deepseek.
- Discussion about copyright litigation and data sources.
- Meta's recent SOTA models like Dino v3 and SAM 3.

**Discussion Highlights:** The discussion focuses on Meta's data practices, leadership, and comparisons to other AI models, with some users defending Meta's recent achievements.

---

## 11. [Running an LLM on a 3DS](https://reddit.com/r/LocalLLaMA/comments/1pl4njj/running_an_llm_on_a_3ds/)

**Author:** u/vreab | **Upvotes:** 281 | **Comments:** 31 | **Date:** 2025-12-12

**Summary:** The post discusses the feasibility and performance of running an LLM on a Nintendo 3DS, drawing comparisons to similar projects on other platforms like the PS Vita and Wii. The community expresses admiration for the technical achievement and curiosity about potential performance improvements on newer hardware.

**Key Points:**
- Running an LLM on a 3DS is technically impressive and feasible
- Similar projects have been done on PS Vita and Wii
- Community is curious about performance improvements on newer 3DS models
- Discussion includes humor and admiration for the project
- Potential for AI integration in games is speculated

**Discussion Highlights:** The discussion highlights the technical achievement of running an LLM on a 3DS, with users expressing admiration and curiosity. There is humor and speculation about the potential for AI in gaming, as well as questions about performance improvements on newer hardware.

---

## 12. [NVIDIA gpt-oss-120b Eagle Throughput model](https://reddit.com/r/LocalLLaMA/comments/1plewrk/nvidia_gptoss120b_eagle_throughput_model/)

**Author:** u/Dear-Success-1441 | **Upvotes:** 234 | **Comments:** 51 | **Date:** 2025-12-13

**Summary:** The post discusses NVIDIA's GPT-OSS-120B-Eagle3-throughput model, an optimized speculative decoding module designed to improve throughput during text generation. It uses NVIDIA’s Eagle3 speculative decoding approach and is licensed for both commercial and non-commercial use.

**Key Points:**
- GPT-OSS-120B-Eagle3-throughput is an optimized speculative decoding module built on the OpenAI gpt-oss-120b base model.
- It uses NVIDIA’s Eagle3 speculative decoding approach to predict a single draft token efficiently.
- The model is licensed under the nvidia-open-model-license for commercial and non-commercial use.
- It is intended for applications like AI agents, chatbots, and retrieval-augmented generation (RAG) systems.
- The model is not supported in llama.cpp, as indicated by a stale feature request.

**Discussion Highlights:** The discussion includes a request for a derestricted version of the model, mentions of the model's potential for CPU inference, and a note about the lack of support in llama.cpp. There is also a humorous comment about waiting for a REAP EAGLE3 HERETIC MOE GGUF version.

---

## 13. [This is how open ai is advertising them selfs on reddit…. They are doomed](https://reddit.com/r/LocalLLaMA/comments/1plcrg8/this_is_how_open_ai_is_advertising_them_selfs_on/)

**Author:** u/ThinkExtension2328 | **Upvotes:** 233 | **Comments:** 77 | **Date:** 2025-12-12

**Summary:** The Reddit post criticizes OpenAI's advertising strategy, highlighting a shift from promoting advanced AI to using astrology ads, which is seen as a decline in their approach.

**Key Points:**
- OpenAI's advertising strategy is criticized for shifting from advanced AI to astrology ads.
- The post suggests that OpenAI's focus on normies rather than programmers is a misstep.
- Comments highlight the irony of OpenAI's shift from warning about open models to using astrology ads.
- There is a consensus that OpenAI's new advertising approach is less effective and potentially damaging to their reputation.

**Discussion Highlights:** The discussion highlights a consensus that OpenAI's shift in advertising strategy is seen as a decline in their approach, with many users criticizing the move towards astrology ads and suggesting it is less effective than targeting programmers.

---

## 14. [Agentic Local AI on CPU = Mistral Vibe + Granite-4-h-1b](https://reddit.com/r/LocalLLaMA/comments/1pkdkjo/agentic_local_ai_on_cpu_mistral_vibe_granite4h1b/)

**Author:** u/PotentialFunny7143 | **Upvotes:** 232 | **Comments:** 40 | **Date:** 2025-12-11

**Summary:** The post discusses the effectiveness of using Mistral Vibe and Granite-4-h-1b for agentic local AI on CPU, highlighting its capabilities and performance.

**Key Points:**
- Mistral Vibe and Granite-4-h-1b are effective for local AI on CPU.
- Performance metrics and hardware requirements are of interest to the community.
- Comparisons with other models like Cline and open code are discussed.
- RAM and CPU consumption details are sought after.
- Upper boundary capabilities are explored.

**Discussion Highlights:** The discussion focuses on performance comparisons, hardware requirements, and the capabilities of Mistral Vibe and Granite-4-h-1b for local AI on CPU.

---

## 15. [Olmo 3.1 32B Think &amp; Instruct: New Additions to the Olmo Model Family](https://reddit.com/r/LocalLLaMA/comments/1pky5u4/olmo_31_32b_think_instruct_new_additions_to_the/)

**Author:** u/Dear-Success-1441 | **Upvotes:** 177 | **Comments:** 22 | **Date:** 2025-12-12

**Summary:** Olmo 3.1 32B Think and Instruct are new 32-billion-parameter models in the Olmo family, optimized for deep reasoning and instruction following, respectively. The Think model excels in multi-step reasoning and code generation, while the Instruct model focuses on conversational fluency and tool-use capabilities.

**Key Points:**
- Olmo 3.1 32B Think is optimized for deep reasoning, math, logic, and code generation.
- Olmo 3.1 32B Instruct is optimized for instruction following, conversational fluency, and tool-use capabilities.
- Both models are fully open source and part of the Olmo family.
- The community appreciates the models' openness and continuous improvement.
- There is anticipation for future developments, such as Mixture of Experts (MOE) models.

**Discussion Highlights:** The community discussion highlights appreciation for the open-source nature of the Olmo models and their continuous improvement. There is also anticipation for future developments, such as Mixture of Experts (MOE) models.

---

## 16. [Mistral 3 Large is DeepSeek V3!?](https://reddit.com/r/LocalLLaMA/comments/1plpc6h/mistral_3_large_is_deepseek_v3/)

**Author:** u/seraschka | **Upvotes:** 162 | **Comments:** 33 | **Date:** 2025-12-13

**Summary:** The post discusses the architectural similarities between Mistral 3 Large and DeepSeek V3, noting that they share nearly identical sizes and architectures, with minor differences in expert configurations. The community highlights the open-source spirit and the adoption of DeepSeek V3's architecture by multiple models.

**Key Points:**
- Mistral 3 Large and DeepSeek V3.2 have almost identical sizes (671B vs 673B).
- Mistral 3 Large uses the same architecture as DeepSeek V3/V3.1 but with adjusted expert configurations.
- Mistral likely trained their model from scratch due to using their own tokenizer.
- The community notes that other models like Kimi K2 and Gigachat also use the DeepSeek V3 architecture.
- The adoption of DeepSeek V3's architecture is seen as a positive aspect of open-source collaboration.

**Discussion Highlights:** The discussion highlights the open-source spirit, with multiple models adopting the DeepSeek V3 architecture. Some users point out that Mistral's use of their own tokenizer suggests independent training, while others appreciate the innovation in multimodal capabilities.

---

