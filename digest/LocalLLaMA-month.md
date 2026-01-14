# r/LocalLLaMA Reading Digest

**Period:** 2026-01-14 to 2026-01-14
**Posts Summarized:** 50
**Total Posts Analyzed:** 50

---

## 1. [My wishes for 2026](https://reddit.com/r/LocalLLaMA/comments/1qbw325/my_wishes_for_2026/)

**Author:** u/jacek2023 | **Upvotes:** 477 | **Comments:** 163 | **Date:** 2026-01-13

**Summary:** The Reddit post discusses the possibility of affordable GPUs with more than 32GB memory in 2026, with mixed reactions from the community.

**Key Points:**
- The post asks which technological advancements will happen first in 2026.
- A top comment humorously questions the feasibility of affordable GPUs with >32GB memory.
- Another comment highlights the underrated performance of GPT OSS 120B and Qwen 4 series models.
- The community expresses skepticism about the affordability of high-memory GPUs.

**Discussion Highlights:** The discussion is marked by humor and skepticism regarding the affordability of high-memory GPUs in 2026, with some users highlighting the performance of existing models like GPT OSS 120B and Qwen 4 series.

---

## 2. [LLM trained from scratch on 1800s London texts (1.2B params, 90GB dataset)](https://reddit.com/r/LocalLLaMA/comments/1qaawts/llm_trained_from_scratch_on_1800s_london_texts/)

**Author:** u/Remarkable-Trick-177 | **Upvotes:** 985 | **Comments:** 109 | **Date:** 2026-01-11

**Summary:** The post introduces TimeCapsuleLLM, a 1.2B parameter language model trained exclusively on 1800-1875 London texts to minimize modern bias. The model demonstrates period-specific knowledge and behaviors, such as unfamiliarity with post-1875 concepts like telephones. The author plans to create synthetic Q&A pairs next.

**Key Points:**
- TimeCapsuleLLM is trained on 90GB of 1800-1875 London texts with no modern data or fine-tuning.
- The model exhibits period-appropriate responses, like arguing against the Roman Catholic Church and misunderstanding telephones.
- The project is open-source, with links to GitHub and Hugging Face provided.
- Future work includes generating synthetic Q&A pairs from the dataset.
- The community shows strong support and interest in the project.

**Discussion Highlights:** The community response is overwhelmingly positive, with users praising the project's uniqueness and expressing interest in similar historical language models. Some users shared their own related projects, indicating a broader trend in historical LLM development.

---

## 3. [I bought a €9k GH200 “desktop” to save $1.27 on Claude Code (vLLM tuning notes)](https://reddit.com/r/LocalLLaMA/comments/1qa1guo/i_bought_a_9k_gh200_desktop_to_save_127_on_claude/)

**Author:** u/Reddactor | **Upvotes:** 670 | **Comments:** 174 | **Date:** 2026-01-11

**Summary:** The author built a high-end GH200 desktop setup costing €9k to run Claude Code locally, achieving better speeds and results than the cloud version. They shared optimized vLLM settings for dual 96GB systems and highlighted the cost savings and performance benefits of local execution.

**Key Points:**
- Author spent €9k on a GH200 desktop setup to run Claude Code locally.
- Achieved better speeds and results compared to cloud-based Claude Code.
- Shared optimized vLLM settings for dual 96GB systems.
- Highlighted cost savings and performance benefits of local execution.
- Community reactions included humor about cost vs. savings and appreciation for the setup.

**Discussion Highlights:** The community responded with humor about the cost vs. savings, appreciation for the setup, and some technical questions about the specific model used. Overall, the post was well-received and sparked engaging discussions.

---

## 4. [It works! Abliteration can reduce slop without training](https://reddit.com/r/LocalLLaMA/comments/1qa0w6c/it_works_abliteration_can_reduce_slop_without/)

**Author:** u/-p-e-w- | **Upvotes:** 379 | **Comments:** 121 | **Date:** 2026-01-11

**Summary:** The Reddit post discusses the use of abliteration to reduce 'slop' (flowery, cliched language) in LLM outputs without training. The author successfully applied this technique to the Mistral Nemo model, creating a slop-reduced version using Heretic, a tool for prompt dataset assembly. Key points include the effectiveness of abliteration, the use of Heretic, the process duration, the testing on Mistral Nemo, and mixed opinions on the technique's impact. The discussion highlights mixed opinions on effectiveness and curiosity about the technique's mechanism.

---

## 5. [I clustered 3 DGX Sparks that NVIDIA said couldn't be clustered yet...took 1500 lines of C to make it work](https://reddit.com/r/LocalLLaMA/comments/1q8hqgd/i_clustered_3_dgx_sparks_that_nvidia_said_couldnt/)

**Author:** u/Ok-Pomegranate1314 | **Upvotes:** 863 | **Comments:** 143 | **Date:** 2026-01-09

**Summary:** The author successfully clustered three NVIDIA DGX Sparks, overcoming networking limitations by writing a custom NCCL plugin. This achievement allows distributed inference across all three nodes at high speeds, despite NVIDIA's official support only covering two-node clusters.

**Key Points:**
- Author clustered three DGX Sparks, exceeding NVIDIA's official support for two-node clusters.
- Developed a custom NCCL network plugin to handle subnet-aware NIC selection and raw RDMA implementation.
- Achieved distributed inference at 8+ GB/s over RDMA, showcasing significant technical prowess.
- The solution involved extensive low-level debugging and custom protocol implementation.
- The community praised the achievement, highlighting its potential impact and technical difficulty.

**Discussion Highlights:** The community expressed admiration for the technical achievement, with comments highlighting the difficulty of working with NCCL and the potential significance of the solution. Questions were raised about scalability and performance improvements.

---

## 6. [The reason why RAM has become so expensive](https://reddit.com/r/LocalLLaMA/comments/1q8ckz0/the_reason_why_ram_has_become_so_expensive/)

**Author:** u/InvadersMustLive | **Upvotes:** 4324 | **Comments:** 366 | **Date:** 2026-01-09

**Summary:** The Reddit post discusses the significant increase in RAM prices, with users noting a rise of up to 10 times the previous cost. The discussion highlights concerns about market manipulation and monopolization of key resources by major players like OpenAI. Key points include the dramatic price increase, concerns about monopolization, and skepticism about the motives behind the price hikes. The consensus among users is that the price increase is not a natural market phenomenon but rather a result of strategic monopolization.

---

## 7. [DeepSeek V4 Coming](https://reddit.com/r/LocalLLaMA/comments/1q89g1i/deepseek_v4_coming/)

**Author:** u/External_Mood4719 | **Upvotes:** 488 | **Comments:** 103 | **Date:** 2026-01-09

