# r/LocalLLaMA Reading Digest

**Period:** 2026-01-26 to 2026-01-26
**Posts Summarized:** 50
**Total Posts Analyzed:** 50

---

## 1. [I just won an Nvidia DGX Spark GB10 at an Nvidia hackathon. What do I do with it?](https://reddit.com/r/LocalLLaMA/comments/1qn3xig/i_just_won_an_nvidia_dgx_spark_gb10_at_an_nvidia/)

**Author:** u/brandon-i | **Upvotes:** 481 | **Comments:** 151 | **Date:** 2026-01-25

**Summary:** The author won an Nvidia DGX Spark GB10 at a hackathon and seeks advice on how to utilize it, having limited experience with fine-tuning models. They mention running a NextJS app that consumed significant memory and are open to suggestions for leveraging the new hardware. Key points include the author's background, their experience with NextJS, and community suggestions like exploring Nvidia's playbooks and running multiple NextJS apps. The discussion highlights include practical advice and humorous comments about selling the hardware.

---

## 2. [Your post is getting popular and we just featured it on our Discord!](https://reddit.com/r/LocalLLaMA/comments/1qkyex0/your_post_is_getting_popular_and_we_just_featured/)

**Author:** u/roculus | **Upvotes:** 563 | **Comments:** 57 | **Date:** 2026-01-23

**Summary:** The Reddit post announces that a user's contribution has been featured on Discord and they have received a special flair. The community discusses the annoyance of bot spam and questions the monetization of the Discord server. Key points include the bot's announcement, community annoyance with bot spam, speculation about monetization, the existence of a pinned thread about the Discord server, and humor about the bot's behavior. The community consensus is that the bot spam is annoying and suggests private messages to the OP instead of public posts.

---

## 3. [Am I the only one who feels that, with all the AI boom, everyone is basically doing the same thing?](https://reddit.com/r/LocalLLaMA/comments/1qk8zj1/am_i_the_only_one_who_feels_that_with_all_the_ai/)

**Author:** u/[deleted] | **Upvotes:** 397 | **Comments:** 189 | **Date:** 2026-01-22

**Summary:** The Reddit post discusses the redundancy in AI tools and applications during the AI boom, highlighting that many new tools are essentially reinventions of existing solutions. The discussion reflects a mix of enthusiasm for the technology and skepticism about the proliferation of shallow implementations. Key points include the redundancy of AI tools, the low barrier to entry leading to similar projects, and the consensus that the current phase is characterized by hype. Some developers are focusing on niche tools to address specific needs.

---

## 4. [Qwen have open-sourced the full family of Qwen3-TTS: VoiceDesign, CustomVoice, and Base, 5 models (0.6B &amp; 1.8B), Support for 10 languages](https://reddit.com/r/LocalLLaMA/comments/1qjul5t/qwen_have_opensourced_the_full_family_of_qwen3tts/)

**Author:** u/Nunki08 | **Upvotes:** 725 | **Comments:** 117 | **Date:** 2026-01-22

**Summary:** Qwen has open-sourced the Qwen3-TTS model family, including VoiceDesign, CustomVoice, and Base models in 0.6B and 1.8B sizes, supporting 10 languages. The release includes resources on GitHub, Hugging Face, and a demo space.

**Key Points:**
- Qwen3-TTS models (0.6B & 1.8B) released with support for 10 languages
- Resources available on GitHub, Hugging Face, blog, paper, and demo space
- Positive community reception with some concerns about voice quality
- Requests for compatibility with tools like llama.cpp
- Appreciation for Qwen's open-source contributions

**Discussion Highlights:** The community generally appreciates Qwen's open-source release, though some users noted concerns about the voice quality sounding like anime dubs. There were requests for compatibility with other tools like llama.cpp, and overall positive feedback for Qwen's contributions.

---

## 5. [Qwen dev on Twitter!!](https://reddit.com/r/LocalLLaMA/comments/1qjtyw8/qwen_dev_on_twitter/)

**Author:** u/Difficult-Cap-7527 | **Upvotes:** 749 | **Comments:** 60 | **Date:** 2026-01-22

**Summary:** The Reddit post discusses Qwen's TTS model announcement, which is reportedly from a vLLM leak. The community is sharing links and discussing its legitimacy.

**Key Points:**
- Qwen's TTS model announcement
- Model is from a vLLM leak
- Hugging Face link provided
- Community discussion on legitimacy

**Discussion Highlights:** The discussion highlights include a locked thread, mentions of the TTS model's source, and a shared Hugging Face link for further exploration.

---

## 6. [8x AMD MI50 32GB at 26 t/s (tg) with MiniMax-M2.1 and 15 t/s (tg) with GLM 4.7 (vllm-gfx906)](https://reddit.com/r/LocalLLaMA/comments/1qjaxfy/8x_amd_mi50_32gb_at_26_ts_tg_with_minimaxm21_and/)

**Author:** u/ai-infos | **Upvotes:** 316 | **Comments:** 128 | **Date:** 2026-01-21

**Summary:** The post details a cost-effective local inference setup using 8x AMD MI50 GPUs, achieving high token generation speeds with MiniMax-M2.1 and GLM 4.7 models. The setup is praised for its performance and affordability.

**Key Points:**
- MiniMax-M2.1 achieves 26.8 tokens/s output and 3000 tokens/s input with a context length of 196,608.
- GLM 4.7 achieves 15.6 tokens/s output and 3000 tokens/s input with a context length of 95,000.
- The total cost for 8 GPUs is $880, providing 256GB VRAM.
- Power draw is 280W idle and 1200W during inference.
- The setup is stable for long context use cases like coding agents.

**Discussion Highlights:** The community highly praises the setup for its cost-effectiveness and performance, with many expressing interest in replicating it. Some users note the difficulty in sourcing the GPUs at the mentioned price.

---

## 7. [Fix for GLM 4.7 Flash has been merged into llama.cpp](https://reddit.com/r/LocalLLaMA/comments/1qiwm3c/fix_for_glm_47_flash_has_been_merged_into_llamacpp/)

**Author:** u/jacek2023 | **Upvotes:** 316 | **Comments:** 86 | **Date:** 2026-01-21

**Summary:** The post announces that a fix for GLM 4.7 Flash has been merged into llama.cpp, with ongoing work on CUDA support. The community discusses performance metrics and user experiences.

**Key Points:**
- Fix for GLM 4.7 Flash merged into llama.cpp
- CUDA support in progress
- Performance metrics shared for different quantizations and GPUs
- Community feedback on model improvements and issues
- Discussion on CPU-only performance

**Discussion Highlights:** Users share performance data for GLM 4.7, noting improvements in model intelligence and discussing prompt processing speeds. Some users inquire about CPU-only performance and the validity of existing GGUF files.

---

## 8. [You have 64gb ram and 16gb VRAM; internet is permanently shut off: what 3 models are the ones you use?](https://reddit.com/r/LocalLLaMA/comments/1qids6a/you_have_64gb_ram_and_16gb_vram_internet_is/)

