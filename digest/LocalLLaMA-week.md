# r/LocalLLaMA Reading Digest

**Period:** 2026-01-21 to 2026-01-21
**Posts Summarized:** 47
**Total Posts Analyzed:** 47

---

## 1. [Current GLM-4.7-Flash implementation confirmed to be broken in llama.cpp](https://reddit.com/r/LocalLLaMA/comments/1qih9r8/current_glm47flash_implementation_confirmed_to_be/)

**Author:** u/Sweet_Albatross9772 | **Upvotes:** 160 | **Comments:** 38 | **Date:** 2026-01-20

**Summary:** The Reddit post confirms that the current GLM-4.7-Flash implementation in llama.cpp is broken, with significant differences in logprobs compared to vLLM, leading to issues like looping and poor performance. A potential fix is already proposed in a pull request.

**Key Points:**
- GLM-4.7-Flash implementation in llama.cpp is confirmed broken
- Significant differences in logprobs compared to vLLM
- Potential fix proposed in a pull request by Piotr
- Community response is generally patient and understanding
- Bugs in new model integrations are common and expected

**Discussion Highlights:** The community acknowledges the issue and is patient, with some users pointing out that bugs in new model integrations are common. There is a general consensus to wait for the fix rather than attempting to troubleshoot immediately.

---

## 2. [You have 64gb ram and 16gb VRAM; internet is permanently shut off: what 3 models are the ones you use?](https://reddit.com/r/LocalLLaMA/comments/1qids6a/you_have_64gb_ram_and_16gb_vram_internet_is/)

**Author:** u/Adventurous-Gold6413 | **Upvotes:** 262 | **Comments:** 191 | **Date:** 2026-01-20

**Summary:** The post discusses the selection of local models for use with 64GB RAM and 16GB VRAM when internet access is unavailable. Users share their preferences and experiences with various models. Key points include the recommendation of books as a valuable resource, the high praise for GPT-OSS-120B for its performance and compatibility, and the mention of Gemma 3 27B and GLM 4.5 Air as viable options. The discussion highlights a consensus around the effectiveness of GPT-OSS-120B for the given hardware setup, with an emphasis on the importance of having diverse models, including abliterated ones.

---

## 3. [Liquid AI released the best thinking Language Model Under 1GB](https://reddit.com/r/LocalLLaMA/comments/1qi512t/liquid_ai_released_the_best_thinking_language/)

**Author:** u/PauLabartaBajo | **Upvotes:** 190 | **Comments:** 46 | **Date:** 2026-01-20

**Summary:** Liquid AI released LFM2.5-1.2B-Thinking, a compact reasoning model optimized for on-device use, excelling in math, tool use, and instruction following. It outperforms larger models in speed and memory efficiency, though some users question its real-world applicability and licensing terms.

**Key Points:**
- LFM2.5-1.2B-Thinking is a 1.2B parameter model designed for concise reasoning and edge deployment.
- It outperforms larger models like Qwen3-1.7B in benchmarks despite fewer parameters.
- Users raise concerns about memory requirements, performance trade-offs, and licensing restrictions.
- The model is available on Hugging Face, LEAP, and Liquid AI Playground.

**Discussion Highlights:** The discussion highlights skepticism about memory efficiency claims, with users noting that quantization may be necessary for edge deployment. Some argue the model's performance is mainly an improvement in math tasks, while others express a desire for larger models with broader real-world applicability. Licensing terms also drew criticism.

---

## 4. [768Gb Fully Enclosed 10x GPU Mobile AI Build](https://reddit.com/r/LocalLLaMA/comments/1qi4uj2/768gb_fully_enclosed_10x_gpu_mobile_ai_build/)

**Author:** u/SweetHomeAbalama0 | **Upvotes:** 668 | **Comments:** 181 | **Date:** 2026-01-20

**Summary:** The post describes a custom-built, fully enclosed 10-GPU mobile AI system designed for running large MoE models and supporting graphic design tasks. The build, costing around $17k, balances performance and budget constraints while addressing mobility and enclosure challenges.

**Key Points:**
- The system features a Threadripper Pro 3995WX, 512GB DDR4, and 10 GPUs (8x 3090 + 2x 5090).
- It is designed for large MoE models, video generation, and high-detail image generation.
- The enclosure was a major challenge, solved using a Thermaltake Core W200 case.
- Budget constraints led to a mix of GPUs to optimize cost and performance.
- The post received significant engagement, with comments highlighting its uniqueness and practicality.

**Discussion Highlights:** The discussion highlights the system's impressive capabilities and the creative solution to the enclosure problem. Comments also joke about the system's portability and power requirements, emphasizing its uniqueness and appeal to the subreddit's audience.

---

## 5. [glm-4.7-flash has the best thinking process with clear steps, I love it](https://reddit.com/r/LocalLLaMA/comments/1qhxlgy/glm47flash_has_the_best_thinking_process_with/)

**Author:** u/uptonking | **Upvotes:** 127 | **Comments:** 31 | **Date:** 2026-01-20

**Summary:** The Reddit post discusses the user's experience with the glm-4.7-flash model, highlighting its structured thinking process and comparing it favorably to other models like nemotron-nano and qwen3-30b. The user appreciates the model's clear reasoning steps but notes its slower performance and seeks ways to optimize it. Key points include the model's detailed thinking process, slower performance compared to other models, appreciation for its reasoning process, and suggestions for optimization. The discussion highlights a consensus on the model's superior reasoning process, with concerns about its slower performance and suggestions for optimization.

---

## 6. [It's been one year since the release of Deepseek-R1](https://reddit.com/r/LocalLLaMA/comments/1qhs2sd/its_been_one_year_since_the_release_of_deepseekr1/)

**Author:** u/Recoil42 | **Upvotes:** 285 | **Comments:** 50 | **Date:** 2026-01-19

**Summary:** The Reddit post commemorates the one-year anniversary of the Deepseek-R1 release, highlighting its significant impact on the AI community, including its influence on major players like Meta and the rapid pace of advancements in the field.

**Key Points:**
- Deepseek-R1 had a major impact, reportedly causing Meta to disband its flagship AI training team and reassess its strategies.
- The release is considered one of the most significant in AI history, second only to the original Llama model.
- The rapid pace of AI advancements is noted, with the past year feeling like several years due to the volume of progress.
- Deepseek-R1's release led to slashed prices and increased transparency in AI model outputs.

**Discussion Highlights:** The discussion highlights the transformative impact of Deepseek-R1 on the AI landscape, with users emphasizing its role in forcing industry changes, accelerating progress, and setting new standards for model performance and transparency.

