# r/LocalLLaMA Reading Digest

**Period:** 2026-01-27 to 2026-01-27
**Posts Summarized:** 48
**Total Posts Analyzed:** 50

---

## 1. [216GB VRAM on the bench. Time to see which combination is best for Local LLM](https://reddit.com/r/LocalLLaMA/comments/1qni356/216gb_vram_on_the_bench_time_to_see_which/)

**Author:** u/eso_logic | **Upvotes:** 353 | **Comments:** 96 | **Date:** 2026-01-26

**Summary:** The post discusses benchmarking secondhand Tesla GPUs for Local LLM performance, comparing their efficiency against modern devices when parallelized. The author has developed a benchmarking suite to quantitatively evaluate these GPUs.

**Key Points:**
- Secondhand Tesla GPUs offer high VRAM at low cost.
- Performance of older GPUs in parallelized setups is being evaluated.
- Cooling and noise are significant concerns with older GPUs.
- Prompt processing speed is a critical factor for usability.
- Some older GPUs lack support or have limited capabilities.

**Discussion Highlights:** The discussion highlights concerns about usability, cooling, and noise levels of older GPUs. There is a consensus that while these GPUs may offer cost-effective VRAM, their performance in prompt processing and overall usability may be limited compared to modern alternatives.

---

## 2. [I just won an Nvidia DGX Spark GB10 at an Nvidia hackathon. What do I do with it?](https://reddit.com/r/LocalLLaMA/comments/1qn3xig/i_just_won_an_nvidia_dgx_spark_gb10_at_an_nvidia/)

**Author:** u/brandon-i | **Upvotes:** 501 | **Comments:** 151 | **Date:** 2026-01-25

**Summary:** The author won an Nvidia DGX Spark GB10 at a hackathon and seeks advice on how to use it, mentioning potential for running multiple NextJS applications and sharing a blog post about their project.

**Key Points:**
- Author is new to fine-tuning models
- Previously used the system for inferencing with a large model
- Potential to run multiple NextJS applications
- Shared a blog post about their hackathon project
- Top comments suggest running multiple apps, exploring Nvidia playbooks, and humorous advice to sell the hardware

**Discussion Highlights:** The discussion highlights include suggestions to run multiple NextJS applications, explore Nvidia's playbooks for guidance, and a humorous comment about selling the hardware for DDR5 memory.

---

## 3. [Your post is getting popular and we just featured it on our Discord!](https://reddit.com/r/LocalLLaMA/comments/1qkyex0/your_post_is_getting_popular_and_we_just_featured/)

**Author:** u/roculus | **Upvotes:** 571 | **Comments:** 57 | **Date:** 2026-01-23

**Summary:** The Reddit post announces that a user's post is popular and has been featured on Discord, with the user receiving a special flair. The community expresses annoyance at the bot's public posts, suggesting private messages instead.

**Key Points:**
- The bot announces the popularity of a user's post and its feature on Discord.
- The user receives a special flair for their contribution.
- The community finds the bot's public posts annoying and suggests private messages.
- There is a pinned thread about the Discord that has been active for months.
- Some users suspect the moderators are trying to monetize the community.

**Discussion Highlights:** The community consensus is that the bot's public posts are annoying and should be sent as private messages instead. There is also suspicion about monetization efforts by the moderators.

---

## 4. [Am I the only one who feels that, with all the AI boom, everyone is basically doing the same thing?](https://reddit.com/r/LocalLLaMA/comments/1qk8zj1/am_i_the_only_one_who_feels_that_with_all_the_ai/)

**Author:** u/[deleted] | **Upvotes:** 401 | **Comments:** 189 | **Date:** 2026-01-22

**Summary:** The Reddit post discusses the redundancy of AI tools and applications during the AI boom, highlighting that many new tools are less polished versions of existing ones. The discussion includes insights on the early days of AI technology and the enthusiasm driving shallow implementations. Key points include the low barrier to entry for AI development, the 'hype stage' of AI technology, and the shift from cryptocurrency to AI expertise. The discussion highlights the early days of AI technology and the enthusiasm driving shallow implementations, with a consensus that the current phase is the 'hype stage.'

---

## 5. [Qwen have open-sourced the full family of Qwen3-TTS: VoiceDesign, CustomVoice, and Base, 5 models (0.6B &amp; 1.8B), Support for 10 languages](https://reddit.com/r/LocalLLaMA/comments/1qjul5t/qwen_have_opensourced_the_full_family_of_qwen3tts/)

**Author:** u/Nunki08 | **Upvotes:** 724 | **Comments:** 118 | **Date:** 2026-01-22

**Summary:** Qwen has open-sourced the Qwen3-TTS model family, including VoiceDesign, CustomVoice, and Base models in 0.6B and 1.8B sizes, supporting 10 languages. The models are available on GitHub, Hugging Face, and include a demo and blog post.

**Key Points:**
- Qwen3-TTS models are open-sourced with 0.6B and 1.8B parameter sizes
- Supports 10 languages and includes VoiceDesign, CustomVoice, and Base models
- Available on GitHub, Hugging Face, with a demo and blog post
- Community appreciates the open-source release for local use
- Some concerns about English voice quality and model compatibility with tools like llama.cpp

**Discussion Highlights:** The community is generally positive about the open-source release, appreciating the ability to run models locally. However, there are concerns about the English voice quality sounding like anime dubs and requests for better compatibility with tools like llama.cpp. Some users also noted the high quality of the provided samples.

---

## 6. [Qwen dev on Twitter!!](https://reddit.com/r/LocalLLaMA/comments/1qjtyw8/qwen_dev_on_twitter/)

**Author:** u/Difficult-Cap-7527 | **Upvotes:** 743 | **Comments:** 60 | **Date:** 2026-01-22

**Summary:** The Reddit post discusses Qwen's TTS model announcement, which is revealed to be from the vLLM leak. The community shares a Hugging Face link for the model.

**Key Points:**
- Qwen's TTS model is announced.
- The model is from the vLLM leak.
- A Hugging Face link is provided for the model.
- The thread is locked as announcements are out.

**Discussion Highlights:** The community is focused on the TTS model's release, its source from the vLLM leak, and sharing relevant links.

---

## 7. [8x AMD MI50 32GB at 26 t/s (tg) with MiniMax-M2.1 and 15 t/s (tg) with GLM 4.7 (vllm-gfx906)](https://reddit.com/r/LocalLLaMA/comments/1qjaxfy/8x_amd_mi50_32gb_at_26_ts_tg_with_minimaxm21_and/)