**Author:** u/Adventurous-Gold6413 | **Upvotes:** 549 | **Comments:** 306 | **Date:** 2026-01-20

**Summary:** The Reddit post discusses the best local models to use with 64GB RAM and 16GB VRAM when internet access is unavailable. The community highlights several models, with a focus on performance and versatility. Top comments suggest models like Gemma 3 27B, GLM 4.5 Air, and GPT-OSS 120B. GPT-OSS 120B is praised for its performance and versatility on the specified hardware. The discussion highlights a consensus around GPT-OSS 120B as a top choice due to its performance and fit for the given hardware. Other models like Gemma 3 27B and GLM 4.5 Air are also recommended. The community shows appreciation for the post and active participation in the discussion.

---

## 9. [768Gb Fully Enclosed 10x GPU Mobile AI Build](https://reddit.com/r/LocalLLaMA/comments/1qi4uj2/768gb_fully_enclosed_10x_gpu_mobile_ai_build/)

**Author:** u/SweetHomeAbalama0 | **Upvotes:** 920 | **Comments:** 273 | **Date:** 2026-01-20

**Summary:** The post describes a custom-built, high-performance AI system designed for running large MoE models and supporting graphic design tasks. The system features a Threadripper Pro 3995WX, 512GB DDR4, 10 GPUs (8x 3090 + 2x 5090), and is enclosed in a Thermaltake Core W200 case for mobility and protection. The total cost was approximately $17k, balancing performance and budget constraints.

**Key Points:**
- The system is designed for large MoE models and graphic design tasks.
- It features a Threadripper Pro 3995WX, 512GB DDR4, and 10 GPUs (8x 3090 + 2x 5090).
- The enclosure (Thermaltake Core W200) ensures mobility and protection from pets.
- The total cost was around $17k, balancing performance and budget.
- The post received significant engagement with 917 upvotes and 273 comments.

**Discussion Highlights:** The discussion highlights include humorous comments about the system's portability and power requirements, as well as appreciation for the innovative enclosure solution. The top comments reflect a mix of admiration for the build and playful remarks about its practicality.

---

## 10. [GLM 4.7 Flash official support merged in llama.cpp](https://reddit.com/r/LocalLLaMA/comments/1qhitrj/glm_47_flash_official_support_merged_in_llamacpp/)

**Author:** u/ayylmaonade | **Upvotes:** 371 | **Comments:** 60 | **Date:** 2026-01-19

**Summary:** The Reddit post announces the official support for GLM 4.7 Flash in llama.cpp, highlighting its community-driven development and performance improvements.

**Key Points:**
- GLM 4.7 Flash now officially supported in llama.cpp
- Support is community-driven, not by Z.ai developers
- Performance improvements noted, with some users reporting faster speeds without flash-attention
- Additional versions of the model are available on Hugging Face
- Post received recognition with a special flair and Discord feature

**Discussion Highlights:** The discussion highlights the community effort behind the implementation and mixed experiences with performance, with some users finding flash-attention slow and others noting speed improvements.

---

## 11. [My gpu poor comrades, GLM 4.7 Flash is your local agent](https://reddit.com/r/LocalLLaMA/comments/1qhii5v/my_gpu_poor_comrades_glm_47_flash_is_your_local/)

**Author:** u/__Maximum__ | **Upvotes:** 464 | **Comments:** 162 | **Date:** 2026-01-19

**Summary:** The Reddit post highlights the author's positive experience with GLM 4.7 Flash, an MoE model that performed reliably in an agentic framework, handling extensive tasks without errors. The author is eager to use it locally once GGUFs are available.

**Key Points:**
- GLM 4.7 Flash performed reliably in an agentic framework, handling extensive tasks without errors.
- The model is anticipated to be available locally soon via GGUFs.
- Comparisons with other models like Nemotron 30B and Qwen3 are discussed.
- Performance benchmarks indicate it may be as smart as SEED OSS 36B but with better performance due to MoE.
- Users are testing the model locally and sharing their experiences.

**Discussion Highlights:** The discussion includes comparisons with other models, performance benchmarks, and user experiences with local testing. There is a consensus that GLM 4.7 Flash is a promising model with good performance and reliability.

---

## 12. [zai-org/GLM-4.7-Flash · Hugging Face](https://reddit.com/r/LocalLLaMA/comments/1qh5wdq/zaiorgglm47flash_hugging_face/)

**Author:** u/Dark_Fire_12 | **Upvotes:** 749 | **Comments:** 230 | **Date:** 2026-01-19

**Summary:** The Reddit post announces the release of the GLM-4.7-Flash model on Hugging Face, generating significant community interest and discussion about its technical features and capabilities.

**Key Points:**
- The model uses MLA, reducing KV cache memory usage.
- It supports a full 200k context, making it accessible for many users.
- Community members express excitement and anticipation for the release.
- Some users note the model's size (30b) and its potential for high performance.

**Discussion Highlights:** The discussion highlights enthusiasm for the model's release, with users praising its technical features like MLA and large context support. There is a consensus on the model's promising capabilities and accessibility.

---

## 13. [4x AMD R9700 (128GB VRAM) + Threadripper 9955WX Build](https://reddit.com/r/LocalLLaMA/comments/1qgdb7f/4x_amd_r9700_128gb_vram_threadripper_9955wx_build/)

**Author:** u/NunzeCs | **Upvotes:** 351 | **Comments:** 104 | **Date:** 2026-01-18

**Summary:** The author built a high-performance system with 4x AMD R9700 GPUs (128GB VRAM) and a Threadripper 9955WX CPU, leveraging a 50% subsidy to stay within a ~10,000€ budget. The system is designed for running large AI models (120B+ parameters) locally, with benchmark results showing strong performance across various models. Key points include the system qualifying for a 50% digitalization subsidy, the setup including 4x AMD R9700 GPUs for a total of 128GB VRAM, and benchmark results demonstrating high performance. The discussion highlights the impressive hardware setup, with comments praising the VRAM capacity and cost-efficiency.

---

## 14. [Qwen 4 might be a long way off !? Lead Dev says they are "slowing down" to focus on quality.](https://reddit.com/r/LocalLLaMA/comments/1qfv1ms/qwen_4_might_be_a_long_way_off_lead_dev_says_they/)

**Author:** u/Difficult-Cap-7527 | **Upvotes:** 456 | **Comments:** 72 | **Date:** 2026-01-17

**Summary:** The Reddit post discusses Qwen 4's development, with the lead developer indicating a slowdown to focus on quality. The community generally appreciates this approach, though some caution against overinterpreting the announcement.

**Key Points:**
- Qwen 4 development is slowing down to prioritize quality
- Community largely supports the focus on quality over rapid releases
- Some users urge caution against speculative interpretations of the announcement
- The post gained significant traction with 456 upvotes and 72 comments
- Top comments highlight appreciation for quality-focused development