---

## 7. [Mosquito - 7.3M parameter tiny knowledge model](https://reddit.com/r/LocalLLaMA/comments/1qhqzsi/mosquito_73m_parameter_tiny_knowledge_model/)

**Author:** u/Lopsided-Repair-3638 | **Upvotes:** 113 | **Comments:** 51 | **Date:** 2026-01-19

**Summary:** The post introduces 'Mosquito', a tiny 7.3M parameter language model that can answer general knowledge questions, though with some humorous inaccuracies. Users shared mixed reactions, highlighting both its surprising capabilities and obvious limitations.

**Key Points:**
- Mosquito is a 7.3M parameter model designed for general knowledge questions
- The model demonstrates surprising capabilities despite its small size
- Users noted humorous inaccuracies, such as defining a dog incorrectly
- Some comments requested quantization for better performance
- The model's responses were inconsistent, with some correct and others nonsensical

**Discussion Highlights:** The discussion was lighthearted, with users sharing funny examples of the model's inaccuracies while acknowledging its potential. There was no clear consensus, but the general tone was amused curiosity.

---

## 8. [Bartowski comes through again. GLM 4.7 flash GGUF](https://reddit.com/r/LocalLLaMA/comments/1qhpima/bartowski_comes_through_again_glm_47_flash_gguf/)

**Author:** u/RenewAi | **Upvotes:** 178 | **Comments:** 50 | **Date:** 2026-01-19

**Summary:** The post announces the release of the GLM 4.7 Flash GGUF model by Bartowski, with mixed user feedback on its performance. Some users report issues with the model's functionality and template errors.

**Key Points:**
- Bartowski released GLM 4.7 Flash GGUF model on Hugging Face
- Users report mixed results, with some experiencing template and syntax errors
- Comparisons made with other quantized versions like Unsloth's Q8
- Some users prefer returning to alternative models like Qwen3 Coder 30
- Ongoing discussion about model performance and usability

**Discussion Highlights:** Users are testing different quantized versions of GLM 4.7 Flash, with reports of template issues and syntax errors. The consensus leans toward caution, as some find the model non-functional or prefer alternatives like Qwen3 Coder 30. The discussion highlights ongoing experimentation and feedback sharing among users.

---

## 9. [Unsloth GLM 4.7-Flash GGUF](https://reddit.com/r/LocalLLaMA/comments/1qhlnsv/unsloth_glm_47flash_gguf/)

**Author:** u/Wooden-Deer-1276 | **Upvotes:** 225 | **Comments:** 44 | **Date:** 2026-01-19

**Summary:** The Reddit post discusses the release of the Unsloth GLM 4.7-Flash GGUF model, with community feedback on its performance and recommendations for optimal usage.

**Key Points:**
- The model is being released with caution to ensure proper functionality.
- Specific quantization settings (e.g., UD-Q4_K_XL) and parameters (e.g., --temp 0.2, --dry-multiplier 1.1) are recommended for best results.
- There are ongoing issues with looping in quantized versions, with BF16 being suggested as the best alternative for now.
- The community is actively engaged, with updates and fixes being shared.
- A BF16 version of the model has been released, as indicated by a shared image.

**Discussion Highlights:** The community emphasizes patience and thorough testing before full release. Key discussions revolve around optimal settings for the model, ongoing technical issues like looping, and the recent release of the BF16 version. There is a consensus on using higher-quality quantizations and specific parameters to mitigate issues.

---

## 10. [GLM 4.7 Flash official support merged in llama.cpp](https://reddit.com/r/LocalLLaMA/comments/1qhitrj/glm_47_flash_official_support_merged_in_llamacpp/)

**Author:** u/ayylmaonade | **Upvotes:** 355 | **Comments:** 57 | **Date:** 2026-01-19

**Summary:** The Reddit post announces the official support for GLM 4.7 Flash in llama.cpp, highlighting its community-driven development and performance improvements. Users discuss its efficiency and share additional resources. Key points include: GLM 4.7 Flash now officially supported in llama.cpp, support is community-driven, performance improvements noted, additional resources and versions shared by community members, and mixed feedback on flash-attention performance. The discussion highlights the community effort behind the integration and shares performance insights. Some users report faster execution times, while others note issues with flash-attention performance. Additional resources and versions are shared for further exploration.

---

## 11. [My gpu poor comrades, GLM 4.7 Flash is your local agent](https://reddit.com/r/LocalLLaMA/comments/1qhii5v/my_gpu_poor_comrades_glm_47_flash_is_your_local/)

**Author:** u/__Maximum__ | **Upvotes:** 447 | **Comments:** 152 | **Date:** 2026-01-19

**Summary:** The Reddit post highlights GLM 4.7 Flash as a reliable local agent, outperforming other MoE models in an agentic framework with successful tool calling and task execution. The community discusses its performance, comparisons with other models, and anticipation for local GGUF versions.

**Key Points:**
- GLM 4.7 Flash is praised for its reliability and performance in agentic tasks.
- It successfully handles complex tasks like cloning repos, running commands, and editing files.
- The community compares it favorably to models like Nemotron 30B and Qwen3.
- Performance benchmarks suggest it is as smart as SEED OSS 36B but with better efficiency.
- GGUF versions are anticipated for local use.

**Discussion Highlights:** The discussion highlights enthusiasm for GLM 4.7 Flash's capabilities, with users sharing benchmarks, comparisons, and early testing results. There is a consensus on its strong performance and potential as a local agent.

---

## 12. [New in llama.cpp: Anthropic Messages API](https://reddit.com/r/LocalLLaMA/comments/1qhaq21/new_in_llamacpp_anthropic_messages_api/)

**Author:** u/paf1138 | **Upvotes:** 163 | **Comments:** 50 | **Date:** 2026-01-19

**Summary:** The Reddit post announces the new Anthropic Messages API in llama.cpp, generating excitement among users who are eager to try it out. The discussion includes practical tips for implementation and mentions Claude's context capabilities.

**Key Points:**
- New Anthropic Messages API introduced in llama.cpp
- Users express enthusiasm and readiness to test the feature
- Practical implementation tips provided for quick setup
- Mention of Claude's 12k context capability

**Discussion Highlights:** The discussion highlights user enthusiasm for the new API, with practical advice on implementation and mentions of Claude's context capabilities. Some users note the feature's age, while others share quick setup methods.

---

## 13. [zai-org/GLM-4.7-Flash · Hugging Face](https://reddit.com/r/LocalLLaMA/comments/1qh5wdq/zaiorgglm47flash_hugging_face/)