**Author:** u/ai-infos | **Upvotes:** 319 | **Comments:** 128 | **Date:** 2026-01-21

**Summary:** The post details a cost-effective local inference setup using 8x AMD MI50 GPUs, achieving high token generation speeds with MiniMax-M2.1 and GLM 4.7 models. The setup is praised for its performance and affordability, with a total VRAM of 256GB for under $1k.

**Key Points:**
- MiniMax-M2.1 achieves 26.8 tokens per second (output) and 3000 tokens per second (input) with a context length of 196,608.
- GLM 4.7 achieves 15.6 tokens per second (output) and 3000 tokens per second (input) with a context length of 95,000.
- The setup costs $880 for 256GB VRAM and draws 280W idle / 1200W during inference.
- The goal is to create one of the most cost-effective solutions for fast, intelligent local inference.
- The community highly praises the setup for its performance and affordability.

**Discussion Highlights:** The community is highly enthusiastic about the setup, with comments highlighting its cost-effectiveness and performance. Some users express interest in replicating the setup but note that current prices for the GPUs are higher than those mentioned in the post.

---

## 8. [Fix for GLM 4.7 Flash has been merged into llama.cpp](https://reddit.com/r/LocalLLaMA/comments/1qiwm3c/fix_for_glm_47_flash_has_been_merged_into_llamacpp/)

**Author:** u/jacek2023 | **Upvotes:** 315 | **Comments:** 86 | **Date:** 2026-01-21

**Summary:** The post announces the integration of GLM 4.7 Flash into llama.cpp, highlighting its significance and ongoing CUDA support. Community feedback includes performance metrics and user experiences.

**Key Points:**
- GLM 4.7 Flash has been merged into llama.cpp
- CUDA support is in progress
- Performance metrics for GLM 4.7 on a 4090 GPU are provided
- Community feedback includes positive experiences and some performance concerns

**Discussion Highlights:** Users share performance data for GLM 4.7 on different hardware, discuss the quality of the model, and inquire about CPU-only performance. Overall, the community is positive about the update.

---

## 9. [You have 64gb ram and 16gb VRAM; internet is permanently shut off: what 3 models are the ones you use?](https://reddit.com/r/LocalLLaMA/comments/1qids6a/you_have_64gb_ram_and_16gb_vram_internet_is/)

**Author:** u/Adventurous-Gold6413 | **Upvotes:** 553 | **Comments:** 306 | **Date:** 2026-01-20

**Summary:** The Reddit post discusses the selection of local models for use with 64GB RAM and 16GB VRAM when internet access is unavailable. Users share their preferred models and experiences. Key points include recommendations for models like Gemma 3 27B, GLM 4.5 Air, and GPT-OSS 120B, with GPT-OSS-120B being praised for its performance and versatility. The discussion highlights a consensus around these models, emphasizing their performance and suitability for the specified hardware.

---

## 10. [768Gb Fully Enclosed 10x GPU Mobile AI Build](https://reddit.com/r/LocalLLaMA/comments/1qi4uj2/768gb_fully_enclosed_10x_gpu_mobile_ai_build/)

**Author:** u/SweetHomeAbalama0 | **Upvotes:** 922 | **Comments:** 273 | **Date:** 2026-01-20

**Summary:** The post describes a custom-built, fully enclosed mobile AI system with 10 GPUs, designed for running large MoE models and supporting graphic design tasks. The build cost approximately $17k and features a Threadripper Pro 3995WX, 512GB DDR4, and a mix of 3090 and 5090 GPUs. The system is enclosed in a Thermaltake Core W200 case for mobility and protection.

**Key Points:**
- The system is designed for running large MoE models and supporting graphic design tasks.
- It features a Threadripper Pro 3995WX, 512GB DDR4, and a mix of 3090 and 5090 GPUs.
- The build cost approximately $17k and is enclosed in a Thermaltake Core W200 case for mobility and protection.
- The enclosure was necessary to protect the hardware from pets and to ensure mobility.
- The discussion highlights the impressive nature of the build and some humorous comments about its portability.

**Discussion Highlights:** The discussion includes humorous comments about the system's portability and its impressive specifications. Some users appreciate the build's capabilities, while others joke about its size and power requirements.

---

## 11. [My gpu poor comrades, GLM 4.7 Flash is your local agent](https://reddit.com/r/LocalLLaMA/comments/1qhii5v/my_gpu_poor_comrades_glm_47_flash_is_your_local/)

**Author:** u/__Maximum__ | **Upvotes:** 463 | **Comments:** 162 | **Date:** 2026-01-19

**Summary:** The Reddit post highlights the effectiveness of GLM 4.7 Flash as a reliable local agent for tasks like coding and command execution, with users eagerly awaiting its local availability via GGUFs. The discussion includes comparisons with other models and notes on its performance and output quality.

**Key Points:**
- GLM 4.7 Flash is praised for its reliability in agentic tasks, such as coding and command execution.
- Users are excited about the upcoming GGUF release for local use.
- Comparisons with other models like Nemotron 30B and Qwen3 are mentioned.
- Performance benchmarks suggest it is competitive with larger models like SEED OSS 36B but with better efficiency.
- The model is noted for its deep thinking and high token output in sessions.

**Discussion Highlights:** The discussion highlights enthusiasm for GLM 4.7 Flash's performance and potential, with users comparing it favorably to other models and noting its efficiency and reliability in various tasks.

---

## 12. [zai-org/GLM-4.7-Flash · Hugging Face](https://reddit.com/r/LocalLLaMA/comments/1qh5wdq/zaiorgglm47flash_hugging_face/)

**Author:** u/Dark_Fire_12 | **Upvotes:** 751 | **Comments:** 230 | **Date:** 2026-01-19

**Summary:** The Reddit post announces the release of GLM-4.7-Flash model, generating significant community interest with 751 upvotes and 230 comments. Users express excitement about its features and potential applications.

**Key Points:**
- GLM-4.7-Flash model release announced
- Uses MLA architecture for efficient KV cache memory usage
- Supports full 200k context length
- Community excitement about 30B model capabilities
- Mixed reactions about model size preferences

**Discussion Highlights:** The community shows strong enthusiasm for the new model release, particularly highlighting its memory efficiency and context length capabilities. Some users express nostalgia for larger models while appreciating the current offering's potential.

---

## 13. [4x AMD R9700 (128GB VRAM) + Threadripper 9955WX Build](https://reddit.com/r/LocalLLaMA/comments/1qgdb7f/4x_amd_r9700_128gb_vram_threadripper_9955wx_build/)

