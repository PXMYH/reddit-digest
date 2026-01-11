# r/LocalLLaMA Reading Digest

**Period:** 2026-01-11 to 2026-01-11
**Posts Summarized:** 50
**Total Posts Analyzed:** 50

---

## 1. [I clustered 3 DGX Sparks that NVIDIA said couldn't be clustered yet...took 1500 lines of C to make it work](https://reddit.com/r/LocalLLaMA/comments/1q8hqgd/i_clustered_3_dgx_sparks_that_nvidia_said_couldnt/)

**Author:** u/Ok-Pomegranate1314 | **Upvotes:** 812 | **Comments:** 139 | **Date:** 2026-01-09

**Summary:** The author successfully clustered three NVIDIA DGX Sparks, overcoming networking limitations by writing a custom NCCL plugin. This achievement allows distributed inference across all three nodes at high speeds, despite NVIDIA's official support only covering two-node clusters.

**Key Points:**
- Author clustered three DGX Sparks, exceeding NVIDIA's official support for two-node clusters.
- Developed a custom NCCL network plugin (~1500 lines of C) to handle subnet-aware NIC selection and raw RDMA implementation.
- Achieved distributed inference at 8+ GB/s over RDMA, demonstrating significant performance.
- The solution addresses challenges like subnet differences, RDMA state machine issues, and deadlocks.
- The community praised the work as impressive and potentially impactful for distributed computing.

**Discussion Highlights:** The community highlighted the technical difficulty of working with NCCL and praised the author's achievement. Questions were raised about scalability and performance gains, indicating interest in broader applications of the solution.

---

## 2. [The reason why RAM has become so expensive](https://reddit.com/r/LocalLLaMA/comments/1q8ckz0/the_reason_why_ram_has_become_so_expensive/)

**Author:** u/InvadersMustLive | **Upvotes:** 3939 | **Comments:** 337 | **Date:** 2026-01-09

**Summary:** The Reddit post discusses the significant increase in RAM prices, with comments suggesting strategic monopolization by certain entities to control future demand and economic viability of competitors.

**Key Points:**
- RAM prices have increased dramatically, with some users reporting up to 10 times the cost compared to the previous year.
- There is speculation about monopolization of RAM resources to control future demand and economic viability of competitors, particularly in the AI and data center sectors.
- The price increase is seen as a potential economic strategy rather than a temporary market fluctuation.
- Users have observed a substantial rise in costs for high-capacity RAM modules, such as DDR5-6400 ECC RDIMM.

**Discussion Highlights:** The discussion highlights concerns about the economic implications of rising RAM prices, with a consensus that the increase may be strategically driven to control market demand and limit competition, particularly in the AI and data center industries.

---

## 3. [DeepSeek V4 Coming](https://reddit.com/r/LocalLLaMA/comments/1q89g1i/deepseek_v4_coming/)

**Author:** u/External_Mood4719 | **Upvotes:** 467 | **Comments:** 97 | **Date:** 2026-01-09

**Summary:** DeepSeek is set to release its next-generation AI model, V4, which focuses on strong code-generation capabilities and outperforms existing models in internal benchmarks. The model is expected to handle long code prompts better and improve reasoning and reliability.

**Key Points:**
- DeepSeek V4 is expected to roll out in the coming weeks with a focus on code generation.
- V4 outperforms mainstream models like Claude and GPT in internal benchmarks.
- The model improves handling of long code prompts and overall reasoning ability.
- Users appreciate DeepSeek's cost-effectiveness and performance.
- Expectations are high for significant improvements in coding and possibly math/agentic capabilities.

**Discussion Highlights:** Users express excitement and high expectations for DeepSeek V4, noting its cost-effectiveness and performance. Some anticipate significant improvements in coding, math, and agentic capabilities, while others speculate on the timeline and potential delays.

---

## 4. [(The Information): DeepSeek To Release Next Flagship AI Model With Strong Coding Ability](https://reddit.com/r/LocalLLaMA/comments/1q88hdc/the_information_deepseek_to_release_next_flagship/)

**Author:** u/Nunki08 | **Upvotes:** 462 | **Comments:** 97 | **Date:** 2026-01-09

**Summary:** DeepSeek is set to release a new flagship AI model with strong coding capabilities, generating excitement and anticipation in the community.

**Key Points:**
- DeepSeek's upcoming model focuses on strong coding abilities
- The announcement has generated significant interest and excitement
- Community members are looking forward to more models and competition in the AI space
- Some users express skepticism about performance claims
- There is anticipation for the model's role-playing capabilities

**Discussion Highlights:** The community shows enthusiasm for DeepSeek's new model, with many expressing excitement about its potential coding capabilities and the overall benefit of more AI models in the market. Some users remain skeptical about performance claims, while others are eager to see the model's role-playing abilities.

---

## 5. [The NO FAKES Act has a "Fingerprinting" Trap that kills Open Source. We need to lobby for a Safe Harbor.](https://reddit.com/r/LocalLLaMA/comments/1q7qcux/the_no_fakes_act_has_a_fingerprinting_trap_that/)

**Author:** u/PostEasy7183 | **Upvotes:** 589 | **Comments:** 86 | **Date:** 2026-01-08

**Summary:** The Reddit post discusses the potential negative impact of the NO FAKES Act on open-source AI development, particularly for voice and likeness replication tools. The author argues that the act could make developers liable for misuse of their tools, effectively stifling innovation and favoring big tech companies. Key points include the creation of a 'digital replica right', potential liability for developers, lack of Section 230 protection, and a call for a 'Safe Harbor' amendment. The discussion highlights concerns about the act's impact on innovation and a call for action to advocate for amendments.

---

## 6. [Jensen Huang saying "AI" 121 times during the NVIDIA CES keynote - cut with one prompt](https://reddit.com/r/LocalLLaMA/comments/1q7d8bj/jensen_huang_saying_ai_121_times_during_the/)

**Author:** u/Prior-Arm-6705 | **Upvotes:** 885 | **Comments:** 140 | **Date:** 2026-01-08

**Summary:** A Reddit user created a compilation video of every instance Jensen Huang said 'AI' during NVIDIA's CES 2025 keynote, totaling 121 times. The process involved using open-source tools to download, parse, and edit the video locally.

**Key Points:**
- Jensen Huang said 'AI' 121 times during the CES 2025 keynote.
- The user employed open-source tools (Dive, yt-dlp-mcp, ffmpeg-mcp-lite) to automate the video compilation.
- The process was entirely local, with no cloud involvement.
- The result was described as 'hypnotic' and summarized the keynote effectively.
- Top comments included humor, criticism of pricing, and praise for the technical execution.

**Discussion Highlights:** The discussion highlighted the effectiveness of the compilation as a summary of the keynote, with some users joking about the frequency of 'AI' mentions and others critiquing NVIDIA's pricing. There was also appreciation for the technical execution and tools used.

---

