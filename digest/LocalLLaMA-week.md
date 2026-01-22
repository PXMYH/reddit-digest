# r/LocalLLaMA Reading Digest

**Period:** 2026-01-22 to 2026-01-22
**Posts Summarized:** 46
**Total Posts Analyzed:** 46

---

## 1. [8x AMD MI50 32GB at 26 t/s (tg) with MiniMax-M2.1 and 15 t/s (tg) with GLM 4.7 (vllm-gfx906)](https://reddit.com/r/LocalLLaMA/comments/1qjaxfy/8x_amd_mi50_32gb_at_26_ts_tg_with_minimaxm21_and/)

**Author:** u/ai-infos | **Upvotes:** 229 | **Comments:** 60 | **Date:** 2026-01-21

**Summary:** The post details a cost-effective local inference setup using 8x AMD MI50 GPUs, achieving high token generation speeds with MiniMax-M2.1 and GLM 4.7 models. The setup is praised for its performance and affordability, with a total VRAM of 256GB for under $1k.

**Key Points:**
- 8x AMD MI50 GPUs provide 256GB VRAM for under $1k.
- MiniMax-M2.1 achieves 26.8 tokens/s output, GLM 4.7 achieves 15.6 tokens/s output.
- Power draw is 280W idle and 1200W during inference.
- The setup is stable for long context tasks, suitable for coding agents.
- Community appreciates the cost-effectiveness and performance.

**Discussion Highlights:** The community is highly positive about the setup, praising its cost-effectiveness and performance. Some users express interest in replacing their current hardware with this setup.

---

## 2. [VibeVoice-ASR released!](https://reddit.com/r/LocalLLaMA/comments/1qj40er/vibevoiceasr_released/)

**Author:** u/k_means_clusterfuck | **Upvotes:** 128 | **Comments:** 31 | **Date:** 2026-01-21

**Summary:** Microsoft has released VibeVoice-ASR, a new ASR model with 9B parameters, praised for its multilingual capabilities and transcription quality, though its large size raises performance concerns.

**Key Points:**
- VibeVoice-ASR is a new ASR model released by Microsoft.
- The model has 9B parameters and is multilingual.
- Users report high transcription quality but express concerns about its large size.
- Comparisons are made with other models like Parakeet and Whisper.
- The model is seen as a potential best option for transcription with diarization.

**Discussion Highlights:** The discussion highlights the model's high quality and multilingual capabilities, with users expressing excitement but also concerns about its large size and performance. Comparisons with other models like Parakeet and Whisper are noted.

---

## 3. [GLM-4.7-Flash-GGUF bug fix - redownload for better outputs](https://reddit.com/r/LocalLLaMA/comments/1qiy0ha/glm47flashgguf_bug_fix_redownload_for_better/)

**Author:** u/etherd0t | **Upvotes:** 104 | **Comments:** 54 | **Date:** 2026-01-21

**Summary:** The post announces a bug fix for the GLM-4.7-Flash-GGUF model, urging users to redownload for improved outputs. It provides recommended parameters for general use and tool-calling, along with a llama.cpp-specific setting.

**Key Points:**
- Bug fix released for GLM-4.7-Flash-GGUF model, improving output quality
- Recommended parameters provided for general use and tool-calling
- Users report significant improvements and successful fixes
- Some users note performance differences compared to other models
- Community expresses appreciation for the update

**Discussion Highlights:** Users confirm the bug fix resolves previous issues with looping outputs. The model is praised for its strength despite its size, though some note it is slower than alternatives like GPT-OSS-20b. Overall, the community is positive about the update and its improvements.

---

## 4. [Fix for GLM 4.7 Flash has been merged into llama.cpp](https://reddit.com/r/LocalLLaMA/comments/1qiwm3c/fix_for_glm_47_flash_has_been_merged_into_llamacpp/)

**Author:** u/jacek2023 | **Upvotes:** 293 | **Comments:** 73 | **Date:** 2026-01-21

**Summary:** A fix for GLM 4.7 Flash has been merged into llama.cpp, with ongoing work on CUDA support. The community is actively discussing performance metrics and compatibility.

**Key Points:**
- Fix for GLM 4.7 Flash merged into llama.cpp
- CUDA support in progress via GitHub PR
- Performance metrics shared for different quantizations and GPUs
- Community discussing CPU-only performance and potential issues
- Positive feedback on model improvements and reduced gibberish

**Discussion Highlights:** Users are sharing performance benchmarks for various configurations, discussing CPU-only performance, and noting improvements in model output quality. Some users report slow prompt processing in specific environments like LMStudio.

---

## 5. [Knowledge distillation with Claude as the interface: trained a 0.6B model to match GPT-class performance on Text2SQL in a singe conversation](https://reddit.com/r/LocalLLaMA/comments/1qiu6jo/knowledge_distillation_with_claude_as_the/)

**Author:** u/party-horse | **Upvotes:** 147 | **Comments:** 33 | **Date:** 2026-01-21

**Summary:** The post describes a workflow for training small, task-specific models using knowledge distillation via Claude, achieving significant performance improvements in Text2SQL tasks with minimal setup overhead.

**Key Points:**
- Knowledge distillation via Claude simplifies the training of small models for specialized tasks.
- The approach uses a large teacher model (DeepSeek-V3) to generate synthetic training data.
- The fine-tuned 0.6B model achieved a 74% score compared to the base model's 36%.
- The process includes task selection, data conversion, teacher evaluation, training, and packaging.
- The community response highlights the potential for local inference and on-device agents.

**Discussion Highlights:** The discussion emphasizes the practicality and efficiency of the approach, with users appreciating its simplicity and potential applications in local inference and on-device agents.

---

## 6. [vLLM v0.14.0 released](https://reddit.com/r/LocalLLaMA/comments/1qim0e9/vllm_v0140_released/)

**Author:** u/jinnyjuice | **Upvotes:** 160 | **Comments:** 32 | **Date:** 2026-01-20

**Summary:** The Reddit post announces the release of vLLM v0.14.0, highlighting new features and updates. Users discuss improvements like automatic context length fitting and the deprecation of certain quantization methods.

**Key Points:**
- Automatic context length fitting to GPU memory to prevent OOM failures
- Deprecation of some quantization methods, including HQQ
- Introduction of Marlin for Turing (sm75) as a major upgrade
- User interest in future sm120 optimizations