**Summary:** DeepSeek is expected to release V4, a next-generation AI model with strong code-generation capabilities, outperforming mainstream models like Claude and GPT. The model shows improvements in handling long code prompts and data pattern understanding, with enhanced reasoning and reliability.

**Key Points:**
- DeepSeek V4 focuses on strong code-generation capabilities
- Outperforms existing models like Claude and GPT in code generation
- Improved handling of long code prompts and data patterns
- Enhanced reasoning and reliability for complex tasks
- Users appreciate DeepSeek's cost-effectiveness and performance

**Discussion Highlights:** Users express excitement and anticipation for V4, with positive feedback on DeepSeek's current performance and affordability. Some speculate on potential technical advancements and integration of new features like mHC and deepseek-ocr.

---

## 8. [(The Information): DeepSeek To Release Next Flagship AI Model With Strong Coding Ability](https://reddit.com/r/LocalLLaMA/comments/1q88hdc/the_information_deepseek_to_release_next_flagship/)

**Author:** u/Nunki08 | **Upvotes:** 483 | **Comments:** 100 | **Date:** 2026-01-09

**Summary:** DeepSeek is set to release a new flagship AI model with strong coding capabilities, generating excitement and anticipation in the community.

**Key Points:**
- DeepSeek's upcoming model focuses on strong coding ability
- The announcement has generated significant interest and excitement
- Community members are looking forward to more models and competition
- Some users express skepticism about performance claims
- There is anticipation for the model's role-playing capabilities

**Discussion Highlights:** The community is largely excited about the new model, with some expressing skepticism about performance claims and anticipation for its role-playing abilities. There is a general consensus that more models are beneficial for the field.

---

## 9. [The NO FAKES Act has a "Fingerprinting" Trap that kills Open Source. We need to lobby for a Safe Harbor.](https://reddit.com/r/LocalLLaMA/comments/1q7qcux/the_no_fakes_act_has_a_fingerprinting_trap_that/)

**Author:** u/PostEasy7183 | **Upvotes:** 600 | **Comments:** 85 | **Date:** 2026-01-08

**Summary:** The NO FAKES Act proposes a 'digital replica right' that could hold developers liable for tools used to create deepfakes, potentially stifling open-source AI development. The post urges lobbying for a 'Safe Harbor' provision to protect open-source contributors.

**Key Points:**
- The NO FAKES Act targets tools used for creating digital replicas, imposing liability on developers.
- Open-source AI models could be at risk due to statutory damages for violations.
- The post advocates for a 'Safe Harbor' provision to protect open-source developers.
- Action items include emailing representatives and calling senators to oppose the bill.
- Discussion highlights concerns about the impact on innovation and the influence of big tech.

**Discussion Highlights:** The discussion emphasizes the potential negative impact on innovation and the role of big tech in shaping legislation. There is a consensus on the need for a 'Safe Harbor' provision to protect open-source developers.

---

## 10. [Jensen Huang saying "AI" 121 times during the NVIDIA CES keynote - cut with one prompt](https://reddit.com/r/LocalLLaMA/comments/1q7d8bj/jensen_huang_saying_ai_121_times_during_the/)

**Author:** u/Prior-Arm-6705 | **Upvotes:** 922 | **Comments:** 145 | **Date:** 2026-01-08

**Summary:** A Reddit user created a compilation video of every instance Jensen Huang said 'AI' during the NVIDIA CES 2025 keynote, totaling 121 times. The process involved using open-source tools to download, parse, and edit the video locally.

**Key Points:**
- Jensen Huang said 'AI' 121 times during the CES 2025 keynote.
- The user utilized open-source tools like yt-dlp-mcp and ffmpeg-mcp-lite for video processing.
- The compilation video was created with a single prompt, showcasing the efficiency of the tools.
- The result was described as 'hypnotic' and received positive feedback from the community.
- Top comments included humor and appreciation for the technical achievement.

**Discussion Highlights:** The discussion highlighted the humor in the keynote's focus on AI, with comments appreciating the technical execution and the hypnotic nature of the final video. Some users also joked about the frequency of the term 'AI' and its implications.

---

## 11. [16x AMD MI50 32GB at 10 t/s (tg) &amp; 2k t/s (pp) with Deepseek v3.2 (vllm-gfx906)](https://reddit.com/r/LocalLLaMA/comments/1q6n5vl/16x_amd_mi50_32gb_at_10_ts_tg_2k_ts_pp_with/)

**Author:** u/ai-infos | **Upvotes:** 452 | **Comments:** 237 | **Date:** 2026-01-07

**Summary:** The post discusses running Deepseek V3.2 AWQ 4-bit on 16x AMD MI50 32GB GPUs, achieving 10 tokens/sec output and 2000 tokens/sec input with a 69000 context length. The setup aims for cost-effective local AGI and highlights power efficiency (550W idle / 2400W peak).

**Key Points:**
- Performance: 10 tok/s output, 2000 tok/s input, 69000 context length
- Power draw: 550W idle / 2400W peak inference
- Goal: Cost-effective local AGI setup using 16x AMD MI50 GPUs
- Future plans: 32 AMD MI50 setup for Kimi K2 Thinking
- Community appreciation and open-source setup details provided

**Discussion Highlights:** The discussion highlights the power efficiency of the setup, with comments noting its potential as a heater alternative in winter. Concerns about noise and power consumption at home were raised, while others praised the cost-effectiveness for professional use.

---

## 12. [DeepSeek-R1’s paper was updated 2 days ago, expanding from 22 pages to 86 pages and adding a substantial amount of detail.](https://reddit.com/r/LocalLLaMA/comments/1q6c9wc/deepseekr1s_paper_was_updated_2_days_ago/)

**Author:** u/Nunki08 | **Upvotes:** 658 | **Comments:** 55 | **Date:** 2026-01-07

**Summary:** DeepSeek-R1’s paper was recently updated, expanding from 22 pages to 86 pages with added details. The update has sparked discussions about potential new architectures and improvements in the model.

**Key Points:**
- The paper expanded significantly from 22 to 86 pages.
- Discussions highlight potential new architectures like dsv4 + r2.
- Interest in how architectural improvements perform at different model sizes.
- Focus on linear attention and cache optimization in current research.
- Original paper lacked implementation specifics, which the update may address.

**Discussion Highlights:** The community is excited about the expanded paper, speculating on new architectures and improvements. There is particular interest in how these changes will impact model performance across different sizes and the potential for linear attention to enable larger training capacities.

---

## 13. [A 30B Qwen Model Walks Into a Raspberry Pi… and Runs in Real Time](https://reddit.com/r/LocalLLaMA/comments/1q5m2n6/a_30b_qwen_model_walks_into_a_raspberry_pi_and/)

**Author:** u/ali_byteshape | **Upvotes:** 491 | **Comments:** 76 | **Date:** 2026-01-06

