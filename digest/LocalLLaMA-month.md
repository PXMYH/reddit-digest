# r/LocalLLaMA Reading Digest

**Period:** 2026-01-10 to 2026-01-10
**Posts Summarized:** 50
**Total Posts Analyzed:** 50

---

## 1. [I clustered 3 DGX Sparks that NVIDIA said couldn't be clustered yet...took 1500 lines of C to make it work](https://reddit.com/r/LocalLLaMA/comments/1q8hqgd/i_clustered_3_dgx_sparks_that_nvidia_said_couldnt/)

**Author:** u/Ok-Pomegranate1314 | **Upvotes:** 776 | **Comments:** 129 | **Date:** 2026-01-09

**Summary:** The author successfully clustered three NVIDIA DGX Sparks, overcoming networking limitations by developing a custom NCCL plugin. This achievement enables distributed inference across all three nodes at high speeds, despite NVIDIA's official support being limited to two-node clusters.

**Key Points:**
- Author clustered three DGX Sparks, exceeding NVIDIA's official two-node support limit.
- Developed a custom NCCL network plugin (~1500 lines of C) to handle subnet-aware NIC selection and raw RDMA implementation.
- Achieved distributed inference at 8+ GB/s over RDMA across all three nodes.
- The solution addresses challenges like subnet mismatches and RDMA state machine issues.
- The project is open-source and available on GitHub for further exploration.

**Discussion Highlights:** The community praised the technical achievement, noting the complexity of working with NCCL and the potential significance of the solution. Questions were raised about scalability and performance gains, indicating strong interest in the project's broader applicability.

---

## 2. [The reason why RAM has become so expensive](https://reddit.com/r/LocalLLaMA/comments/1q8ckz0/the_reason_why_ram_has_become_so_expensive/)

**Author:** u/InvadersMustLive | **Upvotes:** 3825 | **Comments:** 335 | **Date:** 2026-01-09

**Summary:** The Reddit post discusses the significant increase in RAM prices, with comments suggesting strategic monopolization by certain entities to control future demand and economic viability of competitors.

**Key Points:**
- RAM prices have increased dramatically, with some users reporting up to 10 times the cost compared to the previous year.
- There is speculation about monopolization of RAM resources to control future demand and economic viability of competitors, particularly in the AI datacenter space.
- The price increase is seen as a potential economic strategy rather than a temporary market fluctuation.
- Users have observed a substantial rise in costs for high-capacity DDR5 RAM modules.

**Discussion Highlights:** The discussion highlights concerns about the economic implications of rising RAM prices, with a focus on potential monopolistic practices and the impact on AI datacenters. Users share personal experiences of significant price increases and speculate on the long-term effects on the tech industry.

---

## 3. [DeepSeek V4 Coming](https://reddit.com/r/LocalLLaMA/comments/1q89g1i/deepseek_v4_coming/)

**Author:** u/External_Mood4719 | **Upvotes:** 456 | **Comments:** 97 | **Date:** 2026-01-09

**Summary:** DeepSeek is set to release V4, a next-generation AI model with enhanced code-generation capabilities, outperforming mainstream models like Claude and GPT. The model shows improvements in handling long code prompts and overall reasoning ability.

**Key Points:**
- DeepSeek V4 focuses on strong code-generation capabilities
- Outperforms existing models like Claude and GPT in code generation
- Improved handling of long code prompts and data patterns
- Enhanced logical rigor and reasoning ability
- Users anticipate significant improvements in coding and reasoning tasks

**Discussion Highlights:** Users express excitement and high expectations for DeepSeek V4, noting its potential to disrupt the AI landscape. Many appreciate DeepSeek's cost-effectiveness and performance, with some anticipating rapid iterations in 2026.

---

## 4. [(The Information): DeepSeek To Release Next Flagship AI Model With Strong Coding Ability](https://reddit.com/r/LocalLLaMA/comments/1q88hdc/the_information_deepseek_to_release_next_flagship/)

**Author:** u/Nunki08 | **Upvotes:** 459 | **Comments:** 97 | **Date:** 2026-01-09

**Summary:** DeepSeek is set to release a new flagship AI model with strong coding capabilities, generating excitement and anticipation in the community.

**Key Points:**
- DeepSeek's upcoming model focuses on strong coding ability
- The announcement has generated significant interest and excitement
- Community members are eager for more models and competition in the AI space
- Some users express skepticism about marketing claims
- There is a desire for the model to maintain role-playing capabilities

**Discussion Highlights:** The community shows enthusiasm for DeepSeek's new model, with some expressing excitement for increased competition and others cautioning about typical marketing hyperbole. There is a consensus that more models benefit the ecosystem, but some users are concerned about specific capabilities like role-playing being compromised.

---

## 5. [The NO FAKES Act has a "Fingerprinting" Trap that kills Open Source. We need to lobby for a Safe Harbor.](https://reddit.com/r/LocalLLaMA/comments/1q7qcux/the_no_fakes_act_has_a_fingerprinting_trap_that/)

**Author:** u/PostEasy7183 | **Upvotes:** 584 | **Comments:** 86 | **Date:** 2026-01-08

**Summary:** The NO FAKES Act proposes a 'digital replica right' for voices/likenesses, which could make developers liable for damages if their tools are used to create deepfakes. The post urges the community to lobby for a 'Safe Harbor' provision to protect open-source developers.

**Key Points:**
- The NO FAKES Act targets tools used for creating digital replicas, potentially making developers liable for statutory damages.
- The act lacks Section 230 protection, posing a significant risk to open-source developers hosting AI models.
- The post calls for action, including emailing representatives and calling senators to advocate for a Safe Harbor provision.
- The discussion highlights concerns about the act's impact on innovation and the potential for big tech monopolies.
- Some commenters question whether politicians understand the technical implications of the act.

**Discussion Highlights:** The discussion reflects a consensus that the NO FAKES Act could stifle innovation and favor big tech companies. There is a strong call to action for the community to lobby for amendments to protect open-source developers.

---

## 6. [Jensen Huang saying "AI" 121 times during the NVIDIA CES keynote - cut with one prompt](https://reddit.com/r/LocalLLaMA/comments/1q7d8bj/jensen_huang_saying_ai_121_times_during_the/)

**Author:** u/Prior-Arm-6705 | **Upvotes:** 885 | **Comments:** 140 | **Date:** 2026-01-08

**Summary:** A Reddit user created a compilation video of every instance Jensen Huang said 'AI' during NVIDIA's CES 2025 keynote, totaling 121 times. The process involved using open-source tools to download, parse, and edit the video locally.

**Key Points:**
- Jensen Huang said 'AI' 121 times during the CES 2025 keynote.
- The user employed open-source tools (Dive, yt-dlp-mcp, ffmpeg-mcp-lite) to automate the video compilation.
- The process was entirely local, with no cloud involvement.
- The result was described as 'hypnotic' and summarized the keynote effectively.
- Top comments highlighted the summary's accuracy and humor, as well as Jensen's influence on tech pricing.