**Author:** u/Dark_Fire_12 | **Upvotes:** 719 | **Comments:** 225 | **Date:** 2026-01-19

**Summary:** The post announces the release of GLM-4.7-Flash model on Hugging Face, generating significant community interest with 719 upvotes and 225 comments. Users express excitement about the model's capabilities and features.

**Key Points:**
- GLM-4.7-Flash model released on Hugging Face
- Model uses MLA, reducing KV cache memory usage
- Supports full 200k context, making it accessible to more users
- Community expresses enthusiasm and anticipation for the release
- Mentions of model size and architecture details (30b, 3B thinking model)

**Discussion Highlights:** The community shows strong interest in the model's technical features like MLA for memory efficiency and extended context support. There's consensus about the promising nature of this release, with users expressing excitement about running the model locally. Some users also discuss model architecture details and express nostalgia for larger models.

---

## 14. [I made a Top-K implementation that's up to 20x faster than PyTorch CPU (open source)](https://reddit.com/r/LocalLLaMA/comments/1qh0yq8/i_made_a_topk_implementation_thats_up_to_20x/)

**Author:** u/andreabarbato | **Upvotes:** 142 | **Comments:** 104 | **Date:** 2026-01-19

**Summary:** The author developed an AVX2-optimized Top-K implementation that significantly outperforms PyTorch CPU, achieving up to 20x speed improvements depending on vocabulary size. It has been integrated into llama.cpp, resulting in 63% faster prompt processing for a large model.

**Key Points:**
- AVX2-optimized batched Top-K implementation beats PyTorch CPU by 4-20x
- Integrated into llama.cpp, improving prompt processing speed by 63%
- Uses adaptive sampling, AVX2 SIMD, and cache-optimized scanning
- Community feedback includes requests for PR submission and explanations of performance gains
- Some criticism about lack of reproducible benchmarks and vibe coding

**Discussion Highlights:** The community showed strong interest, with top comments requesting a PR submission to llama.cpp and explanations for the performance improvements. Some users criticized the lack of reproducible benchmarks and raised concerns about the code being 'vibe coded.'

---

## 15. [how do you pronounce “gguf”?](https://reddit.com/r/LocalLLaMA/comments/1qglyqz/how_do_you_pronounce_gguf/)

**Author:** u/Hamfistbumhole | **Upvotes:** 109 | **Comments:** 154 | **Date:** 2026-01-18

**Summary:** The Reddit post discusses the pronunciation of 'gguf', with users debating whether it should be pronounced as 'jee-guff', 'giguff', or 'jee jee you eff'. The top comments suggest various pronunciations, with some humorously noting that it should be downloaded silently. Key points include the lack of consensus on pronunciation, humorous suggestions, and the absence of proper phonetic symbols. The discussion is lighthearted and humorous, with no clear consensus on the correct pronunciation.

---

## 16. [Are most major agents really just markdown todo list processors?](https://reddit.com/r/LocalLLaMA/comments/1qgj2n9/are_most_major_agents_really_just_markdown_todo/)

**Author:** u/TheDigitalRhino | **Upvotes:** 101 | **Comments:** 39 | **Date:** 2026-01-18

**Summary:** The Reddit post discusses how major LLM agents decompose tasks into todo lists and process them sequentially, with users confirming this approach is common and effective.

**Key Points:**
- Major LLM agents decompose tasks into smaller, manageable parts.
- This approach is similar to how humans handle complex tasks.
- The strategy has been effective since earlier versions like GPT-3.5.
- Task decomposition is a common and effective strategy among major agents.

**Discussion Highlights:** Users generally agree that breaking down tasks into smaller parts is a standard and effective method used by major LLM agents.

---

## 17. [4x AMD R9700 (128GB VRAM) + Threadripper 9955WX Build](https://reddit.com/r/LocalLLaMA/comments/1qgdb7f/4x_amd_r9700_128gb_vram_threadripper_9955wx_build/)

**Author:** u/NunzeCs | **Upvotes:** 345 | **Comments:** 91 | **Date:** 2026-01-18

**Summary:** The author built a high-performance system with 4x AMD R9700 GPUs (128GB VRAM) and a Threadripper 9955WX CPU, leveraging a 50% subsidy to stay within a 10,000€ budget. The system is designed for running large language models (120B+ parameters) locally, with benchmark results provided for various models.

**Key Points:**
- The system was built to maximize VRAM for running large models locally, with a total of 128GB VRAM from 4x AMD R9700 GPUs.
- The author received a 50% subsidy, reducing the effective cost to ~4,900€.
- Benchmark results show performance metrics for models ranging from 8B to 230B parameters.
- The build includes high-end components like the Threadripper 9955WX CPU and 128GB DDR5 RAM.
- The post gained significant attention, with comments highlighting the impressive hardware and cost.

**Discussion Highlights:** The discussion highlights the impressive hardware setup and the cost-effectiveness due to the subsidy. Comments also show interest in the source of the components and the author's job, as well as comparisons to similar builds.

---

## 18. [Qwen 4 might be a long way off !? Lead Dev says they are "slowing down" to focus on quality.](https://reddit.com/r/LocalLLaMA/comments/1qfv1ms/qwen_4_might_be_a_long_way_off_lead_dev_says_they/)

**Author:** u/Difficult-Cap-7527 | **Upvotes:** 442 | **Comments:** 71 | **Date:** 2026-01-17

**Summary:** The Reddit post discusses a potential slowdown in the development of Qwen 4, with the lead developer emphasizing a focus on quality over quantity. The community generally appreciates this approach, though some caution against jumping to conclusions based on limited information.

**Key Points:**
- Qwen 4 development may be slowing down to focus on quality
- Community appreciates the emphasis on quality over quantity
- Some users caution against overinterpreting limited information
- The post gained significant attention with 442 upvotes and 71 comments
- Top comments highlight both support and skepticism about the development update

**Discussion Highlights:** The discussion reflects a generally positive reception to the focus on quality, with some users expressing appreciation for the careful approach. However, there is also skepticism about the interpretation of the development update, with calls for more concrete information before drawing conclusions.

---

## 19. [128GB VRAM quad R9700 server](https://reddit.com/r/LocalLLaMA/comments/1qfscp5/128gb_vram_quad_r9700_server/)

**Author:** u/Ulterior-Motive_ | **Upvotes:** 527 | **Comments:** 111 | **Date:** 2026-01-17

**Summary:** The post details a server build featuring four AMD Radeon AI PRO R9700 GPUs, totaling 128GB VRAM, which the author chose over MI100 GPUs due to better performance and cost efficiency. The build includes high-end components like a Ryzen 7 5700X CPU and 128GB RAM, with benchmarks showing strong performance in prompt processing.