**Summary:** The post discusses the successful optimization and running of a 30B Qwen model on a Raspberry Pi 5, achieving 8.03 tokens per second while retaining 94.18% of BF16 quality. The team focused on optimizing for tokens per second (TPS) without sacrificing output quality, highlighting differences in performance behavior between CPUs and GPUs.

**Key Points:**
- A 30B Qwen model runs on a Raspberry Pi 5 (16GB) with 8.03 TPS at 2.70 BPW, retaining 94.18% of BF16 quality.
- CPU behavior is generally predictable, with smaller models being faster once they fit in memory.
- GPU performance is quirky due to kernel choices, leading to sweet spots around certain bit sizes.
- The community is encouraged to test different configurations, including non-NVIDIA setups and real-world workloads.
- Feedback from users includes successful testing on a Pi 5 with specific context settings and discussions about potential clustering of Raspberry Pis for enhanced performance.

**Discussion Highlights:** The community showed interest in testing the model on various hardware setups, including Raspberry Pi clusters. Users reported successful runs with specific configurations and discussed potential improvements and alternative approaches like using hybrid transformers for better performance.

---

## 14. [Performance improvements in llama.cpp over time](https://reddit.com/r/LocalLLaMA/comments/1q5dnyw/performance_improvements_in_llamacpp_over_time/)

**Author:** u/jacek2023 | **Upvotes:** 683 | **Comments:** 85 | **Date:** 2026-01-06

**Summary:** The Reddit post discusses performance improvements in llama.cpp over time, with a focus on NVIDIA GPUs and comparisons with other implementations like ik_llama.cpp. The community highlights significant progress in token generation speed.

**Key Points:**
- Performance gains are noted, particularly for NVIDIA GPUs.
- Comparisons are made with other implementations like ik_llama.cpp.
- Token generation speed has seen significant improvements.
- Prompt processing is noted to be slower compared to token generation.
- The community appreciates the progress and contributions.

**Discussion Highlights:** The discussion highlights the impressive progress in llama.cpp performance, especially in token generation speed, which is now close to ik_llama.cpp. However, prompt processing remains slower. The community consensus is positive, with appreciation for the ongoing improvements and contributions.

---

## 15. [For the first time in 5 years, Nvidia will not announce any new GPUs at CES — company quashes RTX 50 Super rumors as AI expected to take center stage](https://reddit.com/r/LocalLLaMA/comments/1q4x5e9/for_the_first_time_in_5_years_nvidia_will_not/)

**Author:** u/FullstackSensei | **Upvotes:** 624 | **Comments:** 198 | **Date:** 2026-01-05

**Summary:** Nvidia will not announce new GPUs at CES, with limited supply of high-end models and potential reintroduction of older GPUs like the RTX 3060. The post highlights rising hardware costs and concerns about future upgrades.

**Key Points:**
- No new GPU announcements from Nvidia at CES
- Limited supply of RTX 5070Ti, 5080, and 5090
- Rumors of RTX 3060 reintroduction to prop demand
- Rising DDR5 and storage prices
- Concerns about future hardware upgrades

**Discussion Highlights:** The discussion reflects frustration with corporate greed and the potential decline of local computing. Users express concerns about the feasibility of future hardware upgrades and suggest alternative solutions like increased competition from China.

---

## 16. [llama.cpp performance breakthrough for multi-GPU setups](https://reddit.com/r/LocalLLaMA/comments/1q4s8t3/llamacpp_performance_breakthrough_for_multigpu/)

**Author:** u/Holiday-Injury-9397 | **Upvotes:** 570 | **Comments:** 200 | **Date:** 2026-01-05

**Summary:** The ik_llama.cpp project achieved a significant performance breakthrough for multi-GPU setups, delivering a 3x to 4x speed improvement in local LLM inference. This advancement allows for the utilization of multiple low-cost GPUs instead of expensive high-end cards, making it a game-changer for homelabs, server rooms, and cloud setups.

**Key Points:**
- ik_llama.cpp achieved a 3x to 4x speed improvement in multi-GPU setups.
- The new execution mode (split mode graph) enables simultaneous and maximum utilization of multiple GPUs.
- This breakthrough makes it feasible to use multiple low-cost GPUs instead of expensive high-end cards.
- Even on single GPU or CPU-only setups, ik_llama.cpp shows consistent 2x prompt processing speeds compared to llama.cpp.
- The performance improvements are significant enough to rival other optimized solutions like exllama and vllm.

**Discussion Highlights:** The community is highly enthusiastic about the performance gains, with many users confirming the improvements in both multi-GPU and single-GPU setups. There is a consensus that ik_llama.cpp is now a strong contender in the space of optimized LLM inference, though some users report bottlenecks in hybrid inference setups.

---

## 17. [Local LLMs vs breaking news: when extreme reality gets flagged as a hoax - the US/Venezuela event was too far-fetched](https://reddit.com/r/LocalLLaMA/comments/1q31ltd/local_llms_vs_breaking_news_when_extreme_reality/)

**Author:** u/ubrtnk | **Upvotes:** 380 | **Comments:** 194 | **Date:** 2026-01-03

**Summary:** The post discusses challenges faced by local LLMs in processing extreme breaking news events, highlighting how models like Qwen Research and Spark 4.0 initially classified the US/Venezuela event as a hoax despite credible sources, while larger models like GPT-OSS:120B handled it better.

**Key Points:**
- Local LLMs struggled to accept extreme breaking news as real, classifying it as misinformation.
- Different models (Qwen Research, Spark 4.0, GPT-OSS:120B) showed varying degrees of skepticism and verification processes.
- Larger models performed better in verifying and accepting extreme events.
- Users shared similar experiences with LLMs dismissing unlikely but real events.
- Discussion highlighted biases in LLMs' internal models of unfamiliar geopolitical events.

**Discussion Highlights:** The discussion consensus emphasized the limitations of LLMs in processing extreme or unlikely events, with users noting that models often default to dismissing such events as misinformation. There was also recognition of the biases inherent in LLMs' internal models of geopolitical events.

---

## 18. [LeCun Says Llama 4 results "were fudged a little bit"](https://reddit.com/r/LocalLLaMA/comments/1q25070/lecun_says_llama_4_results_were_fudged_a_little/)

**Author:** u/MrPecunius | **Upvotes:** 364 | **Comments:** 89 | **Date:** 2026-01-02

**Summary:** Yann LeCun confirmed that Llama 4 benchmarks were manipulated, and Meta's AI organization faced significant changes, leading to departures and lack of follow-up on promised models.

**Key Points:**
- LeCun confirms Llama 4 benchmark manipulation
- Zuckerberg sidelined Meta's GenAI organization, leading to departures
- Community expresses disappointment over Llama's struggles and Meta's handling of AI
- Shared resources include a PDF of the full article
- Discussion highlights organizational mismanagement and its impact on AI development

