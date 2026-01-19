# r/LocalLLaMA Reading Digest

**Period:** 2026-01-19 to 2026-01-19
**Posts Summarized:** 37
**Total Posts Analyzed:** 37

---

## 1. [zai-org/GLM-4.7-Flash · Hugging Face](https://reddit.com/r/LocalLLaMA/comments/1qh5wdq/zaiorgglm47flash_hugging_face/)

**Author:** u/Dark_Fire_12 | **Upvotes:** 449 | **Comments:** 132 | **Date:** 2026-01-19

**Summary:** The Reddit post discusses the release of zai-org/GLM-4.7-Flash on Hugging Face, highlighting its popularity and technical features like reduced memory usage. The community shows strong interest and appreciation for the model.

**Key Points:**
- Post gained significant attention with 449 upvotes and 132 comments
- Community appreciates 30b models and misses larger 70b models
- MLA technology reduces KV cache memory consumption
- Model supports full 200k context, making it accessible to more users
- Users express anticipation and desire for comparisons with larger models

**Discussion Highlights:** The discussion reflects positive reception of the GLM-4.7-Flash model, with users highlighting its technical advantages like memory efficiency and long context support. There's a sense of anticipation and community engagement around this release.

---

## 2. [I made a Top-K implementation that's up to 20x faster than PyTorch CPU (open source)](https://reddit.com/r/LocalLLaMA/comments/1qh0yq8/i_made_a_topk_implementation_thats_up_to_20x/)

**Author:** u/andreabarbato | **Upvotes:** 123 | **Comments:** 79 | **Date:** 2026-01-19

**Summary:** The author developed an AVX2-optimized batched Top-K implementation that significantly outperforms PyTorch CPU, achieving up to 20x speed improvements depending on vocabulary size. This optimization also led to a 63% increase in prompt processing speed for a 120B MoE model in llama.cpp.

**Key Points:**
- AVX2-optimized batched Top-K implementation is 4-20x faster than PyTorch CPU.
- Benchmark results show significant speed improvements across different vocabulary sizes.
- Integration into llama.cpp resulted in a 63% increase in prompt processing speed.
- The implementation uses adaptive sampling, AVX2 SIMD, and cache-optimized scanning.
- GitHub repository and pre-built DLLs are available for use.

**Discussion Highlights:** The community expressed strong interest and encouragement, with requests for a pull request to llama.cpp. Some users sought explanations for the performance gains, while others raised concerns about the lack of reproducible benchmarks and the authenticity of the post.

---

## 3. [4x AMD R9700 (128GB VRAM) + Threadripper 9955WX Build](https://reddit.com/r/LocalLLaMA/comments/1qgdb7f/4x_amd_r9700_128gb_vram_threadripper_9955wx_build/)

**Author:** u/NunzeCs | **Upvotes:** 321 | **Comments:** 88 | **Date:** 2026-01-18

**Summary:** The author built a high-performance system with 4x AMD R9700 GPUs (128GB VRAM) and a Threadripper 9955WX CPU, leveraging a 50% subsidy to maximize VRAM for running large AI models locally. Benchmark results show impressive performance across various models, with the system costing around 9,800€ (effectively 4,900€ after refund). The community reacted positively, with comments highlighting the impressive hardware, curiosity about sourcing and use cases, and comparisons to similar builds. The post was featured on Discord, and the author received special recognition for their contribution.

---

## 4. [Qwen 4 might be a long way off !? Lead Dev says they are "slowing down" to focus on quality.](https://reddit.com/r/LocalLLaMA/comments/1qfv1ms/qwen_4_might_be_a_long_way_off_lead_dev_says_they/)

**Author:** u/Difficult-Cap-7527 | **Upvotes:** 435 | **Comments:** 63 | **Date:** 2026-01-17

**Summary:** The Reddit post discusses the potential delay in Qwen 4 development, with the lead developer indicating a focus on quality over speed. The community generally appreciates this approach, though some caution against overinterpreting the announcement.

**Key Points:**
- Qwen 4 development may be slowing down to prioritize quality
- Community largely supports the focus on quality over quantity
- Some users urge caution against speculative interpretations of the announcement
- Incremental updates are seen as less impactful than meaningful advancements
- The post gained significant traction with 435 upvotes and 63 comments

**Discussion Highlights:** The discussion highlights a consensus that prioritizing quality in AI development is beneficial, though there is debate about the implications of the announcement and the need for substantial progress over frequent updates.

---

## 5. [128GB VRAM quad R9700 server](https://reddit.com/r/LocalLLaMA/comments/1qfscp5/128gb_vram_quad_r9700_server/)

**Author:** u/Ulterior-Motive_ | **Upvotes:** 512 | **Comments:** 109 | **Date:** 2026-01-17

**Summary:** The author upgraded from MI100s to four R9700 GPUs, achieving 128GB VRAM and improved performance at a comparable cost. The new server setup includes detailed specifications and benchmarks, showcasing its capabilities.

**Key Points:**
- Upgrade from MI100s to R9700s for better performance and cost efficiency
- Detailed specifications and benchmarks provided for the new server
- Community engagement and positive feedback highlighted in comments

**Discussion Highlights:** The community praised the upgrade, with comments highlighting the financial irresponsibility joke, appreciation for the setup, and encouragement for the author's contributions.