**Discussion Highlights:** The discussion reflects a consensus that prioritizing quality in Qwen 4's development is beneficial. Users appreciate the focus on meaningful improvements rather than incremental updates, though some advise against jumping to conclusions based on limited information.

---

## 15. [128GB VRAM quad R9700 server](https://reddit.com/r/LocalLLaMA/comments/1qfscp5/128gb_vram_quad_r9700_server/)

**Author:** u/Ulterior-Motive_ | **Upvotes:** 542 | **Comments:** 117 | **Date:** 2026-01-17

**Summary:** The author transitioned from MI100 GPUs to R9700 GPUs for a new server build, detailing the specifications and performance benchmarks of the setup. The build includes 128GB VRAM and 128GB RAM, costing less than an RTX 6000 Blackwell. The post highlights the cost-effectiveness and performance of the R9700 GPUs. Key points include the transition from MI100 to R9700 GPUs due to better performance and cost, detailed specifications of the server build, performance benchmarks showing high token processing rates, cost comparison with RTX 6000 Blackwell, and positive community feedback and engagement. The community responded positively, with comments appreciating the build and expressing interest in similar setups. Some users humorously noted the financial irresponsibility of such high-end builds.

---

## 16. [Best "End of world" model that will run on 24gb VRAM](https://reddit.com/r/LocalLLaMA/comments/1qfkn3a/best_end_of_world_model_that_will_run_on_24gb_vram/)

**Author:** u/gggghhhhiiiijklmnop | **Upvotes:** 342 | **Comments:** 180 | **Date:** 2026-01-17

**Summary:** The user is seeking recommendations for the best LLM model that can run on a PC with 24GB VRAM and 64GB RAM, aiming to hoard data like Wikipedia and other educational resources. The discussion highlights various suggestions, including prioritizing the best available model regardless of size and specific model recommendations like gemma3:27b.

**Key Points:**
- User wants to download and store large datasets like Wikipedia, Wiktionary, etc.
- Looking for LLM models that fit within 24GB VRAM and 64GB RAM constraints
- Suggestions include saving the best LLM available and running it off SSD if necessary
- Specific model recommendations: gemma3:27b with vision capabilities
- Advice to download actual Wikipedia backups for offline access

**Discussion Highlights:** The discussion emphasizes practicality, with a consensus on prioritizing the best available model even if it requires running off SSD. Specific model recommendations like gemma3:27b are highlighted, along with advice on downloading comprehensive datasets like Wikipedia backups.

---

## 17. [GPT-5.2 xhigh, GLM-4.7, Kimi K2 Thinking, DeepSeek v3.2 on Fresh SWE-rebench (December 2025)](https://reddit.com/r/LocalLLaMA/comments/1qefa7q/gpt52_xhigh_glm47_kimi_k2_thinking_deepseek_v32/)

**Author:** u/CuriousPlatypus1881 | **Upvotes:** 380 | **Comments:** 89 | **Date:** 2026-01-16

**Summary:** The post discusses the updated SWE-bench leaderboard results from December 2025, highlighting the performance of various AI models on GitHub PR tasks. Claude Opus 4.5 leads with a 63.3% resolved rate, followed closely by GPT-5.2 (extra high effort) at 61.5%. The post also notes the strong performance of open-source models like GLM-4.7.

**Key Points:**
- Claude Opus 4.5 leads the leaderboard with a 63.3% resolved rate.
- GPT-5.2 (extra high effort) follows closely at 61.5%.
- Gemini 3 Flash Preview outperforms Gemini 3 Pro Preview despite being smaller and cheaper.
- GLM-4.7 is the strongest open-source model, ranking alongside closed models like GPT-5.1-codex.
- GPT-OSS-120B shows significant performance improvement in high-effort reasoning mode.

**Discussion Highlights:** The discussion highlights excitement around the performance of open-source models like GLM-4.7 and anticipation for future releases like DeepSeek v4. There is also a consensus that this benchmark is more believable compared to others.

---

## 18. [I fucking love this community](https://reddit.com/r/LocalLLaMA/comments/1qee2de/i_fucking_love_this_community/)

**Author:** u/alhinai_03 | **Upvotes:** 524 | **Comments:** 54 | **Date:** 2026-01-16

**Summary:** The author expresses gratitude towards the open-source community for enabling them to run large language models on older hardware, highlighting the performance of the nemotron-3-nano-30B-a3b-iq4_nl model on a 10-year-old PC with limited VRAM.

**Key Points:**
- Gratitude towards the open-source community and contributors
- Running large models on older hardware with limited VRAM
- Achieving 14-13.5 tokens per second with a 30B parameter model
- Importance of system memory and MoE architecture for performance
- Community appreciation for optimization efforts

**Discussion Highlights:** The community appreciates the optimization efforts that allow running large models on older hardware, with specific mentions of the effectiveness of system RAM and MoE architecture. There is also interest in learning more about running large models on limited equipment.

---

## 19. [My story of underestimating /r/LocalLLaMA's thirst for VRAM](https://reddit.com/r/LocalLLaMA/comments/1qe2i88/my_story_of_underestimating_rlocalllamas_thirst/)

**Author:** u/EmPips | **Upvotes:** 1362 | **Comments:** 91 | **Date:** 2026-01-15

**Summary:** The Reddit post discusses the author's experience with the subreddit's high demand for VRAM, as indicated by the title and the popularity of the post. The discussion includes comments about the post's popularity, a humorous comparison to the California gold rush, and advice on hardware choices.

**Key Points:**
- The post gained significant attention with 1362 upvotes and 91 comments
- A comment humorously compares the situation to the California gold rush
- Discussion includes advice on hardware choices like the R9700 and 3090s
- The author received a special flair for their contribution

**Discussion Highlights:** The discussion highlights the post's popularity and includes a mix of humor, hardware advice, and community engagement. There is no clear consensus but a variety of perspectives on hardware choices and community interactions.

---

## 20. [Latest upgrade…A100 40 GB](https://reddit.com/r/LocalLLaMA/comments/1qe0cxc/latest_upgradea100_40_gb/)

**Author:** u/inserterikhere | **Upvotes:** 408 | **Comments:** 53 | **Date:** 2026-01-15

**Summary:** The user upgraded their gaming rig to an AI rig by purchasing a faulty A100 GPU for $1000, which worked perfectly upon installation. They previously used a 3090 and 7950x, and the community reacted positively with some expressing concerns about cooling.

**Key Points:**
- User transitioned from a gaming rig to an AI rig using existing parts.
- Purchased a faulty A100 GPU for $1000, which worked upon installation.
- Community expressed concerns about cooling the A100.
- Post received positive reception with 408 upvotes and 53 comments.

**Discussion Highlights:** The community reacted positively to the upgrade, with some users providing technical advice about cooling the A100 GPU. The post was featured on Discord, indicating its popularity.

---