## 7. [16x AMD MI50 32GB at 10 t/s (tg) &amp; 2k t/s (pp) with Deepseek v3.2 (vllm-gfx906)](https://reddit.com/r/LocalLLaMA/comments/1q6n5vl/16x_amd_mi50_32gb_at_10_ts_tg_2k_ts_pp_with/)

**Author:** u/ai-infos | **Upvotes:** 448 | **Comments:** 236 | **Date:** 2026-01-07

**Summary:** The post discusses running Deepseek v3.2 on 16 AMD MI50 GPUs, achieving 10 tokens per second (output) and 2000 tokens per second (input) with a 69000 context length. The setup is cost-effective and aims to provide a local AGI solution without high expenses.

**Key Points:**
- Deepseek v3.2 AWQ 4-bit runs at 10 tok/s (output) and 2000 tok/s (input) on 16 AMD MI50 GPUs.
- Power draw is 550W idle and 2400W peak during inference.
- The setup is open-sourced and aims to be a cost-effective alternative to CPU hardware.
- Future plans include testing 32 AMD MI50 GPUs for Kimi K2 Thinking.
- The author highlights the benefits of tensor parallelism and high bandwidth for prompt processing.

**Discussion Highlights:** The discussion includes appreciation for the cost-effective setup, humor about using the setup as a heater, curiosity about noise levels and power requirements, and general excitement about the project.

---

## 8. [DeepSeek-R1’s paper was updated 2 days ago, expanding from 22 pages to 86 pages and adding a substantial amount of detail.](https://reddit.com/r/LocalLLaMA/comments/1q6c9wc/deepseekr1s_paper_was_updated_2_days_ago/)

**Author:** u/Nunki08 | **Upvotes:** 639 | **Comments:** 55 | **Date:** 2026-01-07

**Summary:** The DeepSeek-R1 paper was recently updated, expanding from 22 to 86 pages with added details. The Reddit post highlights this update and includes discussions on potential new architectures and research directions.

**Key Points:**
- DeepSeek-R1’s paper expanded from 22 to 86 pages with substantial new details.
- Discussion includes speculation about new architectures like dsv4 + r2.
- Interest in how architectural improvements perform at different model sizes.
- Mention of current research focus on linear attention and cache optimization.
- Original paper lacked implementation specifics; update may address this.

**Discussion Highlights:** The community is excited about the expanded paper, with speculation about new model architectures and improvements. There's particular interest in how these advancements might scale across different model sizes and the potential for linear attention to enable larger training capacities.

---

## 9. [A 30B Qwen Model Walks Into a Raspberry Pi… and Runs in Real Time](https://reddit.com/r/LocalLLaMA/comments/1q5m2n6/a_30b_qwen_model_walks_into_a_raspberry_pi_and/)

**Author:** u/ali_byteshape | **Upvotes:** 482 | **Comments:** 76 | **Date:** 2026-01-06

**Summary:** The Reddit post discusses the release of the Qwen3-30B-A3B-Instruct-2507 model, optimized for performance on small hardware like the Raspberry Pi 5. The model achieves 8.03 tokens per second (TPS) at 2.70 bits per weight (BPW) while retaining 94.18% of BF16 quality. The post highlights the trade-offs between model size, speed, and quality, particularly on GPUs. Key points include the model's performance on Raspberry Pi 5, retention of quality, influence of kernel choice on GPUs, community feedback for testing, and discussions on user experiences and potential applications like clustering Raspberry Pis.

---

## 10. [Performance improvements in llama.cpp over time](https://reddit.com/r/LocalLLaMA/comments/1q5dnyw/performance_improvements_in_llamacpp_over_time/)

**Author:** u/jacek2023 | **Upvotes:** 660 | **Comments:** 82 | **Date:** 2026-01-06

**Summary:** The Reddit post discusses performance improvements in llama.cpp over time, with a focus on NVIDIA GPUs and comparisons with other implementations like ik_llama.cpp. The community highlights significant progress in token generation speed.

**Key Points:**
- Performance gains are noted, particularly for NVIDIA GPUs.
- Comparisons are made with other implementations like ik_llama.cpp.
- Token generation speed has seen significant improvements.
- Prompt processing is noted to be slower but still shows progress.

**Discussion Highlights:** The discussion highlights the impressive progress in llama.cpp performance, especially in token generation speed, and compares it favorably with other implementations. The community appreciates the advancements and notes the ongoing improvements in prompt processing speed.

---

## 11. [For the first time in 5 years, Nvidia will not announce any new GPUs at CES — company quashes RTX 50 Super rumors as AI expected to take center stage](https://reddit.com/r/LocalLLaMA/comments/1q4x5e9/for_the_first_time_in_5_years_nvidia_will_not/)

**Author:** u/FullstackSensei | **Upvotes:** 621 | **Comments:** 198 | **Date:** 2026-01-05

**Summary:** Nvidia will not announce new GPUs at CES, focusing instead on AI. The company faces supply issues with high-end GPUs and may reintroduce older models like the RTX 3060. Rising hardware prices and limited availability are causing concern among consumers.

**Key Points:**
- No new GPU announcements at CES, with AI taking center stage
- Limited supply of RTX 5070Ti, 5080, and 5090 GPUs
- Potential reintroduction of the RTX 3060 to meet demand
- Rising prices for DDR5 RAM and storage
- Community frustration over corporate greed and lack of consumer focus

**Discussion Highlights:** The discussion highlights significant frustration among users regarding Nvidia's shift towards AI and away from consumer-focused products. Many express concerns about corporate greed, the high cost of hardware, and the future of local computing. There is a consensus that the current trend is unsustainable and may push consumers towards alternative solutions.

---

## 12. [llama.cpp performance breakthrough for multi-GPU setups](https://reddit.com/r/LocalLLaMA/comments/1q4s8t3/llamacpp_performance_breakthrough_for_multigpu/)

**Author:** u/Holiday-Injury-9397 | **Upvotes:** 556 | **Comments:** 188 | **Date:** 2026-01-05

**Summary:** The ik_llama.cpp project has achieved a significant performance breakthrough for multi-GPU setups, delivering a 3x to 4x speed improvement in local LLM inference. This advancement allows for the utilization of multiple low-cost GPUs instead of expensive high-end cards, making it a game-changer for homelabs, server rooms, and cloud setups.

**Key Points:**
- ik_llama.cpp introduces a new execution mode (split mode graph) for maximum utilization of multiple GPUs.
- Performance improvements range from 3x to 4x, making it a significant leap over previous methods.
- This breakthrough reduces the need for expensive high-end GPUs, enabling the use of multiple low-cost GPUs.
- Even on single GPU or CPU-only setups, ik_llama.cpp shows consistent 2x prompt processing speed improvements.
- The project is seen as competitive with other performance-optimized forks like exllama and vllm.

**Discussion Highlights:** The community is highly enthusiastic about the performance gains, with many users confirming significant speed improvements even on single GPU or CPU-only setups. There is a consensus that ik_llama.cpp is now a strong contender in the performance-optimized LLM inference space, though some users report bottlenecks in hybrid inference setups.