---

## 6. [The Search for Uncensored AI (That Isn’t Adult-Oriented)](https://reddit.com/r/LocalLLaMA/comments/1qfq9ez/the_search_for_uncensored_ai_that_isnt/)

**Author:** u/Fun-Situation-4358 | **Upvotes:** 270 | **Comments:** 231 | **Date:** 2026-01-17

**Summary:** The post discusses the challenge of finding uncensored AI models that prioritize reasoning and creativity over adult-oriented content, highlighting a gap between heavily restricted corporate AI and shallow adult-focused models.

**Key Points:**
- The author seeks an AI that is genuinely unfiltered and technically advanced, focusing on reasoning and creativity.
- Most models marketed as 'uncensored' are optimized for adult use rather than intelligence or depth.
- There is a perceived gap between heavily restricted corporate AI and shallow adult-focused models.
- Techniques to decensor open-source models often reduce their intelligence.
- The Uncensored General Intelligence Leaderboard is referenced as a potential resource.

**Discussion Highlights:** The discussion highlights a shared frustration with the lack of AI models that balance uncensored capabilities with serious problem-solving and creativity. Many users agree that most uncensored models are either too restricted or overly focused on adult content, leaving a gap for models that prioritize reasoning and technical depth.

---

## 7. [China's AGI-NEXT Conference (Qwen, Kimi, Zhipu, Tencent)](https://reddit.com/r/LocalLLaMA/comments/1qfmc05/chinas_aginext_conference_qwen_kimi_zhipu_tencent/)

**Author:** u/nuclearbananana | **Upvotes:** 116 | **Comments:** 22 | **Date:** 2026-01-17

**Summary:** The Reddit post discusses China's AGI-NEXT Conference, highlighting insights on China vs US AGI development, compute resources, and marketing strategies. Key points include Qwen's internal advancements, risk-averse work culture, and the absence of Deepseek despite its talent concentration.

**Key Points:**
- Qwen has internally developed Qwen3.5 with context windows in the millions.
- Chinese AI labs believe the next paradigm is likely to come from OpenAI rather than Google.
- Chinese work culture is described as less willing to take risks for innovation.
- Deepseek, despite its talent concentration, was notably absent from the conference.

**Discussion Highlights:** The discussion highlights Qwen's advancements and the belief that OpenAI is leading the next paradigm shift. There is also a consensus on the risk-averse nature of Chinese AI labs and the notable absence of Deepseek from the conference.

---

## 8. [Best "End of world" model that will run on 24gb VRAM](https://reddit.com/r/LocalLLaMA/comments/1qfkn3a/best_end_of_world_model_that_will_run_on_24gb_vram/)

**Author:** u/gggghhhhiiiijklmnop | **Upvotes:** 324 | **Comments:** 170 | **Date:** 2026-01-17

**Summary:** The user is seeking recommendations for the best LLM model that can run on a PC with 24GB VRAM and 64GB RAM, in preparation for an 'end of world' scenario. The discussion includes suggestions for specific models like gemma3:27b and practical advice on data storage. Key points include hoarding data like Wikipedia, the importance of saving the best possible LLM, and downloading actual Wikipedia backups for offline use. The discussion highlights practical advice on data storage and specific model recommendations.

---

## 9. [DeepSeek Engram : A static memory unit for LLMs](https://reddit.com/r/LocalLLaMA/comments/1qf5oj0/deepseek_engram_a_static_memory_unit_for_llms/)

**Author:** u/Technical-Love-8479 | **Upvotes:** 316 | **Comments:** 47 | **Date:** 2026-01-17

**Summary:** DeepSeek AI introduced Engram, a memory unit for LLMs that separates remembering from reasoning, enabling O(1) knowledge lookup and improving performance.

**Key Points:**
- Engram introduces conditional memory, separating it from reasoning.
- Knowledge lookup is O(1), improving efficiency.
- Enables massive memory scaling without GPU limits.
- Improves reasoning, math, and code performance.
- Frees attention for global reasoning rather than static knowledge.

**Discussion Highlights:** The community is excited about the separation of memory and reasoning, highlighting the efficiency gains and potential for scaling memory independently of model size.

---

## 10. [Prompt Repetition Improves Non-Reasoning LLMs - a paper](https://reddit.com/r/LocalLLaMA/comments/1qeuh0z/prompt_repetition_improves_nonreasoning_llms_a/)

**Author:** u/Foreign-Beginning-49 | **Upvotes:** 110 | **Comments:** 50 | **Date:** 2026-01-16

**Summary:** The Reddit post discusses a paper showing that repeating prompts can significantly improve the performance of non-reasoning LLMs without affecting latency or output format. The technique is simple yet effective across various models and benchmarks.

**Key Points:**
- Repeating prompts improves model performance for non-reasoning tasks.
- Latency remains unaffected as only the pre-fill stage is impacted.
- The technique is simple but demonstrates impressive gains on benchmarks.
- Deepseek is highlighted as an open weights model tested extensively.
- The discussion highlights curiosity about other undiscovered simple techniques.

**Discussion Highlights:** The discussion emphasizes the simplicity and effectiveness of the technique, with users expressing surprise at its impact. There is speculation about other potential undiscovered tricks and the overall lack of understanding of LLM architectures.

---