**Author:** u/NunzeCs | **Upvotes:** 351 | **Comments:** 104 | **Date:** 2026-01-18

**Summary:** The author built a high-performance system with 4x AMD R9700 GPUs (128GB VRAM) and a Threadripper 9955WX CPU, leveraging a 50% subsidy to stay within a ~10,000€ budget. The system is designed for running large AI models locally, with benchmark results showing strong performance across various models. Key points include the system's purpose for local AI model inference, the budget and subsidy details, strong benchmark performance, and positive community reactions. The discussion highlights the impressive hardware setup and trends in high-VRAM configurations.

---

## 14. [Qwen 4 might be a long way off !? Lead Dev says they are "slowing down" to focus on quality.](https://reddit.com/r/LocalLLaMA/comments/1qfv1ms/qwen_4_might_be_a_long_way_off_lead_dev_says_they/)

**Author:** u/Difficult-Cap-7527 | **Upvotes:** 456 | **Comments:** 72 | **Date:** 2026-01-17

**Summary:** The Reddit post discusses the potential delay in Qwen 4 development, with the lead developer indicating a focus on quality over speed. The community generally supports this approach, appreciating the emphasis on quality improvements.

**Key Points:**
- Qwen 4 development may be delayed as the team focuses on quality.
- The lead developer mentioned 'slowing down' to prioritize quality.
- Community reactions are largely positive, supporting the focus on quality.
- Some users caution against jumping to conclusions based on limited information.
- There is appreciation for meaningful advancements over incremental updates.

**Discussion Highlights:** The discussion highlights a consensus that focusing on quality is beneficial for the Qwen series. Users appreciate the developer's approach and caution against spreading unconfirmed rumors. The overall sentiment is supportive of taking the necessary time to improve the model meaningfully.

---

## 15. [128GB VRAM quad R9700 server](https://reddit.com/r/LocalLLaMA/comments/1qfscp5/128gb_vram_quad_r9700_server/)

**Author:** u/Ulterior-Motive_ | **Upvotes:** 539 | **Comments:** 117 | **Date:** 2026-01-17

**Summary:** The author transitioned from MI100 GPUs to R9700 GPUs for a new server build, citing better performance and cost efficiency. The build includes 128GB VRAM and 128GB RAM, with detailed specifications and benchmarks provided. Key points include the transition from MI100 to R9700 GPUs, detailed specifications of the new server build, performance benchmarks showing high token processing rates, and community appreciation and humor about financial irresponsibility. The community responded positively, with top comments appreciating the build and humorously acknowledging the financial investment required.

---

## 16. [Best "End of world" model that will run on 24gb VRAM](https://reddit.com/r/LocalLLaMA/comments/1qfkn3a/best_end_of_world_model_that_will_run_on_24gb_vram/)

**Author:** u/gggghhhhiiiijklmnop | **Upvotes:** 341 | **Comments:** 180 | **Date:** 2026-01-17

**Summary:** The user seeks recommendations for the best LLM model that can run on a PC with 24GB VRAM and 64GB RAM, aiming to hoard data like Wikipedia and other educational resources. The discussion highlights various models and practical considerations for end-of-world scenarios.

**Key Points:**
- User wants a model that fits within 24GB VRAM and 64GB RAM.
- Suggestions include saving the best possible LLM and running it off SSD if necessary.
- Gemma3:27b is recommended for its capabilities, including vision.
- Midnight Miku is suggested for entertainment purposes.
- Downloading actual Wikipedia backups is advised for data preservation.

**Discussion Highlights:** The discussion emphasizes practicality, with a focus on saving the best possible LLM and considering alternative storage solutions like SSDs. Gemma3:27b is highlighted for its advanced features, while other suggestions include entertainment options and data preservation strategies.

---

## 17. [I fucking love this community](https://reddit.com/r/LocalLLaMA/comments/1qee2de/i_fucking_love_this_community/)

**Author:** u/alhinai_03 | **Upvotes:** 528 | **Comments:** 54 | **Date:** 2026-01-16

**Summary:** The post expresses gratitude towards the open-source community for enabling the user to run large language models on a 10-year-old PC with limited hardware, highlighting the efficiency and optimization achieved through community efforts.

**Key Points:**
- The user appreciates the open-source community for their contributions to tools like llama.cpp and vllm.
- The user runs a 30B parameter model at 14-13.5 tokens per second on a PC with only 4GB VRAM.
- Key factors for performance include sufficient system memory and using Mixture of Experts (MoE) architecture models.
- The community's optimization efforts are praised for making such performance possible on older hardware.
- The discussion highlights the practicality of using system RAM and MoE models for running large models on limited hardware.

**Discussion Highlights:** The community consensus emphasizes the importance of system memory and MoE architecture for running large models efficiently on limited hardware. Users also express a desire for more VRAM and RAM to run state-of-the-art models.

---

## 18. [My story of underestimating /r/LocalLLaMA's thirst for VRAM](https://reddit.com/r/LocalLLaMA/comments/1qe2i88/my_story_of_underestimating_rlocalllamas_thirst/)

**Author:** u/EmPips | **Upvotes:** 1358 | **Comments:** 91 | **Date:** 2026-01-15

**Summary:** The post highlights the author's underestimation of the r/LocalLLaMA community's demand for VRAM, with discussions focusing on hardware recommendations and market dynamics.

**Key Points:**
- Author underestimated community's VRAM demand
- Discord feature and special flair mentioned
- Hardware recommendations (3090s or R9700)
- Market behavior discussion (selling cards)
- Image shared in comments

**Discussion Highlights:** The discussion includes hardware recommendations, market behavior insights, and community engagement (Discord feature, special flair).

---

## 19. [Latest upgrade…A100 40 GB](https://reddit.com/r/LocalLLaMA/comments/1qe0cxc/latest_upgradea100_40_gb/)

**Author:** u/inserterikhere | **Upvotes:** 407 | **Comments:** 53 | **Date:** 2026-01-15

**Summary:** The user upgraded their gaming rig to an AI rig by purchasing a faulty A100 GPU for $1000, which worked perfectly upon installation. They detailed their journey from using a 5070ti to eventually acquiring the A100, despite initial plans to sell their old parts.

**Key Points:**
- User transitioned from a gaming rig to an AI rig using existing parts.
- Purchased an A100 GPU listed as faulty for $1000, which worked upon installation.
- Community expressed concerns about cooling the A100 GPU.
- Post received positive reception with 407 upvotes and 53 comments.
- User shared their upgrade journey and the successful integration of the A100.