---

## 13. [Local LLMs vs breaking news: when extreme reality gets flagged as a hoax - the US/Venezuela event was too far-fetched](https://reddit.com/r/LocalLLaMA/comments/1q31ltd/local_llms_vs_breaking_news_when_extreme_reality/)

**Author:** u/ubrtnk | **Upvotes:** 377 | **Comments:** 194 | **Date:** 2026-01-03

**Summary:** The post discusses challenges faced by local LLMs in processing extreme breaking news events, such as the US attacking Venezuela, where models initially classified the event as a hoax despite credible sources. The author shares experiences with different models and their responses to the event.

**Key Points:**
- Local LLMs struggled to accept extreme breaking news as real, classifying it as misinformation.
- Different models (Qwen, Spark, GPT-OSS) had varying responses to the event, with larger models performing better.
- Models required explicit credible sources to acknowledge the event's reality.
- Discussion highlights bias in LLMs' internal models of unfamiliar geopolitical events.
- Some users expressed frustration with LLMs' skepticism and reliance on misinformation flags.

**Discussion Highlights:** The discussion revealed a consensus that LLMs often struggle with extreme or unlikely events, requiring explicit evidence to overcome their internal biases. Users shared similar experiences and expressed concerns about the models' limitations in handling breaking news.

---

## 14. [LeCun Says Llama 4 results "were fudged a little bit"](https://reddit.com/r/LocalLLaMA/comments/1q25070/lecun_says_llama_4_results_were_fudged_a_little/)

**Author:** u/MrPecunius | **Upvotes:** 366 | **Comments:** 89 | **Date:** 2026-01-02

**Summary:** Yann LeCun confirmed that Llama 4 benchmarks were manipulated, and Meta's GenAI organization was sidelined, leading to departures and lack of follow-up on promised models. The community expressed disappointment and shared additional resources.

**Key Points:**
- LeCun confirms Llama 4 benchmark manipulation
- Meta's GenAI organization was sidelined by Zuckerberg
- Many employees left or are leaving Meta
- No follow-up on promised large Llama 4 model
- Community disappointment and shared resources

**Discussion Highlights:** The discussion highlights disappointment in Meta's strategic decisions, with users sharing additional resources and questioning how a well-positioned organization could fail while smaller labs thrive. There is a consensus that Meta's handling of Llama 4 was a missed opportunity.

---

## 15. [Qwen-Image-2512](https://reddit.com/r/LocalLLaMA/comments/1q094a3/qwenimage2512/)

**Author:** u/Nunki08 | **Upvotes:** 711 | **Comments:** 122 | **Date:** 2025-12-31

**Summary:** The post announces the release of Qwen-Image-2512, a new image generation model, and provides links to guides, GGUF files, and various platforms for accessing the model. The community has responded positively, with users testing the model on low-end hardware and sharing creative outputs.

**Key Points:**
- Qwen-Image-2512 is a new image generation model with multiple access points.
- The model can run on low-end hardware, as demonstrated by a user with no GPU.
- The community has shown enthusiasm, with comments praising the model as a 'gift'.
- Users are experimenting with creative prompts, such as generating surreal images.

**Discussion Highlights:** The discussion highlights the model's accessibility and versatility, with users successfully running it on budget hardware and sharing imaginative outputs. The overall sentiment is positive, with appreciation for the model's capabilities and ease of use.

---

## 16. [[In the Wild] Reverse-engineered a Snapchat Sextortion Bot: It’s running a raw Llama-7B instance with a 2048 token window.](https://reddit.com/r/LocalLLaMA/comments/1pzwlie/in_the_wild_reverseengineered_a_snapchat/)

**Author:** u/simar-dmg | **Upvotes:** 739 | **Comments:** 108 | **Date:** 2025-12-30

**Summary:** A user reverse-engineered a Snapchat sextortion bot and discovered it was running a raw Llama-7B instance with a 2048 token window. The bot was vulnerable to a persona-adoption jailbreak, revealing its configuration and malicious payload.

**Key Points:**
- The bot used a Llama-7B model with a 2048 token context window and high temperature setting.
- A 'Grandma Protocol' jailbreak forced the bot to reveal its environment variables and configuration.
- The bot's erratic behavior was due to running on minimal hardware to cut costs.
- Scammers are shifting to open-source models like Llama-7B to avoid API costs and censorship filters.
- The bot eventually revealed a malicious link it was programmed to hide.

**Discussion Highlights:** The discussion highlighted skepticism about the accuracy of the bot's revealed information, with some users suggesting it could be entirely hallucinated. Others questioned the commonality of system prompts including environment variables and debated the reliability of the findings.

---

## 17. [Llama-3.3-8B-Instruct](https://reddit.com/r/LocalLLaMA/comments/1pz7bmv/llama338binstruct/)

**Author:** u/jacek2023 | **Upvotes:** 466 | **Comments:** 78 | **Date:** 2025-12-29

**Summary:** The post announces the release of Llama-3.3-8B-Instruct, a previously API-exclusive model from Meta, now available in GGUF format after the author discovered a method to download it via finetuning. The community is excited and conducting benchmarks to verify its authenticity.

**Key Points:**
- Llama-3.3-8B-Instruct was previously only available via Meta's API.
- The author found a way to download the model through finetuning and released it in GGUF format.
- The community is conducting benchmarks to verify the model's authenticity.
- There are concerns about the model's max position embeddings being limited to 8K.

**Discussion Highlights:** The community is excited about the release, with ongoing benchmarks to verify the model's authenticity. Some users are concerned about the model's max position embeddings being limited to 8K, and there is general appreciation for the author's efforts in making the model available.

---

## 18. [Tencent just released WeDLM 8B Instruct on Hugging Face](https://reddit.com/r/LocalLLaMA/comments/1pyg4yt/tencent_just_released_wedlm_8b_instruct_on/)

**Author:** u/Difficult-Cap-7527 | **Upvotes:** 419 | **Comments:** 62 | **Date:** 2025-12-29

**Summary:** Tencent released WeDLM 8B Instruct on Hugging Face, a diffusion language model that outperforms vLLM-optimized Qwen3-8B in math reasoning tasks by 3-6× speed. The release has garnered significant attention and positive feedback from the community.

**Key Points:**
- WeDLM 8B Instruct is a diffusion language model released by Tencent on Hugging Face.
- It runs 3-6× faster than vLLM-optimized Qwen3-8B on math reasoning tasks.
- The model has an Apache 2.0 license, making it accessible for various uses.
- The community shows strong interest and positive feedback, highlighting its potential.
- A 7B version of the model is also available.

**Discussion Highlights:** The community is excited about the performance and potential of the WeDLM models, with many users expressing interest in the Apache 2.0 license and the impressive benchmark scores. There is a consensus on the promising future of 7-8B models in general.

---

