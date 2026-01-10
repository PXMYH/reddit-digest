# r/LocalLLaMA Reading Digest

**Period:** 2026-01-09 to 2026-01-09
**Posts Summarized:** 44
**Total Posts Analyzed:** 44

---

## 1. [I clustered 3 DGX Sparks that NVIDIA said couldn't be clustered yet...took 1500 lines of C to make it work](https://reddit.com/r/LocalLLaMA/comments/1q8hqgd/i_clustered_3_dgx_sparks_that_nvidia_said_couldnt/)

**Author:** u/Ok-Pomegranate1314 | **Upvotes:** 430 | **Comments:** 83 | **Date:** 2026-01-09

**Summary:** The author successfully clustered three NVIDIA DGX Sparks, overcoming networking limitations by writing a custom NCCL plugin. This achievement allows distributed inference across all three nodes at high speeds, despite NVIDIA's official support only covering two-node clusters.

**Key Points:**
- Author clustered three DGX Sparks, exceeding NVIDIA's official support for two-node clusters.
- Developed a custom NCCL network plugin to handle subnet-aware NIC selection and raw RDMA implementation.
- Achieved distributed inference at 8+ GB/s over RDMA, showcasing significant performance.
- The solution involved extensive low-level debugging and custom protocol implementation.
- Community reaction highlights the technical difficulty and potential impact of the achievement.

**Discussion Highlights:** The community praised the technical complexity of the project, noting that NCCL is typically only used in large training setups. There was interest in the scalability and performance improvements of the solution, with questions about its broader applicability.

---

## 2. [RTX Blackwell Pro 6000 wholesale pricing has dropped by $150-200](https://reddit.com/r/LocalLLaMA/comments/1q8fagh/rtx_blackwell_pro_6000_wholesale_pricing_has/)

**Author:** u/TastesLikeOwlbear | **Upvotes:** 154 | **Comments:** 62 | **Date:** 2026-01-09

**Summary:** The Reddit post discusses a recent drop in wholesale pricing for the RTX Blackwell Pro 6000 cards by $150-200, highlighting a significant price difference compared to the 72GiB 5000 Pro. The author shares insider information to help the community make informed purchasing decisions. Key points include the price drop, comparison with the 5000 Pro, and community reactions expressing gratitude and discussions about potential upgrades.

---

## 3. [The reason why RAM has become so expensive](https://reddit.com/r/LocalLLaMA/comments/1q8ckz0/the_reason_why_ram_has_become_so_expensive/)

**Author:** u/InvadersMustLive | **Upvotes:** 2621 | **Comments:** 256 | **Date:** 2026-01-09

**Summary:** The Reddit post discusses the significant increase in RAM prices, with users suggesting that monopolization of key resources by companies like OpenAI may be driving up costs, making it economically unviable for competitors, particularly in China. The discussion highlights concerns about market manipulation and the potential long-term impact on AI development.

**Key Points:**
- RAM prices have increased dramatically, with some users reporting a 10x rise compared to last year.
- OpenAI is accused of monopolizing RAM to create future demand and stifle competition.
- The price surge is making AI data centers, especially in China, economically unviable.
- Users express skepticism about the sustainability of the current pricing trend.

**Discussion Highlights:** The discussion centers around the economic implications of rising RAM prices, with a consensus that monopolistic practices may be driving the trend. Users share personal experiences of price increases and debate the long-term viability of AI development under these conditions.

---

## 4. [DeepSeek V4 Coming](https://reddit.com/r/LocalLLaMA/comments/1q89g1i/deepseek_v4_coming/)

**Author:** u/External_Mood4719 | **Upvotes:** 341 | **Comments:** 75 | **Date:** 2026-01-09

**Summary:** DeepSeek is expected to release V4, a next-generation AI model with strong code-generation capabilities, outperforming mainstream models like Claude and GPT. The model shows improvements in handling long code prompts and reasoning ability.

**Key Points:**
- DeepSeek V4 focuses on strong code-generation capabilities.
- V4 outperforms existing models like Claude and GPT in code generation.
- Improved handling of long code prompts and data pattern understanding.
- Users anticipate better reasoning and reliability in complex tasks.
- Community discussions highlight excitement and expectations for the new model.

**Discussion Highlights:** Users express enthusiasm for DeepSeek V4, with some noting its potential to disrupt the AI landscape. There is consensus on the model's expected improvements in coding performance and reasoning, though some speculate on the timeline and extent of advancements.

---

## 5. [(The Information): DeepSeek To Release Next Flagship AI Model With Strong Coding Ability](https://reddit.com/r/LocalLLaMA/comments/1q88hdc/the_information_deepseek_to_release_next_flagship/)

**Author:** u/Nunki08 | **Upvotes:** 381 | **Comments:** 88 | **Date:** 2026-01-09

**Summary:** DeepSeek is set to release a new flagship AI model with strong coding capabilities, generating excitement and anticipation in the community.

**Key Points:**
- DeepSeek's upcoming model focuses on strong coding abilities
- The announcement has generated significant interest and excitement
- Community members are looking forward to more details and benchmarks
- There is a mix of enthusiasm and skepticism about the model's performance claims
- The release is seen as a positive development for the AI community

**Discussion Highlights:** The community is largely excited about the new model, with some expressing enthusiasm for more competition in the AI space. There is also a degree of skepticism regarding the performance claims, with users hoping for transparent benchmarks and details.

---

## 6. [Big tech companies, now "DRAM beggars," are staying in Pangyo and Pyeongtaek, demanding "give us some supplies."](https://reddit.com/r/LocalLLaMA/comments/1q84u82/big_tech_companies_now_dram_beggars_are_staying/)

**Author:** u/FullstackSensei | **Upvotes:** 265 | **Comments:** 87 | **Date:** 2026-01-09

**Summary:** The Reddit post discusses a significant surge in DRAM prices, with major tech companies scrambling to secure supplies amid a shortage expected to continue. Prices for DDR4 have risen sharply, and further increases are anticipated.

**Key Points:**
- DRAM prices are rising sharply, with DDR4 prices increasing from $1.40 to $9.30 per GB in a year.
- Major tech companies are competing fiercely to secure DRAM supplies, leading to a shortage.
- The shortage is expected to continue, with prices potentially rising by another 50-60%.
- The demand for DRAM is spreading beyond HBM to server DRAM due to the AI craze.
- Users are expressing shock and making humorous comments about the situation.

