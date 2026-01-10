# r/LocalLLaMA Reading Digest

**Period:** 2026-01-10 to 2026-01-10
**Posts Summarized:** 38
**Total Posts Analyzed:** 38

---

## 1. [I clustered 3 DGX Sparks that NVIDIA said couldn't be clustered yet...took 1500 lines of C to make it work](https://reddit.com/r/LocalLLaMA/comments/1q8hqgd/i_clustered_3_dgx_sparks_that_nvidia_said_couldnt/)

**Author:** u/Ok-Pomegranate1314 | **Upvotes:** 733 | **Comments:** 122 | **Date:** 2026-01-09

**Summary:** The author successfully clustered three DGX Sparks, which NVIDIA officially supports only for two, by writing a custom NCCL network plugin. This involved overcoming subnet and networking challenges with a 1500-line C implementation, achieving distributed inference at 8+ GB/s over RDMA.

**Key Points:**
- Author clustered three DGX Sparks despite NVIDIA's official support for only two.
- Custom NCCL network plugin written from scratch to handle subnet and networking issues.
- Implementation involved subnet-aware NIC selection, raw RDMA verbs, and a custom TCP handshake protocol.
- Achieved distributed inference at 8+ GB/s over RDMA.
- Community response highlights the complexity and potential significance of the achievement.

**Discussion Highlights:** The community praised the technical achievement, noting the difficulty of working with NCCL and the potential impact of the solution. Questions were raised about scalability and performance improvements with multiple nodes.

---

## 2. [RTX Blackwell Pro 6000 wholesale pricing has dropped by $150-200](https://reddit.com/r/LocalLLaMA/comments/1q8fagh/rtx_blackwell_pro_6000_wholesale_pricing_has/)

**Author:** u/TastesLikeOwlbear | **Upvotes:** 209 | **Comments:** 78 | **Date:** 2026-01-09

**Summary:** The Reddit post discusses a significant drop in the wholesale pricing of RTX Blackwell Pro 6000 cards by $150-200 from December to January. The author, who has insider access to wholesale pricing, also advises against buying the 72GiB 5000 Pro due to its higher price relative to the 6000 Pro. The discussion highlights appreciation for the insider information, surprise at the price drop given usual supply constraints, and considerations of upgrading to the RTX Pro 6000 due to potential supply issues with other models.

---

## 3. [The reason why RAM has become so expensive](https://reddit.com/r/LocalLLaMA/comments/1q8ckz0/the_reason_why_ram_has_become_so_expensive/)

**Author:** u/InvadersMustLive | **Upvotes:** 3665 | **Comments:** 316 | **Date:** 2026-01-09

**Summary:** The Reddit post discusses the significant increase in RAM prices, with comments highlighting concerns about monopolization of RAM resources by certain entities, making AI datacenters economically unviable.

**Key Points:**
- RAM prices have increased significantly, with some users reporting up to 10 times the cost compared to the previous year.
- There are concerns about monopolization of RAM resources, particularly by OpenAI, which could make other AI datacenters economically unviable.
- The post and comments suggest that the rising cost of RAM is not a temporary bubble but a strategic move to control future demand.

**Discussion Highlights:** The discussion highlights a consensus that the rising cost of RAM is driven by strategic monopolization, with significant implications for the economic viability of AI datacenters, particularly in China.

---

## 4. [DeepSeek V4 Coming](https://reddit.com/r/LocalLLaMA/comments/1q89g1i/deepseek_v4_coming/)

**Author:** u/External_Mood4719 | **Upvotes:** 445 | **Comments:** 96 | **Date:** 2026-01-09

**Summary:** DeepSeek is expected to release V4, a next-generation AI model with strong code-generation capabilities, outperforming mainstream models like Claude and GPT. The model shows improvements in handling long code prompts and overall reasoning ability.

**Key Points:**
- DeepSeek V4 focuses on strong code-generation capabilities
- Outperforms existing models like Claude and GPT in code generation
- Improved handling of long code prompts and data patterns
- Enhanced reasoning ability and reliability for complex tasks
- Users anticipate significant improvements in coding and reasoning performance

**Discussion Highlights:** Users express excitement and high expectations for DeepSeek V4, noting its potential to disrupt the AI landscape with improved coding and reasoning capabilities. Some users highlight the cost-effectiveness and performance of previous DeepSeek models.

---

## 5. [(The Information): DeepSeek To Release Next Flagship AI Model With Strong Coding Ability](https://reddit.com/r/LocalLLaMA/comments/1q88hdc/the_information_deepseek_to_release_next_flagship/)

**Author:** u/Nunki08 | **Upvotes:** 450 | **Comments:** 97 | **Date:** 2026-01-09

**Summary:** DeepSeek is set to release a new flagship AI model with strong coding capabilities, generating significant interest and discussion in the community.

**Key Points:**
- DeepSeek's upcoming AI model focuses on strong coding abilities
- The announcement has sparked excitement and anticipation in the community
- Users are looking forward to more details and benchmarks
- There is a consensus that more models benefit the AI ecosystem
- Some users express concerns about potential limitations in role-playing abilities

**Discussion Highlights:** The community is largely excited about the new model, with many users expressing anticipation for its release and potential capabilities. There is a general consensus that more models are beneficial for the AI ecosystem. Some users have raised concerns about potential limitations in role-playing abilities.

---

## 6. [Big tech companies, now "DRAM beggars," are staying in Pangyo and Pyeongtaek, demanding "give us some supplies."](https://reddit.com/r/LocalLLaMA/comments/1q84u82/big_tech_companies_now_dram_beggars_are_staying/)