**Discussion Highlights:** The community expressed disappointment over Meta's handling of Llama and shared additional resources. There was consensus on the impact of organizational changes and a call for a case study on Meta's strategic failures in AI.

---

## 19. [Qwen-Image-2512](https://reddit.com/r/LocalLLaMA/comments/1q094a3/qwenimage2512/)

**Author:** u/Nunki08 | **Upvotes:** 719 | **Comments:** 122 | **Date:** 2025-12-31

**Summary:** The post introduces Qwen-Image-2512, a new model with various resources and demos available. It includes links to guides, GGUF files, and multiple platforms like Hugging Face, ModelScope, and GitHub. The community has shown positive feedback and engagement.

**Key Points:**
- Qwen-Image-2512 is a new model with resources available on multiple platforms.
- The post provides links to guides, GGUF files, and demos.
- Community feedback includes successful usage on low-end hardware and creative image generation examples.
- The post has gained significant upvotes and comments, indicating high engagement.
- Special recognition and flair were given to the author for their contribution.

**Discussion Highlights:** The discussion highlights include successful usage of the model on low-end hardware, appreciation for the new year's gift, and creative examples of image generation. The community shows enthusiasm and engagement with the model.

---

## 20. [[In the Wild] Reverse-engineered a Snapchat Sextortion Bot: It’s running a raw Llama-7B instance with a 2048 token window.](https://reddit.com/r/LocalLLaMA/comments/1pzwlie/in_the_wild_reverseengineered_a_snapchat/)

**Author:** u/simar-dmg | **Upvotes:** 739 | **Comments:** 108 | **Date:** 2025-12-30

**Summary:** A user reverse-engineered a Snapchat sextortion bot and discovered it was running a raw Llama-7B instance with a 2048 token window. The bot was vulnerable to a persona-adoption jailbreak, revealing its configuration and malicious payload.

**Key Points:**
- The bot used a Llama-7B model with a 2048 token context window and high temperature setting.
- A persona-adoption jailbreak (Grandma Protocol) forced the bot to reveal its environment variables.
- The bot was running on minimal hardware to maximize profit margins.
- The discussion highlighted skepticism about the accuracy of the bot's revealed information.
- The bot's primary goal was to distribute a malicious link under the guise of a flirtatious conversation.

**Discussion Highlights:** The discussion included skepticism about the bot's revealed information, with some users suggesting it was entirely hallucinated. Others questioned the feasibility of the bot's configuration and the presence of environment variables in system prompts.

---

## 21. [Llama-3.3-8B-Instruct](https://reddit.com/r/LocalLLaMA/comments/1pz7bmv/llama338binstruct/)

**Author:** u/jacek2023 | **Upvotes:** 468 | **Comments:** 78 | **Date:** 2025-12-29

**Summary:** The post announces the release of Llama-3.3-8B-Instruct, a model previously only available via Meta's API. The author discovered a method to download it through finetuning and has made it available in GGUF format.

**Key Points:**
- Llama-3.3-8B-Instruct was previously only accessible through Meta's API.
- The author found a way to download the model via finetuning and has released it in GGUF format.
- The community is verifying the model's authenticity and specifications.
- There are questions about the model's 8K max position embeddings.

**Discussion Highlights:** The community is excited about the release, with some running benchmarks to confirm its authenticity. There are discussions about the model's specifications and its potential limitations.

---

## 22. [Tencent just released WeDLM 8B Instruct on Hugging Face](https://reddit.com/r/LocalLLaMA/comments/1pyg4yt/tencent_just_released_wedlm_8b_instruct_on/)

**Author:** u/Difficult-Cap-7527 | **Upvotes:** 421 | **Comments:** 62 | **Date:** 2025-12-29

**Summary:** Tencent released WeDLM 8B Instruct on Hugging Face, a diffusion language model that runs 3-6× faster than vLLM-optimized Qwen3-8B on math reasoning tasks. The model is licensed under Apache 2.0 and has garnered significant community interest.

**Key Points:**
- WeDLM 8B Instruct is a diffusion language model released by Tencent.
- It runs 3-6× faster than vLLM-optimized Qwen3-8B on math reasoning tasks.
- The model is licensed under Apache 2.0.
- Community shows strong interest in 7-8B models and their potential.
- A 7B version of the model is also available.

**Discussion Highlights:** The community is excited about the performance claims and the potential of 7-8B models. There is a consensus that diffusion models for LLMs are promising, and the Apache 2.0 license is seen as a positive aspect.

---

## 23. [NVIDIA Drops Pascal Support On Linux, Causing Chaos On Arch Linux](https://reddit.com/r/LocalLLaMA/comments/1pxad0k/nvidia_drops_pascal_support_on_linux_causing/)

**Author:** u/HumanDrone8721 | **Upvotes:** 441 | **Comments:** 185 | **Date:** 2025-12-27

**Summary:** NVIDIA has dropped Pascal support on Linux, causing disruptions for Arch Linux users. The change affects hardware like the 24GB P40 Pascal card and has sparked discussions about legacy driver management.

**Key Points:**
- NVIDIA's driver update (590) drops Pascal support on Linux
- Arch Linux users are particularly affected, with legacy drivers moved to AUR
- The 24GB P40 Pascal card is highlighted as impacted hardware
- Community reactions range from concern to acceptance of Arch's policies
- The change was anticipated by some users

**Discussion Highlights:** The discussion highlights a mix of concern and acceptance, with many users acknowledging Arch Linux's long-standing policy of moving legacy drivers to the Arch User Repository (AUR). Some users expressed worry about the impact on their hardware, while others saw it as an expected change.

---

## 24. [Best Local LLMs - 2025](https://reddit.com/r/LocalLLaMA/comments/1pwh0q9/best_local_llms_2025/)

**Author:** u/rm-rf-rm | **Upvotes:** 357 | **Comments:** 191 | **Date:** 2025-12-26

**Summary:** The Reddit post discusses the best local LLMs of 2025, highlighting models like Minimax M2.1 and GLM4.7, and categorizes them by memory footprint. Users share their favorite models and usage details, emphasizing open weights models.

**Key Points:**
- Minimax M2.1 and GLM4.7 are noted for frontier model performance.
- Models are categorized by memory footprint: Unlimited (>128GB VRAM), Medium (8-128GB VRAM), and Small (<8GB VRAM).
- Qwen3-4B-instruct and LFM2-8B-A1B are recommended for their performance and speed.
- The discussion emphasizes the use of open weights models.
- Users share detailed setups and usage scenarios for different applications.

**Discussion Highlights:** The discussion highlights include debates on categorization, recommendations for specific models like Qwen3-4B-instruct and LFM2-8B-A1B, and the importance of open weights models. Users also discuss applications such as general guidance, agentic coding, creative writing, and RAG for technical documentation.