**Discussion Highlights:** Users are shocked by the price increases, with some making humorous remarks about auctioning old RAM sticks. There is also confusion about downvoting patterns on Reddit.

---

## 7. [OK I get it, now I love llama.cpp](https://reddit.com/r/LocalLLaMA/comments/1q7uuxo/ok_i_get_it_now_i_love_llamacpp/)

**Author:** u/vulcan4d | **Upvotes:** 224 | **Comments:** 39 | **Date:** 2026-01-08

**Summary:** The user switched from Ollama to llama.cpp for better performance and control, achieving significant speed improvements through tuning. They shared their hardware setup and optimized commands, highlighting the learning curve and benefits of llama.cpp.

**Key Points:**
- User transitioned from Ollama to llama.cpp for advanced usage and performance tuning.
- Hardware setup includes a 3060 GPU and three P102-100 GPUs with 42GB VRAM and 96GB system RAM.
- Performance tuning with specific commands resulted in a speed increase from 11t/s to 21t/s.
- Discussion includes suggestions for further optimization and critiques of the commands used.
- Alternative tools like Koboldcpp and llama-swap are mentioned in the comments.

**Discussion Highlights:** The discussion highlights suggestions for increasing batch and ubatch sizes for better performance, critiques of the commands used, and mentions of alternative tools like Koboldcpp. There is also a debate about the use of specific settings and the necessity of sudo commands.

---

## 8. [The NO FAKES Act has a "Fingerprinting" Trap that kills Open Source. We need to lobby for a Safe Harbor.](https://reddit.com/r/LocalLLaMA/comments/1q7qcux/the_no_fakes_act_has_a_fingerprinting_trap_that/)

**Author:** u/PostEasy7183 | **Upvotes:** 564 | **Comments:** 86 | **Date:** 2026-01-08

**Summary:** The Reddit post discusses the NO FAKES Act, highlighting its potential negative impact on open-source AI development by imposing liability on developers for tools used to create digital replicas. The author urges the community to lobby for a Safe Harbor provision to protect open-source developers.

**Key Points:**
- The NO FAKES Act creates a 'digital replica right' that could make developers liable for tools used to create replicas.
- Developers hosting TTS or voice-conversion models could face statutory damages if their tools are misused.
- The post calls for a 'Safe Harbor' provision to protect open-source developers.
- The community is encouraged to contact their representatives to oppose the bill unless amended.
- There is concern that the bill could lead to a monopoly by Big Tech companies.

**Discussion Highlights:** The discussion highlights concerns about the bill's potential to stifle innovation and the need for a Safe Harbor provision. Some commenters suggest that the bill is part of a larger effort by Big Tech to control the AI landscape. Others question whether politicians understand the technical implications of the bill.

---

## 9. [Z.ai  (the AI lab behind GLM) has officially IPO'd on the Hong Kong Stock Exchange](https://reddit.com/r/LocalLLaMA/comments/1q7mvuf/zai_the_ai_lab_behind_glm_has_officially_ipod_on/)

**Author:** u/Old-School8916 | **Upvotes:** 252 | **Comments:** 29 | **Date:** 2026-01-08

**Summary:** Z.ai, the AI lab behind GLM, has officially IPO'd on the Hong Kong Stock Exchange, with its stock price rising by 13.17% on the first day. The community is hopeful for the open-weight release of GLM 5 and celebrates the company's success.

**Key Points:**
- Z.ai IPO'd on the Hong Kong Stock Exchange with a 13.17% increase in stock price on the first day.
- GLM 5 is currently in training, with hopes for an open-weight release.
- Community reactions include celebration and anticipation for future developments.
- Minimax is set to IPO a day later, on January 9th.

**Discussion Highlights:** The community is optimistic about Z.ai's IPO success and the potential for open-weight releases of their AI models. There is also anticipation for Minimax's upcoming IPO.

---

## 10. [LFM2.5 1.2B Instruct is amazing](https://reddit.com/r/LocalLLaMA/comments/1q7jd1a/lfm25_12b_instruct_is_amazing/)

**Author:** u/Paramecium_caudatum_ | **Upvotes:** 144 | **Comments:** 37 | **Date:** 2026-01-08

**Summary:** The Reddit post highlights the LFM2.5 1.2B Instruct model as an exceptional small model that outperforms others in its size range, running smoothly on various hardware. It is recommended for agentic tasks, data extraction, and RAG but not for knowledge-intensive tasks or programming.

**Key Points:**
- The model is highly efficient and performs well on basic hardware.
- It is particularly useful for agentic tasks, data extraction, and RAG.
- The model is not recommended for knowledge-intensive tasks or programming.
- Users appreciate its speed and effectiveness for tasks like creating tags and chat headlines.
- Recent updates include tool use capabilities, enhancing its functionality.

**Discussion Highlights:** The discussion consensus emphasizes the model's efficiency and suitability for specific tasks like data extraction and RAG. Users appreciate its performance on basic hardware and recent tool use updates. However, there is a noted caveat about its limitations in knowledge-intensive tasks and programming.

---

## 11. [Qwen3-VL-Reranker - a Qwen Collection](https://reddit.com/r/LocalLLaMA/comments/1q7dlkn/qwen3vlreranker_a_qwen_collection/)

**Author:** u/LinkSea8324 | **Upvotes:** 115 | **Comments:** 39 | **Date:** 2026-01-08

**Summary:** The Reddit post introduces Qwen3-VL-Reranker, a multimodal reranker model, and related Qwen3-VL Embeddings. The discussion highlights enthusiasm for multimodal RAG applications and practical implementations.

**Key Points:**
- Introduction of Qwen3-VL-Reranker, a multimodal reranker model
- Release of Qwen3-VL Embeddings alongside the reranker
- Enthusiasm for multimodal RAG applications in home labs
- Availability of an end-to-end notebook for chaining these models
- Interest in compatibility with OpenWebUI

**Discussion Highlights:** The discussion shows strong interest in multimodal RAG applications, with users sharing practical implementations and resources. There is also curiosity about the compatibility of these models with existing tools like OpenWebUI.

---