**Discussion Highlights:** Users express excitement about the automatic context length feature and discuss the implications of deprecated quantization methods. The Marlin upgrade for Turing is noted as a significant improvement, and there is anticipation for future optimizations.

---

## 7. [Current GLM-4.7-Flash implementation confirmed to be broken in llama.cpp](https://reddit.com/r/LocalLLaMA/comments/1qih9r8/current_glm47flash_implementation_confirmed_to_be/)

**Author:** u/Sweet_Albatross9772 | **Upvotes:** 238 | **Comments:** 51 | **Date:** 2026-01-20

**Summary:** The Reddit post discusses issues with the current GLM-4.7-Flash implementation in llama.cpp, highlighting significant differences in logprobs compared to vLLM, which may explain reported problems like looping and poor performance. A potential fix is already proposed in a pull request.

**Key Points:**
- Current GLM-4.7-Flash implementation in llama.cpp is confirmed broken.
- Significant differences in logprobs compared to vLLM.
- Looping issues, overthinking, and poor performance reported.
- A potential fix is proposed in a pull request.
- Community acknowledges the issue and expects a resolution soon.

**Discussion Highlights:** The community is aware of the issue and is optimistic about a quick resolution. The top comments highlight the specific problem (wrong gating function) and appreciate the open-source nature of the project, expecting minor tweaks to fix the issue.

---

## 8. [You have 64gb ram and 16gb VRAM; internet is permanently shut off: what 3 models are the ones you use?](https://reddit.com/r/LocalLLaMA/comments/1qids6a/you_have_64gb_ram_and_16gb_vram_internet_is/)

**Author:** u/Adventurous-Gold6413 | **Upvotes:** 514 | **Comments:** 287 | **Date:** 2026-01-20

**Summary:** The Reddit post discusses the best local models to use with 64GB RAM and 16GB VRAM when internet access is unavailable. Users share their preferred models and experiences. Key points include recommendations for models like Gemma 3 27B, GLM 4.5 Air, and GPT-OSS 120B, with GPT-OSS-120B being praised for its performance and versatility. The discussion highlights a consensus around these models, with notable community engagement and shared experiences.

---

## 9. [Liquid AI released the best thinking Language Model Under 1GB](https://reddit.com/r/LocalLLaMA/comments/1qi512t/liquid_ai_released_the_best_thinking_language/)

**Author:** u/PauLabartaBajo | **Upvotes:** 224 | **Comments:** 51 | **Date:** 2026-01-20

**Summary:** Liquid AI released LFM2.5-1.2B-Thinking, a compact reasoning model that runs on-device with 900 MB of memory, excelling in math, tool use, and instruction following. It outperforms larger models in speed and efficiency, with broad ecosystem support.

**Key Points:**
- LFM2.5-1.2B-Thinking is optimized for on-device reasoning with low memory usage.
- It generates internal thinking traces for systematic problem-solving.
- The model outperforms larger models in speed and memory efficiency.
- Concerns raised about memory requirements and quantization trade-offs.
- Licensing restrictions (non-Apache/MIT) were criticized by some users.

**Discussion Highlights:** The discussion highlighted concerns about memory requirements, performance trade-offs between Thinking and Instruct variants, and licensing restrictions. Some users expressed a desire for larger models, while others praised the innovation.

---

## 10. [768Gb Fully Enclosed 10x GPU Mobile AI Build](https://reddit.com/r/LocalLLaMA/comments/1qi4uj2/768gb_fully_enclosed_10x_gpu_mobile_ai_build/)

**Author:** u/SweetHomeAbalama0 | **Upvotes:** 833 | **Comments:** 252 | **Date:** 2026-01-20

**Summary:** The post describes a custom-built, fully enclosed mobile AI system with 10 GPUs, designed for running large MoE models and supporting graphic design tasks. The build cost approximately $17k and was optimized for performance within budget constraints.

**Key Points:**
- Custom-built system with 10 GPUs (8x 3090 + 2x 5090) and a Threadripper Pro 3995WX CPU
- Designed for large MoE models, video generation, and high-detail image generation
- Fully enclosed and mobile, with a focus on protecting hardware from pets
- Budget-conscious build, avoiding unnecessary expenses for diminishing returns
- Community reactions highlight the uniqueness and power of the build

**Discussion Highlights:** The community praised the build's power and uniqueness, with humorous comments about its portability and airflow. The post gained significant traction, earning a special flair and being featured on Discord.

---

## 11. [Over 6K novels with reasoning traces to train full book writing LLMs](https://reddit.com/r/LocalLLaMA/comments/1qi3nmd/over_6k_novels_with_reasoning_traces_to_train/)

**Author:** u/XMasterDE | **Upvotes:** 107 | **Comments:** 46 | **Date:** 2026-01-20

**Summary:** Pageshift Entertainment has released an update to their LongPage dataset, expanding it to over 6,000 novels with hierarchical reasoning traces to support training full-book writing LLMs. They are also training a full-book writing model and plan to release it once quality standards are met.

**Key Points:**
- LongPage dataset expanded to 6K+ novels with hierarchical planning traces
- Dataset supports training full-book writing LLMs
- Early checkpoints of a full-book writing model are being tested internally
- Community interest in fiction writing applications and dataset details
- Requests for code release and multi-language dataset support

**Discussion Highlights:** The community shows strong interest in the potential of the dataset for fiction writing, with requests for more details on how the model works and whether it includes specific works like 'Worm by Wildbow.' There is also interest in multi-language support and the release of data processing code.

---

## 12. [glm-4.7-flash has the best thinking process with clear steps, I love it](https://reddit.com/r/LocalLLaMA/comments/1qhxlgy/glm47flash_has_the_best_thinking_process_with/)

**Author:** u/uptonking | **Upvotes:** 137 | **Comments:** 34 | **Date:** 2026-01-20

**Summary:** The Reddit post discusses the user's experience with the glm-4.7-flash model, highlighting its structured thinking process and comparing it favorably to other models like qwen3-30b and nemotron-nano. Despite its slower speed, the user appreciates its clear reasoning steps and plans to use it more extensively.