## 19. [NVIDIA Drops Pascal Support On Linux, Causing Chaos On Arch Linux](https://reddit.com/r/LocalLLaMA/comments/1pxad0k/nvidia_drops_pascal_support_on_linux_causing/)

**Author:** u/HumanDrone8721 | **Upvotes:** 440 | **Comments:** 185 | **Date:** 2025-12-27

**Summary:** NVIDIA has dropped Pascal support on Linux, causing issues for Arch Linux users. The post highlights concerns and discussions around this change, with users expressing worry and sharing experiences with Pascal cards like the 24GB P40.

**Key Points:**
- NVIDIA's decision to drop Pascal support affects Linux users, particularly those on Arch Linux.
- The 24GB P40 is a notable Pascal card mentioned in the discussion.
- Users express concern and share their experiences with the change.
- Arch Linux has a history of moving legacy drivers to AUR, which is not surprising to some users.
- The change is seen as inevitable but disruptive by the community.

**Discussion Highlights:** The discussion highlights a mix of concern and acceptance among users. Some users reminisce about their experiences with Pascal cards, while others point out that Arch Linux has a history of moving legacy drivers to the Arch User Repository (AUR). The overall consensus seems to be that while the change is disruptive, it is not entirely unexpected.

---

## 20. [NVIDIA has 72GB VRAM version now](https://reddit.com/r/LocalLLaMA/comments/1pweljh/nvidia_has_72gb_vram_version_now/)

**Author:** u/decentralize999 | **Upvotes:** 464 | **Comments:** 148 | **Date:** 2025-12-26

**Summary:** The post discusses NVIDIA's new 72GB VRAM version, with the community expressing mixed reactions. Some users suggest larger versions like 128GB, while others focus on pricing and value.

**Key Points:**
- NVIDIA has released a 72GB VRAM version.
- Community interest varies, with some preferring larger versions like 128GB.
- Price comparisons show similar per-gig costs across different VRAM sizes.
- Users suggest waiting for future models like the 5090 with 48GB.
- The choice between models is seen as straightforward based on affordability.

**Discussion Highlights:** The discussion highlights a divide in community preferences, with some advocating for larger VRAM sizes and others focusing on current pricing and value. There is a consensus that the price per gig remains consistent, making the choice dependent on individual budget and needs.

---

## 21. [I wish this GPU VRAM upgrade modification became mainstream and ubiquitous to shred monopoly abuse of NVIDIA](https://reddit.com/r/LocalLLaMA/comments/1pvpkqo/i_wish_this_gpu_vram_upgrade_modification_became/)

**Author:** u/CeFurkan | **Upvotes:** 1014 | **Comments:** 180 | **Date:** 2025-12-25

**Summary:** The post discusses the desire for GPU VRAM upgrade modifications to become mainstream, challenging NVIDIA's monopoly. It highlights that such modifications are already popular in China, with Alibaba offering upgraded GPUs at various price points.

**Key Points:**
- GPU VRAM upgrade modifications are desired to challenge NVIDIA's monopoly
- Such modifications are already mainstream in China
- Alibaba offers upgraded GPUs like 2080Ti, 3080, 4080, 4090, and 5090 with increased VRAM
- Prices range from $300 for a 2080Ti 22GB to $4000 for a 5090 96GB
- Users report successful use of modded GPUs with increased memory

**Discussion Highlights:** The discussion highlights the availability and success of GPU VRAM upgrades in China, with users sharing their positive experiences and the cost-effectiveness of these modifications.

---

## 22. [Why I quit using Ollama](https://reddit.com/r/LocalLLaMA/comments/1pvjpmb/why_i_quit_using_ollama/)

**Author:** u/SoLoFaRaDi | **Upvotes:** 491 | **Comments:** 201 | **Date:** 2025-12-25

**Summary:** The author expresses dissatisfaction with Ollama due to a perceived shift from its original purpose of providing a secure inference platform for local AI models, citing concerns about the addition of proprietary cloud models and bloatware. The discussion reflects a consensus favoring alternatives like llama.cpp and LM Studio.

**Key Points:**
- Author's dissatisfaction with Ollama's shift towards cloud models and bloatware
- Concerns about privacy implications and deviation from the original purpose
- Community consensus favoring alternatives like llama.cpp and LM Studio
- Criticism of Ollama's past claims about improvements in llama.cpp
- Positive feedback on LM Studio as a preferred alternative

**Discussion Highlights:** The discussion highlights a strong preference for alternatives like llama.cpp and LM Studio, with users appreciating their focus on local model inference and lack of proprietary cloud integration. There is a consensus that Ollama has strayed from its original mission, leading to a shift in user loyalty towards other platforms.

---

## 23. [Exclusive: Nvidia buying AI chip startup Groq's assets for about $20 billion in largest deal on record](https://reddit.com/r/LocalLLaMA/comments/1puyq9r/exclusive_nvidia_buying_ai_chip_startup_groqs/)

**Author:** u/fallingdowndizzyvr | **Upvotes:** 663 | **Comments:** 157 | **Date:** 2025-12-24

**Summary:** Nvidia is acquiring AI chip startup Groq's assets for approximately $20 billion, marking the largest deal of its kind. The Reddit post and comments highlight mixed reactions, with some seeing it as beneficial for market competition and others expressing concerns about industry consolidation.

**Key Points:**
- Nvidia's acquisition of Groq's assets for $20 billion
- Mixed reactions: some view it as positive for competition, others as consolidation
- Questions raised about Groq's valuation and regulatory implications
- Community discussions on potential future acquisitions (e.g., Cerebras)

**Discussion Highlights:** The discussion reflects a divide in opinions, with some users optimistic about the deal fostering a competitive market, while others are skeptical, viewing it as another example of industry consolidation. Concerns about regulatory approval and the valuation of Groq are also prominent.

---

## 24. [We asked OSS-120B and GLM 4.6 to play 1,408 Civilization V games from the Stone Age into the future. Here's what we found.](https://reddit.com/r/LocalLLaMA/comments/1pux0yc/we_asked_oss120b_and_glm_46_to_play_1408/)

**Author:** u/vox-deorum | **Upvotes:** 649 | **Comments:** 174 | **Date:** 2025-12-24

**Summary:** The post discusses an experiment where open-source LLMs (OSS-120B and GLM-4.6) were used to play 1,408 games of Civilization V. The LLMs showed slightly better performance in best scores but slightly worse in win rates compared to the baseline AI. Interestingly, the LLMs developed distinct playstyles and could survive full games, a feat not achieved by pure-LLM or pure-RL approaches.

**Key Points:**
- LLMs played 1,408 full Civilization V games with distinct strategies.
- LLMs showed slightly better best scores but slightly worse win rates.
- OSS-120B favored a warmonger playstyle, while GLM-4.6 was more balanced.
- Both models preferred the Order ideology over Freedom.
- The hybrid approach allowed LLMs to survive full games, unlike pure-LLM or pure-RL methods.