## 12. [Jensen Huang saying "AI" 121 times during the NVIDIA CES keynote - cut with one prompt](https://reddit.com/r/LocalLLaMA/comments/1q7d8bj/jensen_huang_saying_ai_121_times_during_the/)

**Author:** u/Prior-Arm-6705 | **Upvotes:** 854 | **Comments:** 138 | **Date:** 2026-01-08

**Summary:** A Reddit user created a compilation video of every instance Jensen Huang said 'AI' during NVIDIA's CES 2025 keynote, totaling 121 times, using open-source tools for video processing. The post gained significant attention, with users discussing the keynote's focus on AI and sharing humorous reactions.

**Key Points:**
- Jensen Huang said 'AI' 121 times during the CES 2025 keynote.
- The user automated the video compilation using open-source tools like Dive, yt-dlp-mcp, and ffmpeg-mcp-lite.
- The post received 854 upvotes and 138 comments, with notable reactions including humor and critiques of NVIDIA's pricing.
- The compilation video was described as 'hypnotic' and was seen as a concise summary of the keynote.

**Discussion Highlights:** The discussion highlighted a mix of humor and critique, with users joking about the frequency of 'AI' mentions and expressing opinions on NVIDIA's pricing and product impact. Some comments praised the technical execution of the video compilation.

---

## 13. [AI21 Labs releases Jamba2](https://reddit.com/r/LocalLLaMA/comments/1q7a62a/ai21_labs_releases_jamba2/)

**Author:** u/jacek2023 | **Upvotes:** 132 | **Comments:** 42 | **Date:** 2026-01-08

**Summary:** AI21 Labs has released Jamba2, a series of open-source language models designed for enterprise reliability. The Jamba2 Mini (52B total parameters, 12B active) and Jamba2 3B models offer high performance with memory efficiency, large context windows, and Apache 2.0 licensing for commercial use.

**Key Points:**
- Jamba2 Mini has 52B total parameters (12B active) and is optimized for enterprise workflows with a 256K context window.
- Jamba2 3B is designed for on-device deployments while maintaining enterprise-grade reliability.
- Both models are released under Apache 2.0 License and excel in benchmarks like IFBench and IFEval.
- Community reactions include skepticism about past Jamba models' performance and curiosity about improvements.
- The 3B model's Hugging Face repository lacks detailed information, raising questions among users.

**Discussion Highlights:** The community discussion highlights mixed reactions, with some users expressing skepticism due to past performance issues of Jamba models. Others are curious about the improvements and the lack of detailed information for the 3B model. There is also a comparison with other models like Qwen3 and Nemotron3.

---

## 14. [Z-image base model is being prepared for release](https://reddit.com/r/LocalLLaMA/comments/1q77rxh/zimage_base_model_is_being_prepared_for_release/)

**Author:** u/Ravencloud007 | **Upvotes:** 158 | **Comments:** 25 | **Date:** 2026-01-08

**Summary:** The Reddit post announces the upcoming release of the Z-image base model, with a link to recent GitHub commits. The community expresses a mix of anticipation, skepticism, and impatience regarding the release.

**Key Points:**
- Z-image base model is being prepared for release
- Community shows anticipation and impatience
- Concerns about whether open weights will be released
- Expectations for image editing capabilities
- Comparisons to other models like Qwen Edit and Flux 2

**Discussion Highlights:** The discussion highlights a mix of excitement and skepticism. Some users are eager for the release, while others express frustration with the prolonged anticipation. There are concerns about the availability of open weights and expectations for the model's capabilities, particularly in image editing.

---

## 15. [Sopro: A 169M parameter real-time TTS model with zero-shot voice cloning](https://reddit.com/r/LocalLLaMA/comments/1q6sp4b/sopro_a_169m_parameter_realtime_tts_model_with/)

**Author:** u/SammyDaBeast | **Upvotes:** 209 | **Comments:** 25 | **Date:** 2026-01-07

**Summary:** The Reddit post introduces Sopro, a 169M parameter text-to-speech model with zero-shot voice cloning, trained on a single GPU. It supports streaming and achieves 0.25 RTF on CPU, though it has some instability and voice likeness issues. Key points include its 169M parameter size, streaming support, training on a single L40S GPU, Apache 2.0 license, and community praise for the project's scope and streaming feature. The discussion highlights community appreciation for the solo effort and streaming support, with questions about training costs, voice quality improvements, and potential for multilingual support.

---

## 16. [16x AMD MI50 32GB at 10 t/s (tg) &amp; 2k t/s (pp) with Deepseek v3.2 (vllm-gfx906)](https://reddit.com/r/LocalLLaMA/comments/1q6n5vl/16x_amd_mi50_32gb_at_10_ts_tg_2k_ts_pp_with/)

**Author:** u/ai-infos | **Upvotes:** 448 | **Comments:** 232 | **Date:** 2026-01-07

**Summary:** The post discusses running Deepseek v3.2 on 16 AMD MI50 GPUs, achieving 10 tokens/sec output and 2000 tokens/sec input with a 69000 context length. The setup aims for cost-effective local AGI with power draw between 550W (idle) and 2400W (peak).

**Key Points:**
- Performance: 10 tok/s output, 2000 tok/s input, 69000 context length
- Power consumption: 550W idle, 2400W peak
- Goal: Cost-effective local AGI without high-end hardware
- Future plans: 32 MI50 setup for Kimi K2 Thinking
- Community appreciation for open-source contributions

**Discussion Highlights:** Users praised the setup's efficiency, with comments highlighting its heating benefits in winter and curiosity about noise levels and home power usage. The post gained significant traction with 448 upvotes and 232 comments.

---

## 17. [DeepSeek-R1’s paper was updated 2 days ago, expanding from 22 pages to 86 pages and adding a substantial amount of detail.](https://reddit.com/r/LocalLLaMA/comments/1q6c9wc/deepseekr1s_paper_was_updated_2_days_ago/)

**Author:** u/Nunki08 | **Upvotes:** 628 | **Comments:** 52 | **Date:** 2026-01-07

**Summary:** The Reddit post discusses the recent update to DeepSeek-R1's paper, which expanded from 22 pages to 86 pages, adding significant detail. The discussion includes comments about potential new architectures, linear attention research, and the value of added implementation specifics. Key points include the paper's expansion, potential new architectures, and community interest in smaller model sizes. The discussion highlights speculation about new architectures and appreciation for the added detail in the updated paper.