## 21. [Soprano 1.1-80M released: 95% fewer hallucinations and 63% preference rate over Soprano-80M](https://reddit.com/r/LocalLLaMA/comments/1qcusnt/soprano_1180m_released_95_fewer_hallucinations/)

**Author:** u/eugenekwek | **Upvotes:** 325 | **Comments:** 54 | **Date:** 2026-01-14

**Summary:** The post announces Soprano 1.1, an improved version of the Soprano TTS model with 95% fewer hallucinations, better audio quality, and a 63% preference rate over the previous version. The model now supports longer sentences and has reduced audio artifacts.

**Key Points:**
- Soprano 1.1 reduces hallucinations by 95% and has a 63% preference rate over Soprano-80M
- The model supports sentences up to 30 seconds long, up from 15 seconds
- Audio artifacts and high-frequency noise have been reduced through further training
- The community appreciates the improvements and expresses interest in future developments like ONNX support
- Positive feedback highlights the model's usability and performance for its size

**Discussion Highlights:** The community response is overwhelmingly positive, with users praising the model's performance and usability. There is interest in additional features like ONNX support, and the developer's efforts are widely appreciated.

---

## 22. [NVIDIA's new 8B model is Orchestrator-8B, a specialized 8-billion-parameter AI designed not to answer everything itself, but to intelligently manage and route complex tasks to different tools (like web search, code execution, other LLMs) for greater efficiency](https://reddit.com/r/LocalLLaMA/comments/1qcuerc/nvidias_new_8b_model_is_orchestrator8b_a/)

**Author:** u/Fear_ltself | **Upvotes:** 722 | **Comments:** 130 | **Date:** 2026-01-14

**Summary:** NVIDIA's Orchestrator-8B is an 8-billion-parameter AI designed to manage and route complex tasks to various tools for greater efficiency. The post suggests this approach may be a step towards AGI by integrating separate components effectively.

**Key Points:**
- Orchestrator-8B is a specialized AI for task management and routing
- It aims to enhance efficiency by leveraging different tools and models
- The approach is seen as a potential path towards AGI
- Community reactions include humor and comparisons to existing frameworks

**Discussion Highlights:** The discussion highlights a mix of enthusiasm and skepticism, with some users drawing parallels to existing agentic frameworks and others humorously comparing the model to a 'middle manager.'

---

## 23. [GLM-Image is released!](https://reddit.com/r/LocalLLaMA/comments/1qc9m6x/glmimage_is_released/)

**Author:** u/foldl-li | **Upvotes:** 600 | **Comments:** 83 | **Date:** 2026-01-13

**Summary:** GLM-Image is a new image generation model with a hybrid autoregressive + diffusion decoder architecture. It excels in text-rendering and knowledge-intensive tasks while supporting various image-to-image tasks.

**Key Points:**
- Hybrid autoregressive + diffusion decoder architecture
- Excels in text-rendering and knowledge-intensive generation
- Supports image editing, style transfer, and multi-subject consistency
- MIT license with no restrictions
- Model size: 13GB diffusion model + 20GB text encoder

**Discussion Highlights:** The community appreciates the MIT license and the model's capabilities. There is interest in quantizing the model for easier use and discussions about its performance compared to other models.

---

## 24. [My wishes for 2026](https://reddit.com/r/LocalLLaMA/comments/1qbw325/my_wishes_for_2026/)

**Author:** u/jacek2023 | **Upvotes:** 653 | **Comments:** 179 | **Date:** 2026-01-13

**Summary:** The Reddit post discusses predictions for 2026, focusing on the feasibility of affordable GPUs with more than 32GB of memory. The community engages in a mix of hopeful and skeptical comments about this possibility.

**Key Points:**
- The post asks which predictions for 2026 are likely to happen first.
- A top comment humorously doubts the possibility of affordable GPUs with >32GB.
- Another comment references 'Qwen 4' and 'Mistral' as potential developments.
- The community shows a mix of optimism and skepticism about technological advancements in 2026.

**Discussion Highlights:** The discussion highlights a divide in opinions, with some users humorously dismissing the idea of affordable high-memory GPUs, while others reference specific models like 'Qwen 4' and 'Mistral' as potential advancements. The overall tone is a mix of hope and skepticism about technological progress in 2026.

---

## 25. [kyutai just introduced Pocket TTS: a 100M-parameter text-to-speech model with high-quality voice cloning that runs on your laptop—no GPU required](https://reddit.com/r/LocalLLaMA/comments/1qbpz5l/kyutai_just_introduced_pocket_tts_a_100mparameter/)

**Author:** u/Nunki08 | **Upvotes:** 397 | **Comments:** 93 | **Date:** 2026-01-13

**Summary:** Kyutai introduced Pocket TTS, a 100M-parameter text-to-speech model with high-quality voice cloning that runs on a laptop without requiring a GPU. The model is available on GitHub and Hugging Face, with a blog post and arXiv paper providing more details.

**Key Points:**
- Pocket TTS is a 100M-parameter model for high-quality voice cloning.
- It runs on a laptop without needing a GPU.
- Available on GitHub, Hugging Face, and detailed in a blog post and arXiv paper.
- Memory usage can balloon during generation, reaching up to 32 GB.
- Interest in finetuning for different languages and comparisons with other small models.

**Discussion Highlights:** The discussion highlights concerns about memory usage during generation, interest in multilingual support, and comparisons with other small models. Users are cautious about the practicality of small models and suggest alternatives for specific use cases.

---

## 26. [GitHub - deepseek-ai/Engram: Conditional Memory via Scalable Lookup: A New Axis of Sparsity for Large Language Models](https://reddit.com/r/LocalLLaMA/comments/1qb034t/github_deepseekaiengram_conditional_memory_via/)

**Author:** u/TKGaming_11 | **Upvotes:** 371 | **Comments:** 93 | **Date:** 2026-01-12

**Summary:** The Reddit post highlights a new paper from DeepSeek titled 'Engram: Conditional Memory via Scalable Lookup', which introduces an innovative approach to memory in large language models. The discussion praises the originality of the work and its potential impact on the field.

**Key Points:**
- DeepSeek's paper introduces a new axis of sparsity for large language models using conditional memory via scalable lookup.
- The n-gram embedding approach is noted for its O(1) lookup efficiency, complementing existing MoE methods.
- The community appreciates DeepSeek's consistent delivery of original and impactful research.
- The paper's technical details, such as using mHC (M=4) for ablations, suggest thorough derisking of the approach.
- The discussion highlights the potential biological plausibility of the approach, drawing parallels to animal and human memory processes.

**Discussion Highlights:** The community consensus is highly positive, with users praising the innovation and technical rigor of the paper. Key highlights include the efficiency of the n-gram embedding approach and its potential to complement existing methods like MoE. The discussion also notes the biological plausibility of the approach, suggesting it aligns with natural memory processes.

---

## 27. [LLM trained from scratch on 1800s London texts (1.2B params, 90GB dataset)](https://reddit.com/r/LocalLLaMA/comments/1qaawts/llm_trained_from_scratch_on_1800s_london_texts/)