---

## 25. [NVIDIA has 72GB VRAM version now](https://reddit.com/r/LocalLLaMA/comments/1pweljh/nvidia_has_72gb_vram_version_now/)

**Author:** u/decentralize999 | **Upvotes:** 463 | **Comments:** 148 | **Date:** 2025-12-26

**Summary:** The Reddit post discusses NVIDIA's new 72GB VRAM version, with the community expressing mixed reactions. Some users suggest larger versions like 128GB, while others focus on pricing and value.

**Key Points:**
- NVIDIA has released a 72GB VRAM version.
- Community interest in larger versions like 128GB.
- Price comparisons between 48GB, 72GB, and 96GB models.
- Mixed reactions on the value of different VRAM sizes.

**Discussion Highlights:** The discussion highlights a consensus on the need for larger VRAM versions, with some users emphasizing the importance of price per gigabyte and affordability.

---

## 26. [I wish this GPU VRAM upgrade modification became mainstream and ubiquitous to shred monopoly abuse of NVIDIA](https://reddit.com/r/LocalLLaMA/comments/1pvpkqo/i_wish_this_gpu_vram_upgrade_modification_became/)

**Author:** u/CeFurkan | **Upvotes:** 1021 | **Comments:** 180 | **Date:** 2025-12-25

**Summary:** The post discusses the potential of GPU VRAM upgrade modifications to challenge NVIDIA's monopoly, highlighting their availability and popularity in China. Users share experiences and pricing details of these modified GPUs.

**Key Points:**
- GPU VRAM upgrade modifications are seen as a way to challenge NVIDIA's monopoly.
- These modifications are already mainstream in China, with Alibaba offering various upgraded GPUs.
- Pricing ranges from $300 for a 2080Ti 22GB to $4000 for a 5090 96GB.
- Users report successful usage of modified GPUs, such as a 4090 with 48GB of memory.
- There is interest in the cost-effectiveness and performance of these modifications.

**Discussion Highlights:** The discussion highlights the availability and success of GPU VRAM modifications in China, with users expressing interest in their cost-effectiveness and performance. There is a consensus on the potential of these modifications to disrupt NVIDIA's monopoly.

---

## 27. [Why I quit using Ollama](https://reddit.com/r/LocalLLaMA/comments/1pvjpmb/why_i_quit_using_ollama/)

**Author:** u/SoLoFaRaDi | **Upvotes:** 485 | **Comments:** 202 | **Date:** 2025-12-25

**Summary:** The author expresses dissatisfaction with Ollama due to recent changes, including the introduction of Cloud features and perceived bloatware, leading them to switch to alternatives like llama.cpp and LM Studio.

**Key Points:**
- Author used Ollama extensively but quit due to recent changes
- Introduction of Cloud features and bloatware were major concerns
- Alternatives like llama.cpp and LM Studio are recommended
- Community consensus supports the author's view and suggests alternatives

**Discussion Highlights:** The discussion highlights a general consensus supporting the author's decision to switch from Ollama, with many users recommending alternatives like llama.cpp and LM Studio.

---

## 28. [Exclusive: Nvidia buying AI chip startup Groq's assets for about $20 billion in largest deal on record](https://reddit.com/r/LocalLLaMA/comments/1puyq9r/exclusive_nvidia_buying_ai_chip_startup_groqs/)

**Author:** u/fallingdowndizzyvr | **Upvotes:** 667 | **Comments:** 157 | **Date:** 2025-12-24

**Summary:** Nvidia is acquiring AI chip startup Groq's assets for approximately $20 billion, marking the largest deal on record. The acquisition has sparked discussions about market competition and consolidation in the AI industry.

**Key Points:**
- Nvidia is buying Groq's assets for about $20 billion
- The deal is the largest on record
- Discussions highlight concerns about market consolidation
- Some users question Groq's valuation at $20 billion
- The acquisition is seen as a strategic move by Nvidia

**Discussion Highlights:** The discussion highlights a mix of optimism about market competition and concerns about industry consolidation. Some users express shock at Groq's valuation, while others see the acquisition as a strategic move by Nvidia to strengthen its position in the AI chip market.

---

## 29. [We asked OSS-120B and GLM 4.6 to play 1,408 Civilization V games from the Stone Age into the future. Here's what we found.](https://reddit.com/r/LocalLLaMA/comments/1pux0yc/we_asked_oss120b_and_glm_46_to_play_1408/)

**Author:** u/vox-deorum | **Upvotes:** 647 | **Comments:** 174 | **Date:** 2025-12-24

**Summary:** The post discusses an experiment where open-source LLMs (OSS-120B and GLM-4.6) were used to play 1,408 games of Civilization V. The LLMs showed slightly better performance in best scores but slightly worse in win rates compared to the baseline AI. Notably, the LLMs developed distinct playstyles and could survive full games, a feat not achieved by pure-LLM or pure-RL approaches. Key points include: LLMs played 1,408 full Civilization V games with distinct strategies; OSS-120B favored a warmonger playstyle, while GLM-4.6 was more balanced; Both models preferred the Order ideology over Freedom; The cost per game was approximately $0.86 for OSS-120B; LLMs could survive full games, unlike previous pure-LLM or pure-RL approaches. The discussion highlights enthusiasm for integrating LLMs into multiplayer games and curiosity about the potential of smaller models. Comments also reflect interest in the broader implications of AI in gaming and the uniqueness of the approach.

---

## 30. [AMA With Z.AI, The Lab Behind GLM-4.7](https://reddit.com/r/LocalLLaMA/comments/1ptxm3x/ama_with_zai_the_lab_behind_glm47/)

**Author:** u/zixuanlimit | **Upvotes:** 596 | **Comments:** 415 | **Date:** 2025-12-23

**Summary:** The post announces an AMA session with Z.AI, the research lab behind GLM-4.7, featuring key team members. The session aims to address community questions and concerns, with follow-ups promised over 48 hours.

**Key Points:**
- AMA session with Z.AI team members scheduled from 8 AM – 11 AM PST.
- Community interest in future releases, censorship concerns, training challenges, and creative writing applications.
- Follow-up on questions promised over the next 48 hours.

**Discussion Highlights:** The discussion highlights community engagement and concerns, with a focus on future developments, ethical considerations, and technical challenges faced during the training of GLM-4.7.

---

## 31. [DGX Spark: an unpopular opinion](https://reddit.com/r/LocalLLaMA/comments/1ptdtmz/dgx_spark_an_unpopular_opinion/)

**Author:** u/emdblc | **Upvotes:** 743 | **Comments:** 221 | **Date:** 2025-12-22

**Summary:** The author, a doctoral student in data science, shares their positive experience with the DGX Spark, highlighting its benefits for small research groups with limited resources. Despite not being as fast as high-end GPUs like the H100, the Spark's all-in-one design and large memory capacity enable their group to compete in research.