**Discussion Highlights:** The community reacted positively to the post, with some users expressing concerns about cooling the A100 GPU. There was also a humorous reference to a meme involving Jensen Huang, CEO of NVIDIA.

---

## 20. [Soprano 1.1-80M released: 95% fewer hallucinations and 63% preference rate over Soprano-80M](https://reddit.com/r/LocalLLaMA/comments/1qcusnt/soprano_1180m_released_95_fewer_hallucinations/)

**Author:** u/eugenekwek | **Upvotes:** 326 | **Comments:** 54 | **Date:** 2026-01-14

**Summary:** The post announces Soprano 1.1, an improved version of the Soprano TTS model with significant reductions in hallucinations and audio artifacts, along with increased sentence length support and user preference.

**Key Points:**
- Soprano 1.1 reduces hallucinations by 95% and audio artifacts significantly.
- The model supports sentences up to 30 seconds long, double the previous limit.
- Blind study shows 63% preference for Soprano 1.1 over the original.
- Positive community feedback on the model's performance for its size.
- Inquiries about future support like ONNX compatibility.

**Discussion Highlights:** The community is impressed with the model's performance, especially given its small size (80M parameters). There is interest in additional features like ONNX support, and overall appreciation for the developer's efforts.

---

## 21. [NVIDIA's new 8B model is Orchestrator-8B, a specialized 8-billion-parameter AI designed not to answer everything itself, but to intelligently manage and route complex tasks to different tools (like web search, code execution, other LLMs) for greater efficiency](https://reddit.com/r/LocalLLaMA/comments/1qcuerc/nvidias_new_8b_model_is_orchestrator8b_a/)

**Author:** u/Fear_ltself | **Upvotes:** 717 | **Comments:** 130 | **Date:** 2026-01-14

**Summary:** NVIDIA's Orchestrator-8B is an 8-billion-parameter AI designed to manage and route complex tasks to various tools, sparking discussions on its role in creating functional systems and comparisons to middle managers.

**Key Points:**
- Orchestrator-8B is a specialized AI for task management and routing
- It aims to create functional systems by connecting with other tools and models
- Comparisons to middle managers and existing frameworks like Claude code style agentic frameworks
- Discussion on the potential of such models in achieving AGI by integrating separate pieces

**Discussion Highlights:** The discussion includes humorous comparisons to middle managers and mentions of Claude code style agentic frameworks as potential next steps in AI development.

---

## 22. [GLM-Image is released!](https://reddit.com/r/LocalLLaMA/comments/1qc9m6x/glmimage_is_released/)

**Author:** u/foldl-li | **Upvotes:** 599 | **Comments:** 83 | **Date:** 2026-01-13

**Summary:** GLM-Image is a new image generation model with a hybrid autoregressive + diffusion decoder architecture. It excels in text-rendering and knowledge-intensive tasks while supporting various image-to-image tasks.

**Key Points:**
- Hybrid autoregressive + diffusion decoder architecture
- Strong performance in text-rendering and knowledge-intensive tasks
- Supports image editing, style transfer, and multi-subject consistency
- MIT license with no restrictions
- High model size (13GB diffusion model + 20GB text encoder)

**Discussion Highlights:** The community appreciates the MIT license and the model's capabilities. There is interest in quantizing the model for easier use and discussions about its performance compared to other models.

---

## 23. [My wishes for 2026](https://reddit.com/r/LocalLLaMA/comments/1qbw325/my_wishes_for_2026/)

**Author:** u/jacek2023 | **Upvotes:** 656 | **Comments:** 179 | **Date:** 2026-01-13

**Summary:** The Reddit post discusses wishes and predictions for 2026, focusing on technological advancements like affordable GPUs with more than 32GB memory. The community engages in a mix of hopeful and skeptical comments about these possibilities.

**Key Points:**
- The post asks which technological advancements will happen first in 2026.
- A significant comment highlights the desire for affordable GPUs with more than 32GB memory.
- Other comments express skepticism about the feasibility of these advancements.
- Mentions of specific AI models like Qwen 4 and Mistral as potential advancements.
- The post gained popularity, being featured on Discord and receiving a special flair.

**Discussion Highlights:** The discussion is centered around the feasibility of technological advancements in 2026, with a mix of optimism and skepticism. The community seems to agree that while some advancements like new AI models are plausible, others like affordable high-memory GPUs are seen as less likely.

---

## 24. [kyutai just introduced Pocket TTS: a 100M-parameter text-to-speech model with high-quality voice cloning that runs on your laptop—no GPU required](https://reddit.com/r/LocalLLaMA/comments/1qbpz5l/kyutai_just_introduced_pocket_tts_a_100mparameter/)

**Author:** u/Nunki08 | **Upvotes:** 405 | **Comments:** 93 | **Date:** 2026-01-13

**Summary:** Kyutai introduced Pocket TTS, a 100M-parameter text-to-speech model with high-quality voice cloning that runs on a laptop without requiring a GPU. The model is available on GitHub and Hugging Face, with a blog post and arXiv paper providing more details.

**Key Points:**
- Pocket TTS is a 100M-parameter TTS model with high-quality voice cloning.
- It runs on a laptop without needing a GPU.
- Available on GitHub, Hugging Face, and detailed in a blog post and arXiv paper.
- Memory usage can balloon during generation, reaching up to 32 GB.
- Interest in finetuning for different languages and comparisons with other small models.

**Discussion Highlights:** The discussion highlights concerns about memory usage during generation, interest in multilingual support, and comparisons with other small TTS models. Users are cautious about the practicality of small models and their performance.

---

## 25. [GitHub - deepseek-ai/Engram: Conditional Memory via Scalable Lookup: A New Axis of Sparsity for Large Language Models](https://reddit.com/r/LocalLLaMA/comments/1qb034t/github_deepseekaiengram_conditional_memory_via/)

**Author:** u/TKGaming_11 | **Upvotes:** 375 | **Comments:** 93 | **Date:** 2026-01-12

**Summary:** The Reddit post highlights a GitHub project by DeepSeek-AI called 'Engram,' which introduces a novel approach to conditional memory in large language models using scalable lookup. The discussion praises the originality and technical depth of the work.

**Key Points:**
- DeepSeek-AI's 'Engram' project introduces a new axis of sparsity for large language models via conditional memory.
- The approach uses n-gram embedding and O(1) lookup, complementing existing MoE methods.
- The community appreciates the originality and technical rigor of DeepSeek's contributions.
- Comparisons are drawn to biological memory systems, suggesting potential broader implications.