**Key Points:**
- glm-4.7-flash has a detailed and clear thinking process with steps like request analysis, brainstorming, drafting, refining, revising, polishing, and final response.
- The model is slower (19 tokens/s) compared to nemotron-nano (30+ tokens/s) but offers better reasoning quality.
- Users appreciate the structured reasoning and lack of self-doubt loops in glm-4.7-flash.
- The model can sometimes loop or not follow the expected thinking flow, requiring adjustments in temperature and other settings.
- There is a discussion about potential tricks to speed up the thinking process without disabling it.

**Discussion Highlights:** The discussion highlights a consensus on the high quality of glm-4.7-flash's reasoning process, with users praising its structured approach and lack of self-doubt loops. There is also a focus on optimizing the model's speed and performance, with suggestions to adjust settings like temperature and repeat penalty.

---

## 13. [It's been one year since the release of Deepseek-R1](https://reddit.com/r/LocalLLaMA/comments/1qhs2sd/its_been_one_year_since_the_release_of_deepseekr1/)

**Author:** u/Recoil42 | **Upvotes:** 292 | **Comments:** 51 | **Date:** 2026-01-19

**Summary:** The Reddit post commemorates the one-year anniversary of the Deepseek-R1 release, highlighting its significant impact on the AI community and its disruptive influence on competitors like Meta's Llama.

**Key Points:**
- Deepseek-R1 had a major impact, reportedly causing Meta to disband its flagship AI training team and reassess its strategy.
- The release is considered one of the most important in AI history, second only to the original Llama model.
- The rapid pace of AI development is emphasized, with progress feeling much faster than anticipated.
- The model's release led to price reductions and increased transparency in AI reasoning outputs.

**Discussion Highlights:** The discussion highlights the consensus on Deepseek-R1's disruptive influence, with users noting its role in forcing competitors to adapt and the rapid pace of AI advancements over the past year.

---

## 14. [Mosquito - 7.3M parameter tiny knowledge model](https://reddit.com/r/LocalLLaMA/comments/1qhqzsi/mosquito_73m_parameter_tiny_knowledge_model/)

**Author:** u/Lopsided-Repair-3638 | **Upvotes:** 115 | **Comments:** 52 | **Date:** 2026-01-19

**Summary:** The post introduces Mosquito, a tiny knowledge model with 7.3M parameters, capable of answering general knowledge questions despite its small size. Users tested the model and found mixed results, with some humorous and incorrect responses.

**Key Points:**
- Mosquito is a 7.3M parameter model designed for general knowledge questions.
- The model demonstrates surprising capabilities but also significant limitations.
- Users reported inaccurate responses, such as defining a dog incorrectly and providing odd answers to simple questions.
- There is a request for a quantized version of the model.
- The model's knowledge gaps are highlighted, such as knowing about LLMs but not basic concepts like dogs.

**Discussion Highlights:** The discussion is marked by a mix of amusement and criticism. Users tested the model with simple questions and found humorous or incorrect answers, such as defining a dog as a group of people or stating that cats eat fruits and vegetables. There is a consensus that while the model is impressive for its size, it has notable limitations and quirks.

---

## 15. [Bartowski comes through again. GLM 4.7 flash GGUF](https://reddit.com/r/LocalLLaMA/comments/1qhpima/bartowski_comes_through_again_glm_47_flash_gguf/)

**Author:** u/RenewAi | **Upvotes:** 178 | **Comments:** 50 | **Date:** 2026-01-19

**Summary:** The post announces the release of the GLM 4.7 Flash GGUF model by Bartowski, with mixed user feedback on its performance. Some users report issues with the model's functionality and template errors.

**Key Points:**
- Bartowski released GLM 4.7 Flash GGUF model on Hugging Face
- Users report mixed results with different quantizations (8-bit, 16-bit)
- Template issues and syntax errors noted in user testing
- Comparison with other models like Qwen3 Coder mentioned
- Ongoing discussion about model performance and usability

**Discussion Highlights:** Users are testing various quantizations of the GLM 4.7 Flash model with mixed results. Some report template and syntax errors, while others compare it unfavorably to alternatives like Qwen3 Coder. The consensus suggests the model may have usability issues that need addressing.

---

## 16. [Unsloth GLM 4.7-Flash GGUF](https://reddit.com/r/LocalLLaMA/comments/1qhlnsv/unsloth_glm_47flash_gguf/)

**Author:** u/Wooden-Deer-1276 | **Upvotes:** 223 | **Comments:** 44 | **Date:** 2026-01-19

**Summary:** The Reddit post discusses the release of the Unsloth GLM 4.7-Flash GGUF model, with community feedback on its performance and recommendations for optimal usage. Key points include: the model has been uploaded with various quantizations, with recommendations to use UD-Q4_K_XL and above; specific parameters like `--temp 0.2 --top-k 50 --top-p 0.95 --min-p 0.01 --dry-multiplier 1.1` are suggested for better performance; there are ongoing issues with looping in quantized versions, with BF16 recommended for best results; the community emphasizes patience and thorough testing before full release; and a BF16 version of the model has been released, as indicated by a shared image. The community is actively engaged in testing and providing feedback on the model, with a consensus to ensure the model works properly before wider release.

---

## 17. [GLM 4.7 Flash official support merged in llama.cpp](https://reddit.com/r/LocalLLaMA/comments/1qhitrj/glm_47_flash_official_support_merged_in_llamacpp/)

**Author:** u/ayylmaonade | **Upvotes:** 353 | **Comments:** 60 | **Date:** 2026-01-19

**Summary:** The Reddit post announces the official support for GLM 4.7 Flash in llama.cpp, highlighting its integration and community contributions. The discussion includes clarifications about the term 'official' and shares additional resources and performance insights. Key points include the official support, clarification on the term 'official', community effort, performance insights, and Discord features. The discussion clarifies the meaning of 'official' support and emphasizes the community's role in the implementation.

---

## 18. [My gpu poor comrades, GLM 4.7 Flash is your local agent](https://reddit.com/r/LocalLLaMA/comments/1qhii5v/my_gpu_poor_comrades_glm_47_flash_is_your_local/)

**Author:** u/__Maximum__ | **Upvotes:** 458 | **Comments:** 159 | **Date:** 2026-01-19