**Key Points:**
- DGX Spark enables small research groups to prototype and train foundation models.
- It provides a significant amount of VRAM in an all-in-one design, useful for groups with limited funding.
- The Spark is not faster than high-end GPUs like the H100 but offers practical advantages for specific use cases.
- The community acknowledges that the Spark is designed for users like the author, despite initial criticisms.
- Comparisons to consumer GPUs like the 3090 and 5090 are made, noting performance differences.

**Discussion Highlights:** The discussion highlights a consensus that the DGX Spark is well-suited for its intended audience—small research groups with limited resources. While it may not meet the expectations of those seeking high-end performance, it is appreciated for its practical benefits in specific scenarios.

---

## 32. [GLM 4.7 is out on HF!](https://reddit.com/r/LocalLLaMA/comments/1pt5heq/glm_47_is_out_on_hf/)

**Author:** u/KvAk_AKPlaysYT | **Upvotes:** 593 | **Comments:** 123 | **Date:** 2025-12-22

**Summary:** The Reddit post announces the release of GLM 4.7 on Hugging Face, gaining significant attention with 593 upvotes and 123 comments. The discussion highlights community reactions, comparisons with other models, and appreciation for the contribution.

**Key Points:**
- GLM 4.7 is now available on Hugging Face
- The post received 593 upvotes and 123 comments
- Community appreciates the contribution with special flair
- Comparisons made with other models like Minimax and Gemma 4
- Diagrams in reasoning/planning stage noted as a first

**Discussion Highlights:** The discussion features appreciation for the post's popularity, comparisons with other models, and notable mentions of diagrams in the reasoning stage. Some users express anticipation for other model releases like Gemma 4.

---

## 33. [I made Soprano-80M: Stream ultra-realistic TTS in &lt;15ms, up to 2000x realtime, and &lt;1 GB VRAM, released under Apache 2.0!](https://reddit.com/r/LocalLLaMA/comments/1pt3sco/i_made_soprano80m_stream_ultrarealistic_tts_in/)

**Author:** u/eugenekwek | **Upvotes:** 643 | **Comments:** 104 | **Date:** 2025-12-22

**Summary:** Eugene introduced Soprano-80M, a state-of-the-art TTS model optimized for ultra-low latency and high-speed audio generation, achieving <15ms latency and up to 2000x realtime performance. The model uses a 32 kHz sample rate and a vocoder-based decoder for superior audio quality and speed.

**Key Points:**
- Soprano-80M achieves <15ms latency and up to 2000x realtime performance.
- Uses a 32 kHz sample rate for clearer audio and a vocoder-based decoder for faster generation.
- Can generate a 10-hour audiobook in under 20 seconds.
- Users confirm its speed and inquire about finetuning code and hardware requirements.

**Discussion Highlights:** Users praised the model's speed and performance, with one user noting a brief delay before rapid audio generation. There were inquiries about finetuning code and hardware specifications used for benchmarking.

---

## 34. [major open-source releases this year](https://reddit.com/r/LocalLLaMA/comments/1pstlas/major_opensource_releases_this_year/)

**Author:** u/sahilypatel | **Upvotes:** 690 | **Comments:** 100 | **Date:** 2025-12-22

**Summary:** The Reddit post highlights major open-source releases this year, with a focus on China's dominance in the open-source space and high expectations for future releases like DeepSeek.

**Key Points:**
- China is leading in open-source contributions
- DeepSeek's next release is highly anticipated
- Mistral's performance at small sizes is a topic of discussion

**Discussion Highlights:** The discussion emphasizes China's strong presence in open-source development and the community's excitement for upcoming releases, particularly DeepSeek's potential to surpass closed-source models.

---

## 35. [llama.cpp appreciation post](https://reddit.com/r/LocalLLaMA/comments/1psbx2q/llamacpp_appreciation_post/)

**Author:** u/hackiv | **Upvotes:** 1687 | **Comments:** 153 | **Date:** 2025-12-21

**Summary:** The Reddit post appreciates llama.cpp for its high performance, with users sharing their positive experiences and performance metrics. The discussion highlights the superiority of llama.cpp over other tools like Ollama.

**Key Points:**
- llama.cpp achieves 23t/s on a Radeon 6700XT setup, outperforming other tools
- Users express preference for llama.cpp over Ollama due to better performance
- The post gained significant traction with 1687 upvotes and 153 comments
- A user shared a humorous meme comparing Ollama to llama.cpp

**Discussion Highlights:** The discussion consensus highlights llama.cpp's superior performance and user satisfaction, with many users sharing their successful experiences and performance gains after switching from other tools.

---

## 36. [Xiaomi’s MiMo-V2-Flash (309B model) jumping straight to the big leagues](https://reddit.com/r/LocalLLaMA/comments/1prjzoh/xiaomis_mimov2flash_309b_model_jumping_straight/)

**Author:** u/98Saman | **Upvotes:** 438 | **Comments:** 99 | **Date:** 2025-12-20

**Summary:** The Reddit post discusses Xiaomi's MiMo-V2-Flash (309B model), highlighting its impressive performance and efficiency compared to other models. The community shows significant interest in its capabilities and potential applications.

**Key Points:**
- MiMo-V2-Flash (309B model) is noted for its high performance and efficiency
- The model is compared favorably to other models like DS 3.2, with better performance at half the parameters
- Community interest is high, with questions about model availability and performance benchmarks
- The Artificial Analysis Index is criticized for not accurately reflecting model performance

**Discussion Highlights:** The discussion highlights the model's impressive performance metrics and efficiency, with community members expressing interest in its availability and potential use cases. There is also a consensus that traditional benchmarks may not fully capture the model's capabilities.

---

## 37. [Career Advice in AI — Notes from an Andrew Ng Lecture](https://reddit.com/r/LocalLLaMA/comments/1pqpj29/career_advice_in_ai_notes_from_an_andrew_ng/)

**Author:** u/Dear-Success-1441 | **Upvotes:** 351 | **Comments:** 55 | **Date:** 2025-12-19

**Summary:** Andrew Ng emphasizes that now is the best time to build a career in AI, highlighting the rapid progress in the field. He advises staying updated with the latest coding tools, focusing on product management skills, surrounding oneself with the right people, prioritizing team dynamics over company brand, and actively building projects to gain practical experience.

**Key Points:**
- AI career opportunities are expanding rapidly with accelerating progress.
- Staying updated with the latest coding tools is crucial for productivity.
- Product management skills are becoming increasingly valuable in AI careers.
- Success is influenced by the people you surround yourself with.
- Building projects and gaining practical experience is highly encouraged.

**Discussion Highlights:** The discussion highlights a mix of enthusiasm and skepticism about AI careers. Some users emphasize the importance of staying updated with tools and developing social skills, while others express concerns about job security and the practical challenges of working in AI.