**Discussion Highlights:** The discussion consensus was that the video effectively captured the essence of the keynote, with humorous remarks about Jensen's frequent use of 'AI' and his impact on tech pricing. Some users also praised the technical execution of the project.

---

## 7. [16x AMD MI50 32GB at 10 t/s (tg) &amp; 2k t/s (pp) with Deepseek v3.2 (vllm-gfx906)](https://reddit.com/r/LocalLLaMA/comments/1q6n5vl/16x_amd_mi50_32gb_at_10_ts_tg_2k_ts_pp_with/)

**Author:** u/ai-infos | **Upvotes:** 445 | **Comments:** 235 | **Date:** 2026-01-07

**Summary:** The post discusses running Deepseek v3.2 on 16 AMD MI50 GPUs, achieving 10 tokens per second (output) and 2000 tokens per second (input) with a context length of 69,000. The setup is cost-effective and aims to provide a local AGI alternative without high costs. Key points include the hardware specifications, performance metrics, power draw, open-source nature, and future plans. The discussion highlights the efficiency of the setup, with comments praising the power draw as a potential heating solution and expressing awe at the performance. Some users inquire about noise levels and power requirements for home use.

---

## 8. [DeepSeek-R1’s paper was updated 2 days ago, expanding from 22 pages to 86 pages and adding a substantial amount of detail.](https://reddit.com/r/LocalLLaMA/comments/1q6c9wc/deepseekr1s_paper_was_updated_2_days_ago/)

**Author:** u/Nunki08 | **Upvotes:** 635 | **Comments:** 55 | **Date:** 2026-01-07

**Summary:** The Reddit post discusses the recent update to DeepSeek-R1's paper, which expanded from 22 pages to 86 pages, adding significant detail. The discussion includes speculation about new architectures and the potential impact of linear attention research.

**Key Points:**
- DeepSeek-R1's paper was updated from 22 pages to 86 pages.
- The update includes substantial additional detail.
- Discussion highlights potential new architectures and linear attention research.
- Community interest in how architectural improvements scale across different model sizes.
- Original paper lacked implementation specifics, which the update may address.

**Discussion Highlights:** The community is excited about the expanded paper, with speculation about new architectures and the impact of linear attention research. There is also interest in how architectural improvements will perform across different model sizes.

---

## 9. [A 30B Qwen Model Walks Into a Raspberry Pi… and Runs in Real Time](https://reddit.com/r/LocalLLaMA/comments/1q5m2n6/a_30b_qwen_model_walks_into_a_raspberry_pi_and/)

**Author:** u/ali_byteshape | **Upvotes:** 488 | **Comments:** 76 | **Date:** 2026-01-06

**Summary:** The post discusses the successful optimization of the Qwen3-30B-A3B-Instruct-2507 model to run efficiently on small hardware like the Raspberry Pi 5, achieving 8.03 tokens per second while retaining 94.18% of BF16 quality. The optimization focuses on balancing memory usage and performance, particularly noting the quirks of GPU kernel choices. Key points include the model's performance on a Raspberry Pi 5, the prioritization of memory as a budget, the influence of GPU kernel choices on performance, the request for community feedback on different setups, and a user's experience with context settings. The community showed interest in testing the model on different hardware setups and discussed potential improvements like combining the model with exo solutions for cluster computing.

---

## 10. [Performance improvements in llama.cpp over time](https://reddit.com/r/LocalLLaMA/comments/1q5dnyw/performance_improvements_in_llamacpp_over_time/)

**Author:** u/jacek2023 | **Upvotes:** 658 | **Comments:** 82 | **Date:** 2026-01-06

**Summary:** The Reddit post discusses performance improvements in llama.cpp over time, focusing on NVIDIA GPU performance gains and comparisons with other implementations.

**Key Points:**
- Performance gains are highlighted for NVIDIA GPUs.
- References to NVIDIA's blog post on open-source AI tool upgrades.
- Comparisons with ik_llama.cpp show significant progress in token generation speed.
- Prompt processing is noted to be slower but overall progress is praised.

**Discussion Highlights:** The discussion highlights significant progress in token generation speed, with comparisons to other implementations and a focus on NVIDIA GPU performance improvements.

---

## 11. [For the first time in 5 years, Nvidia will not announce any new GPUs at CES — company quashes RTX 50 Super rumors as AI expected to take center stage](https://reddit.com/r/LocalLLaMA/comments/1q4x5e9/for_the_first_time_in_5_years_nvidia_will_not/)

**Author:** u/FullstackSensei | **Upvotes:** 626 | **Comments:** 198 | **Date:** 2026-01-05

**Summary:** Nvidia will not announce new GPUs at CES, focusing instead on AI. The company is facing supply issues with high-end GPUs and may reintroduce older models like the RTX 3060. Consumers express frustration over rising hardware costs and limited upgrade options.

**Key Points:**
- No new GPU announcements from Nvidia at CES
- Limited supply of high-end GPUs (RTX 5070Ti, 5080, 5090)
- Potential reintroduction of the RTX 3060 to meet demand
- Rising costs of DDR5 RAM and storage
- Consumer frustration over corporate greed and limited upgrade paths

**Discussion Highlights:** The discussion highlights widespread frustration with Nvidia's decisions, with many users expressing concerns about corporate greed and the future of local computing. There is a consensus that the high cost of hardware and limited availability of new GPUs are significant barriers to upgrading.

---

## 12. [llama.cpp performance breakthrough for multi-GPU setups](https://reddit.com/r/LocalLLaMA/comments/1q4s8t3/llamacpp_performance_breakthrough_for_multigpu/)

**Author:** u/Holiday-Injury-9397 | **Upvotes:** 557 | **Comments:** 185 | **Date:** 2026-01-05

**Summary:** The ik_llama.cpp project achieved a 3x to 4x performance improvement for multi-GPU setups, enabling cost-effective use of multiple low-cost GPUs for local LLM inference.

**Key Points:**
- ik_llama.cpp introduces a new execution mode (split mode graph) for multi-GPU utilization.
- Performance gains of 3x to 4x compared to previous methods.
- Enables use of multiple low-cost GPUs instead of expensive high-end cards.
- Performance improvements also observed on single GPU and CPU-only setups.
- Comparable performance to other optimized frameworks like vllm.

**Discussion Highlights:** The community highlights significant performance gains even on single GPU/CPU setups, with some users noting bottlenecks in hybrid inference setups. There is consensus on the importance of this breakthrough for cost-effective LLM inference.

---

## 13. [Local LLMs vs breaking news: when extreme reality gets flagged as a hoax - the US/Venezuela event was too far-fetched](https://reddit.com/r/LocalLLaMA/comments/1q31ltd/local_llms_vs_breaking_news_when_extreme_reality/)