**Key Points:**
- The author switched from MI100 to R9700 GPUs for better performance and cost efficiency.
- The server build includes four R9700 GPUs, totaling 128GB VRAM, paired with 128GB RAM.
- The total cost of the build was approximately $7,035, which is competitive compared to alternatives like the RTX 6000 Blackwell.
- Performance benchmarks show high token processing speeds, such as 6524.91 tokens per second for the llama 7B Q4_0 model.
- The post received significant engagement, with 527 upvotes and 111 comments, highlighting community interest and appreciation.

**Discussion Highlights:** The discussion highlights include positive community reactions, with comments praising the build and expressing admiration for its performance and cost efficiency. Some users humorously noted the financial irresponsibility of such high-end builds, while others appreciated the detailed benchmarks and specifications provided.

---

## 20. [The Search for Uncensored AI (That Isn’t Adult-Oriented)](https://reddit.com/r/LocalLLaMA/comments/1qfq9ez/the_search_for_uncensored_ai_that_isnt/)

**Author:** u/Fun-Situation-4358 | **Upvotes:** 274 | **Comments:** 215 | **Date:** 2026-01-17

**Summary:** The post discusses the challenge of finding uncensored AI models that prioritize reasoning and creativity over adult-oriented content, highlighting a gap between heavily restricted corporate AI and shallow adult-focused models. Key points include the author's search for genuinely unfiltered AI, the prevalence of adult-oriented models, and the perceived gap in the market. The discussion highlights a shared frustration with the lack of AI models that balance uncensored capabilities with serious problem-solving and creativity.

---

## 21. [China's AGI-NEXT Conference (Qwen, Kimi, Zhipu, Tencent)](https://reddit.com/r/LocalLLaMA/comments/1qfmc05/chinas_aginext_conference_qwen_kimi_zhipu_tencent/)

**Author:** u/nuclearbananana | **Upvotes:** 117 | **Comments:** 22 | **Date:** 2026-01-17

**Summary:** The Reddit post discusses China's AGI-NEXT Conference, highlighting insights on China vs US AGI development, paths to AGI, compute resources, and marketing strategies. It mentions internal advancements like Qwen3.5 and large context windows, and notes the absence of Deepseek despite their talent concentration.

**Key Points:**
- Qwen has internally developed Qwen3.5 and context windows in the millions.
- The next paradigm in AGI is believed to likely come from OpenAI rather than Google.
- Chinese work culture is described as less willing to take risks for innovation.
- Deepseek, despite having strong talent, was notably absent from the conference.

**Discussion Highlights:** The discussion highlights include interest in Qwen's internal advancements, speculation on the next paradigm in AGI, and observations about risk-taking in Chinese work culture. There is also mention of Deepseek's absence despite their strong talent pool.

---

## 22. [Best "End of world" model that will run on 24gb VRAM](https://reddit.com/r/LocalLLaMA/comments/1qfkn3a/best_end_of_world_model_that_will_run_on_24gb_vram/)

**Author:** u/gggghhhhiiiijklmnop | **Upvotes:** 337 | **Comments:** 176 | **Date:** 2026-01-17

**Summary:** The user is seeking recommendations for the best LLM model that can run on a PC with 24GB VRAM and 64GB RAM, in preparation for a hypothetical 'end of world' scenario where they have downloaded extensive data like Wikipedia and Khan Academy.

**Key Points:**
- User wants a model that fits within 24GB VRAM and 64GB RAM.
- Suggestions include saving the best possible LLM and running it off SSD if necessary.
- Specific model recommendations include gemma3:27b for its capabilities and vision features.
- Alternative suggestions like downloading actual Wikipedia backups for offline access.
- Humorous or off-topic comments like 'Midnight Miku for the cold nuclear winter nights.'

**Discussion Highlights:** The discussion highlights a mix of practical advice, such as using gemma3:27b or downloading Wikipedia backups, and humorous or off-topic comments. There is a consensus on prioritizing the best possible LLM within the given hardware constraints.

---

## 23. [DeepSeek Engram : A static memory unit for LLMs](https://reddit.com/r/LocalLLaMA/comments/1qf5oj0/deepseek_engram_a_static_memory_unit_for_llms/)

**Author:** u/Technical-Love-8479 | **Upvotes:** 316 | **Comments:** 47 | **Date:** 2026-01-17

**Summary:** DeepSeek AI introduced Engram, a memory unit for LLMs that separates remembering from reasoning, enabling O(1) knowledge lookup and improving performance without GPU limits.

**Key Points:**
- Engram introduces conditional memory, separating it from reasoning.
- Knowledge lookup is O(1), improving efficiency.
- Enables massive memory scaling without GPU constraints.
- Improves reasoning, math, and code performance.
- Frees attention for global reasoning rather than static knowledge.

**Discussion Highlights:** The community is excited about the separation of memory and reasoning, highlighting the efficiency gains and potential for scaling memory independently of model size.

---

## 24. [Prompt Repetition Improves Non-Reasoning LLMs - a paper](https://reddit.com/r/LocalLLaMA/comments/1qeuh0z/prompt_repetition_improves_nonreasoning_llms_a/)

**Author:** u/Foreign-Beginning-49 | **Upvotes:** 109 | **Comments:** 51 | **Date:** 2026-01-16

**Summary:** The Reddit post discusses a paper showing that repeating prompts can significantly improve the performance of non-reasoning LLMs without affecting latency or output format. The technique is simple yet effective across various models and benchmarks.

**Key Points:**
- Prompt repetition improves non-reasoning LLM performance.
- The technique does not impact latency or output format.
- Deepseek is highlighted as an open weights model tested in the paper.
- The simplicity of the technique raises questions about other untapped improvements.
- Some users have been informally using similar techniques for years.

**Discussion Highlights:** The discussion highlights surprise at the effectiveness of such a simple technique and speculation about other potential improvements. Users also reflect on how little is understood about LLMs and their current architectures.

---

## 25. [performance benchmarks (72GB VRAM) - llama.cpp server - January 2026](https://reddit.com/r/LocalLLaMA/comments/1qennp2/performance_benchmarks_72gb_vram_llamacpp_server/)

**Author:** u/jacek2023 | **Upvotes:** 109 | **Comments:** 34 | **Date:** 2026-01-16