## 11. [performance benchmarks (72GB VRAM) - llama.cpp server - January 2026](https://reddit.com/r/LocalLLaMA/comments/1qennp2/performance_benchmarks_72gb_vram_llamacpp_server/)

**Author:** u/jacek2023 | **Upvotes:** 110 | **Comments:** 34 | **Date:** 2026-01-16

**Summary:** The Reddit post presents performance benchmarks for various AI models run on a system with three RTX 3090 GPUs and 72GB VRAM, focusing solely on speed (tokens/s) rather than accuracy. The benchmarks are informal and not scientific, with the top-performing model being ERNIE-4.5-21B-A3B-Thinking-Q8_0 at 147.85 tokens/s.

**Key Points:**
- Benchmarks measure speed (tokens/s) of AI models on a 72GB VRAM system with three RTX 3090 GPUs.
- The benchmarks are informal and not scientific, focusing only on speed, not accuracy.
- ERNIE-4.5-21B-A3B-Thinking-Q8_0 achieved the highest speed at 147.85 tokens/s.
- Suggestions from comments include filling context to ~10k tokens for further testing and using specific compilation flags for better performance.
- The setup uses default 'llama-fit' mechanism, with potential for better performance through manual tuning.

**Discussion Highlights:** The discussion includes suggestions for further testing, such as measuring performance with a filled context of ~10k tokens and using specific compilation flags like -DGGML_CUDA_PEER_COPY=ON for direct GPU-to-GPU data copying. Some users also inquired about the GPU interconnect setup and noted similarities in performance between certain models.

---

## 12. [I reproduced DeepSeek's mHC at 1.7B params (8xH100). The instability is 3x worse than reported (10k vs 3k), but the model didn't explode.](https://reddit.com/r/LocalLLaMA/comments/1qek917/i_reproduced_deepseeks_mhc_at_17b_params_8xh100/)

**Author:** u/poisson_labs | **Upvotes:** 176 | **Comments:** 29 | **Date:** 2026-01-16

**Summary:** The author reproduced DeepSeek's mHC at 1.7B parameters and found that the instability was 3x worse than reported, with signal amplification of 10,924x. Despite this, the model continued learning, and the issue was resolved using Manifold Hyper-Connections (mHC) with Sinkhorn projection, which maintained variance at 1.0x with no compute overhead.

**Key Points:**
- Signal amplification at 1.7B parameters was 10,924x, worse than the reported 3,000x.
- The model continued learning despite high signal amplification, suggesting modern optimizers and gradient clipping mitigate the issue.
- Manifold Hyper-Connections (mHC) with Sinkhorn projection resolved the instability with zero compute overhead.
- Discussion highlights include skepticism about zero compute overhead and interest in alternative optimizers like muon.
- The project was praised for its resourcefulness and potential to inspire other labs.

**Discussion Highlights:** The discussion included skepticism about the claim of zero compute overhead, interest in exploring alternative optimizers like muon, and praise for the project's resourcefulness and potential impact on the field.

---

## 13. [Maxsun joins Sparkle in making Intel Arc B60 Pro GPUs available to regular consumers, with up to 48GB VRAM](https://reddit.com/r/LocalLLaMA/comments/1qehf0p/maxsun_joins_sparkle_in_making_intel_arc_b60_pro/)

**Author:** u/reps_up | **Upvotes:** 134 | **Comments:** 50 | **Date:** 2026-01-16

**Summary:** Maxsun and Sparkle are making Intel Arc B60 Pro GPUs available to regular consumers, featuring up to 48GB VRAM. The Reddit discussion highlights user interest in higher VRAM capacities and support for frameworks like torch/JAX/ONNX.

**Key Points:**
- Intel Arc B60 Pro GPUs now available to consumers
- Up to 48GB VRAM offered
- User interest in support for torch/JAX/ONNX frameworks
- Requests for higher VRAM capacities (e.g., 128GB)
- Inquiries about availability in Europe

**Discussion Highlights:** Users expressed strong interest in higher VRAM capacities, with some requesting up to 128GB. There were also questions about the support for frameworks like torch/JAX/ONNX and the availability of these GPUs in Europe.

---

## 14. [GPT-5.2 xhigh, GLM-4.7, Kimi K2 Thinking, DeepSeek v3.2 on Fresh SWE-rebench (December 2025)](https://reddit.com/r/LocalLLaMA/comments/1qefa7q/gpt52_xhigh_glm47_kimi_k2_thinking_deepseek_v32/)

**Author:** u/CuriousPlatypus1881 | **Upvotes:** 375 | **Comments:** 89 | **Date:** 2026-01-16

**Summary:** The post discusses the December 2025 update to the SWE-bench leaderboard, highlighting the performance of various AI models on GitHub PR tasks. Claude Opus 4.5 leads with a 63.3% resolved rate, followed closely by GPT-5.2 (extra high effort) at 61.5%. The post also notes the strong performance of open-source models like GLM-4.7 and GPT-OSS-120B.

**Key Points:**
- Claude Opus 4.5 leads the SWE-bench leaderboard with a 63.3% resolved rate.
- GPT-5.2 (extra high effort) follows closely at 61.5%.
- Gemini 3 Flash Preview outperforms Gemini 3 Pro Preview despite being smaller and cheaper.
- GLM-4.7 is the strongest open-source model, ranking alongside closed models like GPT-5.1-codex.
- GPT-OSS-120B shows significant performance improvement in high-effort reasoning mode.