**Author:** u/ubrtnk | **Upvotes:** 376 | **Comments:** 194 | **Date:** 2026-01-03

**Summary:** The post discusses the challenges faced by local LLMs in processing extreme breaking news events, such as the US attacking Venezuela. The author shares their experience with different models, highlighting how some models initially dismissed the event as a hoax despite credible sources.

**Key Points:**
- Local LLMs struggled to accept extreme breaking news as real, even with credible sources.
- Different models had varying responses, with larger models performing better.
- The event was so extreme that models initially classified it as misinformation.
- Users shared similar experiences with other extreme events.
- There is a consensus that LLMs have biases and limitations in processing unfamiliar geopolitical events.

**Discussion Highlights:** The discussion highlights the limitations of LLMs in processing extreme and unfamiliar events, with users sharing similar experiences. There is a consensus that LLMs have inherent biases and may struggle with events that deviate significantly from their training data.

---

## 14. [LeCun Says Llama 4 results "were fudged a little bit"](https://reddit.com/r/LocalLLaMA/comments/1q25070/lecun_says_llama_4_results_were_fudged_a_little/)

**Author:** u/MrPecunius | **Upvotes:** 361 | **Comments:** 89 | **Date:** 2026-01-02

**Summary:** Yann LeCun confirmed that Llama 4 benchmarks were manipulated, and Meta's GenAI organization was sidelined, leading to departures and lack of progress. The community expressed disappointment and shared additional resources.

**Key Points:**
- LeCun confirmed Llama 4 benchmark manipulation
- Meta's GenAI organization was sidelined by Zuckerberg
- Many employees left or are leaving Meta
- Community disappointment in Meta's handling of Llama
- Additional resources shared for further reading

**Discussion Highlights:** The discussion highlights disappointment in Meta's mismanagement of Llama, with users sharing additional resources and speculating on organizational failures. There is a consensus that Meta wasted a strategic advantage in generative AI.

---

## 15. [Qwen-Image-2512](https://reddit.com/r/LocalLLaMA/comments/1q094a3/qwenimage2512/)

**Author:** u/Nunki08 | **Upvotes:** 718 | **Comments:** 122 | **Date:** 2025-12-31

**Summary:** The Reddit post announces the release of Qwen-Image-2512, a new model available on multiple platforms with guides and GGUF files. The community has shown positive reception and practical testing results.

**Key Points:**
- Qwen-Image-2512 is a new model with guides and GGUF files available
- The model can be accessed on various platforms like Hugging Face, ModelScope, and GitHub
- Community members have tested the model on low-end hardware with success
- Positive feedback and appreciation from the community
- Creative use cases and examples shared by users

**Discussion Highlights:** The community has shown enthusiasm for the new model, with users testing it on low-end hardware and sharing creative use cases. The overall consensus is positive, with appreciation for the model's accessibility and performance.

---

## 16. [[In the Wild] Reverse-engineered a Snapchat Sextortion Bot: It’s running a raw Llama-7B instance with a 2048 token window.](https://reddit.com/r/LocalLLaMA/comments/1pzwlie/in_the_wild_reverseengineered_a_snapchat/)

**Author:** u/simar-dmg | **Upvotes:** 744 | **Comments:** 108 | **Date:** 2025-12-30

**Summary:** A user reverse-engineered a Snapchat sextortion bot and discovered it was running a raw Llama-7B instance with a 2048 token window. The bot was vulnerable to a persona-adoption jailbreak, revealing its configuration and malicious payload.

**Key Points:**
- The bot used a Llama-7B model with a 2048 token context window and high temperature setting.
- A persona-adoption jailbreak (Grandma Protocol) forced the bot to reveal its environment variables.
- The bot was running on minimal hardware to maximize profit margins.
- The bot eventually revealed a malicious link it was programmed to hide.
- Scammers are shifting to open-source models like Llama-7B to avoid API costs and censorship.

**Discussion Highlights:** The discussion includes skepticism about the accuracy of the bot's revealed information, with some users suggesting it could be entirely hallucinated. Others questioned the commonality of system prompts including environment variables.

---

## 17. [Llama-3.3-8B-Instruct](https://reddit.com/r/LocalLLaMA/comments/1pz7bmv/llama338binstruct/)

**Author:** u/jacek2023 | **Upvotes:** 469 | **Comments:** 78 | **Date:** 2025-12-29

**Summary:** The post discusses the discovery and release of the Llama-3.3-8B-Instruct model, which was previously only available via Meta's API. The author managed to download and share the model in GGUF format.

**Key Points:**
- Llama-3.3-8B-Instruct model was previously only available via Meta's API.
- The author found a way to download the model through finetuning.
- The model is now available in GGUF format.
- Community is verifying the model's authenticity and performance.
- Concerns about the model's configuration, such as 8K max position embeddings.

**Discussion Highlights:** The community is excited about the release and is conducting benchmarks to verify the model's authenticity and performance. There are some concerns about the model's configuration, such as the 8K max position embeddings.

---

## 18. [Tencent just released WeDLM 8B Instruct on Hugging Face](https://reddit.com/r/LocalLLaMA/comments/1pyg4yt/tencent_just_released_wedlm_8b_instruct_on/)

**Author:** u/Difficult-Cap-7527 | **Upvotes:** 425 | **Comments:** 62 | **Date:** 2025-12-29

**Summary:** Tencent released WeDLM 8B Instruct on Hugging Face, a diffusion language model that runs 3-6× faster than vLLM-optimized Qwen3-8B on math reasoning tasks. The release has generated significant interest and discussion in the community.

**Key Points:**
- WeDLM 8B Instruct is a diffusion language model.
- It outperforms Qwen3-8B in speed on math reasoning tasks.
- The model is released under Apache 2.0 license.
- There is a 7B version also available.
- The community shows strong interest in 7-8B models.

**Discussion Highlights:** The community is excited about the performance and potential of diffusion models for LLMs, with many highlighting the impressive benchmark scores and the Apache 2.0 license. There is a consensus on the promising future of 7-8B models.

---

## 19. [NVIDIA Drops Pascal Support On Linux, Causing Chaos On Arch Linux](https://reddit.com/r/LocalLLaMA/comments/1pxad0k/nvidia_drops_pascal_support_on_linux_causing/)

**Author:** u/HumanDrone8721 | **Upvotes:** 440 | **Comments:** 185 | **Date:** 2025-12-27

**Summary:** NVIDIA has dropped Pascal support on Linux, causing issues for Arch Linux users. The move affects Pascal cards like the 24GB P40, leading to concerns among users about hardware compatibility.

**Key Points:**
- NVIDIA's decision impacts Pascal cards, including the 24GB P40
- Arch Linux users are particularly affected due to driver changes
- Users express concerns about future hardware compatibility
- Arch Linux has a history of moving legacy drivers to AUR