---

## 18. [Don't put off hardware purchases: GPUs, SSDs, and RAM are going to skyrocket in price soon](https://reddit.com/r/LocalLLaMA/comments/1q694ic/dont_put_off_hardware_purchases_gpus_ssds_and_ram/)

**Author:** u/Eisenstein | **Upvotes:** 244 | **Comments:** 233 | **Date:** 2026-01-07

**Summary:** The Reddit post warns of impending price hikes for GPUs, SSDs, and RAM due to supply shortages and increased demand, with significant quarterly price increases projected for 2026.

**Key Points:**
- GPU prices are expected to rise, with NVIDIA's RTX 5090 potentially reaching $5,000.
- NAND flash prices increased by 20% in November, with further rises expected, affecting SSD costs.
- DRAM prices are forecasted to surge by 55-60% for conventional DRAM and over 60% for server DRAM.
- Consoles may face delays due to component shortages.
- Users express frustration and reluctance to purchase at inflated prices.

**Discussion Highlights:** The discussion reflects a consensus of frustration among users, with many planning to delay purchases or avoid upgrades due to the steep price increases. Some commenters note that prices have already risen significantly, while others express concern for the longevity of their current hardware.

---

## 19. [NousResearch/NousCoder-14B · Hugging Face](https://reddit.com/r/LocalLLaMA/comments/1q61wpv/nousresearchnouscoder14b_hugging_face/)

**Author:** u/jacek2023 | **Upvotes:** 164 | **Comments:** 48 | **Date:** 2026-01-06

**Summary:** NousResearch introduced NousCoder-14B, a competitive programming model based on Qwen3-14B, achieving a 7.08% improvement in Pass@1 accuracy on LiveCodeBench v6. The model was trained on 24k coding problems using 48 B200s over four days.

**Key Points:**
- NousCoder-14B is a post-trained model based on Qwen3-14B.
- Achieved 67.87% Pass@1 accuracy, a 7.08% improvement over Qwen3-14B.
- Trained on 24k verifiable coding problems using 48 B200s over four days.
- Community reactions include engagement, skepticism about overfitting, and concerns about language support.
- Anticipation and mixed reactions from the community regarding the model's performance.

**Discussion Highlights:** The community showed engagement with the post, including skepticism about potential overfitting to the test suite and concerns about the model's language support. There was also anticipation and mixed reactions regarding the model's performance.

---

## 20. [Razer is demonstrating a “AI accelerator” box with a Wormhole n150 processor from Tenstorrent at CES](https://reddit.com/r/LocalLLaMA/comments/1q617ug/razer_is_demonstrating_a_ai_accelerator_box_with/)

**Author:** u/Hasuto | **Upvotes:** 119 | **Comments:** 39 | **Date:** 2026-01-06

**Summary:** Razer is showcasing an AI accelerator box featuring Tenstorrent's Wormhole n150 processor at CES. The hardware, which includes 12GB of memory and is priced at $1000, is seen as a proof of concept by the community, with mixed reactions about its practicality and future potential.

**Key Points:**
- Razer's AI accelerator box uses Tenstorrent's Wormhole n150 processor.
- The hardware comes with 12GB memory and is priced at $1000.
- Community views the product as a proof of concept (POC).
- Mixed reactions about the product's practicality and future potential.
- Concerns about rapid obsolescence and value for money.

**Discussion Highlights:** The community consensus is that the Razer AI accelerator is a proof of concept, with some users expressing skepticism about its practicality and value. There are concerns about the product becoming obsolete quickly and whether it offers good value for money. Some users also find the collaboration between Razer and Tenstorrent surprising.

---

## 21. [Unsloth-MLX - Fine-tune LLMs on your Mac (same API as Unsloth)](https://reddit.com/r/LocalLLaMA/comments/1q5mh84/unslothmlx_finetune_llms_on_your_mac_same_api_as/)

**Author:** u/A-Rahim | **Upvotes:** 138 | **Comments:** 25 | **Date:** 2026-01-06

**Summary:** The post introduces Unsloth-MLX, a library that brings Unsloth's fine-tuning experience to Apple Silicon, allowing users to prototype LLM fine-tuning locally on Macs and then scale up to cloud GPUs without changing code. The author emphasizes that this is a personal project aimed at solving a workflow problem rather than replacing Unsloth. Key points include: Unsloth-MLX enables local LLM fine-tuning on Macs with the same API as Unsloth; the project aims to bridge local development and cloud scaling without code changes; the author clarifies that this is a personal project, not affiliated with Unsloth AI or Apple; discussion includes concerns about branding and mentions of related projects like a PR in the Unsloth repo; some comments highlight potential issues with the project's approach and branding. The discussion includes concerns about the use of the Unsloth name in the project, mentions of a related PR in the Unsloth repository, and critiques about the project's branding and approach. Some users appreciate the idea but caution about potential confusion with the original Unsloth project.

---

## 22. [A 30B Qwen Model Walks Into a Raspberry Pi… and Runs in Real Time](https://reddit.com/r/LocalLLaMA/comments/1q5m2n6/a_30b_qwen_model_walks_into_a_raspberry_pi_and/)

**Author:** u/ali_byteshape | **Upvotes:** 485 | **Comments:** 76 | **Date:** 2026-01-06

**Summary:** The post discusses the successful optimization and running of a 30B Qwen model on a Raspberry Pi 5, achieving high performance without significant quality loss. The community provides feedback and additional testing scenarios.

**Key Points:**
- A 30B Qwen model runs on a Raspberry Pi 5 with 8.03 TPS at 2.70 BPW, retaining 94.18% of BF16 quality.
- Optimization focuses on fitting the model within memory constraints and then improving TPS vs quality tradeoffs.
- GPU performance depends on kernel choice, leading to quirky behavior compared to CPUs.
- Community feedback includes testing on different hardware and configurations, as well as suggestions for further optimizations.
- The model's performance is compared favorably against alternatives like Unsloth and MagicQuant.

**Discussion Highlights:** The community is engaged in testing the model on various hardware setups, including Raspberry Pi 5, and discussing potential improvements and alternative approaches like using hybrid transformers. There is a consensus on the model's impressive performance on small hardware.