**Discussion Highlights:** The discussion highlights the surprising performance of Gemini Flash and the excitement around open-source models like GLM-4.7. There is also anticipation for future releases like DeepSeek v4.

---

## 15. [I fucking love this community](https://reddit.com/r/LocalLLaMA/comments/1qee2de/i_fucking_love_this_community/)

**Author:** u/alhinai_03 | **Upvotes:** 488 | **Comments:** 54 | **Date:** 2026-01-16

**Summary:** The author expresses gratitude to the open-source community for enabling them to run large models on a 10-year-old PC with limited GPU VRAM. They highlight the importance of system memory and MoE architecture for achieving decent performance. Key points include the author's appreciation for the community, their achievement of 14-13.5 tokens per second on a 10-year-old PC with 4GB VRAM, the importance of system memory and MoE architecture, and the practicality of these optimizations as discussed in the comments.

---

## 16. [Dang, M2 drives are the new DDR5 apparently.](https://reddit.com/r/LocalLLaMA/comments/1qe4so5/dang_m2_drives_are_the_new_ddr5_apparently/)

**Author:** u/Porespellar | **Upvotes:** 211 | **Comments:** 96 | **Date:** 2026-01-15

**Summary:** The Reddit post discusses the significant increase in prices of M2 drives, with users expressing frustration and sharing their experiences of price hikes. The discussion highlights concerns about the rising costs and the impact on consumers.

**Key Points:**
- Prices of M2 drives have increased significantly.
- Users express frustration and dissatisfaction with the price hikes.
- Some users report spending much more on drives than they did previously.
- There is a sense of uncertainty about when the price increases will end.
- Users are considering keeping old PCs as backups due to the high costs.

**Discussion Highlights:** The discussion highlights a consensus among users about the frustration and financial impact of the rising prices of M2 drives. Many users share personal experiences of price increases and express concerns about the future of hardware costs.

---

## 17. [My story of underestimating /r/LocalLLaMA's thirst for VRAM](https://reddit.com/r/LocalLLaMA/comments/1qe2i88/my_story_of_underestimating_rlocalllamas_thirst/)

**Author:** u/EmPips | **Upvotes:** 1265 | **Comments:** 88 | **Date:** 2026-01-15

**Summary:** The Reddit post discusses the author's experience with the subreddit's high demand for VRAM, as indicated by the title and the popularity of the post. The discussion includes comments about the post's popularity, a humorous reference to the California gold rush, and advice on hardware choices.

**Key Points:**
- The post gained significant attention, as shown by the high number of upvotes and comments.
- A comment humorously compares the situation to the California gold rush, suggesting a rush to acquire necessary equipment.
- There is advice on hardware choices, specifically mentioning the R9700 and 3090 graphics cards.
- The author received recognition for their contribution, including a special flair.

**Discussion Highlights:** The discussion highlights the popularity of the post and the community's engagement. There is a mix of humor, advice on hardware, and recognition for the author's contribution.

---

## 18. [Latest upgrade…A100 40 GB](https://reddit.com/r/LocalLLaMA/comments/1qe0cxc/latest_upgradea100_40_gb/)

**Author:** u/inserterikhere | **Upvotes:** 394 | **Comments:** 52 | **Date:** 2026-01-15

**Summary:** The user upgraded their gaming rig to an AI rig by purchasing a faulty A100 GPU for $1000, which worked perfectly upon installation. The post gained significant attention in the r/LocalLLaMA community.

**Key Points:**
- The user transitioned from a gaming rig to an AI rig using existing parts and new purchases.
- An A100 GPU, listed as faulty, was successfully integrated into the setup.
- The post received positive engagement, including a special flair and feature on Discord.
- Community members expressed concerns about cooling the A100 GPU.
- The upgrade was seen as a significant achievement by the community.

**Discussion Highlights:** The discussion highlighted the community's interest in the upgrade, with some users offering practical advice on cooling the A100 GPU. The post was well-received, as evidenced by the high number of upvotes and comments.

---

## 19. [Not as impressive as most here, but really happy I made it in time!](https://reddit.com/r/LocalLLaMA/comments/1qdtvgs/not_as_impressive_as_most_here_but_really_happy_i/)

**Author:** u/Kahvana | **Upvotes:** 140 | **Comments:** 46 | **Date:** 2026-01-15

**Summary:** The Reddit post discusses the author's successful acquisition of an RTX 5060 Ti GPU in the Netherlands despite supply issues, detailing their system specs and offering advice on checking stock availability. The discussion includes questions about CPU upgrades, comments on build aesthetics, and discussions about GPU performance.

**Key Points:**
- GPU availability challenges in the Netherlands and the importance of checking stock directly with stores
- System specs include AMD Ryzen 5 9600X, 96GB DDR5 RAM, and dual RTX 5060 Ti GPUs
- Community discussions on CPU upgrades, build aesthetics, and GPU performance
- Recommendations for motherboard choices to optimize dual GPU setups
- Power draw during inference is around 300W

**Discussion Highlights:** The discussion highlights practical advice on GPU availability and system optimization, with community members sharing their experiences and recommendations for similar builds. There is a consensus on the importance of checking stock availability directly with stores and choosing the right motherboard for dual GPU setups.