**Discussion Highlights:** Users are worried about the implications of NVIDIA's decision, with some noting the historical context of Arch Linux's handling of legacy drivers. The discussion reflects broader concerns about hardware support and compatibility.

---

## 20. [NVIDIA has 72GB VRAM version now](https://reddit.com/r/LocalLLaMA/comments/1pweljh/nvidia_has_72gb_vram_version_now/)

**Author:** u/decentralize999 | **Upvotes:** 463 | **Comments:** 148 | **Date:** 2025-12-26

**Summary:** The Reddit post discusses NVIDIA's new 72GB VRAM version, questioning the pricing and community interest in different VRAM sizes. The discussion includes comparisons of pricing and specifications for various NVIDIA GPUs.

**Key Points:**
- NVIDIA has released a 72GB VRAM version of their GPU.
- Community members express interest in larger VRAM sizes, such as 128GB.
- Pricing comparisons show the RTX 5000 48GB at $5100, RTX 5000 72GB at $7800, and RTX 6000 96GB at $8300.
- Some users suggest waiting for future models like the 5090 with 48GB.
- The price per gigabyte remains consistent across different VRAM sizes.

**Discussion Highlights:** The community shows a strong interest in larger VRAM sizes and debates the value proposition of different NVIDIA GPU models based on their specifications and pricing.

---

## 21. [I wish this GPU VRAM upgrade modification became mainstream and ubiquitous to shred monopoly abuse of NVIDIA](https://reddit.com/r/LocalLLaMA/comments/1pvpkqo/i_wish_this_gpu_vram_upgrade_modification_became/)

**Author:** u/CeFurkan | **Upvotes:** 1016 | **Comments:** 180 | **Date:** 2025-12-25

**Summary:** The post discusses the desire for GPU VRAM upgrade modifications to become mainstream, challenging NVIDIA's monopoly. It highlights that such modifications are already popular in China, with Alibaba offering upgraded GPUs at various price points.

**Key Points:**
- GPU VRAM upgrade modifications are seen as a way to challenge NVIDIA's monopoly.
- These modifications are already mainstream in China, with Alibaba offering upgraded GPUs.
- Prices for upgraded GPUs range from $300 for a 2080Ti 22GB to $4000 for a 5090 96GB.
- Users report successful use of modified GPUs, such as a 4090 with 48GB of memory.
- There is interest and discussion around the cost-effectiveness and availability of these modifications.

**Discussion Highlights:** The discussion highlights the popularity and feasibility of GPU VRAM upgrades, particularly in China. Users share their experiences with modified GPUs and express interest in the cost and availability of these upgrades.

---

## 22. [Why I quit using Ollama](https://reddit.com/r/LocalLLaMA/comments/1pvjpmb/why_i_quit_using_ollama/)

**Author:** u/SoLoFaRaDi | **Upvotes:** 489 | **Comments:** 201 | **Date:** 2025-12-25

**Summary:** The Reddit post discusses the author's decision to stop using Ollama due to a perceived shift away from its original purpose of providing a secure platform for local AI models, citing concerns over recent updates and the introduction of cloud-based models. The discussion highlights a consensus among users favoring alternatives like llama.cpp and LM Studio.

**Key Points:**
- Author's dissatisfaction with Ollama's recent updates and shift towards cloud-based models
- Concerns over privacy implications and bloatware in Ollama
- User preference for alternatives like llama.cpp and LM Studio
- Discussion consensus favoring llama.cpp for its recent improvements
- Mention of LM Studio as a preferred alternative

**Discussion Highlights:** The discussion reflects a general consensus among users that alternatives like llama.cpp and LM Studio are preferable to Ollama due to their focus on local model inference and recent improvements.

---

## 23. [Exclusive: Nvidia buying AI chip startup Groq's assets for about $20 billion in largest deal on record](https://reddit.com/r/LocalLLaMA/comments/1puyq9r/exclusive_nvidia_buying_ai_chip_startup_groqs/)

**Author:** u/fallingdowndizzyvr | **Upvotes:** 665 | **Comments:** 157 | **Date:** 2025-12-24

**Summary:** Nvidia is acquiring AI chip startup Groq's assets for approximately $20 billion, marking the largest deal on record. The acquisition has sparked discussions about market competition and consolidation in the AI industry.

**Key Points:**
- Nvidia's acquisition of Groq's assets for $20 billion
- Potential positive impact on market competition
- Concerns about industry consolidation
- Skepticism about Groq's valuation
- Speculation about regulatory approval and acquihire tactics

**Discussion Highlights:** The discussion highlights a mix of optimism about market competition and concerns about industry consolidation. Some users question Groq's valuation and speculate about regulatory challenges, while others see the deal as a strategic move by Nvidia.

---

## 24. [We asked OSS-120B and GLM 4.6 to play 1,408 Civilization V games from the Stone Age into the future. Here's what we found.](https://reddit.com/r/LocalLLaMA/comments/1pux0yc/we_asked_oss120b_and_glm_46_to_play_1408/)

**Author:** u/vox-deorum | **Upvotes:** 647 | **Comments:** 174 | **Date:** 2025-12-24

**Summary:** Researchers used open-source LLMs (GPT-OSS-120B and GLM-4.6) to play 1,408 full games of Civilization V, finding that LLMs can survive full games and develop distinct playstyles. The models showed slight improvements in best scores but minor decreases in win rates compared to baseline AI.

**Key Points:**
- LLMs can survive full Civilization V games with a hybrid approach, achieving ~97.5% survival rate.
- OSS-120B favored a warmonger playstyle with more Domination victories, while GLM-4.6 played more balanced.
- Both models preferred the Order ideology (~24% more likely) over Freedom.
- Cost per game was ~$0.86 for OSS-120B, with input tokens scaling linearly as the game progresses.
- The study suggests that even smaller models (e.g., OSS-20B) can perform adequately in this setup.

**Discussion Highlights:** The community expressed excitement about the potential for LLMs to enhance gameplay, with interest in integrating them into multiplayer games. Some users speculated about future applications beyond gaming, while others asked about the feasibility of using smaller models.

---

## 25. [AMA With Z.AI, The Lab Behind GLM-4.7](https://reddit.com/r/LocalLLaMA/comments/1ptxm3x/ama_with_zai_the_lab_behind_glm47/)

**Author:** u/zixuanlimit | **Upvotes:** 591 | **Comments:** 415 | **Date:** 2025-12-23

**Summary:** The Reddit post announces an AMA session with Z.AI, the research lab behind GLM-4.7, featuring several team members. The session aims to address community questions and concerns directly.

**Key Points:**
- AMA session with Z.AI team members
- Focus on community questions and concerns
- Top comments highlight questions about future releases, censorship concerns, training challenges, and creative writing instruction sets
- Session duration: 8 AM – 11 AM PST with follow-up over 48 hours