**Author:** u/FullstackSensei | **Upvotes:** 286 | **Comments:** 93 | **Date:** 2026-01-09

**Summary:** The Reddit post discusses a significant surge in DRAM prices and a shortage expected to continue, with major suppliers demanding higher prices. Users express shock and make humorous remarks about the situation.

**Key Points:**
- DRAM prices have increased significantly, with DDR4 prices rising from $1.40 to $9.30 per GB.
- Major suppliers like Samsung and SK Hynix are demanding a 50-60% increase in server DRAM supply prices.
- The DRAM shortage is expected to continue until the end of the year.
- Tech companies are competing fiercely to secure remaining DRAM inventory.
- Users are shocked by the price increases and making humorous comments.

**Discussion Highlights:** Users are expressing shock at the price increases, with some making humorous remarks about auctioning old RAM sticks and waiting for new technology.

---

## 7. [Minimax also live on Hong Kong Stock Exchange](https://reddit.com/r/LocalLLaMA/comments/1q82zdm/minimax_also_live_on_hong_kong_stock_exchange/)

**Author:** u/No_Conversation9561 | **Upvotes:** 114 | **Comments:** 21 | **Date:** 2026-01-09

**Summary:** The Reddit post discusses Minimax's listing on the Hong Kong Stock Exchange, highlighting its stock performance and community reactions. The discussion includes insights on stock price changes, market trust, and potential future developments.

**Key Points:**
- Minimax is listed on the Hong Kong Stock Exchange
- Stock price has seen significant changes since IPO
- Community discussions include trust in Qwen and potential future developments
- Mixed reactions on the company's future direction and openness

**Discussion Highlights:** The discussion highlights a mix of optimism about Minimax's stock performance and skepticism about its future direction. Key points include the stock's performance since IPO, trust in Qwen, and concerns about potential changes in the company's openness and source availability.

---

## 8. [OK I get it, now I love llama.cpp](https://reddit.com/r/LocalLLaMA/comments/1q7uuxo/ok_i_get_it_now_i_love_llamacpp/)

**Author:** u/vulcan4d | **Upvotes:** 230 | **Comments:** 46 | **Date:** 2026-01-08

**Summary:** The author switched from Ollama to llama.cpp for running LLMs, finding it more efficient with proper tuning. They achieved significant performance improvements (11t/s to 21t/s) by optimizing settings with the help of AI tools.

**Key Points:**
- Switching from Ollama to llama.cpp for better performance
- Hardware setup includes a 3060 GPU and three P102-100 GPUs with 96GB RAM
- Performance optimization achieved through command tuning
- AI tools like ChatGPT and Google AI Studio helped in optimizing settings
- Discussion highlights include suggestions for further optimization and critiques of the commands used

**Discussion Highlights:** The discussion includes suggestions for increasing batch and ubatch sizes for better performance, critiques of the commands used, questions about the necessity of sudo and CUDA_UNIFIED_MEMORY, and recommendations for alternative tools like koboldcpp.

---

## 9. [The NO FAKES Act has a "Fingerprinting" Trap that kills Open Source. We need to lobby for a Safe Harbor.](https://reddit.com/r/LocalLLaMA/comments/1q7qcux/the_no_fakes_act_has_a_fingerprinting_trap_that/)

**Author:** u/PostEasy7183 | **Upvotes:** 588 | **Comments:** 86 | **Date:** 2026-01-08

**Summary:** The NO FAKES Act proposes a 'digital replica right' that could hold developers liable for hosting open-source AI models used to create deepfakes, potentially stifling innovation. The post urges lobbying for a 'Safe Harbor' provision to protect open-source developers. Key points include the Act targeting developers who 'make available' tools primarily used for creating digital replicas, imposing statutory damages, and the call for a 'Safe Harbor' provision to protect open-source developers and prevent a monopoly by Big Tech. The discussion reflects a consensus that the NO FAKES Act could harm open-source development and innovation, with concerns about the bill's potential to stifle innovation and the influence of Big Tech in shaping AI regulations.

---

## 10. [Z.ai  (the AI lab behind GLM) has officially IPO'd on the Hong Kong Stock Exchange](https://reddit.com/r/LocalLLaMA/comments/1q7mvuf/zai_the_ai_lab_behind_glm_has_officially_ipod_on/)

**Author:** u/Old-School8916 | **Upvotes:** 257 | **Comments:** 29 | **Date:** 2026-01-08

**Summary:** Z.ai, the AI lab behind GLM, has officially IPO'd on the Hong Kong Stock Exchange, with its stock price rising by 13.17% on the first day. The community is hopeful about the open-weight release of GLM 5 and celebrates the company's success.

**Key Points:**
- Z.ai IPO'd on the Hong Kong Stock Exchange with a 13.17% increase in stock price on the first day.
- GLM 5 is currently in training, with hopes for an open-weight release.
- Community reactions include celebration and anticipation for future developments.
- Minimax is set to IPO a day later, on January 9th.

**Discussion Highlights:** The community is optimistic about Z.ai's IPO and the potential open-weight release of GLM 5. There is also excitement about Minimax's upcoming IPO and the overall growth in the AI sector.

---

## 11. [LFM2.5 1.2B Instruct is amazing](https://reddit.com/r/LocalLLaMA/comments/1q7jd1a/lfm25_12b_instruct_is_amazing/)