---

## 23. [Liquid AI released LFM2.5 1.2B Instruct](https://reddit.com/r/LocalLLaMA/comments/1q5f1jz/liquid_ai_released_lfm25_12b_instruct/)

**Author:** u/KaroYadgar | **Upvotes:** 109 | **Comments:** 31 | **Date:** 2026-01-06

**Summary:** Liquid AI released LFM2.5, a 1.2B parameter model optimized for on-device applications, featuring improved quality, lower latency, and expanded modality support. The model builds on a hybrid architecture with increased pretraining and reinforcement learning.

**Key Points:**
- LFM2.5 is designed for reliable on-device agentic applications
- Pretraining scaled from 10T to 28T tokens
- Expanded reinforcement learning post-training
- Users appreciate the model's ability to run on local devices
- Interest in benchmark comparisons with previous models

**Discussion Highlights:** Users expressed enthusiasm for the model's local device compatibility and requested more information on benchmarks and use cases. Some users shared positive experiences with previous LFM models and hoped for improvements in instruction following.

---

## 24. [Supertonic2: Lightning Fast, On-Device, Multilingual TTS](https://reddit.com/r/LocalLLaMA/comments/1q5e010/supertonic2_lightning_fast_ondevice_multilingual/)

**Author:** u/ANLGBOY | **Upvotes:** 190 | **Comments:** 42 | **Date:** 2026-01-06

**Summary:** Supertonic2 is a lightweight, multilingual TTS model with 5 supported languages, designed for speed and on-device use. It offers commercial licensing and flexible deployment options.

**Key Points:**
- Supports 5 languages: Korean, Spanish, French, Portuguese, and English
- Lightning fast with RTF 0.006 on M4 Pro and 66M parameters
- On-device TTS with complete privacy and zero network latency
- Open-weight model with commercial use allowed under OpenRAIL-M license
- Users praise its quality and speed but note some pronunciation issues in Korean

**Discussion Highlights:** Users are impressed with the model's quality and speed, though some note pronunciation inaccuracies in Korean. There is demand for additional language support, such as German, Russian, and Arabic. The OpenRAIL-M license is criticized for being user-hostile.

---

## 25. [Performance improvements in llama.cpp over time](https://reddit.com/r/LocalLLaMA/comments/1q5dnyw/performance_improvements_in_llamacpp_over_time/)

**Author:** u/jacek2023 | **Upvotes:** 652 | **Comments:** 78 | **Date:** 2026-01-06

**Summary:** The Reddit post discusses performance improvements in llama.cpp over time, highlighting significant progress and comparisons with other implementations like ik_llama.cpp. The discussion includes mentions of NVIDIA GPU-specific optimizations and community appreciation for the advancements.

**Key Points:**
- Performance gains in llama.cpp have been substantial, approaching the speed of ik_llama.cpp.
- Discussion includes mentions of NVIDIA GPU-specific optimizations and related tools.
- Prompt processing remains slower compared to token generation speed.
- Community recognition and appreciation for the progress made.

**Discussion Highlights:** The discussion highlights the impressive progress in llama.cpp performance, with specific mentions of NVIDIA GPU optimizations and comparisons to other implementations. There is a general consensus on the significant improvements and community appreciation for the advancements.

---

## 26. [Liquid Ai released LFM2.5, family of tiny on-device foundation models.](https://reddit.com/r/LocalLLaMA/comments/1q5a0if/liquid_ai_released_lfm25_family_of_tiny_ondevice/)

**Author:** u/Difficult-Cap-7527 | **Upvotes:** 301 | **Comments:** 54 | **Date:** 2026-01-05

**Summary:** Liquid AI released LFM2.5, a family of tiny on-device foundation models designed for reliable agentic applications. The models feature higher quality, lower latency, and broader modality support in the ~1B parameter class, with five open-weight model instances available.

**Key Points:**
- LFM2.5 is built on a device-optimized hybrid architecture with scaled pretraining from 10T to 28T tokens.
- The models include a general-purpose instruct model, a Japanese-optimized chat model, a vision-language model, a native audio-language model, and base checkpoints for customization.
- Discussion highlights include comparisons with other models like Qwen3-0.6B, observations on performance and instruction-following capabilities, and suggestions for training optimizations.

**Discussion Highlights:** The discussion highlights comparisons with other models, observations on performance and instruction-following capabilities, and suggestions for training optimizations like native FP8 or FP4 support.

---

## 27. [I just saw Intel embrace local LLM inference in their CES presentation](https://reddit.com/r/LocalLLaMA/comments/1q52miw/i_just_saw_intel_embrace_local_llm_inference_in/)

**Author:** u/Mundane-Light6394 | **Upvotes:** 144 | **Comments:** 71 | **Date:** 2026-01-05

**Summary:** Intel emphasized local LLM inference during their CES presentation, highlighting benefits like user privacy, control, and model responsiveness. The discussion suggests that local inference may have a strong future despite Nvidia's cloud-first strategy.

**Key Points:**
- Intel's focus on local inference for privacy, control, and responsiveness
- Local inference may not be dead despite Nvidia's cloud strategy
- Intel Arc Pro B50 GPU mentioned as a cost-effective option for local inference
- Discussion on the potential of local LLM inference becoming more efficient and accessible
- Mention of Intel's support for unified memory and CXL technology

**Discussion Highlights:** The discussion highlights a positive outlook on local LLM inference, with users expressing interest in Intel's hardware offerings and the potential for local inference to become more prevalent. There is also mention of Intel's support for technologies like unified memory and CXL, which could enhance local inference capabilities.

---

## 28. [Rubin uplifts from CES conference going on now](https://reddit.com/r/LocalLLaMA/comments/1q502bi/rubin_uplifts_from_ces_conference_going_on_now/)

**Author:** u/mr_zerolith | **Upvotes:** 220 | **Comments:** 94 | **Date:** 2026-01-05

**Summary:** The Reddit post discusses the Rubin uplifts announced at the CES conference, highlighting excitement around the new technology and its potential performance gains. However, there is some criticism about the lack of consumer-focused announcements and concerns about power requirements and cost.

**Key Points:**
- Exciting announcements about Rubin uplifts at CES
- Potential high cost and power requirements
- Impressive memory bandwidth figures
- Lack of consumer-focused products mentioned
- Performance gains may come with trade-offs in power efficiency