**Discussion Highlights:** The community is particularly interested in future releases, potential censorship issues, training challenges, and the inclusion of creative writing instruction sets.

---

## 26. [DGX Spark: an unpopular opinion](https://reddit.com/r/LocalLLaMA/comments/1ptdtmz/dgx_spark_an_unpopular_opinion/)

**Author:** u/emdblc | **Upvotes:** 744 | **Comments:** 221 | **Date:** 2025-12-22

**Summary:** The author, a doctoral student, shares their positive experience with the DGX Spark, highlighting its benefits for small research groups with limited resources. Despite not being as fast as high-end GPUs like the H100, the DGX Spark's all-in-one design and large memory capacity enable significant research capabilities.

**Key Points:**
- DGX Spark enables small research groups to compete with those having access to high-performance GPUs.
- It is not faster than high-end GPUs like the H100 but offers a large amount of memory in an all-in-one design.
- The device is particularly useful for groups with limited funding and access to computing resources.
- The intended use case of the DGX Spark is for users like the author, despite some community misconceptions.
- Comparisons with other GPUs like the 3090 show that multiple 3090s can outperform a single DGX Spark.

**Discussion Highlights:** The discussion highlights that the DGX Spark is well-suited for its intended demographic, such as small research groups with limited resources. There is a consensus that while it may not match the performance of high-end GPUs, its utility in specific contexts is significant.

---

## 27. [GLM 4.7 is out on HF!](https://reddit.com/r/LocalLLaMA/comments/1pt5heq/glm_47_is_out_on_hf/)

**Author:** u/KvAk_AKPlaysYT | **Upvotes:** 595 | **Comments:** 123 | **Date:** 2025-12-22

**Summary:** The post announces the release of GLM 4.7 on Hugging Face, garnering significant community interest with 595 upvotes and 123 comments. The discussion highlights features like diagrams in reasoning stages and compares it to other models.

**Key Points:**
- GLM 4.7 is now available on Hugging Face
- Post received 595 upvotes and 123 comments
- Community appreciates features like diagrams in reasoning stages
- Comparisons made with other models like Minimax and Gemma 4
- Positive community engagement and recognition for the contributor

**Discussion Highlights:** The community shows enthusiasm for GLM 4.7's features, particularly the inclusion of diagrams in reasoning stages. There is also a notable comparison with other models, indicating a competitive landscape. The post's popularity and the contributor's recognition highlight strong community engagement.

---

## 28. [I made Soprano-80M: Stream ultra-realistic TTS in &lt;15ms, up to 2000x realtime, and &lt;1 GB VRAM, released under Apache 2.0!](https://reddit.com/r/LocalLLaMA/comments/1pt3sco/i_made_soprano80m_stream_ultrarealistic_tts_in/)

**Author:** u/eugenekwek | **Upvotes:** 638 | **Comments:** 104 | **Date:** 2025-12-22

**Summary:** Eugene introduced Soprano-80M, a state-of-the-art TTS model optimized for ultra-low latency and high-speed audio generation, achieving <15ms latency and up to 2000x realtime performance. The model uses a 32 kHz sample rate and a vocoder-based decoder for superior audio quality and speed.

**Key Points:**
- Soprano-80M achieves <15ms latency and up to 2000x realtime performance.
- Uses a 32 kHz sample rate for clearer audio quality.
- Employs a vocoder-based decoder for faster audio generation.
- Can generate a 10-hour audiobook in under 20 seconds.
- Released under Apache 2.0 license.

**Discussion Highlights:** Users praised the model's speed and performance, with one user noting a brief delay before rapid audio generation. Questions were raised about hardware requirements and the availability of finetuning code.

---

## 29. [major open-source releases this year](https://reddit.com/r/LocalLLaMA/comments/1pstlas/major_opensource_releases_this_year/)

**Author:** u/sahilypatel | **Upvotes:** 692 | **Comments:** 100 | **Date:** 2025-12-22

**Summary:** The Reddit post highlights major open-source releases this year, with discussions focusing on the dominance of non-US companies, particularly China, in the open-source space, and high expectations for future models like DeepSeek.

**Key Points:**
- Post recognized for popularity and author given special flair
- Only 3 US companies in the list, with China dominating open-source
- High expectations for DeepSeek to outperform closed-source models
- Discussion about Mistral's performance in small model sizes

**Discussion Highlights:** The discussion highlights a consensus on the growing influence of non-US companies in open-source, particularly China, and optimism about the potential of upcoming models like DeepSeek to surpass closed-source alternatives.

---

## 30. [llama.cpp appreciation post](https://reddit.com/r/LocalLLaMA/comments/1psbx2q/llamacpp_appreciation_post/)

**Author:** u/hackiv | **Upvotes:** 1685 | **Comments:** 153 | **Date:** 2025-12-21

**Summary:** The Reddit post appreciates llama.cpp for its performance, with users sharing their positive experiences and performance metrics. The discussion highlights the superior speed and efficiency of llama.cpp compared to other tools like Ollama.

**Key Points:**
- The post is an appreciation for llama.cpp
- Users report significant performance improvements with llama.cpp
- Comparisons with other tools like Ollama are discussed
- Specific performance metrics are shared, such as 23t/s on certain hardware

**Discussion Highlights:** The discussion emphasizes the performance benefits of llama.cpp, with users sharing their experiences and metrics. There is a consensus on the superiority of llama.cpp in terms of speed and efficiency.

---

## 31. [Xiaomi’s MiMo-V2-Flash (309B model) jumping straight to the big leagues](https://reddit.com/r/LocalLLaMA/comments/1prjzoh/xiaomis_mimov2flash_309b_model_jumping_straight/)

**Author:** u/98Saman | **Upvotes:** 431 | **Comments:** 98 | **Date:** 2025-12-20

**Summary:** Xiaomi's MiMo-V2-Flash (309B model) is gaining attention for its impressive performance, benchmarking similarly to DS 3.2 with half the parameters and higher speed. The community is discussing its capabilities and potential availability.

**Key Points:**
- MiMo-V2-Flash benchmarks similarly to DS 3.2 with half the parameters
- The model is noted for its high speed
- Community interest in model availability and performance comparisons
- Discussion about the Artificial Analysis Index and its reliability

**Discussion Highlights:** The community is impressed with the model's performance and speed, with discussions focusing on its benchmark results and potential availability. There is also debate about the reliability of the Artificial Analysis Index as a performance metric.

---

## 32. [Qwen released Qwen-Image-Layered on Hugging face.](https://reddit.com/r/LocalLLaMA/comments/1pqoi6i/qwen_released_qwenimagelayered_on_hugging_face/)

**Author:** u/Difficult-Cap-7527 | **Upvotes:** 635 | **Comments:** 70 | **Date:** 2025-12-19