**Summary:** The Reddit post by u/jacek2023 presents performance benchmarks for various AI models run on a system with three RTX 3090 GPUs and 72GB VRAM. The benchmarks measure tokens per second for different models, with ERNIE-4.5-21B-A3B-Thinking-Q8_0 achieving the highest speed at 147.85 tokens/s. The post emphasizes that the measurements focus on speed, not accuracy, and are not scientifically rigorous.

**Key Points:**
- Performance benchmarks for AI models on a system with three RTX 3090 GPUs and 72GB VRAM.
- ERNIE-4.5-21B-A3B-Thinking-Q8_0 achieved the highest speed at 147.85 tokens/s.
- The benchmarks measure speed only, not accuracy.
- Suggestions for improving performance include filling the context to ~10k tokens and using specific compilation flags.
- Discussion highlights include the use of specific flags for GPU data copying and inquiries about GPU interconnectivity.

**Discussion Highlights:** The discussion includes suggestions for further performance measurements, such as filling the context to ~10k tokens and using specific compilation flags like -DGGML_CUDA_PEER_COPY=ON for direct GPU data copying. There are also inquiries about the interconnectivity of the RTX 3090 GPUs and comparisons of performance with other setups.

---

## 26. [I reproduced DeepSeek's mHC at 1.7B params (8xH100). The instability is 3x worse than reported (10k vs 3k), but the model didn't explode.](https://reddit.com/r/LocalLLaMA/comments/1qek917/i_reproduced_deepseeks_mhc_at_17b_params_8xh100/)

**Author:** u/poisson_labs | **Upvotes:** 173 | **Comments:** 29 | **Date:** 2026-01-16

**Summary:** The author reproduced DeepSeek's mHC at 1.7B parameters and found that the signal variance amplification was significantly worse than reported (10,924x vs 3,000x), but the model continued to learn without diverging. The Manifold Hyper-Connections (mHC) with Sinkhorn projection was confirmed to solve the instability issue with no compute overhead.

**Key Points:**
- Signal variance amplification at 1.7B parameters was 10,924x, worse than the reported 3,000x.
- Despite high signal amplification, the model did not diverge, possibly due to modern optimizers and gradient clipping.
- Manifold Hyper-Connections (mHC) with Sinkhorn projection completely solves the instability issue with zero compute overhead.
- The author provided detailed breakdowns and loss curves in external links.
- Discussion highlights include skepticism about zero compute overhead and interest in alternative optimizers like muon.

**Discussion Highlights:** The discussion includes skepticism about the claim of zero compute overhead for mHC, interest in exploring alternative optimizers like muon, and appreciation for the resourcefulness of DeepSeek's research.

---

## 27. [Maxsun joins Sparkle in making Intel Arc B60 Pro GPUs available to regular consumers, with up to 48GB VRAM](https://reddit.com/r/LocalLLaMA/comments/1qehf0p/maxsun_joins_sparkle_in_making_intel_arc_b60_pro/)

**Author:** u/reps_up | **Upvotes:** 136 | **Comments:** 50 | **Date:** 2026-01-16

**Summary:** Maxsun and Sparkle are making Intel Arc B60 Pro GPUs available to consumers, featuring up to 48GB VRAM. The Reddit discussion highlights user interest in higher VRAM capacities and inquiries about framework support and availability.

**Key Points:**
- Intel Arc B60 Pro GPUs now available to consumers
- Up to 48GB VRAM offered
- User interest in higher VRAM capacities
- Inquiries about torch/JAX/ONNX support
- Questions about availability in Europe

**Discussion Highlights:** Users expressed strong interest in higher VRAM capacities, with some requesting up to 128GB. There were also questions about the support for frameworks like torch/JAX/ONNX and the availability of these GPUs in Europe.

---

## 28. [GPT-5.2 xhigh, GLM-4.7, Kimi K2 Thinking, DeepSeek v3.2 on Fresh SWE-rebench (December 2025)](https://reddit.com/r/LocalLLaMA/comments/1qefa7q/gpt52_xhigh_glm47_kimi_k2_thinking_deepseek_v32/)

**Author:** u/CuriousPlatypus1881 | **Upvotes:** 376 | **Comments:** 89 | **Date:** 2026-01-16

**Summary:** The post discusses the December 2025 SWE-bench leaderboard results, highlighting the performance of various AI models on GitHub PR tasks. Claude Opus 4.5 leads with a 63.3% resolved rate, followed closely by GPT-5.2 (extra high effort) at 61.5%. GLM-4.7 stands out as the strongest open-source model, ranking alongside closed models like GPT-5.1-codex. The community is particularly excited about the performance of open-source models like GLM-4.7, which ranks in the top 10. There is also anticipation for future releases like DeepSeek v4, with users expressing excitement for February updates.

---

## 29. [I fucking love this community](https://reddit.com/r/LocalLLaMA/comments/1qee2de/i_fucking_love_this_community/)

**Author:** u/alhinai_03 | **Upvotes:** 499 | **Comments:** 54 | **Date:** 2026-01-16

**Summary:** The author expresses gratitude to the open-source community for enabling them to run large language models on older hardware with limited VRAM, highlighting the effectiveness of MoE architectures and sufficient system memory.

**Key Points:**
- Gratitude to the open-source community for their contributions
- Running large models on a 10-year-old PC with 4GB VRAM
- Achieving 14-13.5 tokens per second with nemotron-3-nano-30B-a3b-iq4_nl
- Importance of system memory and MoE architecture for performance
- Community appreciation for optimization efforts

**Discussion Highlights:** The community agrees that the optimization efforts are impressive, highlighting the practicality of using system RAM and MoE architectures for running large models on older hardware.

---

## 30. [New FLUX.2 [Klein] 9B is INSANELY Fast](https://reddit.com/r/LocalLLaMA/comments/1qe9xfi/new_flux2_klein_9b_is_insanely_fast/)

**Author:** u/Lopsided_Dot_4557 | **Upvotes:** 107 | **Comments:** 26 | **Date:** 2026-01-16

**Summary:** The Reddit post highlights the impressive performance of the new FLUX.2 [Klein] 9B model, which offers sub-second inference on RTX 4090 hardware and matches the performance of larger models with 9B parameters. The model features step-distillation and unified text-to-image capabilities, making it highly efficient.

**Key Points:**
- Sub-second inference on RTX 4090 hardware
- 9B parameters matching models 5x its size
- Step-distilled from 50 → 4 steps with zero quality loss
- Unified text-to-image + multi-reference editing
- Efficient GPU usage with decent image quality

**Discussion Highlights:** The discussion highlights include praise for the model's efficiency and speed, though some users note minor issues like occasional image artifacts (e.g., six fingers). There is also curiosity about how it compares to other models like zimage turbo.