**Discussion Highlights:** The discussion highlights a mix of excitement about the technological advancements and criticism regarding the lack of consumer-focused products. There is also concern about the potential high cost and power requirements of the new technology.

---

## 29. [For the first time in 5 years, Nvidia will not announce any new GPUs at CES — company quashes RTX 50 Super rumors as AI expected to take center stage](https://reddit.com/r/LocalLLaMA/comments/1q4x5e9/for_the_first_time_in_5_years_nvidia_will_not/)

**Author:** u/FullstackSensei | **Upvotes:** 624 | **Comments:** 198 | **Date:** 2026-01-05

**Summary:** Nvidia will not announce new GPUs at CES, focusing instead on AI. The company faces supply issues with high-end GPUs and may reintroduce older models like the RTX 3060. Rising hardware prices and limited availability are causing concerns among consumers.

**Key Points:**
- No new GPU announcements at CES
- Limited supply of RTX 5070Ti, 5080, and 5090
- Potential reintroduction of RTX 3060
- Rising DDR5 and storage prices
- Consumer concerns about corporate greed and future upgrades

**Discussion Highlights:** The discussion highlights frustration with corporate greed and the impact on local computing. Users express concerns about the future of hardware upgrades and call for alternative solutions, such as increased competition from China.

---

## 30. [[Release] EchoChamber - Add AI-Generated Audience Reactions to Your SillyTavern Stories &amp; Conversations](https://reddit.com/r/LocalLLaMA/comments/1q4tken/release_echochamber_add_aigenerated_audience/)

**Author:** u/mattjb | **Upvotes:** 108 | **Comments:** 27 | **Date:** 2026-01-05

**Summary:** EchoChamber is a new SillyTavern extension that adds AI-generated audience reactions to stories and conversations, offering various chat styles and customization options.

**Key Points:**
- 10+ built-in chat styles including Discord, Twitter, and MST3K
- Flexible backend support for local models and APIs
- Customizable and theme-integrated
- Real-time contextual reactions from virtual audiences
- Community reactions range from amusement to concern

**Discussion Highlights:** The community reactions are mixed, with some finding it amusing and others expressing concern or discomfort. Comments highlight the novelty and potential implications of having an AI-generated audience.

---

## 31. [llama.cpp performance breakthrough for multi-GPU setups](https://reddit.com/r/LocalLLaMA/comments/1q4s8t3/llamacpp_performance_breakthrough_for_multigpu/)

**Author:** u/Holiday-Injury-9397 | **Upvotes:** 555 | **Comments:** 173 | **Date:** 2026-01-05

**Summary:** The ik_llama.cpp project achieved a significant performance breakthrough for multi-GPU setups, delivering a 3x to 4x speed improvement in local LLM inference. This advancement allows for the use of multiple low-cost GPUs instead of expensive high-end cards, making it a game-changer for homelabs, server rooms, and cloud setups.

**Key Points:**
- ik_llama.cpp achieved a 3x to 4x speed improvement in multi-GPU setups.
- The new execution mode (split mode graph) enables maximum utilization of multiple GPUs.
- This breakthrough reduces the need for expensive high-end GPUs, making it cost-effective.
- Performance improvements are also noted in single GPU and CPU-only setups.
- The project is seen as competitive with other performance-optimized forks like exllama and vllm.

**Discussion Highlights:** The community highlights the significant performance gains and cost-effectiveness of the ik_llama.cpp project. There is consensus on its superiority in single batch processing and its potential to rival other optimized forks. Some users reported bottlenecks in hybrid inference setups, indicating areas for further improvement.

---

## 32. [Falcon H1R 7B, a new reasoning model with 256k context window by the Technology Innovation Institute (TII) in Abu Dhabi](https://reddit.com/r/LocalLLaMA/comments/1q4jnq0/falcon_h1r_7b_a_new_reasoning_model_with_256k/)

**Author:** u/Nunki08 | **Upvotes:** 124 | **Comments:** 27 | **Date:** 2026-01-05

**Summary:** The post introduces Falcon H1R 7B, a new reasoning model with a 256k context window developed by the Technology Innovation Institute (TII) in Abu Dhabi. The model shows impressive benchmarks but raises concerns about real-world usage and the need for new benchmarks.

**Key Points:**
- Falcon H1R 7B is a new reasoning model with a 256k context window by TII in Abu Dhabi.
- The model shows impressive benchmarks but may not translate well to real-world usage.
- There is a call for new, private benchmarks and more agentic benchmarks.
- The model is noted for its efficiency and potential to be sub-32B SOTA if agentic capabilities are included.

**Discussion Highlights:** The discussion highlights concerns about the model's real-world performance despite impressive benchmarks. There is a consensus on the need for new benchmarks and more focus on agentic capabilities. Some users appreciate the model's efficiency and potential.

---

## 33. [What do we think about Gorgon Point (Ryzen AI 9 HX 470)?](https://reddit.com/r/LocalLLaMA/comments/1q4jc99/what_do_we_think_about_gorgon_point_ryzen_ai_9_hx/)

**Author:** u/Everlier | **Upvotes:** 139 | **Comments:** 44 | **Date:** 2026-01-05

**Summary:** The Reddit post discusses the new Gorgon Point (Ryzen AI 9 HX 470) APU, highlighting its support for high-speed memory and potential improvements over previous models, but also noting challenges in accessing the necessary chips. The discussion includes mixed opinions on its significance and future expectations.

**Key Points:**
- Gorgon Point supports DDR5-6400 and LPDDR5X-8533 memory, improving performance for some models.
- Access to necessary chips is currently limited, posing a challenge for manufacturers.
- Gorgon Point is a mid-cycle refresh, not a full replacement for Strix Halo.
- Opinions vary on its significance, with some comparing it to other models like Ryzen AI Max 395.
- There is skepticism about the rapid pace of technological updates and their practical benefits.

**Discussion Highlights:** The discussion highlights a mix of optimism and skepticism. Some users see Gorgon Point as a step forward, while others are critical of the current tech scene and the rapid release of new products. There is also a desire for more significant advancements in the future.

---