**Summary:** Qwen has released Qwen-Image-Layered on Hugging Face, featuring advanced image layering capabilities with Photoshop-grade quality, physically isolated RGBA layers, and infinite decomposition.

**Key Points:**
- Photoshop-grade layering with true native editability
- Physically isolated RGBA layers
- Prompt-controlled structure for specifying layers
- Infinite decomposition for detailed layering
- Core model size is 40GB unquantized

**Discussion Highlights:** The community is excited about the release, with comments highlighting the rapid pace of advancements and inquiries about RAM/VRAM requirements. Some users expressed concern about the large model size (40GB unquantized).

---

## 33. [Realist meme of the year!](https://reddit.com/r/LocalLLaMA/comments/1pqegcr/realist_meme_of_the_year/)

**Author:** u/Slight_Tone_2188 | **Upvotes:** 2129 | **Comments:** 125 | **Date:** 2025-12-19

**Summary:** The Reddit post titled 'Realist meme of the year!' gained significant attention with 2129 upvotes and 125 comments. The discussion revolves around various topics including the need for a cure for cancer, humorous suggestions like downloading more RAM, and debates about the responsibility of AI companies versus hardware manufacturers.

**Key Points:**
- The post received a special flair for its contribution.
- A prominent comment highlights the urgency for a cure for cancer.
- Humorous suggestions like downloading more RAM were made.
- Discussion about the responsibility of AI companies versus hardware manufacturers.
- The post was featured on the subreddit's Discord server.

**Discussion Highlights:** The discussion highlights a mix of serious concerns, such as the need for medical advancements, and humorous remarks. There is also a notable debate about the roles of different companies in the tech industry, with some users pointing fingers at hardware manufacturers for current limitations.

---

## 34. [Kimi K2 Thinking at 28.3 t/s on 4x Mac Studio cluster](https://reddit.com/r/LocalLLaMA/comments/1pq2ry0/kimi_k2_thinking_at_283_ts_on_4x_mac_studio/)

**Author:** u/geerlingguy | **Upvotes:** 542 | **Comments:** 142 | **Date:** 2025-12-18

**Summary:** The post discusses performance testing of Kimi K2 on a cluster of 4x Mac Studios using RDMA Tensor settings, highlighting the challenges in benchmarking and the potential for future improvements with new Apple Silicon chips.

**Key Points:**
- Testing Kimi K2 on a 4x Mac Studio cluster with RDMA Tensor settings
- Challenges in benchmarking due to lack of tools like llama-bench in Exo
- Potential for significant improvements with new Apple Silicon ultra chips featuring MATMUL instructions
- Community appreciation for the testing and sharing of results
- Mention of additional data and resources in a GitHub issue and blog post

**Discussion Highlights:** The discussion highlights community interest in the performance results and appreciation for the testing efforts. There is also anticipation for future improvements with new hardware.

---

## 35. [Google's Gemma models family](https://reddit.com/r/LocalLLaMA/comments/1ppun3v/googles_gemma_models_family/)

**Author:** u/jacek2023 | **Upvotes:** 491 | **Comments:** 119 | **Date:** 2025-12-18

**Summary:** The Reddit post discusses Google's Gemma models family, highlighting the introduction of FunctionGemma and community reactions.

**Key Points:**
- Introduction of FunctionGemma for fine-tuning
- Community excitement and humor about the announcement
- Technical details and model count speculation

**Discussion Highlights:** The community shows enthusiasm for FunctionGemma, with some humorous remarks about the announcement becoming reality. Technical discussions include model counts and potential new releases.

---

## 36. [Hey, LocalLLaMa. We need to talk...](https://reddit.com/r/LocalLLaMA/comments/1pp6jhq/hey_localllama_we_need_to_talk/)

**Author:** u/Eisenstein | **Upvotes:** 424 | **Comments:** 142 | **Date:** 2025-12-17

**Summary:** The post emphasizes the importance of engaging with and providing feedback to contributors in the r/LocalLLaMA community, highlighting that recognition and constructive criticism are crucial for sustaining open-source projects. Key points include encouraging community members to engage with smaller posts, stressing the importance of upvoting and recognizing contributions, and highlighting the need for constructive criticism. The discussion reveals mixed opinions on the quality of some projects, with concerns about AI-generated content, and some users appreciating the sentiment but being skeptical about the quality of certain contributions. The discussion highlights a divide in the community regarding the quality of contributions, with some users appreciating the call for engagement and others expressing skepticism about the value of certain projects.

---

## 37. [Apple introduces SHARP, a model that generates a photorealistic 3D Gaussian representation from a single image in seconds.](https://reddit.com/r/LocalLLaMA/comments/1poy0lb/apple_introduces_sharp_a_model_that_generates_a/)

**Author:** u/themixtergames | **Upvotes:** 1217 | **Comments:** 138 | **Date:** 2025-12-17

**Summary:** Apple has introduced SHARP, a model capable of generating photorealistic 3D Gaussian representations from a single image in seconds. The model is showcased with examples rendered in real-time on Apple Vision Pro and generated on a MacBook Pro M1 Max.

**Key Points:**
- SHARP generates 3D Gaussian representations from a single image quickly.
- Examples were rendered in real-time on Apple Vision Pro.
- The model was generated in 5–10 seconds on a MacBook Pro M1 Max.
- The post received significant engagement with 1217 upvotes and 138 comments.
- Top comments include discussions about GPU requirements, potential applications, and comparisons to cyberpunk's braindance.

**Discussion Highlights:** The discussion highlights include excitement about the technology's speed and real-time rendering capabilities, as well as humorous and speculative comments about its potential applications and limitations.

---

## 38. [Microsoft's TRELLIS 2-4B, An Open-Source Image-to-3D Model](https://reddit.com/r/LocalLLaMA/comments/1porpwd/microsofts_trellis_24b_an_opensource_imageto3d/)

**Author:** u/Dear-Success-1441 | **Upvotes:** 1197 | **Comments:** 130 | **Date:** 2025-12-17

**Summary:** Microsoft's TRELLIS 2-4B is an open-source image-to-3D model with 4 billion parameters, converting single images into 3D assets. The community discussion highlights mixed feedback on its practical utility and suggests potential applications in gaming and design.

**Key Points:**
- Model Type: Flow-Matching Transformers with Sparse Voxel based 3D VAE
- Parameters: 4 Billion
- Input: Single Image, Output: 3D Asset
- Community feedback varies, with some users finding it useful and others questioning its practicality
- Potential applications include gaming and detailed world maps

**Discussion Highlights:** The discussion includes mixed reviews on the model's practicality, with some users suggesting improvements like using multiple images for better results. There is also enthusiasm about potential applications in gaming and design.

---

## 39. [8x Radeon 7900 XTX Build for Longer Context Local Inference - Performance Results &amp; Build Details](https://reddit.com/r/LocalLLaMA/comments/1pogwb6/8x_radeon_7900_xtx_build_for_longer_context_local/)