**Author:** u/Remarkable-Trick-177 | **Upvotes:** 1071 | **Comments:** 114 | **Date:** 2026-01-11

**Summary:** The post introduces TimeCapsuleLLM, a 1.2B parameter language model trained exclusively on 1800-1875 London texts to minimize modern bias. The model demonstrates period-specific knowledge and behaviors, such as unfamiliarity with post-1875 concepts like telephones. The project is open-source and available on GitHub and Hugging Face.

**Key Points:**
- TimeCapsuleLLM is trained on 90GB of 1800-1875 London texts with no modern data or fine-tuning.
- The model exhibits period-specific behaviors, such as generating arguments relevant to the Catholic Emancipation Act of 1829.
- The model is unfamiliar with concepts introduced after 1875, like telephones.
- The project is open-source and available on GitHub and Hugging Face.
- Future steps include creating synthetic Q&A pairs from the dataset.

**Discussion Highlights:** The community response is largely positive, with users praising the project's uniqueness and expressing interest in similar historical language models. Some users shared their own experiences with training models on historical datasets, and there was humorous engagement with the model's 1875 knowledge cutoff.

---

## 28. [I bought a €9k GH200 “desktop” to save $1.27 on Claude Code (vLLM tuning notes)](https://reddit.com/r/LocalLLaMA/comments/1qa1guo/i_bought_a_9k_gh200_desktop_to_save_127_on_claude/)

**Author:** u/Reddactor | **Upvotes:** 695 | **Comments:** 178 | **Date:** 2026-01-11

**Summary:** The author built a high-end €9k GH200 desktop to run Claude Code locally, achieving better speeds and results than the cloud version. They shared optimized vLLM settings for dual 96GB systems and highlighted the cost savings and performance benefits of local execution.

**Key Points:**
- Author spent €9k on a GH200 desktop to run Claude Code locally.
- Achieved better speeds and results compared to cloud-based Claude Code.
- Shared optimized vLLM settings for dual 96GB systems.
- Highlighted cost savings and performance benefits of local execution.
- Discussed challenges with pipeline parallel mode and successful tuning with tensor parallel mode.

**Discussion Highlights:** The community appreciated the setup and shared humorous remarks about the cost and energy consumption. Some users expressed envy over missing out on similar deals, while others sought clarification on specific technical details.

---

## 29. [It works! Abliteration can reduce slop without training](https://reddit.com/r/LocalLLaMA/comments/1qa0w6c/it_works_abliteration_can_reduce_slop_without/)

**Author:** u/-p-e-w- | **Upvotes:** 401 | **Comments:** 129 | **Date:** 2026-01-11

**Summary:** The post discusses using abliteration to reduce 'slop' (flowery language) in LLM outputs without training, demonstrating success with the Mistral Nemo model using the Heretic tool. The process took 2.5 hours and produced a slop-reduced model available on Hugging Face.

**Key Points:**
- Abliteration can reduce slop in LLM outputs without finetuning
- Heretic tool was enhanced with prompt injection features for this task
- Mistral Nemo model showed clear semantic separation between layers 7-10
- The slop-reduced model is available on Hugging Face
- Process took 2.5 hours on an A6000 but could be faster with quantization

**Discussion Highlights:** The community had mixed reactions: some appreciated the reduced slop, while others felt it made the prose too dry. There was also discussion about whether this technique removes semantic meaning or just bans certain phrases. Some users created GGUF versions of the model.

---

## 30. [I clustered 3 DGX Sparks that NVIDIA said couldn't be clustered yet...took 1500 lines of C to make it work](https://reddit.com/r/LocalLLaMA/comments/1q8hqgd/i_clustered_3_dgx_sparks_that_nvidia_said_couldnt/)

**Author:** u/Ok-Pomegranate1314 | **Upvotes:** 896 | **Comments:** 147 | **Date:** 2026-01-09

**Summary:** The author successfully clustered three NVIDIA DGX Sparks, overcoming networking limitations by writing a custom NCCL plugin. This achievement allows distributed inference across all three nodes at high speeds, despite NVIDIA's official support only covering two-node clusters.

**Key Points:**
- Author clustered three DGX Sparks, exceeding NVIDIA's official support for two-node clusters.
- Developed a custom NCCL network plugin (~1500 lines of C) to handle subnet-aware NIC selection and raw RDMA implementation.
- Achieved distributed inference at 8+ GB/s over RDMA, demonstrating significant performance.
- The solution addresses a complex networking challenge, pushing the boundaries of standalone workstation clustering.
- The GitHub repository for the plugin is available for further exploration.

**Discussion Highlights:** The community praised the technical achievement, noting the difficulty of working with NCCL and the potential impact of this solution. Questions were raised about scalability and performance gains, indicating strong interest in the implementation details.

---

## 31. [The reason why RAM has become so expensive](https://reddit.com/r/LocalLLaMA/comments/1q8ckz0/the_reason_why_ram_has_become_so_expensive/)

**Author:** u/InvadersMustLive | **Upvotes:** 4587 | **Comments:** 383 | **Date:** 2026-01-09

**Summary:** The Reddit post discusses the significant increase in RAM prices, with users suggesting that this could be a strategic move to monopolize resources and create future demand. The discussion highlights concerns about economic viability and potential market manipulation.

**Key Points:**
- RAM prices have increased significantly, with some users reporting up to 10 times the previous cost.
- There is speculation that the price increase is a strategic move to monopolize RAM resources.
- The economic viability of other AI data centers, particularly in China, is being questioned.
- Users express skepticism about the sustainability of the current pricing trend.

**Discussion Highlights:** The discussion centers around the economic implications of rising RAM prices, with a consensus that the increase may be strategically motivated to control market demand and limit competition.

---

## 32. [DeepSeek V4 Coming](https://reddit.com/r/LocalLLaMA/comments/1q89g1i/deepseek_v4_coming/)

**Author:** u/External_Mood4719 | **Upvotes:** 504 | **Comments:** 110 | **Date:** 2026-01-09

**Summary:** DeepSeek is expected to release V4, a next-generation AI model with strong code-generation capabilities, outperforming mainstream models like Claude and GPT. The model shows improvements in handling long code prompts and data pattern understanding, with enhanced reasoning and reliability.

**Key Points:**
- DeepSeek V4 focuses on strong code-generation capabilities
- Outperforms existing models like Claude and GPT in code generation
- Improved handling of long code prompts and data patterns
- Enhanced reasoning and reliability for complex tasks
- Users appreciate DeepSeek's cost-effectiveness and performance

**Discussion Highlights:** Users express excitement and anticipation for V4, with some noting its potential disruption in the AI space. Positive feedback on DeepSeek's affordability and performance, with expectations of significant improvements in the new model.

---

## 33. [(The Information): DeepSeek To Release Next Flagship AI Model With Strong Coding Ability](https://reddit.com/r/LocalLLaMA/comments/1q88hdc/the_information_deepseek_to_release_next_flagship/)