**Summary:** The Reddit post highlights the author's positive experience with GLM 4.7 Flash, an MoE model that performed reliably in an agentic framework, handling tasks like cloning repos and running commands without errors. The author is eager to try it locally once GGUFs are available.

**Key Points:**
- GLM 4.7 Flash performed reliably in an agentic framework, handling tasks like cloning repos and running commands without errors.
- The model produced hundreds of thousands of tokens in one session with context compacting.
- Users are anticipating the availability of GGUFs for local use.
- Comparisons with other models like Nemotron 30B and Qwen3 are discussed.
- Performance benchmarks indicate it may be as smart as SEED OSS 36B but with better performance due to MoE.

**Discussion Highlights:** The discussion includes comparisons with other models, performance benchmarks, and user experiences. Some users have already started testing the model locally and note its deep thinking capabilities. There is also a link to a Hugging Face model for those interested in trying it out.

---

## 19. [New in llama.cpp: Anthropic Messages API](https://reddit.com/r/LocalLLaMA/comments/1qhaq21/new_in_llamacpp_anthropic_messages_api/)

**Author:** u/paf1138 | **Upvotes:** 162 | **Comments:** 50 | **Date:** 2026-01-19

**Summary:** The Reddit post announces the introduction of the Anthropic Messages API in llama.cpp, which has been well-received by the community. Users are enthusiastic about trying it out and have shared practical tips for implementation.

**Key Points:**
- Introduction of Anthropic Messages API in llama.cpp
- Enthusiasm and quick adoption by users
- Practical implementation tips shared
- Mentions of specific hardware like M3 Ultra
- Discussion about context usage in Claude Code

**Discussion Highlights:** The discussion highlights a positive reception of the new API, with users sharing practical advice on how to implement it. There is also mention of specific hardware and context usage, indicating a focus on practical applications and performance considerations.

---

## 20. [zai-org/GLM-4.7-Flash · Hugging Face](https://reddit.com/r/LocalLLaMA/comments/1qh5wdq/zaiorgglm47flash_hugging_face/)

**Author:** u/Dark_Fire_12 | **Upvotes:** 727 | **Comments:** 227 | **Date:** 2026-01-19

**Summary:** The post announces the release of GLM-4.7-Flash model, generating significant interest and discussion in the r/LocalLLaMA community. Users express excitement about its features and potential applications.

**Key Points:**
- GLM-4.7-Flash model has been released and is gaining popularity
- The model uses MLA, reducing KV cache memory usage
- It supports full 200k context, making it accessible to more users
- Community members express enthusiasm and nostalgia for larger models
- The release is considered promising by the community

**Discussion Highlights:** The community shows strong interest in the new model's capabilities, particularly its memory efficiency and context length. There's excitement about running it locally and appreciation for the development team's work. Some users express nostalgia for larger models while acknowledging the progress represented by this release.

---

## 21. [I made a Top-K implementation that's up to 20x faster than PyTorch CPU (open source)](https://reddit.com/r/LocalLLaMA/comments/1qh0yq8/i_made_a_topk_implementation_thats_up_to_20x/)

**Author:** u/andreabarbato | **Upvotes:** 151 | **Comments:** 104 | **Date:** 2026-01-19

**Summary:** The author developed an AVX2-optimized Top-K implementation that significantly outperforms PyTorch CPU, achieving up to 20x speed improvements depending on vocabulary size. It integrates with llama.cpp, resulting in 63% faster prompt processing for large models. The implementation is open-source and available on GitHub. Key points include the performance gains, technical details like adaptive sampling and AVX2 SIMD, and community feedback requesting PRs and explanations while raising concerns about benchmark reproducibility. The discussion highlights strong interest in the implementation and some skepticism about its coding style and benchmarking.

---

## 22. [how do you pronounce “gguf”?](https://reddit.com/r/LocalLLaMA/comments/1qglyqz/how_do_you_pronounce_gguf/)

**Author:** u/Hamfistbumhole | **Upvotes:** 110 | **Comments:** 154 | **Date:** 2026-01-18

**Summary:** The Reddit post discusses the pronunciation of 'gguf', with users debating whether it should be pronounced as 'jee-guff', 'giguff', or 'jee jee you eff'. The comments provide various humorous and literal interpretations.

**Key Points:**
- The pronunciation of 'gguf' is debated among users.
- Some suggest pronouncing each letter individually, like '.PNG'.
- Others propose humorous interpretations like 'guh-GUFF' or 'gê-guf'.
- A popular comment suggests that 'gguf' is not pronounced but downloaded silently.

**Discussion Highlights:** The discussion highlights a mix of literal and humorous interpretations, with no clear consensus on the correct pronunciation. The top comment humorously suggests that 'gguf' is not pronounced but downloaded silently.

---

## 23. [4x AMD R9700 (128GB VRAM) + Threadripper 9955WX Build](https://reddit.com/r/LocalLLaMA/comments/1qgdb7f/4x_amd_r9700_128gb_vram_threadripper_9955wx_build/)

**Author:** u/NunzeCs | **Upvotes:** 345 | **Comments:** 91 | **Date:** 2026-01-18

**Summary:** The author built a high-performance system with 4x AMD R9700 GPUs (128GB VRAM) and a Threadripper 9955WX CPU, leveraging a 50% subsidy to stay within a ~10,000€ budget. The system is designed for running large AI models locally, with benchmark results showing strong performance across various models. Key points include the use of a subsidy to reduce costs, the hardware specifications, and the community's positive response. The discussion highlights the build's power and cost-effectiveness, with users asking about component sourcing and noting similarities to their own builds.

---

## 24. [Qwen 4 might be a long way off !? Lead Dev says they are "slowing down" to focus on quality.](https://reddit.com/r/LocalLLaMA/comments/1qfv1ms/qwen_4_might_be_a_long_way_off_lead_dev_says_they/)

**Author:** u/Difficult-Cap-7527 | **Upvotes:** 445 | **Comments:** 71 | **Date:** 2026-01-17

**Summary:** The Reddit post discusses the potential delay in Qwen 4 development, with the lead developer indicating a focus on quality over speed. The community generally supports this approach, appreciating the emphasis on quality improvements.