---

## 20. [Nemotron-3-nano:30b is a spectacular general purpose local LLM](https://reddit.com/r/LocalLLaMA/comments/1qdrf3o/nemotron3nano30b_is_a_spectacular_general_purpose/)

**Author:** u/DrewGrgich | **Upvotes:** 209 | **Comments:** 124 | **Date:** 2026-01-15

**Summary:** The post praises Nemotron-3-nano:30b for its exceptional performance as a general-purpose LLM, noting its superior reasoning quality and robustness in handling various tasks compared to larger models like Llama 3.3:70b. Users highlight its effectiveness for research and analysis, despite its robotic tone, and express anticipation for the upcoming Nemotron 3 super (100b) model.

**Key Points:**
- Nemotron-3-nano:30b is praised for its high intelligence and reasoning quality relative to its size.
- It outperforms larger models like Llama 3.3:70b in general-purpose tasks.
- The model's robotic tone is seen as a feature for research and analysis purposes.
- Users are looking forward to the Nemotron 3 super (100b) model for its promised innovations and speed.
- Some users prefer other models like qwen3-vl-30b-a3b-instruct for their additional capabilities.

**Discussion Highlights:** The discussion highlights the model's impressive performance in reasoning and structured output tasks, with users sharing positive experiences and comparing it favorably to other models. There is also anticipation for future releases and a preference for models with additional capabilities like vision-language (VL) features.

---

## 21. [Thanks to you guys, Soprano TTS now supports OpenAI-compatible endpoint, ONNX, ComfyUI, WebUI, and CLI on CUDA, MPS, ROCm, and CPU!](https://reddit.com/r/LocalLLaMA/comments/1qdpb2v/thanks_to_you_guys_soprano_tts_now_supports/)

**Author:** u/eugenekwek | **Upvotes:** 108 | **Comments:** 25 | **Date:** 2026-01-15

**Summary:** The Reddit post announces updates to Soprano TTS, including support for OpenAI-compatible endpoints, ONNX, ComfyUI, WebUI, and CLI on various devices like CUDA, MPS, ROCm, and CPU. The author thanks the community for their contributions and highlights several new features and improvements.

**Key Points:**
- Soprano TTS now supports multiple inference methods and devices.
- Community contributions include WebUI, CLI, OpenAI-compatible endpoints, ONNX, and ComfyUI support.
- Additional features like automatic hallucination detection and transformers streaming support have been added.
- The post mentions ongoing efforts for ROCm support and requests help for testing.
- The community appreciates the importance of local TTS for accessibility and privacy.

**Discussion Highlights:** The discussion includes questions about comparing Soprano to other TTS models like Kokoro, inquiries about finetuning support, and appreciation for the accessibility and privacy benefits of local TTS. There is also a humorous comment about the 'aah_runlength' variable in the hallucination detector.

---

## 22. [google/translategemma](https://reddit.com/r/LocalLLaMA/comments/1qdok2i/googletranslategemma/)

**Author:** u/BreakfastFriendly728 | **Upvotes:** 176 | **Comments:** 56 | **Date:** 2026-01-15

**Summary:** The Reddit post discusses Google's TranslateGemma model, highlighting its technical report and Hugging Face collection. The discussion focuses on comparisons with other models, the scale of fine-tuning, and limitations like context length.

**Key Points:**
- TranslateGemma models used 4.3 billion tokens during SFT and 10.2 million tokens during reinforcement learning.
- Criticism about the lack of comparison to models like tencent/HY-MT1.5 and absence of Gemma 4.
- Concerns about the limited 2K token input context.
- Requests for GGUF format availability.
- Questions about setting language codes for API usage.

**Discussion Highlights:** The discussion highlights mixed reactions, with some users appreciating the model's release but others criticizing its limitations and lack of comparisons to other advanced models. There is a consensus on the need for more comprehensive benchmarks and broader format support.

---

## 23. [7x Longer Context Reinforcement Learning in Unsloth](https://reddit.com/r/LocalLLaMA/comments/1qdna3t/7x_longer_context_reinforcement_learning_in/)

**Author:** u/danielhanchen | **Upvotes:** 247 | **Comments:** 27 | **Date:** 2026-01-15

**Summary:** Unsloth introduces techniques enabling 7x longer context lengths for Reinforcement Learning, allowing training of models like gpt-oss 20b QLoRA with up to 20K context on a 24GB card without accuracy loss. The post highlights compatibility with various models and features like weight-sharing, Flex Attention, and Float8 training.

**Key Points:**
- Unsloth enables 7x longer context lengths for RL, supporting up to 20K context on a 24GB card.
- Features include weight-sharing, Flex Attention, and Float8 training, all combinable.
- Supports models like Llama, Gemma, and Qwen3 with extended context capabilities.
- Free Colab notebooks and educational resources are provided for implementation.
- Community engagement includes Discord features and special flairs for contributions.

**Discussion Highlights:** The community praised the advancements, with comments highlighting the rapid progress and potential applications. Some users inquired about data sources for long-context training and compatibility with specific models like Qwen3 30B-3A.

---