**Author:** u/Nunki08 | **Upvotes:** 486 | **Comments:** 102 | **Date:** 2026-01-09

**Summary:** DeepSeek is set to release a new flagship AI model with strong coding capabilities, generating excitement and discussion in the community.

**Key Points:**
- DeepSeek's upcoming model focuses on strong coding ability
- Community excitement and anticipation for the new model
- Discussion about potential performance and benchmarks
- Mixed reactions including enthusiasm and skepticism
- Requests for maintaining role-playing abilities

**Discussion Highlights:** The community shows a mix of excitement and skepticism, with anticipation for the model's performance and benchmarks. Some users express enthusiasm for more AI models, while others are cautious about marketing claims.

---

## 34. [The NO FAKES Act has a "Fingerprinting" Trap that kills Open Source. We need to lobby for a Safe Harbor.](https://reddit.com/r/LocalLLaMA/comments/1q7qcux/the_no_fakes_act_has_a_fingerprinting_trap_that/)

**Author:** u/PostEasy7183 | **Upvotes:** 611 | **Comments:** 88 | **Date:** 2026-01-08

**Summary:** The NO FAKES Act proposes a 'digital replica right' that could hold developers liable for misuse of their tools, threatening open-source AI projects. The post urges lobbying for a 'Safe Harbor' provision to protect developers.

**Key Points:**
- The NO FAKES Act targets tools used for digital replicas, potentially making developers liable for misuse.
- Open-source AI projects, like TTS models, could be at risk due to statutory damages.
- The post calls for a 'Safe Harbor' provision to protect developers and open-source repositories.
- Action items include emailing or calling representatives to oppose the bill unless amended.
- Discussion highlights concerns about the bill's impact on innovation and the influence of big tech.

**Discussion Highlights:** The discussion emphasizes the potential negative impact on innovation and the need for a 'Safe Harbor' provision. Some commenters suggest that the bill could be influenced by big tech to stifle competition.

---

## 35. [Jensen Huang saying "AI" 121 times during the NVIDIA CES keynote - cut with one prompt](https://reddit.com/r/LocalLLaMA/comments/1q7d8bj/jensen_huang_saying_ai_121_times_during_the/)

**Author:** u/Prior-Arm-6705 | **Upvotes:** 948 | **Comments:** 147 | **Date:** 2026-01-08

**Summary:** A Reddit user created a compilation video of every instance Jensen Huang said 'AI' during NVIDIA's CES 2025 keynote, totaling 121 times. The process involved using open-source tools to download, parse, and edit the video locally.

**Key Points:**
- Jensen Huang said 'AI' 121 times during the CES 2025 keynote.
- The user employed open-source tools (Dive, yt-dlp-mcp, ffmpeg-mcp-lite) to automate the video compilation.
- The process was entirely local, with no cloud involvement.
- The result was described as 'hypnotic' and garnered significant engagement (948 upvotes, 147 comments).
- Top comments included humor, criticism of pricing, and references to tech culture.

**Discussion Highlights:** The discussion featured a mix of humor, criticism of NVIDIA's pricing, and appreciation for the technical execution. Some comments referenced tech culture (e.g., Gamers Nexus) and Jensen Huang's distinctive attire.

---

## 36. [16x AMD MI50 32GB at 10 t/s (tg) &amp; 2k t/s (pp) with Deepseek v3.2 (vllm-gfx906)](https://reddit.com/r/LocalLLaMA/comments/1q6n5vl/16x_amd_mi50_32gb_at_10_ts_tg_2k_ts_pp_with/)

**Author:** u/ai-infos | **Upvotes:** 460 | **Comments:** 238 | **Date:** 2026-01-07

**Summary:** The post discusses running Deepseek V3.2 AWQ 4-bit on 16x AMD MI50 32GB GPUs, achieving 10 tokens/sec output and 2000 tokens/sec input with a 69000 context length. The setup is cost-effective and aims to provide a local AGI solution without excessive spending.

**Key Points:**
- Performance: 10 tok/s output, 2000 tok/s input, 69000 context length
- Power draw: 550W idle / 2400W peak inference
- Goal: Cost-effective local AGI setup using 16x AMD MI50 32GB
- Future plans: Open-source test setup for 32 AMD MI50 32GB
- Community appreciation and cost-effectiveness highlighted in comments

**Discussion Highlights:** The discussion highlights the setup's popularity, its potential as a cost-effective alternative to CPU hardware, and practical considerations like power usage and noise levels. Users appreciate the cost-effectiveness for professional use and the potential for local AGI development.

---

## 37. [DeepSeek-R1’s paper was updated 2 days ago, expanding from 22 pages to 86 pages and adding a substantial amount of detail.](https://reddit.com/r/LocalLLaMA/comments/1q6c9wc/deepseekr1s_paper_was_updated_2_days_ago/)

**Author:** u/Nunki08 | **Upvotes:** 662 | **Comments:** 54 | **Date:** 2026-01-07

**Summary:** The Reddit post discusses the recent update to DeepSeek-R1’s paper, which expanded from 22 pages to 86 pages, adding significant detail. The discussion includes speculation about new architectures and the potential impact of linear attention research.

**Key Points:**
- DeepSeek-R1’s paper was updated from 22 pages to 86 pages, adding substantial detail.
- The update includes new architectural details and potential improvements.
- Discussion highlights include speculation about new architectures (e.g., dsv4 + r2) and the impact of linear attention research.
- The original paper lacked implementation specifics, and the update is expected to provide more insights into reasoning behavior.

**Discussion Highlights:** The discussion is focused on the implications of the paper update, with users speculating about new architectures and the potential for smaller model sizes. There is also interest in how linear attention research might enable more efficient training.

---

## 38. [A 30B Qwen Model Walks Into a Raspberry Pi… and Runs in Real Time](https://reddit.com/r/LocalLLaMA/comments/1q5m2n6/a_30b_qwen_model_walks_into_a_raspberry_pi_and/)

**Author:** u/ali_byteshape | **Upvotes:** 499 | **Comments:** 79 | **Date:** 2026-01-06

**Summary:** The post discusses the successful optimization of a 30B Qwen model to run efficiently on a Raspberry Pi 5, achieving 8.03 tokens per second while retaining 94.18% of BF16 quality. The optimization process focuses on balancing memory usage and performance, particularly on GPUs where kernel choice significantly impacts speed. Key points include the model's performance on a Raspberry Pi 5, the importance of kernel choice for GPU performance, and community feedback on potential improvements with hybrid transformers and cluster-based solutions. The discussion highlights the community's enthusiasm and shared experiences with the model.

---

## 39. [Performance improvements in llama.cpp over time](https://reddit.com/r/LocalLLaMA/comments/1q5dnyw/performance_improvements_in_llamacpp_over_time/)

**Author:** u/jacek2023 | **Upvotes:** 679 | **Comments:** 85 | **Date:** 2026-01-06