**Key Points:**
- Qwen 4 development may be slowing down to focus on quality
- Community appreciates the focus on quality over quantity
- Uncertainty about whether the statement specifically refers to Qwen 4
- Support for taking necessary time to advance the technology meaningfully
- Mixed reactions with some cautioning against speculative rumors

**Discussion Highlights:** The discussion highlights a general consensus supporting the focus on quality, with many users appreciating the potential for meaningful advancements. Some users caution against jumping to conclusions based on limited information, emphasizing the need for clarity.

---

## 25. [128GB VRAM quad R9700 server](https://reddit.com/r/LocalLLaMA/comments/1qfscp5/128gb_vram_quad_r9700_server/)

**Author:** u/Ulterior-Motive_ | **Upvotes:** 530 | **Comments:** 116 | **Date:** 2026-01-17

**Summary:** The author upgraded from MI100 GPUs to four R9700 GPUs for better performance and cost efficiency, detailing the specifications and benchmarks of their new 128GB VRAM server build. Key points include the transition from MI100 to R9700 GPUs for improved performance and cost savings, detailed specifications of the new server build, performance benchmarks showing high token processing rates, and community appreciation for the build and its cost-effectiveness. The community praised the build for its performance and cost efficiency, with some users joking about the financial irresponsibility of such upgrades.

---

## 26. [The Search for Uncensored AI (That Isn’t Adult-Oriented)](https://reddit.com/r/LocalLLaMA/comments/1qfq9ez/the_search_for_uncensored_ai_that_isnt/)

**Author:** u/Fun-Situation-4358 | **Upvotes:** 274 | **Comments:** 216 | **Date:** 2026-01-17

**Summary:** The post discusses the challenge of finding uncensored AI models that prioritize reasoning and creativity over adult-oriented content, highlighting a gap between heavily restricted corporate AI and shallow adult-focused models.

**Key Points:**
- The author seeks an AI that is genuinely unfiltered and technically advanced, focusing on reasoning and creativity.
- Most models marketed as 'uncensored' are optimized for adult use rather than intelligence or depth.
- There is a perceived gap between heavily restricted corporate AI and shallow adult-focused models.
- Techniques used to decensor open-source models often reduce their intelligence.
- The Uncensored General Intelligence Leaderboard is suggested as a resource.

**Discussion Highlights:** The discussion highlights a shared frustration with the lack of AI models that balance uncensored capabilities with serious problem-solving and creativity. Many commenters agree that most uncensored models are either adult-focused or lack depth, and some suggest resources like the Uncensored General Intelligence Leaderboard for finding suitable models.

---

## 27. [China's AGI-NEXT Conference (Qwen, Kimi, Zhipu, Tencent)](https://reddit.com/r/LocalLLaMA/comments/1qfmc05/chinas_aginext_conference_qwen_kimi_zhipu_tencent/)

**Author:** u/nuclearbananana | **Upvotes:** 117 | **Comments:** 22 | **Date:** 2026-01-17

**Summary:** The Reddit post discusses China's AGI-NEXT Conference, highlighting insights on China vs US AGI development, paths to AGI, compute resources, and marketing strategies. The discussion includes details about Qwen's internal advancements and the perceived innovation culture in Chinese AI labs.

**Key Points:**
- Qwen has internally developed Qwen3.5 and context windows in the millions.
- Chinese AI labs are perceived as less willing to take risks for innovation.
- Deepseek is noted for its talent concentration but was absent from the conference.
- The next paradigm in AI is believed to likely come from OpenAI rather than Google.

**Discussion Highlights:** The discussion highlights Qwen's advancements and the perceived risk-averse culture in Chinese AI labs. There is also a notable absence of Deepseek, despite its strong talent pool, and a consensus that OpenAI may lead the next AI paradigm shift.

---

## 28. [Best "End of world" model that will run on 24gb VRAM](https://reddit.com/r/LocalLLaMA/comments/1qfkn3a/best_end_of_world_model_that_will_run_on_24gb_vram/)

**Author:** u/gggghhhhiiiijklmnop | **Upvotes:** 333 | **Comments:** 177 | **Date:** 2026-01-17

**Summary:** The post discusses finding the best 'end of world' model that can run on a PC with 24GB VRAM and 64GB RAM. The author is hoarding data and seeks recommendations for models to download and store. The discussion highlights practical advice and specific model suggestions.

**Key Points:**
- The author is hoarding data like Wikipedia, Wiktionary, and Khan Academy.
- The model needs to fit and run on a PC with 24GB VRAM and 64GB RAM.
- Top comment suggests saving the best LLM possible and running it off SSD if necessary.
- Gemma3:27b is recommended for its capabilities, including vision.
- Practical advice includes downloading actual Wikipedia backups for offline use.

**Discussion Highlights:** The discussion highlights a consensus around practical solutions, with recommendations for specific models like Gemma3:27b and advice on downloading comprehensive data backups. The top comment emphasizes the importance of saving the best possible LLM and running it off SSD if needed.

---

## 29. [DeepSeek Engram : A static memory unit for LLMs](https://reddit.com/r/LocalLLaMA/comments/1qf5oj0/deepseek_engram_a_static_memory_unit_for_llms/)

**Author:** u/Technical-Love-8479 | **Upvotes:** 323 | **Comments:** 47 | **Date:** 2026-01-17

**Summary:** DeepSeek AI introduced Engram, a memory unit for LLMs that separates remembering from reasoning, enabling O(1) knowledge lookup and improving performance without GPU limits.

**Key Points:**
- Engram introduces conditional memory, separating static knowledge from reasoning.
- Knowledge lookup is O(1), improving efficiency and performance.
- Enables massive memory scaling without GPU constraints.
- Improves reasoning, math, and code performance.
- Frees attention for global reasoning rather than static knowledge.

**Discussion Highlights:** The community highlights the significance of separating memory from reasoning, the efficiency of O(1) lookup, and the potential for scaling memory independently of model size.

---

## 30. ["Welcome to the Local Llama. How janky's your rig?](https://reddit.com/r/LocalLLaMA/comments/1qf514i/welcome_to_the_local_llama_how_jankys_your_rig/)

**Author:** u/ForsookComparison | **Upvotes:** 100 | **Comments:** 22 | **Date:** 2026-01-16

**Summary:** The Reddit post in r/LocalLLaMA discusses various unconventional and humorous setups for running AI models locally, highlighting the creative and sometimes 'janky' solutions users employ.