**Author:** u/Paramecium_caudatum_ | **Upvotes:** 148 | **Comments:** 37 | **Date:** 2026-01-08

**Summary:** The Reddit post highlights the LFM2.5 1.2B Instruct model as an exceptional small model that outperforms others in its size range, running smoothly on various hardware. It is recommended for agentic tasks, data extraction, and RAG, but not for knowledge-intensive tasks or programming.

**Key Points:**
- The model is highly efficient and runs well on basic hardware.
- It excels in agentic tasks, data extraction, and RAG.
- Not recommended for knowledge-intensive tasks or programming.
- Users appreciate its speed and effectiveness for tasks like creating tags and chat headlines.
- Recent updates include tool use capabilities, enhancing its functionality.

**Discussion Highlights:** Users consensus highlights the model's efficiency and versatility for specific tasks, with notable appreciation for its speed and recent tool use updates. Some users express curiosity about its performance in real agent setups and acknowledge the importance of its limitations.

---

## 12. [Qwen3-VL-Reranker - a Qwen Collection](https://reddit.com/r/LocalLLaMA/comments/1q7dlkn/qwen3vlreranker_a_qwen_collection/)

**Author:** u/LinkSea8324 | **Upvotes:** 112 | **Comments:** 39 | **Date:** 2026-01-08

**Summary:** The Reddit post introduces Qwen3-VL-Reranker, a multimodal reranker model, and related Qwen3-VL Embeddings. Users express excitement about multimodal RAG capabilities and share resources for implementation.

**Key Points:**
- Introduction of Qwen3-VL-Reranker, a multimodal reranker model
- Release of Qwen3-VL Embeddings alongside the reranker
- User enthusiasm for multimodal RAG applications in home labs
- Availability of an end-to-end notebook for chaining models together
- Discussion about compatibility with OpenWebUI

**Discussion Highlights:** The discussion highlights strong interest in multimodal RAG capabilities, with users sharing practical resources like notebooks and exploring integration possibilities with existing tools like OpenWebUI.

---

## 13. [Jensen Huang saying "AI" 121 times during the NVIDIA CES keynote - cut with one prompt](https://reddit.com/r/LocalLLaMA/comments/1q7d8bj/jensen_huang_saying_ai_121_times_during_the/)

**Author:** u/Prior-Arm-6705 | **Upvotes:** 877 | **Comments:** 141 | **Date:** 2026-01-08

**Summary:** A Reddit user used open-source tools to count and compile every instance of the word 'AI' in Jensen Huang's CES 2025 keynote, resulting in a video with 121 clips. The process involved downloading the video, parsing subtitles, and editing clips locally.

**Key Points:**
- Jensen Huang said 'AI' 121 times during the CES 2025 keynote.
- The user employed open-source tools like Dive, yt-dlp-mcp, and ffmpeg-mcp-lite to automate the process.
- The final video was created by downloading, parsing timestamps, cutting clips, and merging them.
- The community found the result hypnotic and humorous, with some suggesting it summarized the keynote effectively.
- Top comments included reactions to the video's hypnotic effect and jokes about the frequency of 'AI' mentions.

**Discussion Highlights:** The community reacted positively, with many finding the video humorous and a good summary of the keynote. Some comments joked about the frequency of 'AI' mentions and the hypnotic effect of the compilation. There was also appreciation for the technical process and tools used.

---

## 14. [AI21 Labs releases Jamba2](https://reddit.com/r/LocalLLaMA/comments/1q7a62a/ai21_labs_releases_jamba2/)

**Author:** u/jacek2023 | **Upvotes:** 131 | **Comments:** 42 | **Date:** 2026-01-08

**Summary:** AI21 Labs has released Jamba2, featuring two models: Jamba2 Mini (12B active parameters, 52B total) and Jamba2 3B (3B parameters). Jamba2 Mini is designed for enterprise reliability with a 256K context window and Apache 2.0 License, while Jamba2 3B is optimized for on-device deployments.

**Key Points:**
- Jamba2 Mini has 12B active parameters and is built for enterprise reliability.
- Jamba2 Mini features a 256K context window and is released under Apache 2.0 License.
- Jamba2 3B is designed for on-device deployments with 3B parameters.
- Both models aim to provide high performance and reliability for enterprise and consumer use.
- The release includes benchmarks showing superior performance in various tasks.

**Discussion Highlights:** The discussion includes mixed reactions, with some users skeptical about the performance improvements over previous Jamba models. Notable comments highlight the naming of the 52B model as 'Mini' and the lack of information on the 3B model's Hugging Face repository. There is also a comparison table provided by a user, showing benchmark results for Jamba2 models against other models like Qwen3 and Nemotron3.

---

## 15. [Z-image base model is being prepared for release](https://reddit.com/r/LocalLLaMA/comments/1q77rxh/zimage_base_model_is_being_prepared_for_release/)

**Author:** u/Ravencloud007 | **Upvotes:** 159 | **Comments:** 25 | **Date:** 2026-01-08

**Summary:** The Reddit post discusses the upcoming release of the Z-image base model, with the community expressing a mix of anticipation and skepticism. Some users are eager for the release, while others are frustrated by the prolonged teasing.

**Key Points:**
- The Z-image base model is being prepared for release.
- Community members express anticipation and frustration over the prolonged teasing.
- There is speculation about the model's capabilities, including image editing features.
- Some users hope for open weights to be released alongside the model.
- Comparisons are made to other models like Qwen Edit and Flux 2.