**Summary:** The Reddit post discusses performance improvements in llama.cpp over time, with a focus on NVIDIA GPUs and comparisons with other implementations like ik_llama.cpp. The community highlights significant progress in token generation speed.

**Key Points:**
- Performance gains are noted, particularly for NVIDIA GPUs.
- Comparisons are made with other implementations like ik_llama.cpp.
- Token generation speed has seen significant improvements.
- Prompt processing is noted to be slower compared to token generation.

**Discussion Highlights:** The discussion highlights the impressive progress in llama.cpp performance, especially in token generation speed, and compares it favorably with other implementations. There is a consensus on the significant improvements made over time.

---

## 40. [Liquid Ai released LFM2.5, family of tiny on-device foundation models.](https://reddit.com/r/LocalLLaMA/comments/1q5a0if/liquid_ai_released_lfm25_family_of_tiny_ondevice/)

**Author:** u/Difficult-Cap-7527 | **Upvotes:** 316 | **Comments:** 56 | **Date:** 2026-01-05

**Summary:** Liquid AI released LFM2.5, a family of tiny on-device foundation models designed for reliable agentic applications. The models feature higher quality, lower latency, and broader modality support in the ~1B parameter class, with five open-weight instances including general-purpose, Japanese-optimized, vision-language, audio-language, and base checkpoints.

**Key Points:**
- LFM2.5 builds on a device-optimized hybrid architecture with scaled pretraining (10T → 28T tokens) and expanded reinforcement learning.
- Five model instances are available, covering general-purpose, Japanese chat, vision-language, audio-language, and customizable base checkpoints.
- Performance metrics show a data ratio of 23,334:1 for 1.2B parameters trained on 28T tokens, compared to Qwen3-0.6B at 60,000:1.
- User feedback highlights speed and instruction-following challenges, with comparisons to other models like Qwen3-8B.
- Discussion includes suggestions for native FP8/FP4 training and requests for larger model variants.

**Discussion Highlights:** Users praised the model's speed and versatility but noted issues with instruction following for special formats. Comparisons with Qwen3 models were frequent, and there was a consensus on the need for larger variants or optimized training for on-device performance.

---

## 41. [For the first time in 5 years, Nvidia will not announce any new GPUs at CES — company quashes RTX 50 Super rumors as AI expected to take center stage](https://reddit.com/r/LocalLLaMA/comments/1q4x5e9/for_the_first_time_in_5_years_nvidia_will_not/)

**Author:** u/FullstackSensei | **Upvotes:** 628 | **Comments:** 195 | **Date:** 2026-01-05

**Summary:** Nvidia will not announce new GPUs at CES, focusing instead on AI. The company is facing supply issues with high-end GPUs and may re-release older models like the RTX 3060. Hardware prices, including DDR5 RAM and storage, are rising significantly.

**Key Points:**
- No new GPU announcements at CES, with a focus on AI
- Limited supply of high-end GPUs (RTX 5070Ti, 5080, 5090) and potential re-release of RTX 3060
- Rising hardware prices, including DDR5 RAM and storage
- Community frustration with corporate greed and lack of consumer focus
- Suggestions for alternative solutions, such as increased competition from China

**Discussion Highlights:** The discussion highlights frustration with Nvidia's focus on AI over consumer products, concerns about corporate greed, and suggestions for alternative solutions to address hardware shortages and high prices.

---

## 42. [llama.cpp performance breakthrough for multi-GPU setups](https://reddit.com/r/LocalLLaMA/comments/1q4s8t3/llamacpp_performance_breakthrough_for_multigpu/)

**Author:** u/Holiday-Injury-9397 | **Upvotes:** 580 | **Comments:** 204 | **Date:** 2026-01-05

**Summary:** The ik_llama.cpp project achieved a significant performance breakthrough for multi-GPU setups, delivering a 3x to 4x speed improvement in local LLM inference. This advancement allows for the use of multiple low-cost GPUs instead of expensive high-end cards, making it a game-changer for homelabs and server rooms.

**Key Points:**
- ik_llama.cpp introduced a new execution mode (split mode graph) for multi-GPU configurations.
- The breakthrough delivers a 3x to 4x speed improvement in local LLM inference.
- This advancement makes it feasible to use multiple low-cost GPUs instead of expensive high-end cards.
- Even on single GPU or CPU-only setups, ik_llama.cpp shows consistent 2x prompt processing speeds compared to llama.cpp.
- The performance improvements are significant enough to rival other optimized LLM inference solutions like exllama and vllm.

**Discussion Highlights:** The community is highly enthusiastic about the performance gains, with many users confirming the speed improvements on various setups. There is a consensus that ik_llama.cpp is now a strong competitor to other optimized LLM inference solutions. Some users reported bottlenecks in hybrid inference setups, indicating areas for further optimization.

---

## 43. [GLM-Image model from Z.ai is coming](https://reddit.com/r/LocalLLaMA/comments/1q41bw1/glmimage_model_from_zai_is_coming/)

**Author:** u/Ravencloud007 | **Upvotes:** 317 | **Comments:** 59 | **Date:** 2026-01-04

**Summary:** The Reddit post announces the upcoming GLM-Image model from Z.ai, which has generated significant interest in the community. The model is highly anticipated, with users expressing excitement about its potential capabilities and comparing it favorably to existing models.

**Key Points:**
- The GLM-Image model from Z.ai is being introduced and has gained attention.
- The model is expected to have a large number of parameters (e.g., 103b).
- Z.ai's image model is currently a community favorite.
- Users are curious about the computational resources required to use the model.
- There is a desire for a model that combines small size, ease of fine-tuning, and high quality.

**Discussion Highlights:** The community is enthusiastic about the GLM-Image model, with many users expressing anticipation for its release. There is a consensus that Z.ai's models are highly regarded, and users are hopeful that this new model will meet their expectations for performance and usability.

---

## 44. [Local LLMs vs breaking news: when extreme reality gets flagged as a hoax - the US/Venezuela event was too far-fetched](https://reddit.com/r/LocalLLaMA/comments/1q31ltd/local_llms_vs_breaking_news_when_extreme_reality/)

**Author:** u/ubrtnk | **Upvotes:** 382 | **Comments:** 194 | **Date:** 2026-01-03

**Summary:** The post discusses the challenges local LLMs face when processing extreme or unlikely breaking news events, such as the US attacking Venezuela. The author shares experiences with different LLMs, highlighting their initial skepticism and eventual acknowledgment of the event's reality.

**Key Points:**
- Local LLMs initially classified extreme breaking news as hoaxes or misinformation despite credible sources.
- Different LLMs (Qwen Research, Spark, GPT-OSS) exhibited varying degrees of skepticism and eventual acknowledgment.
- The event's extreme nature caused LLMs to question its reality, requiring additional evidence and reasoning rules.
- Discussion highlights include similar experiences with other unlikely events and the bias of LLMs towards familiar geopolitical events.
- Consensus suggests that LLMs may struggle with unfamiliar or extreme events, requiring more robust verification processes.