## 24. [RTX 5070 Ti and RTX 5060 Ti 16 GB no longer manufactured](https://reddit.com/r/LocalLLaMA/comments/1qdh28f/rtx_5070_ti_and_rtx_5060_ti_16_gb_no_longer/)

**Author:** u/Paramecium_caudatum_ | **Upvotes:** 227 | **Comments:** 95 | **Date:** 2026-01-15

**Summary:** Nvidia has significantly reduced supply for the RTX 5070 Ti and RTX 5060 Ti 16 GB GPUs due to memory shortages, leading to price increases and limited availability. The 8 GB configuration of the RTX 5060 Ti remains unaffected.

**Key Points:**
- Nvidia has killed off supply for the RTX 5070 Ti and reduced supply for the RTX 5060 Ti 16 GB.
- Memory supply shortages are a contributing factor to the reduced supply.
- Prices for the RTX 5070 Ti have increased by approximately $100 over MSRP, with further hikes expected.
- The 8 GB configuration of the RTX 5060 Ti is not affected by the supply issues.
- Users express disappointment and share their experiences with the affected GPUs.

**Discussion Highlights:** Users in the discussion express frustration over the supply issues and price hikes, with some sharing their recent purchases and experiences. There is a consensus that the supply shortages have disrupted upgrade plans and increased costs for consumers.

---

## 25. [LFM 2.5 is insanely good](https://reddit.com/r/LocalLLaMA/comments/1qdax6z/lfm_25_is_insanely_good/)

**Author:** u/guiopen | **Upvotes:** 104 | **Comments:** 33 | **Date:** 2026-01-14

**Summary:** The Reddit post highlights the impressive performance of the LFM 2.5 model, noting its effectiveness in basic QA and summarization tasks, despite its small size. The author compares its performance favorably to larger models and expresses excitement about future developments.

**Key Points:**
- LFM 2.5 is praised for its performance, comparable to larger models like Llama 2 7B and Llama 3 8B.
- The model excels in basic QA and summarization tasks, even at lower quantization levels like Q6.
- It performs well in Portuguese, despite not being officially supported.
- Some users note limitations in basic QA without retrieval systems and mixed experiences with summarization tasks.
- The author is optimistic about the upcoming 8B-a1B MoE model.

**Discussion Highlights:** The discussion highlights a consensus on the model's impressive performance for its size, with some users noting limitations in specific tasks like basic QA and summarization. Overall, the sentiment is positive, with excitement about future developments.

---

## 26. [I trained a model to 'unslop' AI prose](https://reddit.com/r/LocalLLaMA/comments/1qd88v2/i_trained_a_model_to_unslop_ai_prose/)

**Author:** u/N8Karma | **Upvotes:** 204 | **Comments:** 71 | **Date:** 2026-01-14

**Summary:** The author trained a model to reverse AI-generated 'slop' by restoring original prose quality from passages processed by GPT-4o-mini. The model, named 'Unslopper-30B-A3B-bf16', is open-source and can fool AI detectors like Pangram, indicating improved human-like readability.

**Key Points:**
- Model trained to reverse AI-generated 'slop' and restore original prose
- Model can fool AI detectors like Pangram, indicating improved readability
- Open-source model available on Hugging Face
- Example provided showing improved prose quality
- Discussion highlights include positive feedback and comparisons to diffusion models

**Discussion Highlights:** The discussion highlights positive feedback on the model's ability to improve readability and comparisons to diffusion models. Some users expressed skepticism about the training data size but acknowledged the potential of the approach.

---

## 27. [Zhipu AI breaks US chip reliance with first major model trained on Huawei stack (GLM-Image)](https://reddit.com/r/LocalLLaMA/comments/1qd6nho/zhipu_ai_breaks_us_chip_reliance_with_first_major/)

**Author:** u/fallingdowndizzyvr | **Upvotes:** 416 | **Comments:** 45 | **Date:** 2026-01-14

**Summary:** Zhipu AI has developed the GLM-Image 9B model using Huawei hardware, marking a significant step in reducing reliance on US chips like Nvidia. The development is seen as a response to the Chinese ban on Nvidia, with discussions highlighting both the technological achievement and the current limitations of the model.

**Key Points:**
- Zhipu AI's GLM-Image 9B model is trained on Huawei hardware, reducing dependence on US chips.
- The development is a response to the Chinese ban on Nvidia, with expectations of scaling up to larger models.
- The model's outputs are currently not highly rated, but it is seen as a tech demo or MVP.
- The progression of model sizes (e.g., SD1.5, SDXL, Flux.1) is noted, with Zhipu AI being less than 2 years behind using Huawei hardware.

**Discussion Highlights:** The discussion highlights the significance of Zhipu AI's achievement in using Huawei hardware to train a major model, despite the current limitations in output quality. There is a consensus that this is a notable step towards reducing reliance on US chips, with expectations of further advancements in the near future.

---

## 28. [Popularity of DDR3 motherboards is growing rapidly - VideoCardz.com](https://reddit.com/r/LocalLLaMA/comments/1qcvk9n/popularity_of_ddr3_motherboards_is_growing/)

**Author:** u/FullstackSensei | **Upvotes:** 146 | **Comments:** 66 | **Date:** 2026-01-14

**Summary:** The author expresses frustration over rising DDR3 memory prices, which are affecting their homelabbing hobby. They fear that DDR3 prices will skyrocket, making it difficult to replace or upgrade their current setup.