---

## 31. [Dang, M2 drives are the new DDR5 apparently.](https://reddit.com/r/LocalLLaMA/comments/1qe4so5/dang_m2_drives_are_the_new_ddr5_apparently/)

**Author:** u/Porespellar | **Upvotes:** 217 | **Comments:** 97 | **Date:** 2026-01-15

**Summary:** The Reddit post discusses the significant increase in prices of M2 drives, with users expressing frustration over the rising costs. Many users share their personal experiences with price hikes and discuss the impact on their purchasing decisions.

**Key Points:**
- M2 drive prices have increased significantly
- Users express frustration over rising costs
- Personal experiences with price hikes are shared
- Impact on purchasing decisions is discussed

**Discussion Highlights:** The discussion highlights a consensus among users about the frustration and financial strain caused by the rising prices of M2 drives. Many users share their personal experiences and discuss the impact on their purchasing decisions, with some opting to keep older hardware as a backup.

---

## 32. [My story of underestimating /r/LocalLLaMA's thirst for VRAM](https://reddit.com/r/LocalLLaMA/comments/1qe2i88/my_story_of_underestimating_rlocalllamas_thirst/)

**Author:** u/EmPips | **Upvotes:** 1306 | **Comments:** 88 | **Date:** 2026-01-15

**Summary:** The Reddit post discusses the author's experience with the subreddit's high demand for VRAM, as indicated by the title and the context of the comments. The post gained significant attention, as shown by the upvotes and comments.

**Key Points:**
- The post gained popularity with 1306 upvotes and 88 comments.
- The author received recognition, including a special flair and a feature on Discord.
- Comments discuss the demand for VRAM and related hardware, with references to specific graphics cards and their performance.
- The discussion includes comparisons between different graphics cards and their suitability for various tasks.

**Discussion Highlights:** The discussion highlights the community's interest in VRAM and hardware performance, with specific mentions of graphics cards like the 3090 and R9700. There is also a humorous reference to the California gold rush, comparing the demand for VRAM to the rush for gold.

---

## 33. [Latest upgrade…A100 40 GB](https://reddit.com/r/LocalLLaMA/comments/1qe0cxc/latest_upgradea100_40_gb/)

**Author:** u/inserterikhere | **Upvotes:** 402 | **Comments:** 54 | **Date:** 2026-01-15

**Summary:** The user upgraded their gaming rig to an AI rig by purchasing a faulty A100 GPU for $1000, which worked perfectly upon installation. They previously used a 3090 and 7950x for AI tasks but decided to upgrade due to the low price of the A100, despite it being listed as faulty.

**Key Points:**
- User transitioned from a gaming rig to an AI rig using existing parts.
- Purchased an A100 GPU listed as faulty for $1000, which worked upon installation.
- Previously used a 3090 and 7950x for AI tasks.
- Community expressed concerns about cooling the A100.
- Post received positive reception with 402 upvotes and 54 comments.

**Discussion Highlights:** The community reacted positively to the post, with some users expressing concerns about cooling the A100 GPU. One comment suggested using a blower fan or water cooling to prevent overheating. The post was also featured on the subreddit's Discord server.

---

## 34. [Not as impressive as most here, but really happy I made it in time!](https://reddit.com/r/LocalLLaMA/comments/1qdtvgs/not_as_impressive_as_most_here_but_really_happy_i/)

**Author:** u/Kahvana | **Upvotes:** 145 | **Comments:** 44 | **Date:** 2026-01-15

**Summary:** The author shares their experience building a PC in the Netherlands, highlighting challenges with GPU availability and pricing. They successfully assembled a system with two RTX 5060 Ti GPUs and other high-end components, emphasizing the importance of checking stock availability directly with stores.

**Key Points:**
- GPU availability and pricing are challenging in the Netherlands.
- The author recommends calling stores to check stock availability due to inaccurate online listings.
- The build includes high-end components like two RTX 5060 Ti GPUs and 96GB of DDR5 RAM.
- The motherboard was chosen for its PCI-E 5.0 splitting capabilities to optimize GPU performance.
- Discussion highlights include questions about CPU upgrades for inference speed and recommendations for GPU cooling solutions.

**Discussion Highlights:** The discussion includes questions about potential CPU upgrades for better inference performance, humorous comments about the tidiness of the build, and recommendations for managing GPU heat during prolonged use. There is also a consensus on the cost-effectiveness of the build compared to higher-end alternatives.

---

## 35. [Nemotron-3-nano:30b is a spectacular general purpose local LLM](https://reddit.com/r/LocalLLaMA/comments/1qdrf3o/nemotron3nano30b_is_a_spectacular_general_purpose/)

**Author:** u/DrewGrgich | **Upvotes:** 215 | **Comments:** 125 | **Date:** 2026-01-15

**Summary:** The Reddit post praises Nemotron-3-nano:30b as an exceptionally intelligent 30b model, outperforming larger models like Llama 3.3:70b in general-purpose tasks, though it has a robotic tone unsuitable for creative or chat purposes. Users recommend it for research and analysis due to its high reasoning quality and are eagerly anticipating the upcoming Nemotron 3 super (100b) version.

**Key Points:**
- Nemotron-3-nano:30b is highly praised for its intelligence and performance in general-purpose tasks.
- It outperforms larger models like Llama 3.3:70b in reasoning and structured output tasks.
- The model's robotic tone is seen as a feature for research and analysis purposes.
- Users are looking forward to the Nemotron 3 super (100b) version for additional innovations and speed improvements.
- Some users prefer Qwen3-vl-30b-a3b-instruct for its vision-language capabilities.

**Discussion Highlights:** The discussion highlights the model's exceptional reasoning quality and performance in structured tasks, with users appreciating its robotic tone for research purposes. There is anticipation for the upcoming Nemotron 3 super (100b) version, and some users compare it favorably to other models like Qwen3-vl-30b-a3b-instruct for specific use cases.

---

## 36. [Thanks to you guys, Soprano TTS now supports OpenAI-compatible endpoint, ONNX, ComfyUI, WebUI, and CLI on CUDA, MPS, ROCm, and CPU!](https://reddit.com/r/LocalLLaMA/comments/1qdpb2v/thanks_to_you_guys_soprano_tts_now_supports/)

**Author:** u/eugenekwek | **Upvotes:** 109 | **Comments:** 26 | **Date:** 2026-01-15

**Summary:** The Reddit post announces updates to Soprano TTS, highlighting community contributions that enable support for OpenAI-compatible endpoints, ONNX, ComfyUI, WebUI, and CLI across various platforms (CUDA, MPS, ROCm, CPU). The author expresses gratitude for the community's support and contributions.