**Key Points:**
- Users share unconventional hardware setups for running AI models.
- Discussion includes humorous and creative solutions to hardware limitations.
- Specific mentions of hardware like GPUs (e.g., 3090, MI50) and cooling solutions (e.g., baby oil, blower fans).
- Comments highlight the challenges and workarounds for running high-performance computing on limited budgets.
- Community engagement with upvotes and replies indicating interest in the topic.

**Discussion Highlights:** The discussion is light-hearted and creative, with users sharing their unique and sometimes humorous solutions to hardware challenges. There is a sense of community and shared interest in optimizing local AI setups, even with limited resources.

---

## 31. [Prompt Repetition Improves Non-Reasoning LLMs - a paper](https://reddit.com/r/LocalLLaMA/comments/1qeuh0z/prompt_repetition_improves_nonreasoning_llms_a/)

**Author:** u/Foreign-Beginning-49 | **Upvotes:** 110 | **Comments:** 51 | **Date:** 2026-01-16

**Summary:** The Reddit post discusses a paper showing that repeating prompts can significantly improve the performance of non-reasoning LLMs without affecting latency or output format. The technique is simple yet effective across various models and benchmarks.

**Key Points:**
- Prompt repetition improves non-reasoning LLM performance
- No impact on latency or output format
- Simple technique with notable gains
- Deepseek is highlighted as an open weights model tested
- Discussion highlights potential undiscovered simple tricks

**Discussion Highlights:** The discussion emphasizes the simplicity and effectiveness of the technique, with users expressing surprise at its impact and speculating about other potential undiscovered tricks. There is a consensus on the significance of the findings and the need for more systematic testing of simple techniques.

---

## 32. [performance benchmarks (72GB VRAM) - llama.cpp server - January 2026](https://reddit.com/r/LocalLLaMA/comments/1qennp2/performance_benchmarks_72gb_vram_llamacpp_server/)

**Author:** u/jacek2023 | **Upvotes:** 111 | **Comments:** 39 | **Date:** 2026-01-16

**Summary:** The Reddit post presents performance benchmarks for various models run on a setup with three RTX 3090 GPUs and a Ryzen Threadripper 1920X, measuring tokens per second for each model. The benchmarks are not scientific but provide a practical comparison of model speeds.

**Key Points:**
- Hardware setup includes three RTX 3090 GPUs and a Ryzen Threadripper 1920X.
- Performance is measured in tokens per second, with ERNIE-4.5-21B-A3B-Thinking-Q8_0 achieving the highest speed at 147.85 tokens/s.
- The benchmarks are informal and focus solely on speed, not accuracy.
- Suggestions from comments include filling the context to ~10k tokens for further performance testing and using specific flags during compilation for better GPU performance.
- The discussion highlights potential improvements and additional testing methods.

**Discussion Highlights:** The discussion includes suggestions for further performance testing, such as filling the context to ~10k tokens and using specific compilation flags for better GPU performance. There is also a mention of similar performance between certain models and inquiries about the GPU setup.

---

## 33. [I reproduced DeepSeek's mHC at 1.7B params (8xH100). The instability is 3x worse than reported (10k vs 3k), but the model didn't explode.](https://reddit.com/r/LocalLLaMA/comments/1qek917/i_reproduced_deepseeks_mhc_at_17b_params_8xh100/)

**Author:** u/poisson_labs | **Upvotes:** 173 | **Comments:** 29 | **Date:** 2026-01-16

**Summary:** The author reproduced DeepSeek's mHC at 1.7B parameters and found that the instability was 3x worse than reported (10k vs 3k), but the model continued learning without exploding. They confirmed that Manifold Hyper-Connections (mHC) with Sinkhorn projection solves the issue with zero compute overhead.

**Key Points:**
- Instability at 1.7B parameters was measured at 10,924x signal amplification, worse than DeepSeek's reported 3,000x.
- Despite high signal amplification, the model did not diverge, likely due to modern optimizers and gradient clipping.
- Manifold Hyper-Connections (mHC) with Sinkhorn projection effectively solves the instability issue.
- The solution has zero compute overhead, contrary to some skepticism in the comments.
- Discussion highlights include questions about muon optimizers and appreciation for DeepSeek's contributions.

**Discussion Highlights:** The discussion includes skepticism about the zero compute overhead claim, curiosity about alternative optimizers like muon, and appreciation for DeepSeek's innovative work. Some users also highlighted the resourcefulness of hardware-constrained labs.

---

## 34. [Maxsun joins Sparkle in making Intel Arc B60 Pro GPUs available to regular consumers, with up to 48GB VRAM](https://reddit.com/r/LocalLLaMA/comments/1qehf0p/maxsun_joins_sparkle_in_making_intel_arc_b60_pro/)

**Author:** u/reps_up | **Upvotes:** 140 | **Comments:** 50 | **Date:** 2026-01-16

**Summary:** Maxsun and Sparkle are making Intel Arc B60 Pro GPUs available to regular consumers, featuring up to 48GB VRAM. The Reddit post highlights this development and includes discussions about VRAM capacity, software support, and availability in Europe.

**Key Points:**
- Intel Arc B60 Pro GPUs are now available to consumers with up to 48GB VRAM.
- Users express interest in higher VRAM capacities (e.g., 128GB) for advanced computing tasks.
- Questions about software support (torch/JAX/ONNX) and availability in Europe are raised.
- Discussion includes humorous remarks about VRAM configurations (e.g., 2x24GB).

**Discussion Highlights:** The discussion highlights a strong interest in high VRAM capacities for machine learning and other compute-intensive tasks. Users are curious about software compatibility and availability, particularly in Europe. There is a mix of technical questions and light-hearted comments about VRAM configurations.

---

## 35. [GPT-5.2 xhigh, GLM-4.7, Kimi K2 Thinking, DeepSeek v3.2 on Fresh SWE-rebench (December 2025)](https://reddit.com/r/LocalLLaMA/comments/1qefa7q/gpt52_xhigh_glm47_kimi_k2_thinking_deepseek_v32/)

**Author:** u/CuriousPlatypus1881 | **Upvotes:** 379 | **Comments:** 89 | **Date:** 2026-01-16