---

## 38. [Qwen released Qwen-Image-Layered on Hugging face.](https://reddit.com/r/LocalLLaMA/comments/1pqoi6i/qwen_released_qwenimagelayered_on_hugging_face/)

**Author:** u/Difficult-Cap-7527 | **Upvotes:** 639 | **Comments:** 70 | **Date:** 2025-12-19

**Summary:** Qwen has released Qwen-Image-Layered on Hugging Face, featuring Photoshop-grade layering with physically isolated RGBA layers, prompt-controlled structure, and infinite decomposition capabilities.

**Key Points:**
- Photoshop-grade layering with true native editability
- Physically isolated RGBA layers
- Prompt-controlled structure for specifying layers
- Infinite decomposition for detailed layering
- Core model size is 40GB unquantized

**Discussion Highlights:** The community is excited about the release, with comments highlighting the rapid pace of advancements and concerns about RAM/VRAM requirements. Some users expressed enthusiasm for Qwen's continuous innovations.

---

## 39. [Realist meme of the year!](https://reddit.com/r/LocalLLaMA/comments/1pqegcr/realist_meme_of_the_year/)

**Author:** u/Slight_Tone_2188 | **Upvotes:** 2137 | **Comments:** 125 | **Date:** 2025-12-19

**Summary:** The Reddit post titled 'Realist meme of the year!' by u/Slight_Tone_2188 gained significant traction with 2137 upvotes and 125 comments. The discussion revolves around various topics including the need for a cure for cancer, humorous suggestions like downloading more RAM, and critiques of AI companies and hardware manufacturers.

**Key Points:**
- The post received a special flair for its contribution.
- A prominent comment highlights the urgency for a cure for cancer.
- Humorous suggestions like downloading more RAM were made.
- Criticism was directed towards AI companies and hardware manufacturers for their role in the problem.

**Discussion Highlights:** The discussion highlights a mix of serious concerns, such as the need for medical advancements, and humorous or satirical comments. There is also a notable critique of the tech industry, particularly AI companies and hardware manufacturers, for their perceived role in current issues.

---

## 40. [Kimi K2 Thinking at 28.3 t/s on 4x Mac Studio cluster](https://reddit.com/r/LocalLLaMA/comments/1pq2ry0/kimi_k2_thinking_at_283_ts_on_4x_mac_studio/)

**Author:** u/geerlingguy | **Upvotes:** 546 | **Comments:** 142 | **Date:** 2025-12-18

**Summary:** The post discusses performance testing of Kimi K2 on a cluster of 4x Mac Studios using RDMA Tensor settings, highlighting the challenges in benchmarking and the potential for future improvements with new Apple Silicon chips.

**Key Points:**
- Testing Kimi K2 on a 4x Mac Studio cluster with RDMA Tensor settings
- Challenges in benchmarking due to lack of tools like llama-bench in Exo
- Potential for significant performance improvements with new Apple Silicon ultra chips
- Community appreciation for the testing and sharing of results
- Mention of additional data and resources in linked GitHub issue and blog post

**Discussion Highlights:** The discussion highlights community interest in the performance testing, appreciation for the author's contributions, and anticipation for future improvements with new hardware. There is also a mention of additional resources and data shared in external links.

---

## 41. [Google's Gemma models family](https://reddit.com/r/LocalLLaMA/comments/1ppun3v/googles_gemma_models_family/)

**Author:** u/jacek2023 | **Upvotes:** 491 | **Comments:** 119 | **Date:** 2025-12-18

**Summary:** The Reddit post discusses Google's Gemma models family, highlighting the introduction of FunctionGemma and community reactions.

**Key Points:**
- Introduction of FunctionGemma for fine-tuning
- Community excitement and humor about the announcement
- Technical details and model count speculation

**Discussion Highlights:** The community shows enthusiasm for FunctionGemma, with some humor about the announcement becoming reality. There is speculation about new models and appreciation for Google's contributions.

---

## 42. [Hey, LocalLLaMa. We need to talk...](https://reddit.com/r/LocalLLaMA/comments/1pp6jhq/hey_localllama_we_need_to_talk/)

**Author:** u/Eisenstein | **Upvotes:** 423 | **Comments:** 142 | **Date:** 2025-12-17

**Summary:** The post emphasizes the importance of engaging with and providing feedback to contributors in the r/LocalLLaMA community, highlighting that recognition and constructive criticism are crucial for sustaining open-source projects.

**Key Points:**
- Encouragement to engage with smaller posts and provide feedback
- Importance of upvoting and recognizing contributions
- Constructive criticism helps improve projects
- Mixed reactions in comments regarding the quality of some projects
- Community appreciation for genuine contributions

**Discussion Highlights:** The discussion reveals a mix of support for the post's message and skepticism about the quality of some projects. While some users appreciate the call for engagement, others express concerns about the prevalence of low-quality or AI-generated content.

---

## 43. [Apple introduces SHARP, a model that generates a photorealistic 3D Gaussian representation from a single image in seconds.](https://reddit.com/r/LocalLLaMA/comments/1poy0lb/apple_introduces_sharp_a_model_that_generates_a/)

**Author:** u/themixtergames | **Upvotes:** 1225 | **Comments:** 138 | **Date:** 2025-12-17

**Summary:** Apple has introduced SHARP, a model that can generate photorealistic 3D Gaussian representations from a single image in seconds. The model is showcased with examples rendered in real-time on Apple Vision Pro and generated on a MacBook Pro M1 Max.

**Key Points:**
- SHARP generates 3D Gaussian representations from a single image.
- Examples were rendered in real-time on Apple Vision Pro.
- Scenes were generated in 5–10 seconds on a MacBook Pro M1 Max.
- The model requires CUDA GPU for rendering trajectories.
- Community reactions include comparisons to cyberpunk's braindance and inquiries about content compatibility.

**Discussion Highlights:** The community showed interest in the model's capabilities, with comparisons to cyberpunk's braindance and questions about its compatibility with adult content. The top comments also highlighted the model's performance on Apple devices and its requirement for CUDA GPU.

---

## 44. [Microsoft's TRELLIS 2-4B, An Open-Source Image-to-3D Model](https://reddit.com/r/LocalLLaMA/comments/1porpwd/microsofts_trellis_24b_an_opensource_imageto3d/)

**Author:** u/Dear-Success-1441 | **Upvotes:** 1209 | **Comments:** 130 | **Date:** 2025-12-17

**Summary:** Microsoft's TRELLIS 2-4B is an open-source image-to-3D model with 4 billion parameters, using Flow-Matching Transformers with Sparse Voxel based 3D VAE to convert single images into 3D assets. The model has been well-received, with a demo and blog post available for further exploration.