**Key Points:**
- Soprano TTS now supports OpenAI-compatible endpoints, ONNX, ComfyUI, WebUI, and CLI.
- Community contributions include WebUI, CLI, OpenAI-compatible endpoint, ONNX, and ComfyUI support.
- Additional features include an automatic hallucination detector and transformers streaming support.
- Platform support expanded to CUDA, MPS, ROCm, and CPU.
- Author thanks the community for their contributions and support.

**Discussion Highlights:** The discussion includes comparisons to Kokoro for consistency, interest in finetuning support, appreciation for local TTS for accessibility and privacy, and inquiries about hardware compatibility.

---

## 37. [google/translategemma](https://reddit.com/r/LocalLLaMA/comments/1qdok2i/googletranslategemma/)

**Author:** u/BreakfastFriendly728 | **Upvotes:** 176 | **Comments:** 56 | **Date:** 2026-01-15

**Summary:** The Reddit post discusses Google's TranslateGemma model, highlighting its technical report and key features. Users express concerns about its limited context size and lack of comparisons to other models.

**Key Points:**
- TranslateGemma model by Google
- 4.3B tokens used during SFT
- 2K token input context limit
- Lack of comparison to other models like tencent/HY-MT1.5
- User requests for GGUF format

**Discussion Highlights:** Users are critical of the model's limited context size and the lack of comprehensive comparisons. There is also a demand for additional formats like GGUF.

---

## 38. [7x Longer Context Reinforcement Learning in Unsloth](https://reddit.com/r/LocalLLaMA/comments/1qdna3t/7x_longer_context_reinforcement_learning_in/)

**Author:** u/danielhanchen | **Upvotes:** 245 | **Comments:** 28 | **Date:** 2026-01-15

**Summary:** Unsloth introduces techniques enabling 7x longer context lengths for Reinforcement Learning, allowing training of models like gpt-oss 20b QLoRA with up to 20K context on a 24GB card without accuracy loss. The post highlights compatibility with various models and features like weight-sharing, Flex Attention, and Float8 training.

**Key Points:**
- Unsloth enables 7x longer context lengths for RL, supporting up to 20K context on a 24GB card.
- Features include weight-sharing, Flex Attention, and Float8 training for memory efficiency.
- Compatibility with models like Llama, Gemma, and Qwen3-8B for extended context training.
- Free Colab notebooks and educational resources provided for implementation.
- Community recognition and interest in further scalability and data sources.

**Discussion Highlights:** The community praised the advancements, with discussions focusing on scalability (e.g., 'road to 10X moves fast') and practical questions about training data sources for long contexts. Some users inquired about compatibility with specific models like Qwen3 30B-3A.

---

## 39. [RTX 5070 Ti and RTX 5060 Ti 16 GB no longer manufactured](https://reddit.com/r/LocalLLaMA/comments/1qdh28f/rtx_5070_ti_and_rtx_5060_ti_16_gb_no_longer/)

**Author:** u/Paramecium_caudatum_ | **Upvotes:** 232 | **Comments:** 95 | **Date:** 2026-01-15

**Summary:** Nvidia has reduced supply for the RTX 5070 Ti and RTX 5060 Ti 16 GB due to memory shortages, leading to price increases and limited availability. The 8 GB configuration of the RTX 5060 Ti remains unaffected.

**Key Points:**
- Nvidia has killed off supply for the RTX 5070 Ti and reduced supply for the RTX 5060 Ti 16 GB
- Prices for the RTX 5070 Ti have risen ~$100 over MSRP, with further hikes expected
- The 8 GB configuration of the RTX 5060 Ti is unaffected by the supply issues
- Users express disappointment and share their experiences with the GPUs
- Some users report securing GPUs at lower prices before the supply issues

**Discussion Highlights:** Users express frustration over the supply issues and price hikes, with some sharing their recent purchases and experiences. There is a consensus that the supply reduction has disrupted upgrade plans for many.

---

## 40. [LFM 2.5 is insanely good](https://reddit.com/r/LocalLLaMA/comments/1qdax6z/lfm_25_is_insanely_good/)

**Author:** u/guiopen | **Upvotes:** 106 | **Comments:** 33 | **Date:** 2026-01-14

**Summary:** The Reddit post highlights the impressive performance of the LFM 2.5 model, noting its effectiveness despite its small size (~1b parameters). The author compares it favorably to larger models and praises its performance in Portuguese, a non-officially supported language. The discussion includes mixed reviews on its capabilities, with some users noting limitations in basic QA and summarization tasks.

**Key Points:**
- LFM 2.5 is praised for its performance, comparable to models 3x larger
- Effective in Portuguese despite not being officially supported
- Performs well in basic QA and summarization tasks at Q6 quantization
- Some users report limitations in basic QA without retrieval systems
- Mixed reviews on summarization capabilities at different quantization levels

**Discussion Highlights:** The discussion highlights a consensus on the model's impressive performance for its size, with some users noting specific use cases and limitations. There is excitement about the potential of the upcoming 8b-a1b moe model.

---

## 41. [I trained a model to 'unslop' AI prose](https://reddit.com/r/LocalLLaMA/comments/1qd88v2/i_trained_a_model_to_unslop_ai_prose/)

**Author:** u/N8Karma | **Upvotes:** 206 | **Comments:** 71 | **Date:** 2026-01-14

**Summary:** The author trained a model to reverse the 'enslopping' effect of AI-generated prose by using GPT-4o-mini to enhance literary passages and then training a model to revert them back to their original form. The resulting model, Unslopper-30B-A3B-bf16, can produce more human-like prose and is available as open-source software. Key points include the model's ability to fool AI detectors, its open-source availability, and the goal to improve readability of AI-generated text. The community praised the model for its ability to produce more natural and enjoyable prose, with some users comparing the training process to diffusion models and others expressing skepticism about the training data size.

---

## 42. [Zhipu AI breaks US chip reliance with first major model trained on Huawei stack (GLM-Image)](https://reddit.com/r/LocalLLaMA/comments/1qd6nho/zhipu_ai_breaks_us_chip_reliance_with_first_major/)

**Author:** u/fallingdowndizzyvr | **Upvotes:** 418 | **Comments:** 45 | **Date:** 2026-01-14

**Summary:** Zhipu AI has developed the GLM-Image model using Huawei hardware, marking a significant step in reducing reliance on US chips. The Reddit discussion highlights the impact of the Chinese ban on Nvidia and the rapid advancements in AI model development.