**Discussion Highlights:** The discussion highlights the struggles of LLMs in processing extreme or unlikely events, with users sharing similar experiences and noting the bias of LLMs towards familiar geopolitical events. There is a consensus that LLMs may require more robust verification processes to handle such events effectively.

---

## 45. [LeCun Says Llama 4 results "were fudged a little bit"](https://reddit.com/r/LocalLLaMA/comments/1q25070/lecun_says_llama_4_results_were_fudged_a_little/)

**Author:** u/MrPecunius | **Upvotes:** 364 | **Comments:** 89 | **Date:** 2026-01-02

**Summary:** Yann LeCun confirmed that Llama 4 benchmarks were manipulated, leading to organizational changes at Meta and a lack of follow-up on the promised model. The discussion highlights disappointment in Meta's strategic decisions and their impact on the AI community.

**Key Points:**
- LeCun confirms Llama 4 benchmark manipulation
- Zuckerberg sidelined Meta's GenAI organization, leading to departures
- No follow-up on the promised large Llama 4 model
- Community disappointment in Meta's strategic decisions
- Shared resources for further reading on the topic

**Discussion Highlights:** The discussion reflects a consensus on Meta's strategic missteps, with users expressing disappointment in the lack of progress and sharing additional resources. Some users also questioned how a well-positioned organization like Meta could falter while smaller labs thrive.

---

## 46. [Qwen-Image-2512](https://reddit.com/r/LocalLLaMA/comments/1q094a3/qwenimage2512/)

**Author:** u/Nunki08 | **Upvotes:** 721 | **Comments:** 122 | **Date:** 2025-12-31

**Summary:** The Reddit post introduces Qwen-Image-2512, a new model available on multiple platforms including Hugging Face, ModelScope, and GitHub. It provides links to guides, demos, and APIs, and highlights user experiences and community feedback.

**Key Points:**
- Qwen-Image-2512 is available on various platforms like Hugging Face, ModelScope, and GitHub.
- The model can be tried in Qwen Chat and has demos available on Hugging Face and ModelScope.
- Users have successfully run the model on low-end hardware without a GPU.
- The community appreciates the model as a new year's gift.
- Users are experimenting with creative image generation tasks.

**Discussion Highlights:** The discussion highlights include successful implementation on low-end hardware, appreciation for the model as a gift, and creative use cases like generating unique images.

---

## 47. [[In the Wild] Reverse-engineered a Snapchat Sextortion Bot: It’s running a raw Llama-7B instance with a 2048 token window.](https://reddit.com/r/LocalLLaMA/comments/1pzwlie/in_the_wild_reverseengineered_a_snapchat/)

**Author:** u/simar-dmg | **Upvotes:** 747 | **Comments:** 110 | **Date:** 2025-12-30

**Summary:** A user reverse-engineered a Snapchat sextortion bot and discovered it was running a raw Llama-7B instance with a 2048 token window. The bot was vulnerable to a persona-adoption jailbreak, revealing its configuration and malicious payload.

**Key Points:**
- The bot used a Llama-7B model with a 2048 token context window and high temperature setting.
- A persona-adoption jailbreak (Grandma Protocol) forced the bot to reveal its environment variables.
- The bot was running on minimal hardware to reduce costs and avoid API fees.
- The bot eventually revealed a malicious link it was programmed to hide.
- Discussion highlights skepticism about the accuracy of the bot's revealed information.

**Discussion Highlights:** The top comments express skepticism about the bot's revealed information, suggesting it may be entirely hallucinated. Some users question the feasibility of the bot's configuration and the validity of the data dump.

---

## 48. [Llama-3.3-8B-Instruct](https://reddit.com/r/LocalLLaMA/comments/1pz7bmv/llama338binstruct/)

**Author:** u/jacek2023 | **Upvotes:** 467 | **Comments:** 77 | **Date:** 2025-12-29

**Summary:** The post discusses the discovery and release of the Llama-3.3-8B-Instruct model, which was previously only available via Meta's API. The author found a way to download it through finetuning and has made it available in GGUF format.

**Key Points:**
- The Llama-3.3-8B-Instruct model was previously only available via Meta's API.
- The author discovered a way to download the model through finetuning.
- The model is now available in GGUF format on Hugging Face.
- The community is verifying the model's authenticity and performance.
- There is excitement and interest in the discovery within the community.

**Discussion Highlights:** The community is actively verifying the model's authenticity and performance through benchmarks and evaluations. There is significant excitement and appreciation for the author's discovery and release of the model.

---

## 49. [Z AI is going for an IPO on Jan 8 and set to raise $560 million. Z.ai is set to be the first AI-native LLM company to list on the global market.](https://reddit.com/r/LocalLLaMA/comments/1pz68fz/z_ai_is_going_for_an_ipo_on_jan_8_and_set_to/)

**Author:** u/Difficult-Cap-7527 | **Upvotes:** 343 | **Comments:** 121 | **Date:** 2025-12-29

**Summary:** Z AI is set to go public on January 8 with an IPO aiming to raise $560 million, marking it as the first AI-native LLM company to list globally. The announcement has sparked discussions about the future of open-source AI models.

**Key Points:**
- Z AI's IPO is scheduled for January 8, aiming to raise $560 million.
- Concerns about the future of open-source AI models post-IPO.
- Debate on whether Z AI will continue releasing open weight models.
- Mixed reactions from the community, with some expressing concerns about commercialization.

**Discussion Highlights:** The discussion highlights a divide in the community, with some users expressing concerns about the potential end of open-source contributions from Z AI, while others argue that commercial success is necessary for sustainability. There is no clear consensus, but the sentiment leans towards cautious optimism mixed with skepticism.

---

## 50. [Tencent just released WeDLM 8B Instruct on Hugging Face](https://reddit.com/r/LocalLLaMA/comments/1pyg4yt/tencent_just_released_wedlm_8b_instruct_on/)

**Author:** u/Difficult-Cap-7527 | **Upvotes:** 421 | **Comments:** 62 | **Date:** 2025-12-29

**Summary:** Tencent released WeDLM 8B Instruct on Hugging Face, a diffusion language model that outperforms vLLM-optimized Qwen3-8B in math reasoning tasks by 3-6 times. The model has garnered significant attention and positive feedback from the community.

**Key Points:**
- WeDLM 8B Instruct is a diffusion language model released by Tencent on Hugging Face.
- It runs 3-6 times faster than vLLM-optimized Qwen3-8B on math reasoning tasks.
- The model is released under the Apache 2.0 license.
- Community feedback highlights the potential of 7-8B models and the impressive benchmark scores of WeDLM.
- A 7B version of the model is also available.

**Discussion Highlights:** The community is excited about the release, noting the significant performance improvements and the potential of smaller models. There is a consensus on the promising future of 7-8B models and appreciation for the open-source license.

---