**Author:** u/Beautiful_Trust_8151 | **Upvotes:** 738 | **Comments:** 220 | **Date:** 2025-12-16

**Summary:** The post details an 8x Radeon 7900 XTX GPU build for local AI inference, achieving 192 GB VRAM and stable performance with up to 200+ tokens per second during prompt processing. The setup costs around $6-7k and offers flexibility and long-context capability for specific work use cases.

**Key Points:**
- 8x AMD Radeon 7900 XTX GPUs with 192 GB VRAM total, paired with an Intel Core i7-14700F and 192 GB system RAM.
- Performance: 437 tokens/sec (empty context) and 27 tokens/sec (generation), dropping to 200+ tokens/sec and 16 tokens/sec at 19k context.
- Total build cost: ~$6-7k, with a $500 PCIe Gen4 x16 switch for GPU connectivity.
- Advantages: Upgradability, customizability, and genuine long-context capability.
- Discussion highlights: Appreciation for the build's budget efficiency and performance potential with models like Qwen3-235B-A22B.

**Discussion Highlights:** The discussion highlights appreciation for the build's cost efficiency and performance potential, with suggestions for testing other models like Qwen3-235B-A22B. Some users compare it favorably to professional-grade GPUs like the RTX Pro 6000, noting its challenges in setup and power consumption.

---

## 40. [Meta announced a new SAM Audio Model for audio editing that can segment sound from complex audio mixtures using text, visual, and time span prompts.](https://reddit.com/r/LocalLLaMA/comments/1po7i0c/meta_announced_a_new_sam_audio_model_for_audio/)

**Author:** u/Difficult-Cap-7527 | **Upvotes:** 525 | **Comments:** 86 | **Date:** 2025-12-16

**Summary:** Meta has introduced a new SAM Audio Model that revolutionizes audio editing by allowing users to isolate specific sounds from complex audio mixtures using text, visual, and time span prompts.

**Key Points:**
- SAM Audio Model enables easy isolation of sounds from complex audio mixtures.
- The model uses text, visual, and time span prompts for audio segmentation.
- Potential applications include filtering out unwanted noises in virtual meetings.
- The model's effectiveness in isolating sounds from videos is highlighted as impressive.
- Questions about the model's applicability to musical instruments were raised.

**Discussion Highlights:** The discussion highlights the potential of the SAM Audio Model in practical applications like virtual meetings and its impressive capability to isolate sounds from videos. There is also curiosity about its applicability to musical instruments.

---

## 41. [I'm strong enough to admit that this bugs the hell out of me](https://reddit.com/r/LocalLLaMA/comments/1pnfaqo/im_strong_enough_to_admit_that_this_bugs_the_hell/)

**Author:** u/ForsookComparison | **Upvotes:** 1812 | **Comments:** 393 | **Date:** 2025-12-15

**Summary:** The post expresses frustration about a 'perfect workstation' setup, with discussions focusing on performance comparisons between Mac and GPU-based systems.

**Key Points:**
- The post title indicates annoyance with a specific issue.
- An image link is central to the discussion, likely depicting a workstation.
- Comments debate the effectiveness of Mac vs. GPU setups.
- The discussion highlights differing opinions on workstation performance.

**Discussion Highlights:** The discussion centers around the performance of different workstation setups, with some users favoring Mac systems and others advocating for full GPU setups. The image linked in the comments appears to be a focal point of the debate.

---

## 42. [NVIDIA releases Nemotron 3 Nano, a new 30B hybrid reasoning model!](https://reddit.com/r/LocalLLaMA/comments/1pn8upp/nvidia_releases_nemotron_3_nano_a_new_30b_hybrid/)

**Author:** u/Difficult-Cap-7527 | **Upvotes:** 851 | **Comments:** 181 | **Date:** 2025-12-15

**Summary:** NVIDIA has released Nemotron 3 Nano, a 30B hybrid reasoning model with a 1M context window, claiming best-in-class performance for SWE-Bench, reasoning, and chat. The model is available in GGUF format and is noted for its speed, achieving 110 tokens per second in local generation.

**Key Points:**
- Nemotron 3 Nano is a 30B hybrid reasoning model with a 1M context window.
- It claims best-in-class performance for SWE-Bench, reasoning, and chat.
- The model is available in GGUF format and is noted for its speed (110 t/s generation).
- The Nemotron 3 family includes three sizes of MoE models.
- Community reactions highlight the model's speed and the surprising 'nano' designation for a 30B model.

**Discussion Highlights:** The community discussion highlights the model's impressive speed (110 t/s generation) and clarifies that the Nemotron 3 family includes three sizes of MoE models. There is also some humor and surprise about the 'nano' designation for a 30B model.

---

## 43. [New Google model incoming!!!](https://reddit.com/r/LocalLLaMA/comments/1pn37mw/new_google_model_incoming/)

**Author:** u/[deleted] | **Upvotes:** 1274 | **Comments:** 262 | **Date:** 2025-12-15

**Summary:** The Reddit post discusses anticipation and speculation around an upcoming new Google model, with links to a tweet and Hugging Face page. The community expresses hope for improvements over previous models like Gemma3-Math and potential multi-modal capabilities.

**Key Points:**
- Anticipation of a new Google model
- Hope for improvements over previous models like Gemma3-Math
- Desire for multi-modal capabilities
- Community excitement and hype
- Speculation about potential model names like Gemma 4

**Discussion Highlights:** The discussion highlights a strong sense of anticipation and hope within the community for a significant improvement in Google's upcoming model. There is a consensus on the desire for multi-modal capabilities and better performance compared to previous iterations.

---

## 44. [Aaaand... is gone...](https://reddit.com/r/LocalLLaMA/comments/1pmungj/aaaand_is_gone/)

**Author:** u/HumanDrone8721 | **Upvotes:** 947 | **Comments:** 219 | **Date:** 2025-12-14

**Summary:** The Reddit post titled 'Aaaand... is gone...' discusses the apparent discontinuation or reduced relevance of SATA drives, sparking a conversation about storage solutions and their future.

**Key Points:**
- The post is a link with no text content, focusing on the title.
- Comments suggest the topic is about SATA drives and their availability.
- One comment jokes about buying more storage, indicating a lighthearted tone.
- Another comment dismisses the topic as a 'nothingburger,' suggesting it's not a major issue.
- The discussion highlights differing opinions on the significance of the topic.

**Discussion Highlights:** The discussion is mixed, with some users seeing the topic as significant enough to warrant action (e.g., buying more storage), while others dismiss it as irrelevant or overhyped. The consensus is not clear-cut, but the conversation provides insights into community perspectives on storage technology.

---

## 45. [8x RTX Pro 6000 server complete](https://reddit.com/r/LocalLLaMA/comments/1plwgun/8x_rtx_pro_6000_server_complete/)