**Key Points:**
- Author's frustration with rising DDR3 prices impacting homelabbing
- Fear of DDR3 prices skyrocketing and affecting replacement parts
- Discussion on the reuse and recycling era of consumer hardware
- Mention of DDR2 motherboards potentially becoming the next target
- Observation that RAM prices have always been cyclical

**Discussion Highlights:** The discussion highlights a consensus on the cyclical nature of RAM prices and the potential for older hardware to become more valuable. Some users share their experiences with selling or upgrading their systems, while others express concerns about future price hikes.

---

## 29. [NeuTTS Nano: 120M Parameter On-Device TTS based on Llama3](https://reddit.com/r/LocalLLaMA/comments/1qcv304/neutts_nano_120m_parameter_ondevice_tts_based_on/)

**Author:** u/TeamNeuphonic | **Upvotes:** 211 | **Comments:** 44 | **Date:** 2026-01-14

**Summary:** Neuphonic has released NeuTTS Nano, a lightweight 120M parameter text-to-speech model based on Llama3, designed for embedded systems and mobile devices. It offers instant voice cloning and realistic prosody, targeting applications where RAM and VRAM constraints are critical.

**Key Points:**
- 120M parameter model, 3x smaller than NeuTTS Air
- Built on Llama3 with a simple LM + codec architecture
- Optimized for mobile, Jetson, and Raspberry Pi via GGML format
- Supports instant voice cloning with a 3-second sample
- Community interest in multilingual support and performance benchmarks

**Discussion Highlights:** The community shows strong interest in multilingual support, with requests for European languages. Feedback on voice quality is mixed, with some users finding the output unnatural or emotionless. There is also curiosity about performance benchmarks on various hardware.

---

## 30. [Soprano 1.1-80M released: 95% fewer hallucinations and 63% preference rate over Soprano-80M](https://reddit.com/r/LocalLLaMA/comments/1qcusnt/soprano_1180m_released_95_fewer_hallucinations/)

**Author:** u/eugenekwek | **Upvotes:** 316 | **Comments:** 54 | **Date:** 2026-01-14

**Summary:** The post announces Soprano 1.1, an improved version of the Soprano TTS model with significant reductions in hallucinations and audio artifacts, along with enhanced stability and support for longer sentences. The community response is overwhelmingly positive, highlighting the model's impressive performance for its size.

**Key Points:**
- Soprano 1.1 reduces hallucinations by 95% and lowers WER by 50% compared to the previous version.
- The model now supports sentences up to 30 seconds long, doubling the previous limit.
- Blind study shows 63% preference for Soprano 1.1 over the original model.
- Community feedback emphasizes the model's usability and performance for an 80M parameter model.
- Discussion includes inquiries about future support, such as ONNX compatibility.

**Discussion Highlights:** The community response is highly positive, with users expressing surprise at the model's quality given its small size. There is interest in future developments, such as ONNX support, and appreciation for the developer's efforts.

---

## 31. [NVIDIA's new 8B model is Orchestrator-8B, a specialized 8-billion-parameter AI designed not to answer everything itself, but to intelligently manage and route complex tasks to different tools (like web search, code execution, other LLMs) for greater efficiency](https://reddit.com/r/LocalLLaMA/comments/1qcuerc/nvidias_new_8b_model_is_orchestrator8b_a/)

**Author:** u/Fear_ltself | **Upvotes:** 701 | **Comments:** 129 | **Date:** 2026-01-14

**Summary:** NVIDIA's Orchestrator-8B is an 8-billion-parameter AI designed to manage and route complex tasks to various tools for greater efficiency. The post discusses its potential as a step towards AGI by integrating different models and tools effectively.

**Key Points:**
- Orchestrator-8B is a specialized AI for task management and routing.
- It aims to enhance efficiency by connecting with other tools and models.
- The post suggests this approach could be a step towards AGI.
- Top comments highlight its role as a 'middle manager' and its potential in agentic frameworks.

**Discussion Highlights:** The discussion highlights the model's role in managing tasks and its potential in creating functional AI systems. There is a consensus on the importance of integrating different models and tools for advanced AI capabilities.

---

## 32. [Which are the top LLMs under 8B right now?](https://reddit.com/r/LocalLLaMA/comments/1qcl543/which_are_the_top_llms_under_8b_right_now/)

**Author:** u/Additional_Secret_75 | **Upvotes:** 174 | **Comments:** 108 | **Date:** 2026-01-14

**Summary:** The post discusses the best LLMs under 8B parameters for local use, focusing on models suitable for chat, research, and coding with low VRAM requirements. Users share their experiences and recommendations for various models.

**Key Points:**
- Qwen3 4B and Qwen3 8B are highlighted for their performance in the under 8B range.
- Gemma 3n E4B is praised for its reasoning and multimodal capabilities.
- Nanbeige 3B is mentioned as a notable model.
- Users emphasize the importance of low VRAM usage and lack of heavy censorship.

**Discussion Highlights:** The discussion highlights Qwen3 and Gemma 3n E4B as top performers in the under 8B category, with a focus on their capabilities in chat, research, and coding tasks. Users also share resources like the GPU Poor LLM Arena for further comparisons.

---