**Discussion Highlights:** The discussion is overwhelmingly positive, with users highlighting the innovative nature of the n-gram embedding approach and its potential to complement existing methods like MoE. There is a consensus on the technical depth and originality of DeepSeek's work, with some users drawing parallels to biological memory systems.

---

## 26. [LLM trained from scratch on 1800s London texts (1.2B params, 90GB dataset)](https://reddit.com/r/LocalLLaMA/comments/1qaawts/llm_trained_from_scratch_on_1800s_london_texts/)

**Author:** u/Remarkable-Trick-177 | **Upvotes:** 1069 | **Comments:** 114 | **Date:** 2026-01-11

**Summary:** The post introduces TimeCapsuleLLM, a 1.2B parameter language model trained exclusively on 1800-1875 London texts to minimize modern bias. The model demonstrates period-specific knowledge and limitations, such as unfamiliarity with post-1875 concepts like telephones. The project is open-source and available on GitHub and Hugging Face.

**Key Points:**
- TimeCapsuleLLM is trained on 90GB of 1800-1875 London texts with no modern data or fine-tuning.
- The model shows period-appropriate responses, like arguing against the Roman Catholic Church and misunderstanding telephones.
- The project is open-source, with code on GitHub and the model on Hugging Face.
- Future work includes creating synthetic Q&A pairs from the dataset.
- The community appreciates the project, with comments highlighting its uniqueness and potential.

**Discussion Highlights:** The community response is overwhelmingly positive, with users praising the project's creativity and potential. Some commenters share similar interests in training models on historical data, while others humorously reference the model's 1875 cutoff date.

---

## 27. [I bought a €9k GH200 “desktop” to save $1.27 on Claude Code (vLLM tuning notes)](https://reddit.com/r/LocalLLaMA/comments/1qa1guo/i_bought_a_9k_gh200_desktop_to_save_127_on_claude/)

**Author:** u/Reddactor | **Upvotes:** 694 | **Comments:** 178 | **Date:** 2026-01-11

**Summary:** The author built a high-end GH200 desktop system to run Claude Code locally, achieving better performance and cost savings compared to cloud-based solutions. They shared optimized vLLM settings for dual 96GB systems and highlighted the benefits of local code reviews.

**Key Points:**
- Author spent €9k on a GH200 desktop to run Claude Code locally
- Achieved better speeds than cloud-based Claude Code with Sonnet
- Shared optimized vLLM settings for dual 96GB systems
- Highlighted cost savings and performance benefits of local setup
- Community praised the setup but joked about the high initial cost

**Discussion Highlights:** The community appreciated the detailed setup and shared jokes about the high initial cost, emphasizing the fun and learning experience. Some users expressed envy over missing out on similar deals.

---

## 28. [It works! Abliteration can reduce slop without training](https://reddit.com/r/LocalLLaMA/comments/1qa0w6c/it_works_abliteration_can_reduce_slop_without/)

**Author:** u/-p-e-w- | **Upvotes:** 402 | **Comments:** 129 | **Date:** 2026-01-11

**Summary:** The post discusses using abliteration to reduce 'slop' (flowery, cliched language) in LLM outputs without training. The author modified the Heretic tool to create a slop-reducing configuration, demonstrating its effectiveness on the Mistral Nemo model.

**Key Points:**
- Abliteration can reduce slop in LLM outputs without training
- Heretic tool was modified to support prompt prefixes/suffixes for slop reduction
- Mistral Nemo model showed clear semantic separation between layers 7 and 10
- Process took 2.5 hours on an A6000 but can be faster with quantization
- Results show reduced slop but mixed opinions on effectiveness

**Discussion Highlights:** The discussion highlights mixed opinions on the effectiveness of slop reduction. Some users prefer the reduced slop, while others find it makes the prose dry. There is also curiosity about whether the technique reduces semantic meaning or outright bans certain phrases.

---

## 29. [I clustered 3 DGX Sparks that NVIDIA said couldn't be clustered yet...took 1500 lines of C to make it work](https://reddit.com/r/LocalLLaMA/comments/1q8hqgd/i_clustered_3_dgx_sparks_that_nvidia_said_couldnt/)

**Author:** u/Ok-Pomegranate1314 | **Upvotes:** 891 | **Comments:** 147 | **Date:** 2026-01-09

**Summary:** The author successfully clustered three NVIDIA DGX Sparks, overcoming networking limitations by writing a custom NCCL plugin. This achievement, involving complex low-level programming, enables distributed inference across all three nodes at high speeds.

**Key Points:**
- Author clustered three DGX Sparks despite NVIDIA's official support for only two.
- Developed a custom NCCL network plugin to handle subnet-aware NIC selection and raw RDMA implementation.
- Achieved distributed inference at 8+ GB/s over RDMA, showcasing significant technical prowess.
- The solution involved extensive low-level debugging and is shared on GitHub for community use.
- Community response highlights the impressiveness and potential impact of the work.

**Discussion Highlights:** The community praised the technical achievement, with comments highlighting the difficulty of working with NCCL and the potential significance of the solution. Questions about scalability and performance improvements were also raised.

---

## 30. [The reason why RAM has become so expensive](https://reddit.com/r/LocalLLaMA/comments/1q8ckz0/the_reason_why_ram_has_become_so_expensive/)

**Author:** u/InvadersMustLive | **Upvotes:** 4589 | **Comments:** 383 | **Date:** 2026-01-09

**Summary:** The Reddit post discusses the significant increase in RAM prices, with comments highlighting concerns about monopolization by OpenAI and the economic impact on data centers, particularly in China.

**Key Points:**
- RAM prices have increased significantly, with some users reporting a 10x increase.
- OpenAI is accused of monopolizing RAM to create future demand and make other AI data centers economically unviable.
- The economic impact is particularly severe for Chinese data centers.
- Some users express skepticism about the sustainability of the price increase.

**Discussion Highlights:** The discussion highlights concerns about monopolistic practices by OpenAI and the economic impact on data centers. There is a consensus that the price increase is significant and potentially unsustainable, with some users expressing skepticism about the situation.

---

## 31. [DeepSeek V4 Coming](https://reddit.com/r/LocalLLaMA/comments/1q89g1i/deepseek_v4_coming/)

**Author:** u/External_Mood4719 | **Upvotes:** 502 | **Comments:** 110 | **Date:** 2026-01-09

**Summary:** DeepSeek is expected to release V4, a next-generation AI model with strong code-generation capabilities, outperforming mainstream models like Claude and GPT. The model shows improvements in handling long code prompts and overall reasoning ability.