**Discussion Highlights:** The discussion highlights a mix of excitement and skepticism. Some users are eagerly awaiting the release, while others are frustrated by the prolonged teasing. There is also speculation about the model's capabilities and comparisons to other existing models.

---

## 16. [Sopro: A 169M parameter real-time TTS model with zero-shot voice cloning](https://reddit.com/r/LocalLLaMA/comments/1q6sp4b/sopro_a_169m_parameter_realtime_tts_model_with/)

**Author:** u/SammyDaBeast | **Upvotes:** 210 | **Comments:** 25 | **Date:** 2026-01-07

**Summary:** Sopro is a 169M parameter real-time TTS model with zero-shot voice cloning, trained on a single L40S GPU. It supports streaming and achieves 0.25 RTF on CPU, requiring 3-12 seconds of reference audio for voice cloning.

**Key Points:**
- 169M parameters with streaming support
- Zero-shot voice cloning with 3-12 seconds of reference audio
- 0.25 RTF on CPU, generating 30 seconds of audio in 7.5 seconds
- Trained on a single L40S GPU with limited compute budget
- Apache 2.0 license and open-source on GitHub

**Discussion Highlights:** Users praised the project for its efficiency and streaming support, with questions about training costs, voice quality improvements, and potential for multilingual support.

---

## 17. [16x AMD MI50 32GB at 10 t/s (tg) &amp; 2k t/s (pp) with Deepseek v3.2 (vllm-gfx906)](https://reddit.com/r/LocalLLaMA/comments/1q6n5vl/16x_amd_mi50_32gb_at_10_ts_tg_2k_ts_pp_with/)

**Author:** u/ai-infos | **Upvotes:** 450 | **Comments:** 233 | **Date:** 2026-01-07

**Summary:** The post discusses running Deepseek v3.2 on 16x AMD MI50 32GB GPUs, achieving 10 tokens/sec output and 2000 tokens/sec input with a 69000 context length. The setup draws 550W idle and 2400W peak power, aiming for cost-effective local AGI solutions.

**Key Points:**
- Deepseek v3.2 runs at 10 tokens/sec output and 2000 tokens/sec input on 16x AMD MI50 GPUs
- Power consumption is 550W idle and 2400W peak during inference
- Goal is cost-effective local AGI without high-end hardware costs
- Community appreciates the setup, noting heating benefits and asking about noise levels
- Future plans include testing 32 AMD MI50 GPUs for Kimi K2 Thinking

**Discussion Highlights:** The community is excited about the setup, with comments highlighting the heating benefits during winter and concerns about noise levels. There is also curiosity about how the user manages 2400W power draw at home.

---

## 18. [DeepSeek-R1’s paper was updated 2 days ago, expanding from 22 pages to 86 pages and adding a substantial amount of detail.](https://reddit.com/r/LocalLLaMA/comments/1q6c9wc/deepseekr1s_paper_was_updated_2_days_ago/)

**Author:** u/Nunki08 | **Upvotes:** 632 | **Comments:** 54 | **Date:** 2026-01-07

**Summary:** The Reddit post discusses the recent update to DeepSeek-R1's paper, which expanded from 22 pages to 86 pages, adding significant detail. The discussion includes comments on potential new architectures, linear attention research, and the value of added implementation specifics.

**Key Points:**
- DeepSeek-R1's paper was updated from 22 pages to 86 pages.
- The update includes substantial additional detail.
- Discussion highlights potential new architectures and linear attention research.
- Comments appreciate the added implementation specifics.

**Discussion Highlights:** The discussion includes speculation about new architectures, interest in linear attention research, and appreciation for the added implementation details in the updated paper.

---

## 19. [Don't put off hardware purchases: GPUs, SSDs, and RAM are going to skyrocket in price soon](https://reddit.com/r/LocalLLaMA/comments/1q694ic/dont_put_off_hardware_purchases_gpus_ssds_and_ram/)

**Author:** u/Eisenstein | **Upvotes:** 242 | **Comments:** 233 | **Date:** 2026-01-07

**Summary:** The post warns about imminent price hikes for GPUs, SSDs, and RAM due to supply shortages and increased demand, with specific examples like NVIDIA's RTX 5090 potentially reaching $5,000. The discussion reflects concern and skepticism about the timing and impact of these price increases.

**Key Points:**
- GPU prices are set to rise, with NVIDIA's RTX 5090 potentially reaching $5,000.
- NAND flash prices increased by 20% in November, with further increases expected, affecting SSD prices.
- DRAM prices are projected to surge by 55-60% for conventional DRAM and over 60% for server DRAM.
- Consoles may face delays due to component shortages.
- Users express concern and skepticism, with some planning to delay purchases.

**Discussion Highlights:** The discussion highlights a mix of concern and skepticism, with users expressing intentions to delay purchases or noting that price increases have already begun. Some comments reflect frustration with corporate pricing strategies.

---

## 20. [NousResearch/NousCoder-14B · Hugging Face](https://reddit.com/r/LocalLLaMA/comments/1q61wpv/nousresearchnouscoder14b_hugging_face/)

**Author:** u/jacek2023 | **Upvotes:** 167 | **Comments:** 48 | **Date:** 2026-01-06

**Summary:** NousResearch introduced NousCoder-14B, a competitive programming model based on Qwen3-14B, achieving a 7.08% improvement in Pass@1 accuracy on LiveCodeBench v6. The model was trained on 24k coding problems using 48 B200s over four days.