## 33. [GLM-Image is released!](https://reddit.com/r/LocalLLaMA/comments/1qc9m6x/glmimage_is_released/)

**Author:** u/foldl-li | **Upvotes:** 595 | **Comments:** 83 | **Date:** 2026-01-13

**Summary:** GLM-Image is a new image generation model with a hybrid autoregressive + diffusion decoder architecture. It excels in text-rendering and knowledge-intensive tasks while supporting various image-to-image tasks.

**Key Points:**
- Hybrid autoregressive + diffusion decoder architecture
- Excels in text-rendering and knowledge-intensive generation
- Supports image editing, style transfer, and multi-subject consistency
- MIT license with no restrictions
- High benchmark scores comparable to other models

**Discussion Highlights:** The community appreciates the MIT license and the model's capabilities. There is excitement about its performance and potential for quantization and optimization.

---

## 34. [Soprano TTS training code released: Create your own 2000x realtime on-device text-to-speech model with Soprano-Factory!](https://reddit.com/r/LocalLLaMA/comments/1qc5nml/soprano_tts_training_code_released_create_your/)

**Author:** u/eugenekwek | **Upvotes:** 318 | **Comments:** 36 | **Date:** 2026-01-13

**Summary:** The Reddit post announces the release of Soprano-Factory, a training code for creating custom text-to-speech models with ultra-low latency and high performance. The author, u/eugenekwek, highlights the model's ability to run up to 2000x realtime on GPU and supports lossless streaming with 15 ms latency. The post also introduces Soprano-Encoder for converting raw audio into audio tokens. Key points include the ability to train custom TTS models with voices, styles, and languages, high performance metrics, and a compact 600-line codebase. The community discussion highlights excitement about the model's speed and streaming capabilities, with some users expressing a desire for more natural pauses in TTS models.

---

## 35. [My wishes for 2026](https://reddit.com/r/LocalLLaMA/comments/1qbw325/my_wishes_for_2026/)

**Author:** u/jacek2023 | **Upvotes:** 640 | **Comments:** 178 | **Date:** 2026-01-13

**Summary:** The Reddit post discusses predictions for 2026, focusing on the possibility of affordable GPUs with more than 32GB memory. The community engages in a mix of hopeful and skeptical comments about this prospect.

**Key Points:**
- The post asks which predictions for 2026 are likely to happen first.
- A top comment humorously dismisses the idea of affordable GPUs with more than 32GB as unrealistic.
- Another comment references specific AI models (Qwen 4, Mistral) as more plausible developments.
- The community shows a mix of humor and skepticism about the feasibility of affordable high-memory GPUs.
- The post gained significant traction with 640 upvotes and 178 comments.

**Discussion Highlights:** The discussion highlights a consensus of skepticism regarding the affordability of high-memory GPUs in 2026, with some users humorously dismissing the idea. There is also mention of other AI models as more realistic advancements for the year.

---

## 36. [kyutai just introduced Pocket TTS: a 100M-parameter text-to-speech model with high-quality voice cloning that runs on your laptop—no GPU required](https://reddit.com/r/LocalLLaMA/comments/1qbpz5l/kyutai_just_introduced_pocket_tts_a_100mparameter/)

**Author:** u/Nunki08 | **Upvotes:** 393 | **Comments:** 91 | **Date:** 2026-01-13

**Summary:** Kyutai introduced Pocket TTS, a 100M-parameter text-to-speech model with high-quality voice cloning that runs on a laptop without requiring a GPU. The model is available on GitHub and Hugging Face, with a blog post and arXiv paper providing more details.

**Key Points:**
- Pocket TTS is a 100M-parameter TTS model with high-quality voice cloning.
- It runs on a laptop without needing a GPU.
- The model is available on GitHub and Hugging Face.
- A warning about memory usage during generation was highlighted in the comments.
- Discussion includes inquiries about language support and comparisons with other small models.

**Discussion Highlights:** The discussion highlights a warning about memory usage ballooning during generation, reaching up to 32 GB on one user's system. There are also inquiries about fine-tuning the model for different languages and comparisons with other small TTS models.

---

## 37. [baichuan-inc/Baichuan-M3-235B · Hugging Face](https://reddit.com/r/LocalLLaMA/comments/1qbjbrf/baichuanincbaichuanm3235b_hugging_face/)

**Author:** u/jacek2023 | **Upvotes:** 120 | **Comments:** 34 | **Date:** 2026-01-12

**Summary:** Baichuan-M3 is a new-generation medical-enhanced large language model by Baichuan AI, designed to improve clinical decision-making with high-fidelity inquiry and low hallucination rates. It outperforms GPT-5.2 in medical benchmarks and offers efficient deployment options.

**Key Points:**
- Baichuan-M3 focuses on clinical decision-making and reduces hallucinations.
- It surpasses GPT-5.2 in medical benchmarks like HealthBench and BCOSCE.
- The model achieves efficient deployment with W4 quantization and speculative decoding.
- Users discuss hardware requirements and potential use cases like private medical opinions.
- Some users express interest in fine-tuning or vision capabilities.

**Discussion Highlights:** The discussion includes reactions about hardware needs (e.g., RTX 6000 pro), interest in fine-tuning (Qwen), and appreciation for the model's medical use cases. Some users highlight the lack of vision capabilities as a limitation.

---