**Key Points:**
- Zhipu AI's GLM-Image model is trained on Huawei hardware, reducing dependence on US chips.
- The Chinese ban on Nvidia is driving innovation in alternative hardware solutions.
- AI models are advancing rapidly, with significant improvements in model size and capabilities over short periods.
- The GLM-Image model has received mixed reviews regarding its performance.
- The model is seen as a tech demo or MVP showcasing alternative architectures.

**Discussion Highlights:** The discussion emphasizes the technological significance of Zhipu AI's achievement, despite concerns about the model's current performance. There is a consensus that this development is a step towards scaling up models using non-US hardware.

---

## 43. [Popularity of DDR3 motherboards is growing rapidly - VideoCardz.com](https://reddit.com/r/LocalLLaMA/comments/1qcvk9n/popularity_of_ddr3_motherboards_is_growing/)

**Author:** u/FullstackSensei | **Upvotes:** 147 | **Comments:** 66 | **Date:** 2026-01-14

**Summary:** The author expresses frustration over rising DDR4 RAM prices, which are affecting their homelabbing hobby and making it difficult to upgrade or replace components. The discussion highlights concerns about the increasing cost of older hardware and the potential for DDR3 prices to rise as well.

**Key Points:**
- Author's frustration with rising DDR4 RAM prices impacting homelabbing plans
- Concerns about DDR3 prices potentially skyrocketing next
- Discussion on the reuse and recycling era of consumer hardware
- Mixed experiences with selling or upgrading older DDR3 systems
- Observations on the cyclical nature of RAM prices and market trends

**Discussion Highlights:** The discussion reflects a consensus that hardware prices, especially for older generations like DDR3 and DDR4, are becoming increasingly volatile. Many users share experiences of selling or upgrading older systems, with some noting profits from selling decade-old hardware. There is also a recognition of the cyclical nature of RAM prices and the potential for market corrections.

---

## 44. [NeuTTS Nano: 120M Parameter On-Device TTS based on Llama3](https://reddit.com/r/LocalLLaMA/comments/1qcv304/neutts_nano_120m_parameter_ondevice_tts_based_on/)

**Author:** u/TeamNeuphonic | **Upvotes:** 209 | **Comments:** 44 | **Date:** 2026-01-14

**Summary:** Neuphonic has released NeuTTS Nano, a 120M parameter on-device TTS model based on Llama3, designed for embedded systems and mobile devices. It offers instant voice cloning and realistic prosody in a compact package.

**Key Points:**
- NeuTTS Nano is a 120M parameter TTS model, 3x smaller than NeuTTS Air.
- Built on Llama3 with a simple LM + codec architecture, provided in GGML format.
- Designed for smart home devices, robotics, and mobile apps with tight RAM constraints.
- Community interest in multilingual support and benchmarks for different hardware.
- Mixed feedback on voice quality, with some users finding it unnatural.

**Discussion Highlights:** The community shows strong interest in multilingual support and hardware benchmarks, with mixed opinions on voice quality. Some users request European language support and express concerns about the naturalness of the generated voices.

---

## 45. [Soprano 1.1-80M released: 95% fewer hallucinations and 63% preference rate over Soprano-80M](https://reddit.com/r/LocalLLaMA/comments/1qcusnt/soprano_1180m_released_95_fewer_hallucinations/)

**Author:** u/eugenekwek | **Upvotes:** 323 | **Comments:** 54 | **Date:** 2026-01-14

**Summary:** The post announces Soprano 1.1, an improved version of the Soprano TTS model with significant reductions in hallucinations and audio artifacts, along with enhanced stability and support for longer sentences. The community response is overwhelmingly positive, with users praising the model's performance and expressing interest in further developments.

**Key Points:**
- Soprano 1.1 reduces hallucinations by 95% and lowers WER by 50% compared to the previous version.
- The model now supports sentences up to 30 seconds long, doubling the previous limit.
- A blind study showed a 63% preference rate for Soprano 1.1 over the original model.
- Community feedback highlights the model's impressive performance for its size (80M parameters).
- Users are inquiring about additional features like ONNX support.

**Discussion Highlights:** The community is highly positive about Soprano 1.1, with many users expressing surprise at its performance given its small size. There is interest in further improvements and additional features, such as ONNX support. The overall consensus is that the model is a significant step forward in small-scale TTS technology.

---

## 46. [NVIDIA's new 8B model is Orchestrator-8B, a specialized 8-billion-parameter AI designed not to answer everything itself, but to intelligently manage and route complex tasks to different tools (like web search, code execution, other LLMs) for greater efficiency](https://reddit.com/r/LocalLLaMA/comments/1qcuerc/nvidias_new_8b_model_is_orchestrator8b_a/)

**Author:** u/Fear_ltself | **Upvotes:** 711 | **Comments:** 129 | **Date:** 2026-01-14

**Summary:** NVIDIA's Orchestrator-8B is an 8-billion-parameter AI designed to manage and route complex tasks to various tools, sparking discussions on its potential in creating functional systems and comparisons to middle managers.

**Key Points:**
- Orchestrator-8B is a specialized AI for task management and routing
- It aims to create functional systems by connecting with other tools and models
- Comparisons to middle managers and existing frameworks like Claude code style agentic frameworks
- Discussion on the potential of combining separate AI pieces for AGI-like functionality

**Discussion Highlights:** The discussion includes humorous comparisons to middle managers and mentions of Claude code style agentic frameworks as potential next steps in AI development.

---

## 47. [Which are the top LLMs under 8B right now?](https://reddit.com/r/LocalLLaMA/comments/1qcl543/which_are_the_top_llms_under_8b_right_now/)

**Author:** u/Additional_Secret_75 | **Upvotes:** 178 | **Comments:** 108 | **Date:** 2026-01-14

**Summary:** The post discusses the best local LLMs under 8B parameters for general chat, research, and coding, with a focus on models that are not overly censored and run efficiently on limited VRAM. Users share their experiences and recommendations for top-performing models in this category.

**Key Points:**
- Qwen3 4B and Qwen3 8B models are highlighted for their performance and vision capabilities.
- Gemma-3n-E4B is praised for its reasoning, multimodal abilities, and efficiency.
- The discussion emphasizes models that balance performance with resource efficiency.
- Users recommend checking the GPU Poor LLM Arena for comparisons.
- Models like Nanbeige 3B are also mentioned as viable options.

**Discussion Highlights:** The consensus leans towards Qwen3 and Gemma-3n-E4B models for their balance of performance, multimodal capabilities, and efficiency. Users also recommend exploring community-driven comparisons and benchmarks to make informed decisions.

---