**Key Points:**
- DeepSeek V4 focuses on strong code-generation capabilities
- Outperforms existing models like Claude and GPT in code generation
- Improved handling of long code prompts and data patterns
- Enhanced reasoning ability and reliability for complex tasks
- Users appreciate DeepSeek's cost-effectiveness and performance

**Discussion Highlights:** Users express excitement and anticipation for V4, with positive feedback on DeepSeek's current performance and affordability. Some speculate on potential delays due to extensive training and post-training processes.

---

## 32. [(The Information): DeepSeek To Release Next Flagship AI Model With Strong Coding Ability](https://reddit.com/r/LocalLLaMA/comments/1q88hdc/the_information_deepseek_to_release_next_flagship/)

**Author:** u/Nunki08 | **Upvotes:** 484 | **Comments:** 102 | **Date:** 2026-01-09

**Summary:** DeepSeek is set to release a new flagship AI model with strong coding capabilities, generating significant interest and discussion in the community.

**Key Points:**
- DeepSeek's upcoming model emphasizes strong coding ability
- The announcement has sparked excitement and anticipation
- Community members express enthusiasm for more AI models
- Some comments highlight skepticism about performance claims
- Discussion includes hopes for retained role-playing abilities

**Discussion Highlights:** The community shows a mix of excitement and skepticism, with many welcoming the competition and innovation in AI models, while others express caution about overhyped claims and hope for balanced capabilities.

---

## 33. [The NO FAKES Act has a "Fingerprinting" Trap that kills Open Source. We need to lobby for a Safe Harbor.](https://reddit.com/r/LocalLLaMA/comments/1q7qcux/the_no_fakes_act_has_a_fingerprinting_trap_that/)

**Author:** u/PostEasy7183 | **Upvotes:** 618 | **Comments:** 88 | **Date:** 2026-01-08

**Summary:** The NO FAKES Act proposes a 'digital replica right' that could make developers liable for hosting open-source AI models used to create deepfakes, potentially stifling innovation. The post urges lobbying for a 'Safe Harbor' provision to protect developers.

**Key Points:**
- The NO FAKES Act targets developers who 'make available' tools primarily used for creating digital replicas.
- Developers could face statutory damages of $5k-$25k per violation without Section 230 protection.
- The post calls for a 'Safe Harbor' provision to protect open-source developers.
- Action items include emailing or calling representatives to oppose the bill unless amended.
- Comments highlight concerns about the bill's impact on innovation and the influence of big tech corporations.

**Discussion Highlights:** The discussion reflects a consensus that the bill could harm innovation and give monopolistic power to big tech companies. Many commenters express skepticism about politicians' understanding of technology and the potential consequences of the bill.

---

## 34. [Jensen Huang saying "AI" 121 times during the NVIDIA CES keynote - cut with one prompt](https://reddit.com/r/LocalLLaMA/comments/1q7d8bj/jensen_huang_saying_ai_121_times_during_the/)

**Author:** u/Prior-Arm-6705 | **Upvotes:** 942 | **Comments:** 147 | **Date:** 2026-01-08

**Summary:** The post describes a project where someone counted Jensen Huang saying 'AI' 121 times during NVIDIA's CES 2025 keynote and created a compilation video using open-source tools. The process involved downloading the video, parsing subtitles, and editing clips locally.

**Key Points:**
- Jensen Huang said 'AI' 121 times during the CES 2025 keynote.
- The author used open-source tools (yt-dlp-mcp and ffmpeg-mcp-lite) to create a compilation video.
- The process was entirely local, with no cloud involvement.
- The result was described as 'hypnotic'.
- Comments included reactions to the project and mentions of AI costs.

**Discussion Highlights:** The discussion included reactions to the project, mentions of the cost of AI, and references to other tech communities like Gamers Nexus. Some comments were removed, and others praised the technical execution.

---

## 35. [16x AMD MI50 32GB at 10 t/s (tg) &amp; 2k t/s (pp) with Deepseek v3.2 (vllm-gfx906)](https://reddit.com/r/LocalLLaMA/comments/1q6n5vl/16x_amd_mi50_32gb_at_10_ts_tg_2k_ts_pp_with/)

**Author:** u/ai-infos | **Upvotes:** 459 | **Comments:** 238 | **Date:** 2026-01-07

**Summary:** The post discusses running Deepseek V3.2 AWQ 4-bit on 16x AMD MI50 32GB GPUs, achieving 10 tokens/sec output and 2000 tokens/sec input with a 69000 context length. The setup aims for cost-effective local AGI and highlights power efficiency (550W idle, 2400W peak).

**Key Points:**
- Performance: 10 tok/s output, 2000 tok/s input, 69000 context length
- Power draw: 550W idle, 2400W peak inference
- Goal: Cost-effective local AGI setup using 16x AMD MI50 GPUs
- Future plans: 32 AMD MI50 setup for Kimi K2 Thinking
- Discussion highlights power efficiency and cost-effectiveness for professional use

**Discussion Highlights:** Comments highlight the power efficiency of the setup, with users noting its potential as a heater alternative and its cost-effectiveness for professional coding. Some users express curiosity about noise levels and home power requirements.

---

## 36. [DeepSeek-R1’s paper was updated 2 days ago, expanding from 22 pages to 86 pages and adding a substantial amount of detail.](https://reddit.com/r/LocalLLaMA/comments/1q6c9wc/deepseekr1s_paper_was_updated_2_days_ago/)

**Author:** u/Nunki08 | **Upvotes:** 661 | **Comments:** 54 | **Date:** 2026-01-07

**Summary:** The Reddit post discusses the recent update to DeepSeek-R1’s paper, which expanded from 22 pages to 86 pages, adding significant detail. The discussion includes speculation about new architectures and the potential impact of linear attention research.

**Key Points:**
- DeepSeek-R1’s paper was updated, expanding from 22 pages to 86 pages.
- The update includes substantial additional detail.
- Discussion highlights potential new architectures and improvements.
- Linear attention research is mentioned as a key focus.
- Community interest in how architectural improvements scale across model sizes.

**Discussion Highlights:** The discussion includes speculation about new architectures (e.g., 'dsv4 + r2') and the impact of linear attention research. There is also interest in how architectural improvements perform across different model sizes. The community appreciates the added implementation specifics in the updated paper.

---

## 37. [A 30B Qwen Model Walks Into a Raspberry Pi… and Runs in Real Time](https://reddit.com/r/LocalLLaMA/comments/1q5m2n6/a_30b_qwen_model_walks_into_a_raspberry_pi_and/)

**Author:** u/ali_byteshape | **Upvotes:** 497 | **Comments:** 79 | **Date:** 2026-01-06