**Author:** u/koushd | **Upvotes:** 633 | **Comments:** 266 | **Date:** 2025-12-13

**Summary:** The Reddit post details the author's journey of upgrading their GPU server over several years, culminating in a powerful setup with 8x RTX Pro 6000 GPUs, a Threadripper PRO 9955WX CPU, and 384 GB RAM. The post highlights challenges faced during upgrades, including heat management and hardware compatibility issues.

**Key Points:**
- The server setup includes 8x RTX Pro 6000 GPUs, providing 768 GB VRAM.
- The author faced significant challenges with heat management and hardware compatibility during upgrades.
- The final setup uses a Threadripper PRO 9955WX CPU and 384 GB RAM.
- The post received significant engagement, with 633 upvotes and 266 comments.
- Top comments include praise for the setup and concerns about the hardware's physical setup and power requirements.

**Discussion Highlights:** The discussion highlights a mix of admiration for the powerful setup and concerns about the practicality and safety of the hardware configuration. Some commenters praised the setup as 'epyc,' while others criticized the use of a 'shitty aluminum frame' and the potential risks of such a high-power setup.

---

## 46. [OpenAI's flagship model, ChatGPT-5.2 Thinking, ranks  most censored AI on Sansa benchmark.](https://reddit.com/r/LocalLLaMA/comments/1plnuqu/openais_flagship_model_chatgpt52_thinking_ranks/)

**Author:** u/Difficult-Cap-7527 | **Upvotes:** 628 | **Comments:** 111 | **Date:** 2025-12-13

**Summary:** The Reddit post discusses OpenAI's ChatGPT-5.2 model being ranked as the most censored AI on the Sansa benchmark, with users noting issues in follow-up questions and research capabilities compared to previous versions.

**Key Points:**
- ChatGPT-5.2 is ranked as the most censored AI on the Sansa benchmark.
- Users report issues with follow-up questions and research capabilities.
- Difficulties in generating clinical notes for QA model evaluation.
- Curiosity about the testing criteria given Grok's low ranking.
- Observations about Gemini being less censored than other models.

**Discussion Highlights:** Users express dissatisfaction with ChatGPT-5.2's performance in follow-up questions and research tasks, noting a decline compared to previous versions. There is also discussion about the model's censorship levels and the criteria used for benchmarking.

---

## 47. [The new monster-server](https://reddit.com/r/LocalLLaMA/comments/1pl0ojb/the_new_monsterserver/)

**Author:** u/eribob | **Upvotes:** 589 | **Comments:** 125 | **Date:** 2025-12-12

**Summary:** The Reddit post describes a powerful home server setup called the 'Monster server,' built with high-end GPUs and a Ryzen 3950x CPU, designed for running local LLMs and homelab tasks. The user expresses satisfaction with the performance and cost-effectiveness of the build.

**Key Points:**
- The server uses a Ryzen 3950x CPU and multiple GPUs, including RTX 3090s and an RTX 4090.
- The setup includes 128GB of RAM, 10GBe networking, and a mix of NVMe and HDD storage.
- The user runs a 120B parameter LLM entirely in VRAM with high performance.
- Community feedback includes nostalgia for early 2000s overclocking forums and technical discussions about GPU configurations.
- Some users question the efficiency of a 3-GPU setup compared to 2 or 4 GPUs.

**Discussion Highlights:** The discussion highlights a mix of admiration for the build, technical feedback on GPU configurations, and curiosity about the user's location due to their affordable 10GBe internet. Some users also request more details about the second PSU setup.

---

## 48. [Someone from NVIDIA made a big mistake and uploaded the parent folder of their upcoming model on Hugging Face](https://reddit.com/r/LocalLLaMA/comments/1pkpxss/someone_from_nvidia_made_a_big_mistake_and/)

**Author:** u/Nunki08 | **Upvotes:** 1342 | **Comments:** 158 | **Date:** 2025-12-12

**Summary:** An NVIDIA employee accidentally uploaded the parent folder of an upcoming model on Hugging Face, sparking interest and urgency among users to save the content before potential removal.

**Key Points:**
- Accidental upload of NVIDIA's upcoming model parent folder on Hugging Face
- Users urged to save content before potential takedown
- Mentions of specific models like Nano and 30B-A3B
- Positive sentiment towards Nemotron lineup
- Concerns about censorship and content removal

**Discussion Highlights:** The discussion highlights a sense of urgency to preserve the accidentally uploaded content, with users expressing interest in specific models and concerns about potential censorship. There is also appreciation for NVIDIA's Nemotron projects.

---

## 49. [Training an LLM only on 1800s London texts - 90GB dataset](https://reddit.com/r/LocalLLaMA/comments/1pkpsee/training_an_llm_only_on_1800s_london_texts_90gb/)

**Author:** u/Remarkable-Trick-177 | **Upvotes:** 729 | **Comments:** 81 | **Date:** 2025-12-12

**Summary:** The post discusses the TimeCapsuleLLM project, which involves training an LLM on a 90GB dataset of 1800s London texts. The author has conducted a bias report and trained a small evaluation model to assess the dataset before scaling up.

**Key Points:**
- 90GB dataset with 135,000 documents from 1800-1875 London texts
- Bias report covering temporal, gender/pronoun, and geographic bias
- Evaluation model trained on a 15GB subset (300M parameters, 10K steps)
- Community appreciation and suggestions for improvement
- Discussion on dataset inclusion criteria and model architecture

**Discussion Highlights:** The community shows strong support for the project, with suggestions for dataset refinement and model architecture improvements. There is interest in the project's progress and potential applications.

---

## 50. [What is the smartest uncensored nsfw LLM you can run with 12GB VRAM and 32GB RAM?](https://reddit.com/r/LocalLLaMA/comments/1pkidf6/what_is_the_smartest_uncensored_nsfw_llm_you_can/)

**Author:** u/Dex921 | **Upvotes:** 408 | **Comments:** 135 | **Date:** 2025-12-11

**Summary:** The post asks for recommendations on the smartest uncensored NSFW LLM that can be run with 12GB VRAM and 32GB RAM, including both local and closed-source options. Users discuss various models and their experiences.

**Key Points:**
- The post allows for both local and closed-source LLM recommendations.
- TheDrummer_Cydonia-24B is mentioned as a truly uncensored local model.
- Qwen3 32B is noted for good NSFW roleplay results on a laptop with RTX3070 and 32GB RAM.
- Users suggest checking u/TheLocalDrummer posts and r/SillyTavernAI for more information.
- The discussion highlights a focus on uncensored and NSFW capabilities.

**Discussion Highlights:** The discussion primarily focuses on uncensored and NSFW capabilities of various LLMs. TheDrummer_Cydonia-24B and Qwen3 32B are highlighted as viable options for local use. Users also recommend checking specific posts and threads for more detailed information.

---