## 34. [I built a visual AI workflow tool that runs entirely in your browser - Ollama, LM Studio, llama.cpp and Most cloud API's all work out of the box. Agents/Websearch/TTS/Etc.](https://reddit.com/r/LocalLLaMA/comments/1q4f0tm/i_built_a_visual_ai_workflow_tool_that_runs/)

**Author:** u/l33t-Mt | **Upvotes:** 156 | **Comments:** 58 | **Date:** 2026-01-05

**Summary:** The Reddit post introduces 'EmergentFlow,' a visual AI workflow tool that runs entirely in the browser, supporting various AI models and APIs. It is free to use with unlimited access to local models and offers a Pro tier for additional features. Key points include its support for Ollama, LM Studio, llama.cpp, and various cloud APIs, and community feedback comparing it to tools like n8n and Flowise. The discussion highlights comparisons to other tools and concerns about using API keys for online models.

---

## 35. [Introducing Adaptive-P: A New Sampler for Creative Text Generation (llama.cpp PR)](https://reddit.com/r/LocalLLaMA/comments/1q42wtt/introducing_adaptivep_a_new_sampler_for_creative/)

**Author:** u/DragPretend7554 | **Upvotes:** 120 | **Comments:** 27 | **Date:** 2026-01-04

**Summary:** Adaptive-P is a new sampling method for creative text generation that addresses repetitive patterns by targeting a probability range and using a feedback loop to maintain diversity. It has been integrated into Kobold.cpp and is in staging for SillyTavern.

**Key Points:**
- Adaptive-P targets a probability range to encourage diverse token selection
- It uses an exponential moving average for adaptive feedback
- The method prevents probability accumulation in the tail of the distribution
- It has been merged into Kobold.cpp and is in staging for SillyTavern
- Users report improved word diversity and logic preservation compared to traditional samplers

**Discussion Highlights:** Users generally praise Adaptive-P for its effectiveness in creative tasks and its versatility in targeting different probability ranges. There is consensus on its superiority over traditional sampling methods like temperature and top-p for creative text generation.

---

## 36. [GLM-Image model from Z.ai is coming](https://reddit.com/r/LocalLLaMA/comments/1q41bw1/glmimage_model_from_zai_is_coming/)

**Author:** u/Ravencloud007 | **Upvotes:** 316 | **Comments:** 58 | **Date:** 2026-01-04

**Summary:** The Reddit post announces the upcoming GLM-Image model from Z.ai, which has generated significant interest in the community. The model is highly anticipated, with users expressing excitement about its potential capabilities and comparing it favorably to existing models.

**Key Points:**
- GLM-Image model from Z.ai is being introduced
- The model has generated significant community interest with 316 upvotes and 58 comments
- Users are excited about the model's potential, with one comment mentioning a feeling of 103 billion parameters
- Z.ai's image model is currently the community favorite, setting a high bar for new models
- There is a desire for models that balance size, ease of fine-tuning, and quality

**Discussion Highlights:** The discussion highlights a strong community interest and excitement about the GLM-Image model. Users are comparing it favorably to existing models and expressing a desire for models that are powerful yet manageable in terms of size and ease of use. The overall consensus is one of anticipation and high expectations for the new model.

---

## 37. [MultiverseComputingCAI/HyperNova-60B · Hugging Face](https://reddit.com/r/LocalLLaMA/comments/1q3p9oz/multiversecomputingcaihypernova60b_hugging_face/)

**Author:** u/jacek2023 | **Upvotes:** 129 | **Comments:** 60 | **Date:** 2026-01-04

**Summary:** The Reddit post discusses HyperNova 60B, a model based on the gpt-oss-120b architecture with 59B parameters, 4.8B active parameters, and MXFP4 quantization. It supports configurable reasoning effort and requires less than 40GB of GPU memory. The discussion includes user experiences with hardware compatibility and performance metrics.

**Key Points:**
- HyperNova 60B is based on the gpt-oss-120b architecture
- It has 59B parameters with 4.8B active parameters and uses MXFP4 quantization
- The model supports configurable reasoning effort (low, medium, high)
- GPU usage is less than 40GB
- Users report successful deployment on 3090 + 5060 ti with 40GB total memory

**Discussion Highlights:** Users shared their experiences with hardware compatibility, noting that a 3090 + 5060 ti setup with 40GB total memory can handle the model with a 130k context. Performance metrics of around 3k prefill and 100 token generation were reported. There was also interest in the novel compression technology used, with requests for more information or papers.

---

## 38. [Local LLMs vs breaking news: when extreme reality gets flagged as a hoax - the US/Venezuela event was too far-fetched](https://reddit.com/r/LocalLLaMA/comments/1q31ltd/local_llms_vs_breaking_news_when_extreme_reality/)

**Author:** u/ubrtnk | **Upvotes:** 376 | **Comments:** 194 | **Date:** 2026-01-03

**Summary:** The post discusses the challenges faced by local LLMs in processing extreme or unlikely breaking news events, such as the US attacking Venezuela and capturing Maduro. The author shares their experience with different LLMs, highlighting how these models initially classified the event as a hoax despite credible sources.

**Key Points:**
- Local LLMs struggled to accept extreme breaking news as real, classifying it as a hoax.
- Different LLMs (Qwen Research, Spark 4.0, GPT-OSS:120B) had varying responses to the news.
- Providing credible sources helped some LLMs acknowledge the event's reality.
- Commenters shared similar experiences with LLMs dismissing unlikely events.
- Discussion highlights the bias and limitations of LLMs in processing unfamiliar geopolitical events.

**Discussion Highlights:** The discussion highlights the limitations and biases of LLMs in processing unfamiliar or extreme geopolitical events. Commenters shared similar experiences and expressed curiosity about the future of AI in handling such events.

---

## 39. [Llama.cpp running on Android with Snapdragon 888 and 8GB of ram. Compiled/Built on device. [Guide/Tutorial]](https://reddit.com/r/LocalLLaMA/comments/1q2wvsj/llamacpp_running_on_android_with_snapdragon_888/)

**Author:** u/hackiv | **Upvotes:** 133 | **Comments:** 31 | **Date:** 2026-01-03

**Summary:** The post provides a step-by-step guide to running Llama.cpp on an Android device with a Snapdragon 888 processor and 8GB of RAM. It involves using Termux to compile and run the model, downloading a quantized model from HuggingFace, and launching a local server to interact with the model.