**Key Points:**
- NousCoder-14B is a post-trained model based on Qwen3-14B.
- Achieved 67.87% Pass@1 accuracy, a 7.08% improvement over Qwen3-14B.
- Trained on 24k verifiable coding problems using 48 B200s in four days.
- Community discussions highlight concerns about overfitting and language limitations.
- Post gained significant attention with 167 upvotes and 48 comments.

**Discussion Highlights:** The community showed mixed reactions, with excitement about the model's potential but also concerns about overfitting to the test suite and limitations in language support beyond Python.

---

## 21. [Razer is demonstrating a “AI accelerator” box with a Wormhole n150 processor from Tenstorrent at CES](https://reddit.com/r/LocalLLaMA/comments/1q617ug/razer_is_demonstrating_a_ai_accelerator_box_with/)

**Author:** u/Hasuto | **Upvotes:** 120 | **Comments:** 39 | **Date:** 2026-01-06

**Summary:** Razer is showcasing an AI accelerator box featuring Tenstorrent's Wormhole n150 processor at CES. The hardware, which includes 12GB of memory and is priced at $1000, is seen as a proof of concept by the community, with mixed reactions about its cost and future viability.

**Key Points:**
- Razer's AI accelerator box uses Tenstorrent's Wormhole n150 processor.
- The hardware comes with 12GB memory and is priced at $1000.
- Community views the product as a proof of concept (POC).
- Mixed reactions about the cost and future relevance of the hardware.
- Tenstorrent's new Blackhole part is mentioned as an upcoming alternative with 32GB memory.

**Discussion Highlights:** The community consensus is that the Razer AI accelerator is a proof of concept, with some users expressing skepticism about its cost and long-term usefulness. The discussion also highlights Tenstorrent's upcoming Blackhole processor as a potential improvement over the current Wormhole n150.

---

## 22. [Unsloth-MLX - Fine-tune LLMs on your Mac (same API as Unsloth)](https://reddit.com/r/LocalLLaMA/comments/1q5mh84/unslothmlx_finetune_llms_on_your_mac_same_api_as/)

**Author:** u/A-Rahim | **Upvotes:** 135 | **Comments:** 26 | **Date:** 2026-01-06

**Summary:** The post introduces Unsloth-MLX, a library that brings Unsloth's fine-tuning experience to Apple Silicon, allowing users to prototype LLM fine-tuning locally on Macs and then scale up to cloud GPUs without changing code. The author emphasizes code portability and workflow efficiency.

**Key Points:**
- Unsloth-MLX enables local LLM fine-tuning on Macs with Apple Silicon.
- It maintains the same API as Unsloth, allowing seamless transition to cloud GPUs.
- The project aims to solve the 'Context Switch' problem for developers using Macs.
- Concerns were raised about the use of Unsloth's branding in the project name.
- A related PR was mentioned, indicating ongoing efforts within the Unsloth community.

**Discussion Highlights:** The discussion highlights concerns about branding and potential confusion with the original Unsloth project. Some users appreciated the idea but criticized the naming choice. There was also mention of a related PR in the Unsloth repository, suggesting ongoing development in this area.

---

## 23. [A 30B Qwen Model Walks Into a Raspberry Pi… and Runs in Real Time](https://reddit.com/r/LocalLLaMA/comments/1q5m2n6/a_30b_qwen_model_walks_into_a_raspberry_pi_and/)

**Author:** u/ali_byteshape | **Upvotes:** 486 | **Comments:** 76 | **Date:** 2026-01-06

**Summary:** The post discusses the successful optimization of a 30B Qwen model to run efficiently on a Raspberry Pi 5, achieving 8.03 tokens per second while retaining 94.18% of BF16 quality. The optimization focuses on balancing memory usage and performance, particularly on GPUs where kernel choice significantly impacts speed. Key points include the model's performance on a Raspberry Pi 5, the optimization strategy prioritizing memory as a budget, and the influence of kernel choice on GPU performance. The community showed interest in further testing and potential enhancements, such as combining the model with other technologies like Mamba2 hybrid transformers.

---

## 24. [Liquid AI released LFM2.5 1.2B Instruct](https://reddit.com/r/LocalLLaMA/comments/1q5f1jz/liquid_ai_released_lfm25_12b_instruct/)

**Author:** u/KaroYadgar | **Upvotes:** 108 | **Comments:** 31 | **Date:** 2026-01-06

**Summary:** Liquid AI released LFM2.5, a 1.2B parameter model optimized for on-device applications, featuring improved quality, lower latency, and expanded modality support. The model builds on a hybrid architecture with scaled pretraining and enhanced reinforcement learning.

**Key Points:**
- LFM2.5 is designed for reliable on-device agentic applications with higher quality and lower latency.
- The model features a hybrid architecture, scaled pretraining from 10T to 28T tokens, and expanded reinforcement learning.
- Users express enthusiasm for running the model on personal devices and curiosity about its performance improvements.
- Some users highlight the potential of tiny models for hobbyist use and seek guidance on relevant keywords for learning.
- Previous models like LFM2-8B-A1B received praise for speed and intelligence, with hopes for better instruction following in LFM2.5.

**Discussion Highlights:** The discussion reflects excitement about the model's potential for local use, with users expressing interest in performance benchmarks and practical applications. There is a consensus on the value of small, efficient models for hobbyists and a desire for improved instruction-following capabilities.

---

## 25. [Supertonic2: Lightning Fast, On-Device, Multilingual TTS](https://reddit.com/r/LocalLLaMA/comments/1q5e010/supertonic2_lightning_fast_ondevice_multilingual/)