**Discussion Highlights:** The discussion highlights enthusiasm for the potential of LLMs in gaming, with users expressing interest in playing against local models and integrating LLMs into multiplayer games. Some users also inquired about the impact of model size on performance and the possibility of treating the game as a multi-level agent-based model.

---

## 25. [AMA With Z.AI, The Lab Behind GLM-4.7](https://reddit.com/r/LocalLLaMA/comments/1ptxm3x/ama_with_zai_the_lab_behind_glm47/)

**Author:** u/zixuanlimit | **Upvotes:** 589 | **Comments:** 415 | **Date:** 2025-12-23

**Summary:** The post announces an AMA session with Z.AI, the research lab behind GLM-4.7, featuring several team members. The session is scheduled for 8 AM – 11 AM PST, with follow-ups over the next 48 hours.

**Key Points:**
- AMA session with Z.AI team members
- Scheduled for 8 AM – 11 AM PST with 48-hour follow-up
- Community questions focus on future releases, censorship, training challenges, and creative writing applications
- High engagement with 589 upvotes and 415 comments

**Discussion Highlights:** The community shows strong interest in future developments, ethical considerations, technical challenges, and creative applications of the GLM-4.7 model.

---

## 26. [DGX Spark: an unpopular opinion](https://reddit.com/r/LocalLLaMA/comments/1ptdtmz/dgx_spark_an_unpopular_opinion/)

**Author:** u/emdblc | **Upvotes:** 740 | **Comments:** 221 | **Date:** 2025-12-22

**Summary:** The author, a doctoral student in data science, shares their positive experience with the DGX Spark, highlighting its benefits for small research groups with limited resources. Despite not being as fast as high-end GPUs like the H100, the Spark's all-in-one design and large memory capacity enable their group to compete in foundation model research.

**Key Points:**
- DGX Spark enables small research groups with limited resources to compete in foundation model research.
- The Spark is not faster than high-end GPUs like the H100 but offers a large amount of memory in an all-in-one design.
- The Spark is particularly useful for groups with limited access to high-performance GPUs.
- The Spark's intended use case is acknowledged and appreciated by the community, despite initial criticisms.
- The Spark is compared to consumer GPUs like the 3090, with some noting that multiple 3090s can outperform a single Spark.

**Discussion Highlights:** The discussion highlights a consensus that the DGX Spark is well-suited for its intended audience—small research groups with limited resources. While it may not match the performance of high-end GPUs, its large memory capacity and all-in-one design are valued. Some comments also note that the Spark's performance is comparable to or even surpassed by multiple consumer GPUs like the 3090.

---

## 27. [GLM 4.7 is out on HF!](https://reddit.com/r/LocalLLaMA/comments/1pt5heq/glm_47_is_out_on_hf/)

**Author:** u/KvAk_AKPlaysYT | **Upvotes:** 591 | **Comments:** 123 | **Date:** 2025-12-22

**Summary:** The Reddit post announces the release of GLM 4.7 on Hugging Face, garnering significant engagement with 591 upvotes and 123 comments. The discussion highlights include appreciation for the contribution, comparisons with other models, and mentions of unique features like diagrams in reasoning stages.

**Key Points:**
- GLM 4.7 is now available on Hugging Face
- Post received high engagement (591 upvotes, 123 comments)
- Discussion includes comparisons with other models like Minimax and Gemma 4
- Unique features such as diagrams in reasoning stages are noted
- Community appreciation for the contributor's efforts

**Discussion Highlights:** The discussion highlights appreciation for the contributor's efforts, comparisons with other models, and mentions of unique features like diagrams in reasoning stages. There is also a notable comment about the absence of Gemma 4.

---

## 28. [I made Soprano-80M: Stream ultra-realistic TTS in &lt;15ms, up to 2000x realtime, and &lt;1 GB VRAM, released under Apache 2.0!](https://reddit.com/r/LocalLLaMA/comments/1pt3sco/i_made_soprano80m_stream_ultrarealistic_tts_in/)

**Author:** u/eugenekwek | **Upvotes:** 643 | **Comments:** 104 | **Date:** 2025-12-22

**Summary:** Eugene introduced Soprano-80M, a state-of-the-art TTS model designed for ultra-low latency and high-speed audio generation, achieving <15ms latency and up to 2000x realtime performance. The model uses a 32 kHz sample rate and a vocoder-based decoder for superior audio quality and speed.

**Key Points:**
- Soprano-80M achieves <15ms latency and up to 2000x realtime performance.
- Uses a 32 kHz sample rate for clearer audio and a vocoder-based decoder for faster generation.
- Can generate a 10-hour audiobook in under 20 seconds.
- Users report extremely fast performance with minimal GPU usage initially.
- Questions raised about hardware requirements and finetuning code availability.

**Discussion Highlights:** Users confirmed the model's speed and efficiency, with one noting minimal GPU usage followed by rapid generation. There was interest in finetuning code and hardware specifications, with some users questioning the performance metrics compared to similar models.

---

## 29. [major open-source releases this year](https://reddit.com/r/LocalLLaMA/comments/1pstlas/major_opensource_releases_this_year/)

**Author:** u/sahilypatel | **Upvotes:** 692 | **Comments:** 100 | **Date:** 2025-12-22

**Summary:** The Reddit post highlights major open-source releases this year, with a focus on the dominance of China in the open-source space and high expectations for future models like DeepSeek.

**Key Points:**
- China is dominating the open-source space
- High expectations for DeepSeek's future performance
- Discussion on Mistral's effectiveness at smaller sizes

**Discussion Highlights:** The discussion highlights the dominance of China in open-source contributions and the community's high expectations for future models like DeepSeek, with some debate on the effectiveness of Mistral at smaller sizes.

---

## 30. [llama.cpp appreciation post](https://reddit.com/r/LocalLLaMA/comments/1psbx2q/llamacpp_appreciation_post/)

**Author:** u/hackiv | **Upvotes:** 1682 | **Comments:** 153 | **Date:** 2025-12-21

**Summary:** The Reddit post appreciates llama.cpp, highlighting its superior performance compared to other tools like LM Studio and Ollama. Users share their positive experiences and performance metrics.

**Key Points:**
- llama.cpp offers significantly higher performance (e.g., 23t/s vs 8t/s on similar hardware)
- Users are switching from other tools like Ollama to llama.cpp
- The community appreciates contributions and provides special recognition
- Hardware specifics (e.g., Radeon 6700XT) are mentioned in performance discussions

**Discussion Highlights:** The discussion highlights the performance advantages of llama.cpp over alternatives, with users sharing their migration experiences and hardware setups. There is a consensus on the superiority of llama.cpp in terms of speed and efficiency.

---

## 31. [Xiaomi’s MiMo-V2-Flash (309B model) jumping straight to the big leagues](https://reddit.com/r/LocalLLaMA/comments/1prjzoh/xiaomis_mimov2flash_309b_model_jumping_straight/)

**Author:** u/98Saman | **Upvotes:** 437 | **Comments:** 98 | **Date:** 2025-12-20