**Summary:** The post discusses the updated SWE-bench leaderboard results from December 2025, highlighting the performance of various AI models on GitHub PR tasks. Claude Opus 4.5 leads with a 63.3% resolved rate, followed closely by GPT-5.2 (extra high effort) at 61.5%. The post also notes the strong performance of open-source models like GLM-4.7 and GPT-OSS-120B.

**Key Points:**
- Claude Opus 4.5 leads the leaderboard with a 63.3% resolved rate.
- GPT-5.2 (extra high effort) follows closely at 61.5%.
- Gemini 3 Flash Preview outperforms Gemini 3 Pro Preview despite being smaller and cheaper.
- GLM-4.7 is the strongest open-source model, ranking alongside closed models like GPT-5.1-codex.
- GPT-OSS-120B shows significant performance improvement in high-effort reasoning mode.

**Discussion Highlights:** The discussion highlights the surprising performance of Gemini Flash and the excitement around open-source models like GLM-4.7. There is also anticipation for future releases like DeepSeek v4.

---

## 36. [I fucking love this community](https://reddit.com/r/LocalLLaMA/comments/1qee2de/i_fucking_love_this_community/)

**Author:** u/alhinai_03 | **Upvotes:** 511 | **Comments:** 54 | **Date:** 2026-01-16

**Summary:** The author expresses gratitude towards the open-source community for enabling them to run large models on older hardware, highlighting the efficiency of MoE architectures and system memory.

**Key Points:**
- Gratitude towards the open-source community for their contributions
- Running large models on a 10-year-old PC with limited GPU VRAM
- Achieving 14-13.5 tokens per second with a 30B parameter model
- Importance of system memory and MoE architecture for performance
- Community appreciation for optimization efforts

**Discussion Highlights:** The community appreciates the author's achievement and highlights the importance of system memory and MoE architectures for running large models on limited hardware. There is a consensus on the practicality of this setup and admiration for the optimization efforts in the community.

---

## 37. [New FLUX.2 [Klein] 9B is INSANELY Fast](https://reddit.com/r/LocalLLaMA/comments/1qe9xfi/new_flux2_klein_9b_is_insanely_fast/)

**Author:** u/Lopsided_Dot_4557 | **Upvotes:** 104 | **Comments:** 26 | **Date:** 2026-01-16

**Summary:** The FLUX.2 [Klein] 9B model by Black Forest Labs is praised for its speed and efficiency, achieving sub-second inference on RTX 4090 hardware and matching the performance of larger models with 9B parameters. It features step-distillation and unified text-to-image capabilities.

**Key Points:**
- Sub-second inference on RTX 4090 hardware
- 9B parameters matching models 5x its size
- Step-distilled from 50 → 4 steps with zero quality loss
- Unified text-to-image + multi-reference editing
- Efficient GPU usage with decent image quality

**Discussion Highlights:** Users highlight the model's speed and efficiency, though some note minor issues like occasional anatomical inaccuracies (e.g., extra fingers). There is interest in comparing it to other models like zimage turbo.

---

## 38. [Dang, M2 drives are the new DDR5 apparently.](https://reddit.com/r/LocalLLaMA/comments/1qe4so5/dang_m2_drives_are_the_new_ddr5_apparently/)

**Author:** u/Porespellar | **Upvotes:** 218 | **Comments:** 97 | **Date:** 2026-01-15

**Summary:** The Reddit post discusses the significant increase in prices of M2 drives, with users expressing frustration and sharing their experiences of rising costs. Key points include the dramatic price increases, user frustration, personal experiences of price hikes, uncertainty about when the increases will end, and considerations of keeping old PCs as backups. The discussion highlights a consensus among users about the frustration and concern over the rising prices of M2 drives, with many sharing personal experiences of significant price increases.

---

## 39. [My story of underestimating /r/LocalLLaMA's thirst for VRAM](https://reddit.com/r/LocalLLaMA/comments/1qe2i88/my_story_of_underestimating_rlocalllamas_thirst/)

**Author:** u/EmPips | **Upvotes:** 1335 | **Comments:** 90 | **Date:** 2026-01-15

**Summary:** The post highlights the author's underestimation of the subreddit's demand for VRAM, with discussions focusing on hardware recommendations and market dynamics.

**Key Points:**
- Author underestimated VRAM demand
- Hardware recommendations (3090s, R9700)
- Market behavior (selling cards)
- Community engagement (Discord feature)

**Discussion Highlights:** The discussion includes hardware advice and observations on market trends, with some users sharing their experiences and plans.

---

## 40. [Latest upgrade…A100 40 GB](https://reddit.com/r/LocalLLaMA/comments/1qe0cxc/latest_upgradea100_40_gb/)

**Author:** u/inserterikhere | **Upvotes:** 401 | **Comments:** 54 | **Date:** 2026-01-15

**Summary:** The user upgraded their gaming rig to an AI rig by purchasing a faulty A100 GPU for $1000, which worked perfectly upon installation. They detailed their journey from using a 3080 to eventually acquiring the A100, highlighting the cost-effective nature of their upgrades.

**Key Points:**
- User transitioned from a gaming rig to an AI rig using existing parts.
- Purchased an A100 GPU listed as faulty for $1000, which worked upon installation.
- Community expressed concerns about cooling the A100 and provided advice.
- Post received positive reception with high upvotes and comments.
- User shared their upgrade path, including previous purchases like a 3090 and 7950x.

**Discussion Highlights:** The community reacted positively to the post, with some users providing technical advice on cooling the A100. There was also humor and appreciation for the user's successful upgrade despite the initial risk of purchasing a faulty GPU.

---

## 41. [Not as impressive as most here, but really happy I made it in time!](https://reddit.com/r/LocalLLaMA/comments/1qdtvgs/not_as_impressive_as_most_here_but_really_happy_i/)

**Author:** u/Kahvana | **Upvotes:** 149 | **Comments:** 44 | **Date:** 2026-01-15

**Summary:** The author shares their experience building a PC in the Netherlands, highlighting the challenges of securing GPUs and their satisfaction with completing the build just before the RTX 5060 Ti became unavailable. They provide specs and tips for others in similar situations.