**Author:** u/ANLGBOY | **Upvotes:** 193 | **Comments:** 43 | **Date:** 2026-01-06

**Summary:** Supertonic2 is a lightweight, multilingual TTS model with 5 supported languages, designed for speed and on-device use. It offers commercial licensing and flexible deployment options.

**Key Points:**
- Supports 5 languages: Korean, Spanish, French, Portuguese, and English
- Lightning fast with RTF 0.006 on M4 Pro and 66M parameters
- On-device TTS with privacy and zero network latency
- Open-weight model with commercial use allowed under OpenRAIL-M license
- User feedback highlights high quality but notes some pronunciation issues in Korean

**Discussion Highlights:** Users praised the model's speed and quality, though some noted pronunciation inaccuracies in Korean. There was demand for additional languages like German, Russian, and Arabic. The OpenRAIL-M license was criticized for being user-hostile.

---

## 26. [Performance improvements in llama.cpp over time](https://reddit.com/r/LocalLLaMA/comments/1q5dnyw/performance_improvements_in_llamacpp_over_time/)

**Author:** u/jacek2023 | **Upvotes:** 658 | **Comments:** 82 | **Date:** 2026-01-06

**Summary:** The Reddit post discusses performance improvements in llama.cpp over time, with a focus on recent upgrades and their impact on speed and efficiency. The discussion highlights significant progress in token generation speed and comparisons with other tools like ik_llama.cpp.

**Key Points:**
- Performance gains in llama.cpp have been significant over time.
- The improvements are particularly notable for NVIDIA GPUs.
- Token generation speed in llama.cpp is now close to ik_llama.cpp.
- Prompt processing remains slower compared to token generation.
- The community appreciates the progress and contributions.

**Discussion Highlights:** The discussion emphasizes the impressive performance gains in llama.cpp, especially for NVIDIA GPUs, and notes that while token generation speed has improved significantly, prompt processing is still relatively slower. The community consensus is positive, appreciating the progress and contributions made.

---

## 27. [Liquid Ai released LFM2.5, family of tiny on-device foundation models.](https://reddit.com/r/LocalLLaMA/comments/1q5a0if/liquid_ai_released_lfm25_family_of_tiny_ondevice/)

**Author:** u/Difficult-Cap-7527 | **Upvotes:** 305 | **Comments:** 54 | **Date:** 2026-01-05

**Summary:** Liquid AI released LFM2.5, a family of tiny on-device foundation models designed for reliable agentic applications. The models feature higher quality, lower latency, and broader modality support in the ~1B parameter class, with five open-weight model instances including general-purpose, Japanese-optimized, vision-language, audio-language, and base checkpoints.

**Key Points:**
- LFM2.5 is built on a device-optimized hybrid architecture with scaled pretraining from 10T to 28T tokens.
- The models include five instances: general-purpose instruct, Japanese-optimized chat, vision-language, native audio-language, and base checkpoints.
- User discussions highlight comparisons with other models like Qwen3-0.6B, noting the high data-to-parameter ratio and performance feedback.
- Some users appreciate the speed and capabilities but note issues with instruction following for special formats.
- There is a call for larger model sizes from some community members.

**Discussion Highlights:** The discussion highlights comparisons with other models, user experiences with speed and instruction following, and a mixed consensus on the need for larger model sizes.

---

## 28. [I just saw Intel embrace local LLM inference in their CES presentation](https://reddit.com/r/LocalLLaMA/comments/1q52miw/i_just_saw_intel_embrace_local_llm_inference_in/)

**Author:** u/Mundane-Light6394 | **Upvotes:** 143 | **Comments:** 71 | **Date:** 2026-01-05

**Summary:** Intel's CES presentation highlighted the importance of local LLM inference, emphasizing user privacy, control, and model responsiveness, contrasting with Nvidia's cloud-first strategy. The discussion suggests that local inference may have a significant future, supported by hardware advancements and community interest.

**Key Points:**
- Intel emphasizes local inference for privacy, control, and responsiveness
- Local inference may not be dead, with potential for growth
- Hardware advancements (e.g., Intel Arc Pro B50 GPU) support local inference
- Community interest and support for local inference is strong
- Unified memory and CXL technology could enhance local inference capabilities

**Discussion Highlights:** The discussion highlights strong community support for local inference, with many users believing it to be the future. There is optimism about hardware advancements making local inference more accessible and efficient. Some users also express hope for technologies like unified memory and CXL to further enhance local inference capabilities.

---

## 29. [Rubin uplifts from CES conference going on now](https://reddit.com/r/LocalLLaMA/comments/1q502bi/rubin_uplifts_from_ces_conference_going_on_now/)

**Author:** u/mr_zerolith | **Upvotes:** 223 | **Comments:** 95 | **Date:** 2026-01-05

**Summary:** The Reddit post discusses the Rubin uplifts announced at the CES conference, highlighting their performance and cost implications. Users express excitement but also note the lack of consumer-focused announcements.

**Key Points:**
- Rubin uplifts announced at CES with significant performance gains
- High cost implications, potentially around $100k per unit
- Impressive memory bandwidth figures
- Lack of consumer-focused announcements at CES
- Performance gains come with increased power requirements

**Discussion Highlights:** Users are excited about the performance gains and memory bandwidth of the Rubin uplifts but express concerns about the high cost and power requirements. There is also disappointment about the lack of consumer-focused announcements at CES.

---