**Summary:** The post discusses Xiaomi's MiMo-V2-Flash (309B model), highlighting its impressive performance and efficiency compared to other models. The discussion includes comparisons with models like DS 3.2 and questions about the availability of open weights.

**Key Points:**
- MiMo-V2-Flash (309B model) is noted for its high performance and efficiency.
- Comparisons with other models like DS 3.2 show MiMo-V2-Flash performing well with fewer parameters.
- Questions about the availability of open weights and GGUF format are raised.
- The Artificial Analysis Index is criticized for not accurately reflecting model performance.

**Discussion Highlights:** The discussion highlights the model's impressive benchmarks and efficiency, with some users questioning the reliability of certain performance indices and expressing interest in the availability of open weights.

---

## 32. [Qwen released Qwen-Image-Layered on Hugging face.](https://reddit.com/r/LocalLLaMA/comments/1pqoi6i/qwen_released_qwenimagelayered_on_hugging_face/)

**Author:** u/Difficult-Cap-7527 | **Upvotes:** 635 | **Comments:** 70 | **Date:** 2025-12-19

**Summary:** Qwen has released Qwen-Image-Layered on Hugging Face, featuring Photoshop-grade layering with physically isolated RGBA layers, prompt-controlled structure, and infinite decomposition capabilities.

**Key Points:**
- Photoshop-grade layering with true native editability
- Physically isolated RGBA layers
- Prompt-controlled structure for specifying layers
- Infinite decomposition for detailed layering
- Model size is 40GB unquantized

**Discussion Highlights:** The community is excited about the release, with discussions focusing on the model's capabilities, RAM/VRAM requirements, and its large size.

---

## 33. [Realist meme of the year!](https://reddit.com/r/LocalLLaMA/comments/1pqegcr/realist_meme_of_the_year/)

**Author:** u/Slight_Tone_2188 | **Upvotes:** 2125 | **Comments:** 125 | **Date:** 2025-12-19

**Summary:** The post titled 'Realist meme of the year!' is a link post with no text content, sparking a discussion with 125 comments. The top comments include mentions of a Discord feature, humorous references to a cure for cancer, and discussions on hardware limitations and corporate responsibility.

**Key Points:**
- The post is a link post with no text content
- Top comments include a Discord feature mention
- Humorous reference to a cure for cancer
- Discussion on hardware limitations
- Corporate responsibility in technology

**Discussion Highlights:** The discussion highlights a mix of humor, technological constraints, and societal expectations, with a focus on the role of corporations in addressing hardware limitations.

---

## 34. [Kimi K2 Thinking at 28.3 t/s on 4x Mac Studio cluster](https://reddit.com/r/LocalLLaMA/comments/1pq2ry0/kimi_k2_thinking_at_283_ts_on_4x_mac_studio/)

**Author:** u/geerlingguy | **Upvotes:** 546 | **Comments:** 142 | **Date:** 2025-12-18

**Summary:** The post discusses performance testing of Kimi K2 on a cluster of 4x Mac Studios, highlighting the use of RDMA Tensor settings and the challenges in benchmarking. The author, u/geerlingguy, mentions ongoing testing and the lack of standardized benchmarking tools like llama-bench in Exo.

**Key Points:**
- Performance testing of Kimi K2 on a 4x Mac Studio cluster with RDMA Tensor settings.
- Challenges in benchmarking due to the lack of standardized tools like llama-bench in Exo.
- Ongoing testing and debugging efforts to stabilize RDMA support.
- Mention of future improvements with new Apple Silicon ultra chips and MATMUL instructions.
- Community appreciation for the author's contributions and testing efforts.

**Discussion Highlights:** The discussion highlights the community's interest in the performance testing and future improvements. There is appreciation for the author's efforts and a mention of potential significant improvements with upcoming Apple Silicon ultra chips. The community also acknowledges the challenges in benchmarking and the lack of standardized tools.

---

## 35. [Google's Gemma models family](https://reddit.com/r/LocalLLaMA/comments/1ppun3v/googles_gemma_models_family/)

**Author:** u/jacek2023 | **Upvotes:** 494 | **Comments:** 119 | **Date:** 2025-12-18

**Summary:** The Reddit post discusses Google's Gemma models family, highlighting the introduction of FunctionGemma and community reactions. The discussion includes technical details and enthusiastic responses from users.

**Key Points:**
- Introduction of FunctionGemma for fine-tuning
- Community excitement and jokes about Gemma models
- Technical details and model counts discussed
- Positive reception and special recognition for the post

**Discussion Highlights:** The discussion highlights the introduction of FunctionGemma, community enthusiasm, and technical insights. Users expressed excitement and humor about the new models, with some providing detailed analysis and others showing strong support for Google's advancements.

---

## 36. [Hey, LocalLLaMa. We need to talk...](https://reddit.com/r/LocalLLaMA/comments/1pp6jhq/hey_localllama_we_need_to_talk/)

**Author:** u/Eisenstein | **Upvotes:** 426 | **Comments:** 142 | **Date:** 2025-12-17

**Summary:** The post encourages community members to engage more with smaller projects by providing feedback and upvotes, emphasizing the importance of supporting open-source contributions. The discussion highlights mixed reactions, with some agreeing on the need for engagement while others criticize low-quality projects.

**Key Points:**
- Encouragement to engage with and support smaller projects
- Importance of feedback and upvotes for open-source contributors
- Mixed reactions in comments regarding project quality
- Criticism of AI-generated or low-effort projects
- Community appreciation for genuine contributions

**Discussion Highlights:** The discussion reveals a divide between those who support the call for engagement and those who criticize the quality of many projects. Some commenters appreciate the sentiment but are hesitant to support projects they perceive as low-effort or overly ambitious without substance.

---

## 37. [Apple introduces SHARP, a model that generates a photorealistic 3D Gaussian representation from a single image in seconds.](https://reddit.com/r/LocalLLaMA/comments/1poy0lb/apple_introduces_sharp_a_model_that_generates_a/)

**Author:** u/themixtergames | **Upvotes:** 1224 | **Comments:** 138 | **Date:** 2025-12-17

**Summary:** Apple has introduced SHARP, a model capable of generating photorealistic 3D Gaussian representations from a single image in seconds. The model is showcased with examples rendered in real-time on Apple Vision Pro and generated on a MacBook Pro M1 Max.

**Key Points:**
- SHARP generates photorealistic 3D Gaussian representations from a single image.
- The model operates in seconds and is demonstrated on Apple Vision Pro and MacBook Pro M1 Max.
- The GitHub repository and research paper are provided for further details.
- Community discussion includes comparisons to cyberpunk's braindance and inquiries about the model's capabilities.

**Discussion Highlights:** The community shows interest in the model's capabilities, with comparisons to cyberpunk's braindance and questions about its applications. The top comments highlight the model's performance on Apple devices and its potential uses.

---