**Key Points:**
- Uses Termux for compilation and execution on Android
- Requires downloading a quantized model from HuggingFace
- Model is saved in cache for future use without re-downloading
- Additional packages like git and libandroid-spawn may be needed
- Discussion highlights curiosity about performance metrics and hardware utilization

**Discussion Highlights:** The discussion includes questions about performance metrics (tokens/sec) and hardware utilization (CPU, NPU, or GPU). Users also expressed surprise at the capability to run Llama.cpp on ARM architecture and shared additional installation steps.

---

## 40. [ElevenLabs is killing my budget. What are the best "hidden gem" alternatives for documentary style TTS?](https://reddit.com/r/LocalLLaMA/comments/1q2sfwx/elevenlabs_is_killing_my_budget_what_are_the_best/)

**Author:** u/Ancient_Routine8576 | **Upvotes:** 233 | **Comments:** 126 | **Date:** 2026-01-03

**Summary:** The Reddit post discusses the high cost of ElevenLabs for TTS in documentary-style YouTube videos and seeks cheaper or local alternatives with a dark, authoritative tone. The discussion highlights several local and lesser-known TTS options like Soprano, Kokoro, VibeVoice, XTTS v2, and F5 TTS, with some users recommending specific tools based on ease of use and quality. The discussion primarily focuses on recommending local and lesser-known TTS tools that offer a documentary-style tone at a lower cost. Users share their experiences with various tools, highlighting ease of use, quality, and limitations. There is also anticipation for Google's upcoming voice synthesis technology.

---

## 41. [Don't sleep on granite 4 small if you got an 8+32+ system](https://reddit.com/r/LocalLLaMA/comments/1q2s3hp/dont_sleep_on_granite_4_small_if_you_got_an_832/)

**Author:** u/Zestyclose-Shift710 | **Upvotes:** 122 | **Comments:** 39 | **Date:** 2026-01-03

**Summary:** The post discusses the performance of Granite 4 Small, a hybrid transformer+mamba model, on a system with 32GB RAM and an 8GB GPU. The user achieved ~7 tkps generation speed with a 50-page context, highlighting its efficiency compared to other models.

**Key Points:**
- Granite 4 Small (32B total / 9B activated) maintains speed (~7 tkps) even with large context (~50.5k tokens).
- The setup involves using a MoE model with all experts on CPU, freeing up VRAM for context length.
- Comparisons with Qwen 30B A3B and other models are discussed in the comments.
- Performance benchmarks and potential optimizations are shared in the discussion.

**Discussion Highlights:** The discussion includes comparisons with other models like Qwen 30B A3B, performance benchmarks, and suggestions for optimizing speed using specific parameters in Jan (a FOSS LM Studio alternative).

---

## 42. [GLM-4.7-REAP-50-W4A16: 50% Expert-Pruned + INT4 Quantized GLM-4 (179B params, ~92GB)](https://reddit.com/r/LocalLLaMA/comments/1q2pons/glm47reap50w4a16_50_expertpruned_int4_quantized/)

**Author:** u/Maxious | **Upvotes:** 179 | **Comments:** 72 | **Date:** 2026-01-03

**Summary:** The post introduces GLM-4.7-REAP-50-W4A16, a 50% expert-pruned and INT4 quantized version of GLM-4 with 179B parameters (~92GB). The discussion focuses on technical details like calibration methods, benchmark results, and comparisons with other models.

**Key Points:**
- GLM-4.7-REAP-50-W4A16 is a pruned and quantized version of GLM-4 with 179B parameters (~92GB).
- Concerns about expert activation during calibration and the tasks used for REAP pruning.
- Interest in benchmark results and comparisons with other models like MiniMax M2.1 and EXL3 GLM.
- Community engagement and recognition for the contribution.

**Discussion Highlights:** The community is interested in technical details about calibration and benchmarks, and there is a comparison with other similar models.

---

## 43. [Built a fully local AI assistant with long-term memory, tool orchestration, and a 3D UI (runs on a GTX 1650)](https://reddit.com/r/LocalLLaMA/comments/1q2onpg/built_a_fully_local_ai_assistant_with_longterm/)

**Author:** u/atif_dev | **Upvotes:** 107 | **Comments:** 40 | **Date:** 2026-01-03

**Summary:** The Reddit post describes a personal project called ATOM, a fully local AI assistant with features like long-term memory, tool orchestration, and a 3D UI, running on a GTX 1650. The project is experimental and focuses on exploring local AI systems, memory consolidation, and tool-centric reasoning.

**Key Points:**
- ATOM is a fully local AI assistant designed like an operating system for intelligence.
- Key components include local LLM, tool orchestration, long-term memory with ChromaDB, and a 3D UI.
- The project runs on limited hardware (GTX 1650) and is experimental.
- Discussion highlights include praise for the coherent setup and suggestions for alternative tools like llama.cpp.
- The project is not a product but a personal engineering exploration.

**Discussion Highlights:** The discussion highlights praise for the coherent setup and suggestions for alternative tools like llama.cpp. There is also curiosity about the choice of edge/piper over kokoro and interest in long-term memory performance.

---

## 44. [What is the smartest uncensored nsfw LLM you can run with 20GB VRAM and 24GB RAM](https://reddit.com/r/LocalLLaMA/comments/1q2o033/what_is_the_smartest_uncensored_nsfw_llm_you_can/)

**Author:** u/Death_12_35_taken | **Upvotes:** 190 | **Comments:** 75 | **Date:** 2026-01-03

**Summary:** The post seeks recommendations for an uncensored, smart, and fast LLM that can run locally with 20GB VRAM and 24GB RAM. Users suggest models like Dolphin-Mistral-24B-Venice-Edition and provide links to relevant resources.

**Key Points:**
- Looking for an uncensored, smart, and fast LLM
- Must run locally with 20GB VRAM and 24GB RAM
- Dolphin-Mistral-24B-Venice-Edition is recommended
- Links to Hugging Face models and leaderboards provided
- Interest in models up to 70B parameters

**Discussion Highlights:** The discussion highlights the Dolphin-Mistral-24B-Venice-Edition as a strong candidate, with additional resources and leaderboards shared for further exploration. There is also interest in larger models (70B parameters).

---