## 30. [For the first time in 5 years, Nvidia will not announce any new GPUs at CES — company quashes RTX 50 Super rumors as AI expected to take center stage](https://reddit.com/r/LocalLLaMA/comments/1q4x5e9/for_the_first_time_in_5_years_nvidia_will_not/)

**Author:** u/FullstackSensei | **Upvotes:** 628 | **Comments:** 198 | **Date:** 2026-01-05

**Summary:** Nvidia will not announce new GPUs at CES, focusing instead on AI. The post discusses limited supply of new GPUs, potential re-release of older models, and rising hardware prices, expressing concerns about future upgrades.

**Key Points:**
- Nvidia will not announce new GPUs at CES, focusing on AI.
- Limited supply of RTX 5070Ti, 5080, and 5090, with rumors of RTX 3060 re-release.
- Rising prices of DDR5 RAM and storage, making upgrades expensive.
- Concerns about future hardware upgrades due to high costs and limited availability.
- Discussion highlights corporate greed and the need for alternative solutions.

**Discussion Highlights:** The discussion highlights frustration with corporate greed, the high cost of hardware, and the lack of new GPU announcements. Users express concerns about the future of local computing and the need for alternative solutions, such as increased competition from other manufacturers.

---

## 31. [[Release] EchoChamber - Add AI-Generated Audience Reactions to Your SillyTavern Stories &amp; Conversations](https://reddit.com/r/LocalLLaMA/comments/1q4tken/release_echochamber_add_aigenerated_audience/)

**Author:** u/mattjb | **Upvotes:** 106 | **Comments:** 27 | **Date:** 2026-01-05

**Summary:** EchoChamber is a new extension for SillyTavern that adds AI-generated audience reactions to stories and conversations, offering various chat styles and customization options.

**Key Points:**
- 10+ built-in chat styles including Discord, Twitter, and NSFW options
- Flexible backend support for local models and APIs
- Quick controls for toggling and adjusting the reaction feed
- Fully customizable with community-sharing options
- Automatic theme integration with SillyTavern

**Discussion Highlights:** The community reactions are mixed, with some users finding the extension amusing and others expressing concern or excitement about its implications.

---

## 32. [llama.cpp performance breakthrough for multi-GPU setups](https://reddit.com/r/LocalLLaMA/comments/1q4s8t3/llamacpp_performance_breakthrough_for_multigpu/)

**Author:** u/Holiday-Injury-9397 | **Upvotes:** 562 | **Comments:** 183 | **Date:** 2026-01-05

**Summary:** The ik_llama.cpp project has achieved a significant performance breakthrough for multi-GPU setups, delivering a 3x to 4x speed improvement in local LLM inference. This advancement allows for the utilization of multiple low-cost GPUs instead of expensive high-end enterprise cards.

**Key Points:**
- ik_llama.cpp introduces a new execution mode (split mode graph) for multi-GPU configurations.
- The breakthrough enables simultaneous and maximum utilization of multiple GPUs.
- This development is cost-effective, allowing the use of low-cost GPUs instead of expensive enterprise cards.
- Performance improvements are also noted on single GPU and CPU-only setups.
- The project is seen as a game-changer in the context of high GPU and memory prices.

**Discussion Highlights:** The community is highly positive about the breakthrough, with many users confirming performance improvements on various setups. There is a consensus that this development is significant for both multi-GPU and single-GPU configurations. Some users have noted specific performance metrics and comparisons with other tools like exllama and vllm.

---

## 33. [Falcon H1R 7B, a new reasoning model with 256k context window by the Technology Innovation Institute (TII) in Abu Dhabi](https://reddit.com/r/LocalLLaMA/comments/1q4jnq0/falcon_h1r_7b_a_new_reasoning_model_with_256k/)

**Author:** u/Nunki08 | **Upvotes:** 123 | **Comments:** 27 | **Date:** 2026-01-05

**Summary:** The post introduces Falcon H1R 7B, a new reasoning model with a 256k context window developed by the Technology Innovation Institute (TII) in Abu Dhabi. The model shows impressive benchmarks but faces skepticism about real-world performance. The discussion highlights concerns about overfitting and the need for new, private benchmarks.

**Key Points:**
- Falcon H1R 7B is a new reasoning model with a 256k context window by TII in Abu Dhabi
- The model shows impressive benchmarks but may not translate well to real-world usage
- There is a call for new, private benchmarks to evaluate models more effectively
- Some users note that the model tends to overthink
- There is interest in seeing more agentic benchmarks

**Discussion Highlights:** The discussion reveals skepticism about the model's real-world performance despite impressive benchmarks. Users express fatigue with overfitted models and call for new, private benchmarks. There is also interest in more agentic benchmarks and concerns about the model's tendency to overthink.

---

## 34. [What do we think about Gorgon Point (Ryzen AI 9 HX 470)?](https://reddit.com/r/LocalLLaMA/comments/1q4jc99/what_do_we_think_about_gorgon_point_ryzen_ai_9_hx/)

**Author:** u/Everlier | **Upvotes:** 143 | **Comments:** 44 | **Date:** 2026-01-05

**Summary:** The Reddit post discusses the new Gorgon Point APU, highlighting its support for high-speed memory and potential improvements over previous models. However, there are concerns about the accessibility of the required chips and the overall impact of frequent hardware updates.