**Summary:** The post discusses the successful optimization of a 30B Qwen model to run efficiently on a Raspberry Pi 5, achieving 8.03 tokens per second while retaining 94.18% of BF16 quality. The optimization focuses on balancing memory usage and performance, particularly on GPUs where kernel choice significantly impacts speed. Key points include the model's performance on a Raspberry Pi 5, the quirky nature of GPU performance due to kernel choices, and the community's interest in testing the model on various setups. The community showed interest in testing the model on various setups, including clusters of Raspberry Pis and non-NVIDIA hardware. One user successfully ran the model on a Raspberry Pi 5 after adjusting the context size.

---

## 38. [Performance improvements in llama.cpp over time](https://reddit.com/r/LocalLLaMA/comments/1q5dnyw/performance_improvements_in_llamacpp_over_time/)

**Author:** u/jacek2023 | **Upvotes:** 686 | **Comments:** 85 | **Date:** 2026-01-06

**Summary:** The Reddit post discusses performance improvements in llama.cpp over time, with a focus on NVIDIA GPUs and comparisons with other implementations like ik_llama.cpp. The community highlights significant progress in token generation speed.

**Key Points:**
- Performance gains are particularly noted for NVIDIA GPUs.
- Token generation speed in llama.cpp has improved significantly, approaching the performance of ik_llama.cpp.
- Prompt processing remains slower compared to token generation.
- The post was featured on Discord, indicating community interest.
- Ongoing discussions about merges and further optimizations.

**Discussion Highlights:** The community consensus highlights the impressive progress in llama.cpp performance, especially for NVIDIA GPUs, with token generation speed nearly matching ik_llama.cpp. However, prompt processing is still noted to be slower. The discussion also includes references to NVIDIA's blog on open-source AI tools and ongoing optimizations.

---

## 39. [For the first time in 5 years, Nvidia will not announce any new GPUs at CES — company quashes RTX 50 Super rumors as AI expected to take center stage](https://reddit.com/r/LocalLLaMA/comments/1q4x5e9/for_the_first_time_in_5_years_nvidia_will_not/)

**Author:** u/FullstackSensei | **Upvotes:** 628 | **Comments:** 194 | **Date:** 2026-01-05

**Summary:** Nvidia will not announce new GPUs at CES, focusing instead on AI. There are concerns about limited supply of high-end GPUs, rising hardware prices, and the potential reintroduction of older models like the RTX 3060.

**Key Points:**
- Nvidia quashes RTX 50 Super rumors, focusing on AI at CES
- Limited supply of high-end GPUs (5070Ti, 5080, 5090) and rising hardware prices
- Potential reintroduction of older models like the RTX 3060
- Community concerns about corporate greed and the future of local computing
- Suggestions for alternative solutions, such as increased competition from China

**Discussion Highlights:** The discussion highlights concerns about corporate greed and the impact on local computing. There is a consensus that the current situation is challenging for consumers looking to upgrade their hardware, with suggestions for alternative solutions to increase competition and availability.

---

## 40. [llama.cpp performance breakthrough for multi-GPU setups](https://reddit.com/r/LocalLLaMA/comments/1q4s8t3/llamacpp_performance_breakthrough_for_multigpu/)

**Author:** u/Holiday-Injury-9397 | **Upvotes:** 578 | **Comments:** 204 | **Date:** 2026-01-05

**Summary:** The ik_llama.cpp project achieved a 3x to 4x performance improvement for multi-GPU setups, enabling cost-effective use of multiple low-cost GPUs for local LLM inference.

**Key Points:**
- ik_llama.cpp introduced a new execution mode (split mode graph) for multi-GPU utilization.
- Performance improvements range from 3x to 4x compared to previous methods.
- The breakthrough allows using multiple low-cost GPUs instead of expensive high-end cards.
- Even single GPU or CPU-only setups see a 2x speed improvement.
- The project is open-source and details are available on GitHub.

**Discussion Highlights:** The community highlights the significant performance gains, cost-effectiveness, and open-source nature of the project. Some users report additional speed improvements even on single GPU or CPU-only setups. There is also a mention of potential bottlenecks in hybrid inference setups.

---

## 41. [GLM-Image model from Z.ai is coming](https://reddit.com/r/LocalLLaMA/comments/1q41bw1/glmimage_model_from_zai_is_coming/)

**Author:** u/Ravencloud007 | **Upvotes:** 321 | **Comments:** 59 | **Date:** 2026-01-04

**Summary:** The Reddit post announces the upcoming GLM-Image model from Z.ai, which has generated significant interest in the community. The model is highly anticipated, with users expressing excitement about its potential capabilities and comparing it favorably to existing models.

**Key Points:**
- GLM-Image model from Z.ai is being introduced
- The model is highly anticipated with 321 upvotes and 59 comments
- Community members express excitement about its potential, with one comment mentioning a feeling of 103b parameters
- Z.ai's image model is currently the community favorite
- Users are curious about the computational resources required to use the new model

**Discussion Highlights:** The discussion highlights a strong community interest and enthusiasm for the GLM-Image model. Users are comparing it favorably to existing models and expressing curiosity about its capabilities and resource requirements. There is a consensus that Z.ai's image model is currently the community favorite, and the new model is expected to be significant.

---

## 42. [Local LLMs vs breaking news: when extreme reality gets flagged as a hoax - the US/Venezuela event was too far-fetched](https://reddit.com/r/LocalLLaMA/comments/1q31ltd/local_llms_vs_breaking_news_when_extreme_reality/)

**Author:** u/ubrtnk | **Upvotes:** 378 | **Comments:** 194 | **Date:** 2026-01-03

**Summary:** The post discusses the challenges faced by local LLMs in processing extreme or unlikely breaking news events, such as the US attacking Venezuela and capturing Maduro. The author shares their experience with different LLMs, highlighting how these models initially classified the event as a hoax despite credible sources.

**Key Points:**
- Local LLMs struggled to accept extreme breaking news as real, classifying it as a hoax.
- Different LLMs (Qwen Research, Spark 4.0, GPT-OSS:120B) had varying responses to the news.
- Providing credible sources helped some LLMs acknowledge the event's reality.
- Commenters shared similar experiences with LLMs dismissing unlikely events.
- Discussion highlights the bias and limitations of LLMs in processing unfamiliar geopolitical events.

**Discussion Highlights:** The discussion consensus suggests that LLMs have inherent biases and limitations in processing unfamiliar or extreme geopolitical events. Commenters shared similar experiences and expressed curiosity about how these biases might shape future AI historical narratives.