**Key Points:**
- The author faced difficulties securing an RTX 5060 Ti GPU due to supply issues and had to pay a premium to get one in stock.
- They recommend calling stores to check stock availability, as online listings may not be accurate.
- The build includes an AMD Ryzen 5 9600X, 96GB DDR5 RAM, and two RTX 5060 Ti GPUs, optimized for inference tasks.
- The discussion includes questions about CPU upgrades for inference speed and recommendations for GPU cooling and motherboard selection.

**Discussion Highlights:** The discussion focuses on potential CPU upgrades for better inference performance, cooling solutions for dual GPUs, and recommendations for motherboards that optimize dual GPU setups.

---

## 42. [Nemotron-3-nano:30b is a spectacular general purpose local LLM](https://reddit.com/r/LocalLLaMA/comments/1qdrf3o/nemotron3nano30b_is_a_spectacular_general_purpose/)

**Author:** u/DrewGrgich | **Upvotes:** 211 | **Comments:** 125 | **Date:** 2026-01-15

**Summary:** The Reddit post praises Nemotron-3-nano:30b for its exceptional performance as a general-purpose local LLM, noting its intelligence and superior reasoning quality compared to larger models like Llama 3.3:70b. Users highlight its effectiveness for research and analysis, despite its robotic tone.

**Key Points:**
- Nemotron-3-nano:30b is highly intelligent and performs well for general-purpose tasks.
- It outperforms larger models like Llama 3.3:70b in reasoning quality.
- The robotic tone is seen as a feature for research and analysis purposes.
- Users are looking forward to the upcoming Nemotron 3 super (100b) model.
- Some users prefer Qwen3-vl-30b-a3b-instruct for its vision-language capabilities.

**Discussion Highlights:** The discussion highlights the model's impressive reasoning capabilities and its suitability for research and analysis tasks. Users also express anticipation for the upcoming Nemotron 3 super (100b) model and compare it with other models like Qwen3-vl-30b-a3b-instruct.

---

## 43. [Thanks to you guys, Soprano TTS now supports OpenAI-compatible endpoint, ONNX, ComfyUI, WebUI, and CLI on CUDA, MPS, ROCm, and CPU!](https://reddit.com/r/LocalLLaMA/comments/1qdpb2v/thanks_to_you_guys_soprano_tts_now_supports/)

**Author:** u/eugenekwek | **Upvotes:** 108 | **Comments:** 26 | **Date:** 2026-01-15

**Summary:** The Reddit post announces major updates to Soprano TTS, including support for OpenAI-compatible endpoints, ONNX, ComfyUI, WebUI, and CLI across various hardware platforms like CUDA, MPS, ROCm, and CPU. The author expresses gratitude for community contributions that expanded Soprano's capabilities. Key points include: Soprano TTS now supports multiple inference methods and hardware platforms; community contributions added WebUI, CLI, OpenAI-compatible endpoints, ONNX, and ComfyUI support; additional features include an automatic hallucination detector and transformers streaming support; the post highlights the importance of community collaboration in improving the project; discussion includes questions about performance comparisons, finetuning support, and hardware compatibility. The discussion highlights questions about Soprano's performance compared to other TTS models like Kokoro, interest in finetuning support, and appreciation for the project's focus on accessibility and privacy. There is also curiosity about hardware compatibility, such as the use of an L40S GPU.

---

## 44. [google/translategemma](https://reddit.com/r/LocalLLaMA/comments/1qdok2i/googletranslategemma/)

**Author:** u/BreakfastFriendly728 | **Upvotes:** 177 | **Comments:** 56 | **Date:** 2026-01-15

**Summary:** The Reddit post discusses Google's TranslateGemma model, highlighting its technical report and key features. Users in the comments express concerns about the lack of comparisons to other models, the limited input context, and the absence of GGUF support. The discussion highlights concerns about the model's limitations, such as the input context size and the lack of certain features like GGUF support. Users also express interest in more comprehensive comparisons with other models.

---

## 45. [7x Longer Context Reinforcement Learning in Unsloth](https://reddit.com/r/LocalLLaMA/comments/1qdna3t/7x_longer_context_reinforcement_learning_in/)

**Author:** u/danielhanchen | **Upvotes:** 250 | **Comments:** 28 | **Date:** 2026-01-15

**Summary:** Unsloth introduces advancements enabling 7x longer context lengths for Reinforcement Learning, allowing training of models with up to 20K context on a 24GB card and 380K context on a 192GB NVIDIA B200 GPU, with no accuracy degradation.

**Key Points:**
- Unsloth enables 7x longer context lengths for RL, up to 20K context on a 24GB card.
- Supports 380K context on a 192GB NVIDIA B200 GPU and 110K context on an 80GB VRAM H100.
- Features like weight-sharing, Flex Attention, and Float8 training can be combined.
- Compatibility with various models including Llama, Gemma, and Qwen3.
- Free Colab notebooks available for fine-tuning with new features.

**Discussion Highlights:** The discussion highlights the post's popularity, the rapid pace of advancements, and questions about training data and model compatibility.

---

## 46. [RTX 5070 Ti and RTX 5060 Ti 16 GB no longer manufactured](https://reddit.com/r/LocalLLaMA/comments/1qdh28f/rtx_5070_ti_and_rtx_5060_ti_16_gb_no_longer/)

**Author:** u/Paramecium_caudatum_ | **Upvotes:** 233 | **Comments:** 95 | **Date:** 2026-01-15

**Summary:** Nvidia has reduced supply for the RTX 5070 Ti and RTX 5060 Ti 16 GB due to memory shortages, leading to price increases and limited availability. The 8 GB configuration of the RTX 5060 Ti remains unaffected.

**Key Points:**
- Nvidia has killed off supply for the RTX 5070 Ti and reduced supply for the RTX 5060 Ti 16 GB
- Prices for the RTX 5070 Ti have risen ~$100 over MSRP, with further hikes expected
- The 8 GB configuration of the RTX 5060 Ti is unaffected by the supply issues
- Users express disappointment and frustration over the supply issues and price increases
- Some users have managed to purchase the affected GPUs before the price hikes

**Discussion Highlights:** The discussion highlights frustration among users who were planning to upgrade their GPUs but are now facing higher prices and limited availability. Some users share their experiences of purchasing the GPUs before the price increases, while others express disappointment with Nvidia's supply management.

---