**Key Points:**
- Gorgon Point supports DDR5-6400 and LPDDR5X-8533, improving performance for certain models.
- Manufacturers may face challenges in obtaining the necessary chips.
- Gorgon Point is a mid-cycle refresh, not a full replacement for Strix Halo.
- Some users express skepticism about the rapid pace of hardware updates.
- Comparisons are made with other models like Ryzen AI Max 395.

**Discussion Highlights:** The discussion highlights a mix of optimism about the performance improvements and skepticism regarding the practicality and accessibility of the new APU. There is also a consensus that frequent hardware updates may not always be beneficial.

---

## 35. [I built a visual AI workflow tool that runs entirely in your browser - Ollama, LM Studio, llama.cpp and Most cloud API's all work out of the box. Agents/Websearch/TTS/Etc.](https://reddit.com/r/LocalLLaMA/comments/1q4f0tm/i_built_a_visual_ai_workflow_tool_that_runs/)

**Author:** u/l33t-Mt | **Upvotes:** 153 | **Comments:** 58 | **Date:** 2026-01-05

**Summary:** The post introduces EmergentFlow, a visual AI workflow tool that runs entirely in the browser, supporting various local and cloud-based AI models. It is free to use with unlimited access to local models and offers a Pro tier for additional features. The tool aims to provide a sandbox for developing AI workflows without requiring complex setup.

**Key Points:**
- EmergentFlow is a visual node-based editor for AI workflows that runs in the browser.
- Supports Ollama, LM Studio, llama.cpp, and various cloud APIs like OpenAI and Gemini.
- Free tier allows unlimited use of local models; Pro tier offers additional server credits and collaboration features.
- Users compare it to tools like n8n and Flowise, questioning its unique advantages.
- Some users express skepticism about mixing local LLM usage with cloud API dependencies.

**Discussion Highlights:** The discussion includes comparisons to existing tools like n8n and Flowise, with some users questioning the necessity of EmergentFlow. Others highlight its ease of use and browser-based execution. There is also skepticism about combining local LLM usage with cloud-based APIs.

---

## 36. [Introducing Adaptive-P: A New Sampler for Creative Text Generation (llama.cpp PR)](https://reddit.com/r/LocalLLaMA/comments/1q42wtt/introducing_adaptivep_a_new_sampler_for_creative/)

**Author:** u/DragPretend7554 | **Upvotes:** 120 | **Comments:** 27 | **Date:** 2026-01-04

**Summary:** Adaptive-P is a new sampling method for creative text generation that addresses repetitive patterns by targeting a probability range and using a feedback loop to maintain diversity. It has been integrated into Kobold.cpp and is in staging for SillyTavern.

**Key Points:**
- Adaptive-P targets a probability range to encourage diverse token selection.
- It uses a feedback loop to adjust the target probability dynamically.
- The method prevents repetitive high-confidence chains in text generation.
- It has been merged into Kobold.cpp and is in staging for SillyTavern.
- Users report improved word diversity and logic preservation compared to traditional samplers.

**Discussion Highlights:** Users generally praise Adaptive-P for its effectiveness in creative tasks and its versatility in targeting different probability ranges. There is consensus on its superiority over traditional sampling methods like temperature and top-p.

---

## 37. [GLM-Image model from Z.ai is coming](https://reddit.com/r/LocalLLaMA/comments/1q41bw1/glmimage_model_from_zai_is_coming/)

**Author:** u/Ravencloud007 | **Upvotes:** 318 | **Comments:** 58 | **Date:** 2026-01-04

**Summary:** The Reddit post announces the upcoming GLM-Image model from Z.ai, which has generated significant interest in the community. The model is highly anticipated, with users expressing excitement about its potential capabilities and comparing it favorably to existing models.

**Key Points:**
- GLM-Image model from Z.ai is being introduced
- The model has generated significant community interest with 318 upvotes and 58 comments
- Users are excited about the model's potential, with one comment mentioning a feeling of 103 billion parameters
- Z.ai's image model is currently the community favorite
- There is a desire for a model that combines small size, ease of fine-tuning, and high quality

**Discussion Highlights:** The discussion highlights a strong community interest and excitement about the GLM-Image model. Users are comparing it favorably to existing models and expressing a desire for a model that balances size, ease of use, and quality. The overall consensus is positive, with anticipation for the model's release.

---

## 38. [MultiverseComputingCAI/HyperNova-60B · Hugging Face](https://reddit.com/r/LocalLLaMA/comments/1q3p9oz/multiversecomputingcaihypernova60b_hugging_face/)

**Author:** u/jacek2023 | **Upvotes:** 133 | **Comments:** 60 | **Date:** 2026-01-04

**Summary:** The Reddit post discusses HyperNova 60B, a model based on the gpt-oss-120b architecture with 59B parameters, 4.8B active parameters, and MXFP4 quantization. It supports configurable reasoning effort and requires less than 40GB of GPU memory. The discussion includes user experiences with hardware compatibility and performance metrics.

**Key Points:**
- HyperNova 60B is based on the gpt-oss-120b architecture with 59B parameters and 4.8B active parameters.
- It uses MXFP4 quantization and supports configurable reasoning effort (low, medium, high).
- The model requires less than 40GB of GPU memory.
- Users report successful deployment on 3090 + 5060 ti with 40GB total VRAM and performance metrics of around 3k prefill / 100 token generation.
- There is interest in the novel compression technology used, with requests for more information or papers.

**Discussion Highlights:** The discussion highlights user experiences with hardware compatibility, performance metrics, and interest in the novel compression technology used in HyperNova 60B. Users report successful deployment on specific GPU configurations and express curiosity about the underlying technology.

---