## 38. [Microsoft's TRELLIS 2-4B, An Open-Source Image-to-3D Model](https://reddit.com/r/LocalLLaMA/comments/1porpwd/microsofts_trellis_24b_an_opensource_imageto3d/)

**Author:** u/Dear-Success-1441 | **Upvotes:** 1197 | **Comments:** 130 | **Date:** 2025-12-17

**Summary:** Microsoft's TRELLIS 2-4B is an open-source image-to-3D model with 4 billion parameters, converting single images into 3D assets. The community discussion highlights mixed feedback on its practical utility and suggests potential applications in gaming and design.

**Key Points:**
- Model Type: Flow-Matching Transformers with Sparse Voxel based 3D VAE
- Parameters: 4 Billion
- Input: Single Image, Output: 3D Asset
- Community feedback indicates mixed results and practical limitations
- Potential applications in gaming and design suggested

**Discussion Highlights:** The community discussion includes mixed reviews on the model's practical utility, with some users pointing out limitations and others suggesting innovative applications like combining with GIS data for video game world maps.

---

## 39. [8x Radeon 7900 XTX Build for Longer Context Local Inference - Performance Results &amp; Build Details](https://reddit.com/r/LocalLLaMA/comments/1pogwb6/8x_radeon_7900_xtx_build_for_longer_context_local/)

**Author:** u/Beautiful_Trust_8151 | **Upvotes:** 744 | **Comments:** 220 | **Date:** 2025-12-16

**Summary:** The post details an 8x Radeon 7900 XTX GPU build for local AI inference, highlighting its performance, cost (~$6-7k), and advantages like upgradability and long-context capability. The system achieves stable performance with up to 131k tokens and consumes around 900W during inference.

**Key Points:**
- 8x Radeon 7900 XTX GPUs with 192 GB VRAM total, paired with an Intel i7-14700F and 192 GB RAM.
- Performance: 437 tokens/sec (prompt) and 27 tokens/sec (generation) with empty context; drops to ~200 and 16 tokens/sec at 19k tokens.
- Total cost ~$6-7k, using a $500 PCIe switch for GPU connectivity.
- Advantages: Upgradability, customizability, and genuine long-context capability.
- Discussion highlights the build's cost-effectiveness and uniqueness in the AI era.

**Discussion Highlights:** The discussion appreciates the build's cost-effectiveness compared to professional GPUs and its role in the early AI era. Users also suggest testing other models like Qwen3-235B-A22B and note the power consumption (1.21 GW for 8 GPUs).

---

## 40. [Meta announced a new SAM Audio Model for audio editing that can segment sound from complex audio mixtures using text, visual, and time span prompts.](https://reddit.com/r/LocalLLaMA/comments/1po7i0c/meta_announced_a_new_sam_audio_model_for_audio/)

**Author:** u/Difficult-Cap-7527 | **Upvotes:** 525 | **Comments:** 86 | **Date:** 2025-12-16

**Summary:** Meta announced a new SAM Audio Model that can segment sound from complex audio mixtures using text, visual, and time span prompts, transforming audio processing.

**Key Points:**
- SAM Audio Model can isolate any sound from complex audio mixtures using text, visual, and time span prompts.
- Potential applications include isolating and subtracting unwanted noises in Microsoft Teams meetings.
- The model's ability to pick specific sounds from complex audio is highly praised.
- Model sizes and specifications are available for reference.
- Questions about its applicability to music instruments were raised.

**Discussion Highlights:** The discussion highlights the model's potential for practical applications like noise reduction in meetings and its impressive capability to isolate specific sounds from complex audio. There is also interest in its applicability to music instruments.

---

## 41. [I'm strong enough to admit that this bugs the hell out of me](https://reddit.com/r/LocalLLaMA/comments/1pnfaqo/im_strong_enough_to_admit_that_this_bugs_the_hell/)

**Author:** u/ForsookComparison | **Upvotes:** 1805 | **Comments:** 393 | **Date:** 2025-12-15

**Summary:** The post expresses frustration with a 'perfect workstation' setup, sparking discussions about workstation performance and Mac capabilities.

**Key Points:**
- Post title indicates frustration with workstation setup
- Discussion includes Discord invitation and image link
- Comments debate Mac Mini performance vs. GPU setups
- Consensus that Macs may not be ideal for full GPU workloads

**Discussion Highlights:** The discussion highlights differing opinions on workstation performance, with some users emphasizing GPU capabilities over Mac setups.

---

## 42. [They're finally here (Radeon 9700)](https://reddit.com/r/LocalLLaMA/comments/1pnd5uf/theyre_finally_here_radeon_9700/)

**Author:** u/Zeikos | **Upvotes:** 369 | **Comments:** 69 | **Date:** 2025-12-15

**Summary:** The post announces the arrival of Radeon 9700 GPUs, sparking community interest in benchmarks and performance metrics. Users express nostalgia for the historic GPU name and request detailed testing data.

**Key Points:**
- Radeon 9700 GPUs have arrived
- Community requests benchmarks and performance data
- Nostalgia for the historic Radeon 9700 name
- Interest in noise, heat levels, and training benchmarks

**Discussion Highlights:** The community is highly engaged and eager for performance data, with a consensus on the need for comprehensive benchmarks and comparisons.

---

## 43. [NVIDIA releases Nemotron 3 Nano, a new 30B hybrid reasoning model!](https://reddit.com/r/LocalLLaMA/comments/1pn8upp/nvidia_releases_nemotron_3_nano_a_new_30b_hybrid/)

**Author:** u/Difficult-Cap-7527 | **Upvotes:** 854 | **Comments:** 181 | **Date:** 2025-12-15

**Summary:** NVIDIA has released Nemotron 3 Nano, a 30B hybrid reasoning model with a 1M context window and top performance in SWE-Bench, reasoning, and chat tasks. The model is part of a family of MoE models and has been praised for its speed and efficiency.

**Key Points:**
- Nemotron 3 Nano is a 30B hybrid reasoning model with a 1M context window.
- It excels in SWE-Bench, reasoning, and chat performance.
- The model family includes three sizes: Nano (30B), Medium (100B), and Large (300B).
- Users report impressive speed (110 t/s generation).
- Community discussion highlights the model's efficiency and performance.

**Discussion Highlights:** The community is excited about the model's speed and performance, with some users noting its efficiency and the broader context of the Nemotron 3 family of MoE models.

---

## 44. [New Google model incoming!!!](https://reddit.com/r/LocalLLaMA/comments/1pn37mw/new_google_model_incoming/)

**Author:** u/[deleted] | **Upvotes:** 1275 | **Comments:** 262 | **Date:** 2025-12-15

**Summary:** The Reddit post discusses anticipation and speculation around an upcoming Google model, with users expressing hopes for improvements over previous models like Gemma3-Math and expectations for a multi-modal replacement for existing models.

**Key Points:**
- Anticipation of a new Google model
- Hopes for improvements over previous models like Gemma3-Math
- Expectations for a multi-modal replacement for existing models
- High engagement with 1275 upvotes and 262 comments
- Speculation about the model being Gemma 4