---

## 43. [LeCun Says Llama 4 results "were fudged a little bit"](https://reddit.com/r/LocalLLaMA/comments/1q25070/lecun_says_llama_4_results_were_fudged_a_little/)

**Author:** u/MrPecunius | **Upvotes:** 363 | **Comments:** 89 | **Date:** 2026-01-02

**Summary:** Yann LeCun confirmed that Llama 4 benchmarks were manipulated, and Meta's AI division faced significant restructuring, leading to departures and lack of follow-up on promised models. The community expressed disappointment in Meta's handling of the project.

**Key Points:**
- LeCun confirmed Llama 4 benchmark manipulation
- Meta's AI division was restructured, leading to departures
- Llama 4's promised large model was never released
- Community disappointment in Meta's strategic decisions
- Shared resources for further reading on the topic

**Discussion Highlights:** The discussion highlighted disappointment in Meta's strategic decisions, with users sharing additional resources and questioning how a well-positioned organization could falter while smaller labs thrived. There was also clarification on LeCun's role within Meta.

---

## 44. [Qwen-Image-2512](https://reddit.com/r/LocalLLaMA/comments/1q094a3/qwenimage2512/)

**Author:** u/Nunki08 | **Upvotes:** 720 | **Comments:** 122 | **Date:** 2025-12-31

**Summary:** The Reddit post introduces Qwen-Image-2512, a new image generation model, with links to documentation, demos, and resources. Users share experiences running the model on various hardware and creative applications.

**Key Points:**
- Qwen-Image-2512 is a new image generation model with multiple resources available.
- Users successfully ran the model on low-end hardware without a GPU.
- The model supports creative use cases like generating complex images.
- Multiple platforms (Hugging Face, ModelScope, GitHub) host the model and demos.

**Discussion Highlights:** Users expressed enthusiasm for the model's capabilities, sharing successful runs on low-end hardware and creative image generation examples. The community appreciated the model as a 'New Year's gift' and a 'Cool Christmas present.'

---

## 45. [[In the Wild] Reverse-engineered a Snapchat Sextortion Bot: It’s running a raw Llama-7B instance with a 2048 token window.](https://reddit.com/r/LocalLLaMA/comments/1pzwlie/in_the_wild_reverseengineered_a_snapchat/)

**Author:** u/simar-dmg | **Upvotes:** 746 | **Comments:** 110 | **Date:** 2025-12-30

**Summary:** A user reverse-engineered a Snapchat sextortion bot and discovered it was running a raw Llama-7B instance with a 2048 token window. The bot was vulnerable to a persona-adoption jailbreak, revealing its configuration and malicious payload.

**Key Points:**
- The bot used a Llama-7B model with a 2048 token context window and high temperature setting.
- A 'Grandma Protocol' jailbreak forced the bot to reveal its environment variables and configuration.
- The bot was likely running on minimal hardware to reduce costs.
- The post sparked discussions about the reliability of the bot's responses and the prevalence of such scams.
- Some commenters questioned the authenticity of the bot's revealed information.

**Discussion Highlights:** The discussion highlighted skepticism about the bot's responses, with some users suggesting the information could be hallucinated. Others appreciated the detailed analysis and the insights into how scammers are using open-source models to avoid costs.

---

## 46. [Llama-3.3-8B-Instruct](https://reddit.com/r/LocalLLaMA/comments/1pz7bmv/llama338binstruct/)

**Author:** u/jacek2023 | **Upvotes:** 469 | **Comments:** 77 | **Date:** 2025-12-29

**Summary:** The post discusses the discovery and release of the Llama-3.3-8B-Instruct model, which was previously only available via Meta's API. The author managed to download and share the model by reversing a fine-tuned adapter.

**Key Points:**
- Llama-3.3-8B-Instruct was previously only accessible through Meta's API.
- The author found a way to download the model by reversing a fine-tuned adapter.
- The model is being verified by the community for authenticity and features.
- The post gained significant attention with 469 upvotes and 77 comments.

**Discussion Highlights:** The community is actively verifying the model's authenticity and discussing its features, such as the 8K position embeddings. There is excitement about the model's release and its potential performance compared to other Llama models.

---

## 47. [Z AI is going for an IPO on Jan 8 and set to raise $560 million. Z.ai is set to be the first AI-native LLM company to list on the global market.](https://reddit.com/r/LocalLLaMA/comments/1pz68fz/z_ai_is_going_for_an_ipo_on_jan_8_and_set_to/)

**Author:** u/Difficult-Cap-7527 | **Upvotes:** 348 | **Comments:** 121 | **Date:** 2025-12-29

**Summary:** Z AI is set to go public with an IPO on January 8, aiming to raise $560 million, marking it as the first AI-native LLM company to list globally. The Reddit post and comments highlight concerns about the future of open-source AI and the inevitability of monetization in the AI industry.

**Key Points:**
- Z AI's IPO is scheduled for January 8 with a target of $560 million.
- Z AI is positioned as the first AI-native LLM company to go public.
- Community concerns about the impact on open-source AI.
- Debate on whether Z AI will continue releasing open weight models.
- General acceptance that companies need to monetize eventually.

**Discussion Highlights:** The discussion reflects a mix of excitement and concern. While some users worry about the future of open-source AI, others argue that monetization is a natural progression for companies. There is a notable consensus that companies must eventually generate revenue, with differing opinions on how this will affect open-source contributions.

---

## 48. [Tencent just released WeDLM 8B Instruct on Hugging Face](https://reddit.com/r/LocalLLaMA/comments/1pyg4yt/tencent_just_released_wedlm_8b_instruct_on/)

**Author:** u/Difficult-Cap-7527 | **Upvotes:** 426 | **Comments:** 62 | **Date:** 2025-12-29

**Summary:** Tencent released WeDLM 8B Instruct, a diffusion language model on Hugging Face that runs 3-6× faster than vLLM-optimized Qwen3-8B on math reasoning tasks. The release has garnered significant attention and positive feedback from the community.

**Key Points:**
- WeDLM 8B Instruct is a diffusion language model released by Tencent on Hugging Face.
- It outperforms vLLM-optimized Qwen3-8B by 3-6× on math reasoning tasks.
- The model is released under the Apache 2.0 license.
- Community feedback highlights the potential of 7-8B models and interest in diffusion models for LLMs.
- A 7B version of the model is also available.

**Discussion Highlights:** The community is excited about the performance and potential of diffusion models for LLMs, with many expressing interest in the 7-8B model size range. The Apache 2.0 license and impressive benchmark scores are also noted as positive aspects.

---