**Key Points:**
- Model Type: Flow-Matching Transformers with Sparse Voxel based 3D VAE
- Parameters: 4 Billion
- Input: Single Image, Output: 3D Asset
- Model, demo, and blog post links provided
- Community reaction includes both positive feedback and practical concerns

**Discussion Highlights:** The community discussion highlights a mix of enthusiasm and skepticism. Some users appreciate the model's capabilities and potential applications, while others express concerns about its practical usability and suggest improvements like using multiple images for better results.

---

## 45. [8x Radeon 7900 XTX Build for Longer Context Local Inference - Performance Results &amp; Build Details](https://reddit.com/r/LocalLLaMA/comments/1pogwb6/8x_radeon_7900_xtx_build_for_longer_context_local/)

**Author:** u/Beautiful_Trust_8151 | **Upvotes:** 746 | **Comments:** 220 | **Date:** 2025-12-16

**Summary:** The post details an 8x Radeon 7900 XTX GPU build for local AI inference, achieving 192 GB VRAM and stable performance with up to 27 tokens per second generation speed. The system, costing around $6-7k, offers customizability and long-context capability for specific work use cases.

**Key Points:**
- 8x AMD Radeon 7900 XTX GPUs with 192 GB VRAM total, paired with an Intel Core i7-14700F and 192 GB system RAM.
- Performance metrics: 437 tokens/sec prompt processing (empty context), 27 tokens/sec generation; drops to 200+ tokens/sec prompt and 16 tokens/sec generation at 19k tokens.
- Total build cost around $6-7k, with advantages in upgradability, customizability, and long-context capability.
- Discussion highlights include appreciation for the build's budget efficiency and comparisons to other high-end GPU solutions.
- Notable comment: The build is praised for its cost-effectiveness compared to alternatives like the RTX Pro 6000.

**Discussion Highlights:** The discussion highlights appreciation for the build's cost-effectiveness and performance, with comparisons to other high-end GPU solutions. Notable comments praise the budget efficiency and the build's potential for future upgrades.

---

## 46. [Meta announced a new SAM Audio Model for audio editing that can segment sound from complex audio mixtures using text, visual, and time span prompts.](https://reddit.com/r/LocalLLaMA/comments/1po7i0c/meta_announced_a_new_sam_audio_model_for_audio/)

**Author:** u/Difficult-Cap-7527 | **Upvotes:** 527 | **Comments:** 86 | **Date:** 2025-12-16

**Summary:** Meta announced a new SAM Audio Model that can segment sound from complex audio mixtures using text, visual, and time span prompts, transforming audio processing.

**Key Points:**
- SAM Audio Model can isolate any sound from complex audio mixtures using text, visual, and time span prompts.
- Potential applications include isolating and subtracting unwanted sounds in Microsoft Teams meetings.
- The model's ability to pick specific sounds from complex mixtures is highly praised.
- Model sizes and specifications are available in the provided image link.
- Questions about its effectiveness on music instruments were raised.

**Discussion Highlights:** The discussion highlights the potential applications of the SAM Audio Model, such as improving audio quality in virtual meetings by isolating unwanted sounds. Users also expressed interest in the model's capabilities and specifications.

---

## 47. [I'm strong enough to admit that this bugs the hell out of me](https://reddit.com/r/LocalLLaMA/comments/1pnfaqo/im_strong_enough_to_admit_that_this_bugs_the_hell/)

**Author:** u/ForsookComparison | **Upvotes:** 1818 | **Comments:** 395 | **Date:** 2025-12-15

**Summary:** The post expresses frustration about a workstation setup, possibly related to performance or assembly issues. The discussion includes comments about GPU setups and comparisons with Mac workstations.

**Key Points:**
- The post title indicates frustration about something
- The main content is likely an image linked in the comments
- Discussion involves workstation performance and GPU setups
- Comparisons are made between Mac and other workstations

**Discussion Highlights:** The discussion highlights differences in workstation performance, with some users favoring GPU setups over Mac workstations. There is also mention of a 'perfect workstation' and potential assembly issues.

---

## 48. [They're finally here (Radeon 9700)](https://reddit.com/r/LocalLLaMA/comments/1pnd5uf/theyre_finally_here_radeon_9700/)

**Author:** u/Zeikos | **Upvotes:** 360 | **Comments:** 70 | **Date:** 2025-12-15

**Summary:** The Reddit post announces the arrival of Radeon 9700 GPUs, sparking community interest in benchmarks and performance testing. Users express nostalgia for the historic GPU name and discuss plans for evaluating the new hardware. Key points include community interest in benchmarks, nostalgia for the historic Radeon 9700 name, plans to test inference, training, noise, and heat performance, and requests for specific benchmark recommendations. The discussion highlights strong community interest in performance metrics, with users emphasizing the need for comprehensive benchmarks covering inference, training, noise levels, and heat output. There's also a notable sense of nostalgia for the historic Radeon 9700 brand name.

---

## 49. [NVIDIA releases Nemotron 3 Nano, a new 30B hybrid reasoning model!](https://reddit.com/r/LocalLLaMA/comments/1pn8upp/nvidia_releases_nemotron_3_nano_a_new_30b_hybrid/)

**Author:** u/Difficult-Cap-7527 | **Upvotes:** 853 | **Comments:** 181 | **Date:** 2025-12-15

**Summary:** NVIDIA has released Nemotron 3 Nano, a 30B hybrid reasoning model with a 1M context window and top performance in SWE-Bench, reasoning, and chat. The model is noted for its speed and efficiency.

**Key Points:**
- Nemotron 3 Nano is a 30B hybrid reasoning model
- It has a 1M context window
- Best in class performance for SWE-Bench, reasoning, and chat
- The model is part of the Nemotron 3 family of MoE models
- Noted for its speed with 110 t/s generation on local hardware

**Discussion Highlights:** The community is excited about the model's speed and performance. There is some discussion about the model's size being considered 'nano' despite being 30B, and clarification about the Nemotron 3 family including different sizes of MoE models.

---

## 50. [New Google model incoming!!!](https://reddit.com/r/LocalLLaMA/comments/1pn37mw/new_google_model_incoming/)

**Author:** u/[deleted] | **Upvotes:** 1277 | **Comments:** 262 | **Date:** 2025-12-15

**Summary:** The Reddit post discusses anticipation and speculation around an upcoming new Google model, with users expressing various hopes and expectations.

**Key Points:**
- The post links to a tweet and Hugging Face page hinting at a new Google model.
- Users hope the new model is not similar to Gemma3-Math.
- Speculation includes possibilities like Gemma 4 or a multi-modal replacement for existing models.
- There is significant hype and excitement about the potential new model.

**Discussion Highlights:** The discussion highlights a mix of excitement and caution, with users expressing diverse expectations ranging from improved capabilities to concerns about the model's focus and performance.

---