**Discussion Highlights:** The discussion highlights a strong sense of anticipation and hope for significant improvements in the new model, with users expressing specific desires for multi-modal capabilities and better performance compared to previous iterations.

---

## 45. [Aaaand... is gone...](https://reddit.com/r/LocalLLaMA/comments/1pmungj/aaaand_is_gone/)

**Author:** u/HumanDrone8721 | **Upvotes:** 950 | **Comments:** 219 | **Date:** 2025-12-14

**Summary:** The Reddit post discusses the discontinuation of a product or service, sparking a mix of reactions from users. Some see it as a significant event, while others downplay its impact.

**Key Points:**
- The post is gaining popularity and has been featured on Discord.
- Users express concern about storage needs, with one mentioning buying a 2TB SSD.
- There is a humorous reaction with a GIF and a reference to a dystopian future.
- Some users argue that the event is not as significant as others make it out to be.

**Discussion Highlights:** The discussion highlights a divide in opinions, with some users preparing for the change by upgrading their storage, while others dismiss the event as insignificant. The overall tone is a mix of humor, concern, and indifference.

---

## 46. [8x RTX Pro 6000 server complete](https://reddit.com/r/LocalLLaMA/comments/1plwgun/8x_rtx_pro_6000_server_complete/)

**Author:** u/koushd | **Upvotes:** 632 | **Comments:** 266 | **Date:** 2025-12-13

**Summary:** The user detailed their journey of upgrading a GPU server from a single 3080 to an 8x RTX Pro 6000 setup with a Threadripper PRO 9955WX and 384 GB RAM, facing challenges like overheating and power management. The post highlights the iterative process of hardware upgrades and the complexities of managing high-end compute resources.

**Key Points:**
- Upgraded from a single 3080 to 8x RTX Pro 6000 GPUs with a Threadripper PRO 9955WX and 384 GB RAM
- Faced overheating issues and power management challenges
- Used a workaround with two systems in pipeline parallel to manage four GPUs
- Discussion highlights include concerns about the setup's physical stability and power requirements
- Community reactions range from admiration to skepticism about the setup's practicality

**Discussion Highlights:** The discussion includes a mix of admiration for the setup's power and skepticism about its practicality and stability. Top comments highlight concerns about the physical setup, power management, and the overall cost-effectiveness of the build.

---

## 47. [OpenAI's flagship model, ChatGPT-5.2 Thinking, ranks  most censored AI on Sansa benchmark.](https://reddit.com/r/LocalLLaMA/comments/1plnuqu/openais_flagship_model_chatgpt52_thinking_ranks/)

**Author:** u/Difficult-Cap-7527 | **Upvotes:** 626 | **Comments:** 111 | **Date:** 2025-12-13

**Summary:** OpenAI's ChatGPT-5.2 model is ranked as the most censored AI on the Sansa benchmark, with users reporting performance issues and increased censorship compared to previous versions.

**Key Points:**
- ChatGPT-5.2 is ranked as the most censored AI on the Sansa benchmark.
- Users report performance issues, particularly with follow-up questions and research tasks.
- The model denies more requests than previous versions, especially in clinical note evaluations.
- Comparisons with other models like Gemini and Mistral highlight differences in censorship levels.

**Discussion Highlights:** Users express dissatisfaction with ChatGPT-5.2's performance and increased censorship, noting it as worse than previous versions. There is curiosity about the benchmark criteria and comparisons with other models like Gemini and Mistral.

---

## 48. [The new monster-server](https://reddit.com/r/LocalLLaMA/comments/1pl0ojb/the_new_monsterserver/)

**Author:** u/eribob | **Upvotes:** 594 | **Comments:** 125 | **Date:** 2025-12-12

**Summary:** The user shares their upgraded 'Monster server' setup, featuring a Ryzen 3950x CPU, three GPUs (2x RTX 3090 and 1x RTX 4090), 128GB RAM, and extensive storage. They use it to run local LLMs like GPT-OSS-120B for research and coding. The post includes details on hardware configuration, performance, and user experiences.

**Key Points:**
- Upgraded server with Ryzen 3950x, 3 GPUs, and 128GB RAM
- Uses GPT-OSS-120B for research and coding
- 10GB fiber internet for $50/month
- Discussion includes feedback on GPU setup and heat management
- User envies the setup and asks for details on PSU connection

**Discussion Highlights:** Users discuss the hardware setup, with some expressing envy and others providing technical feedback. Key topics include the efficiency of the 3-GPU setup, heat management, and details on the second PSU connection. The post is well-received, with one comment noting its similarity to early 2000s overclocking forums.

---

## 49. [Someone from NVIDIA made a big mistake and uploaded the parent folder of their upcoming model on Hugging Face](https://reddit.com/r/LocalLLaMA/comments/1pkpxss/someone_from_nvidia_made_a_big_mistake_and/)

**Author:** u/Nunki08 | **Upvotes:** 1350 | **Comments:** 158 | **Date:** 2025-12-12

**Summary:** An NVIDIA employee accidentally uploaded the parent folder of their upcoming model on Hugging Face, sparking interest and urgency among users to save the files before potential removal.

**Key Points:**
- Accidental upload of NVIDIA's upcoming model files on Hugging Face
- Urgency among users to save the files before they are taken down
- Mentions of specific models like Nano and 30B-A3B
- Positive sentiment towards the Nemotron lineup
- Concerns about potential censoring of the uploaded content

**Discussion Highlights:** The discussion highlights a sense of urgency to preserve the accidentally uploaded files, with users expressing interest in specific models and concerns about potential censorship. There is also appreciation for the Nemotron lineup and its promising projects.

---

## 50. [Training an LLM only on 1800s London texts - 90GB dataset](https://reddit.com/r/LocalLLaMA/comments/1pkpsee/training_an_llm_only_on_1800s_london_texts_90gb/)

**Author:** u/Remarkable-Trick-177 | **Upvotes:** 724 | **Comments:** 81 | **Date:** 2025-12-12

**Summary:** The post discusses the TimeCapsuleLLM project, which involves training an LLM on a 90GB dataset of 1800-1875 London texts. The author has conducted a bias report and trained a small evaluation model to assess the dataset before scaling up.

**Key Points:**
- The dataset consists of 90GB with 135,000 documents from 1800-1875 London texts.
- A bias report covering temporal, gender/pronoun, and geographic bias has been generated.
- A small evaluation model (300M parameters) was trained on a 15GB subset to evaluate the dataset.
- The example output shows the model's attempt to answer a question about Charles Dickens.
- The community appreciates the detailed work and suggests considering MoE for better compute efficiency.

**Discussion Highlights:** The community shows strong support for the project, with comments highlighting the detailed work and suggesting improvements like using Mixture of Experts (MoE) for better compute efficiency. There is also interest in the inclusion criteria for texts and the progress of the project.

---

