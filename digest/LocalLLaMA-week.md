# r/LocalLLaMA Reading Digest

**Period:** 2026-01-22 to 2026-01-22
**Posts Summarized:** 47
**Total Posts Analyzed:** 47

---

## 1. [Qwen have open-sourced the full family of Qwen3-TTS: VoiceDesign, CustomVoice, and Base, 5 models (0.6B &amp; 1.8B), Support for 10 languages](https://reddit.com/r/LocalLLaMA/comments/1qjul5t/qwen_have_opensourced_the_full_family_of_qwen3tts/)

**Author:** u/Nunki08 | **Upvotes:** 505 | **Comments:** 77 | **Date:** 2026-01-22

**Summary:** Qwen has open-sourced the Qwen3-TTS model family, including 5 models (0.6B & 1.8B) with support for 10 languages. The release includes resources like GitHub, Hugging Face, a blog post, a paper, and a demo.

**Key Points:**
- Open-sourcing of Qwen3-TTS model family
- 5 models available (0.6B & 1.8B)
- Support for 10 languages
- Multiple resources provided (GitHub, Hugging Face, blog, paper, demo)
- Community reactions highlight interest in running models in compiled languages and comments on voice quality

**Discussion Highlights:** The community shows strong interest in running these models in compiled languages like llama.cpp or mistral.rs. There are mixed reactions to the voice quality, with some noting it sounds like anime dubs, while others appreciate the sample outputs. The blog example of a sarcastic teenage girl voice generated laughter and discussion.

---

## 2. [Qwen dev on Twitter!!](https://reddit.com/r/LocalLLaMA/comments/1qjtyw8/qwen_dev_on_twitter/)

**Author:** u/Difficult-Cap-7527 | **Upvotes:** 580 | **Comments:** 60 | **Date:** 2026-01-22

**Summary:** The Reddit post discusses Qwen's TTS model announcement, with the community confirming it is from a vLLM leak and sharing relevant links.

**Key Points:**
- Qwen's TTS model is from a vLLM leak
- Thread is locked as announcements are out
- Hugging Face link provided for the model
- Community discussion focuses on the model's source and details

**Discussion Highlights:** The community confirms the TTS model's source and shares relevant links, with the thread locked to prevent further discussion.

---

## 3. [GLM 4.7 flash FA fix for CUDA has been merged into llama.cpp](https://reddit.com/r/LocalLLaMA/comments/1qjrsur/glm_47_flash_fa_fix_for_cuda_has_been_merged_into/)

**Author:** u/jacek2023 | **Upvotes:** 140 | **Comments:** 45 | **Date:** 2026-01-22

**Summary:** The Reddit post discusses the recent merge of GLM 4.7 flash FA fix for CUDA into llama.cpp, highlighting performance issues and user experiences.

**Key Points:**
- GLM 4.7 flash FA fix for CUDA has been merged into llama.cpp
- Quantized cache is not working well, causing CPU performance issues
- Performance for Pascal is reported to be half the speed of non-flash-attention kernels
- Users report successful builds and model functionality despite some issues
- Ongoing discussions about bug reports and performance optimizations

**Discussion Highlights:** The discussion highlights performance issues with quantized cache and Pascal GPUs, while some users report successful builds and model functionality. There is ongoing work on bug reports and performance optimizations.

---

## 4. [Fei Fei Li dropped a non-JEPA world model, and the spatial intelligence is insane](https://reddit.com/r/LocalLLaMA/comments/1qjjrmq/fei_fei_li_dropped_a_nonjepa_world_model_and_the/)

**Author:** u/coloradical5280 | **Upvotes:** 166 | **Comments:** 73 | **Date:** 2026-01-21

**Summary:** Fei-Fei Li's World Labs launched Marble, a generative world model using Neural Radiance Fields (NeRF) and Gaussian splatting, enabling fast, editable 3D environments with VR support and export capabilities. The technology is praised for its spatial intelligence but criticized for its limited scope and lack of open-source availability.

**Key Points:**
- Marble uses NeRF and Gaussian splatting for fast 3D world generation.
- Environments are stateful, editable, and support VR and exports to Unreal/Unity/Blender.
- Criticism includes skepticism about it being a true 'world model' and lack of open-source availability.
- Mixed reactions on the product's value given the $230M funding.
- Early-stage technology with rough edges but significant potential.

**Discussion Highlights:** The discussion highlights skepticism about Marble's classification as a 'world model,' criticism of its closed-source nature, and mixed opinions on its practicality and scope. Some users appreciate its potential but note limitations in environment size and overall impact.

---

## 5. [Wrote a guide for running Claude Code with GLM-4.7 Flash locally with llama.cpp](https://reddit.com/r/LocalLLaMA/comments/1qjf6ys/wrote_a_guide_for_running_claude_code_with_glm47/)

**Author:** u/tammamtech | **Upvotes:** 105 | **Comments:** 44 | **Date:** 2026-01-21

**Summary:** The post provides a guide for running Claude Code with GLM-4.7 Flash locally using llama.cpp, including installation instructions, model running commands, and multi-model setup options. It highlights the ability to replicate Ollama features in llama.cpp and includes Docker setup instructions. Key points include the guide for running Claude Code with GLM-4.7 Flash locally using llama.cpp, commands for running the model and Docker setup, discussion of multi-model setup with config files, the ability to free GPU memory on idle, and the support for Anthropic API in llama.cpp. The discussion includes comments about the implementation of the Anthropic API endpoint, questions about VRAM and performance, and suggestions for contributing to open-source alternatives.

---

## 6. [8x AMD MI50 32GB at 26 t/s (tg) with MiniMax-M2.1 and 15 t/s (tg) with GLM 4.7 (vllm-gfx906)](https://reddit.com/r/LocalLLaMA/comments/1qjaxfy/8x_amd_mi50_32gb_at_26_ts_tg_with_minimaxm21_and/)

**Author:** u/ai-infos | **Upvotes:** 304 | **Comments:** 113 | **Date:** 2026-01-21

**Summary:** The post details a cost-effective local inference setup using 8x AMD MI50 GPUs, achieving high token generation speeds with MiniMax-M2.1 and GLM 4.7 models. The setup is praised for its performance and affordability, with a total VRAM of 256GB for under $1k.

**Key Points:**
- MiniMax-M2.1 achieves 26.8 tokens/s output and 3000 tokens/s input with a context length of 196,608.
- GLM 4.7 achieves 15.6 tokens/s output and 3000 tokens/s input with a context length of 95,000.
- Total cost for 8 GPUs is $880, providing 256GB VRAM.
- Power draw is 280W idle and 1200W during inference.
- The setup is stable for long context use cases like coding agents.

**Discussion Highlights:** The community highly praises the setup for its cost-effectiveness and performance, with many expressing interest in replicating it. Some users note the difficulty in sourcing the GPUs at the stated price.

---

## 7. [VibeVoice-ASR released!](https://reddit.com/r/LocalLLaMA/comments/1qj40er/vibevoiceasr_released/)

**Author:** u/k_means_clusterfuck | **Upvotes:** 152 | **Comments:** 39 | **Date:** 2026-01-21

**Summary:** Microsoft released VibeVoice-ASR, a multilingual automatic speech recognition model with 9B parameters. Users report high accuracy (e.g., 91% on Chinese audio) and good performance despite its size, though some note challenges with polyphonic characters.

**Key Points:**
- VibeVoice-ASR is a 9B parameter multilingual ASR model released by Microsoft.
- Users report high accuracy (e.g., 91% on Chinese audio) and good performance.
- Challenges noted with polyphonic characters in names affecting transcription.
- Comparisons made to other tools like Whisper and Parakeet.
- No official benchmarks provided, raising questions about its comparative performance.

**Discussion Highlights:** Users highlight the model's strong performance in multilingual contexts, particularly in Chinese, but note limitations with specific linguistic features like polyphonic characters. Some users express concerns about the lack of benchmarks and the model's large size compared to alternatives like Whisper and Parakeet.

---

## 8. [One-shot single page web development: pacman clone - GLM 4.7 vs GLM 4.7 Flash vs GLM 4.5 Air vs Gemini 3 Pro vs Gemini 3 Flash - Results available for online testing - Prompt and instructions provided for testing with other models](https://reddit.com/r/LocalLLaMA/comments/1qj13uh/oneshot_single_page_web_development_pacman_clone/)

**Author:** u/ex-arman68 | **Upvotes:** 103 | **Comments:** 47 | **Date:** 2026-01-21

**Summary:** The Reddit post discusses a one-shot Pacman clone development test comparing various models, with GLM 4.7 emerging as the top performer, surpassing expectations and outperforming Gemini models. The post provides links to the generated webpages and invites others to test additional models. Key points include GLM 4.7 ranking as the best performer, followed by Minimax M2.1 and Gemini 3 Flash, while Gemini 3 Pro and GLM 4.7 Flash performed poorly. The discussion highlighted the unexpected superiority of GLM 4.7 over Gemini models, praised the testing methodology, and shared additional results from other models like Minimax M2.1 and Qwen3-Coder-30B.

---

## 9. [GLM-4.7-Flash-GGUF bug fix - redownload for better outputs](https://reddit.com/r/LocalLLaMA/comments/1qiy0ha/glm47flashgguf_bug_fix_redownload_for_better/)

**Author:** u/etherd0t | **Upvotes:** 110 | **Comments:** 57 | **Date:** 2026-01-21

**Summary:** The post announces a bug fix for the GLM-4.7-Flash-GGUF model, with updated GGUFs available for download. Users report significant improvements in performance and usability after applying the fix.

**Key Points:**
- Bug fix for GLM-4.7-Flash-GGUF model released, addressing looping and poor outputs
- Updated GGUFs available for download with improved performance
- Recommended parameters provided for general use and tool-calling
- Users report positive experiences with the fixed version, noting its strength and usability
- Some users mention performance differences compared to other models like GPT-OSS-20b

**Discussion Highlights:** The discussion highlights the effectiveness of the bug fix, with users expressing satisfaction and improved usability. Some users also compare performance with other models and discuss potential future improvements.

---

## 10. [Fix for GLM 4.7 Flash has been merged into llama.cpp](https://reddit.com/r/LocalLLaMA/comments/1qiwm3c/fix_for_glm_47_flash_has_been_merged_into_llamacpp/)

**Author:** u/jacek2023 | **Upvotes:** 310 | **Comments:** 86 | **Date:** 2026-01-21

**Summary:** A fix for GLM 4.7 Flash has been merged into llama.cpp, with ongoing work on CUDA support. The community is discussing performance metrics and sharing their experiences with the updated model.

**Key Points:**
- Fix for GLM 4.7 Flash merged into llama.cpp
- CUDA support in progress via a GitHub pull request
- Performance metrics shared for GLM 4.7 unsloth on a 4090 GPU
- Discussion on CPU-only performance and user experiences
- Positive feedback on model improvements and reduced gibberish

**Discussion Highlights:** Users are sharing performance data and experiences, with general consensus that the model is improved. Some users report slow prompt processing in LMStudio, while others discuss the feasibility of running the model on CPU-only systems.

---

## 11. [Knowledge distillation with Claude as the interface: trained a 0.6B model to match GPT-class performance on Text2SQL in a singe conversation](https://reddit.com/r/LocalLLaMA/comments/1qiu6jo/knowledge_distillation_with_claude_as_the/)

**Author:** u/party-horse | **Upvotes:** 161 | **Comments:** 37 | **Date:** 2026-01-21

**Summary:** The post describes a workflow for training small, task-specific models using knowledge distillation via Claude, achieving significant performance improvements in Text2SQL tasks with minimal setup overhead.

**Key Points:**
- Knowledge distillation via Claude simplifies the process of training small models for specialized tasks.
- The approach involves using a large teacher model to generate synthetic training data and then training a smaller student model.
- The method achieved a 74% score on Text2SQL tasks, compared to the base model's 36%.
- The process includes task selection, data conversion, teacher evaluation, training, and packaging.
- The discussion highlights the potential for on-device agents and the use of open-source tools.

**Discussion Highlights:** The discussion emphasizes the usefulness of the approach for training small models for specific tasks, with some users suggesting improvements like using SQL AST for checking matches and the potential for open-source alternatives.

---

## 12. [vLLM v0.14.0 released](https://reddit.com/r/LocalLLaMA/comments/1qim0e9/vllm_v0140_released/)

**Author:** u/jinnyjuice | **Upvotes:** 169 | **Comments:** 32 | **Date:** 2026-01-20

**Summary:** The Reddit post announces the release of vLLM v0.14.0, highlighting new features and updates. Users discuss improvements like automatic context length fitting and the deprecation of certain quantization methods.

**Key Points:**
- Automatic context length fitting to GPU memory to prevent OOM failures
- Deprecation of some quantization methods, including HQQ
- Introduction of Marlin for Turing (sm75) as a major upgrade
- User interest in future sm120 optimizations

**Discussion Highlights:** Users are excited about the automatic context length feature and the Marlin upgrade for Turing. There is some discussion about the deprecation of quantization methods like HQQ, and anticipation for future optimizations.

---

## 13. [Current GLM-4.7-Flash implementation confirmed to be broken in llama.cpp](https://reddit.com/r/LocalLLaMA/comments/1qih9r8/current_glm47flash_implementation_confirmed_to_be/)

**Author:** u/Sweet_Albatross9772 | **Upvotes:** 238 | **Comments:** 56 | **Date:** 2026-01-20

**Summary:** The Reddit post confirms that the current GLM-4.7-Flash implementation in llama.cpp is broken, with significant differences in logprobs compared to vLLM, leading to issues like looping and poor performance. A potential fix is already available in a pull request.

**Key Points:**
- GLM-4.7-Flash implementation in llama.cpp is confirmed broken
- Significant differences in logprobs compared to vLLM
- Potential fix available in pull request #18980
- Community acknowledges the issue and expects a quick resolution
- Common practice to wait for bugs to be sorted out before using new models

**Discussion Highlights:** The community is aware of the issue and expects a quick fix. There is a consensus that such issues are common with new model implementations and that waiting for bugs to be resolved is a good practice.

---

## 14. [You have 64gb ram and 16gb VRAM; internet is permanently shut off: what 3 models are the ones you use?](https://reddit.com/r/LocalLLaMA/comments/1qids6a/you_have_64gb_ram_and_16gb_vram_internet_is/)

**Author:** u/Adventurous-Gold6413 | **Upvotes:** 533 | **Comments:** 290 | **Date:** 2026-01-20

**Summary:** The post discusses the best local models to use with 64GB RAM and 16GB VRAM when internet access is unavailable. The community suggests several models, with a focus on performance and versatility.

**Key Points:**
- Gemma 3 27B, GLM 4.5 Air, and GPT-OSS 120B are recommended models.
- GPT-OSS-120B is praised for its performance and versatility.
- The community appreciates the contribution of models like GPT-OSS-120B to the open-source ecosystem.
- Books are humorously suggested as an alternative to models.

**Discussion Highlights:** The discussion highlights a consensus around GPT-OSS-120B as a top choice due to its performance and versatility. Other models like Gemma 3 27B and GLM 4.5 Air are also mentioned as strong contenders. The community appreciates the availability of powerful open-source models.

---

## 15. [Liquid AI released the best thinking Language Model Under 1GB](https://reddit.com/r/LocalLLaMA/comments/1qi512t/liquid_ai_released_the_best_thinking_language/)

**Author:** u/PauLabartaBajo | **Upvotes:** 225 | **Comments:** 52 | **Date:** 2026-01-20

**Summary:** Liquid AI released LFM2.5-1.2B-Thinking, a compact reasoning model that runs on-device with 900 MB of memory, excelling in math, tool use, and instruction following. It outperforms larger models in speed and efficiency, with broad ecosystem support.

**Key Points:**
- LFM2.5-1.2B-Thinking is optimized for on-device reasoning with low memory usage.
- It generates internal thinking traces for systematic problem-solving.
- The model outperforms larger models in speed and memory efficiency.
- Concerns raised about memory requirements and quantization trade-offs.
- Performance varies across benchmarks, with notable strength in math tasks.

**Discussion Highlights:** The discussion highlights concerns about memory requirements and quantization, with some users noting performance trade-offs across different benchmarks. There is also a desire for larger models and criticism of the licensing terms.

---

## 16. [768Gb Fully Enclosed 10x GPU Mobile AI Build](https://reddit.com/r/LocalLLaMA/comments/1qi4uj2/768gb_fully_enclosed_10x_gpu_mobile_ai_build/)

**Author:** u/SweetHomeAbalama0 | **Upvotes:** 857 | **Comments:** 256 | **Date:** 2026-01-20

**Summary:** The post describes a custom-built, fully enclosed 10-GPU mobile AI system designed for running large MoE models and supporting graphic design tasks. The build balances performance and cost, using a mix of GPUs and a sturdy enclosure to protect against environmental factors like pets.

**Key Points:**
- The system features a Threadripper Pro 3995WX, 512GB DDR4, and a mix of 8x 3090 and 2x 5090 GPUs.
- The build prioritizes mobility and enclosure to protect hardware from pets.
- The total cost was around $17k, with a focus on avoiding diminishing returns on performance.
- The enclosure solution was a major challenge, ruling out mining frames for aesthetic and structural reasons.
- The post gained significant attention, with comments highlighting its uniqueness and practicality.

**Discussion Highlights:** The discussion highlights the build's uniqueness and practicality, with comments praising its design and humorously noting its portability. The consensus appreciates the balance between performance, cost, and mobility.

---

## 17. [Over 6K novels with reasoning traces to train full book writing LLMs](https://reddit.com/r/LocalLLaMA/comments/1qi3nmd/over_6k_novels_with_reasoning_traces_to_train/)

**Author:** u/XMasterDE | **Upvotes:** 110 | **Comments:** 46 | **Date:** 2026-01-20

**Summary:** The post announces an update to the LongPage dataset, expanding it to over 6,000 novels with hierarchical reasoning traces for training full-book writing LLMs. The team is also training a model on this dataset and plans to release it soon. Key points include the dataset's expansion, its support for training full-book writing LLMs, and the community's interest in the project. The discussion highlights enthusiasm for the project, with users expressing interest in the model's capabilities and potential applications.

---

## 18. [glm-4.7-flash has the best thinking process with clear steps, I love it](https://reddit.com/r/LocalLLaMA/comments/1qhxlgy/glm47flash_has_the_best_thinking_process_with/)

**Author:** u/uptonking | **Upvotes:** 136 | **Comments:** 34 | **Date:** 2026-01-20

**Summary:** The Reddit post discusses the user's experience with the glm-4.7-flash model, highlighting its structured thinking process and comparing it favorably to other models like nemotron-nano and qwen3-30b. The user appreciates the model's clear reasoning steps but notes its slower performance and occasional looping issues. Key points include the model's detailed thinking process, slower performance compared to nemotron-nano, user preference over other models, occasional looping issues, and the potential for parameter adjustments to improve performance. The discussion highlights a general appreciation for the model's reasoning process and suggestions for tweaking parameters to avoid looping issues.

---

## 19. [It's been one year since the release of Deepseek-R1](https://reddit.com/r/LocalLLaMA/comments/1qhs2sd/its_been_one_year_since_the_release_of_deepseekr1/)

**Author:** u/Recoil42 | **Upvotes:** 294 | **Comments:** 51 | **Date:** 2026-01-19

**Summary:** The Reddit post commemorates the one-year anniversary of the release of Deepseek-R1, highlighting its significant impact on the AI community. The discussion reflects on the model's influence and the rapid pace of advancements in the field.

**Key Points:**
- Deepseek-R1 had a major impact, reportedly causing significant disruption in the AI community.
- The release is considered one of the most important in AI history, second only to the original Llama model.
- The rapid pace of advancements in AI is noted, with the past year feeling like several years due to the volume of progress.
- The model's release led to price reductions and increased transparency in AI reasoning outputs.

**Discussion Highlights:** The discussion highlights the transformative impact of Deepseek-R1, with users emphasizing its role in reshaping the AI landscape and accelerating progress. There is also curiosity about how current smaller models compare to R1 in performance.

---

## 20. [Mosquito - 7.3M parameter tiny knowledge model](https://reddit.com/r/LocalLLaMA/comments/1qhqzsi/mosquito_73m_parameter_tiny_knowledge_model/)

**Author:** u/Lopsided-Repair-3638 | **Upvotes:** 119 | **Comments:** 53 | **Date:** 2026-01-19

**Summary:** The post introduces 'Mosquito', a tiny knowledge model with 7.3M parameters that can answer general knowledge questions, though with some humorous inaccuracies. The demo and model are available on Hugging Face.

**Key Points:**
- Mosquito is a 7.3M parameter model
- It can answer general knowledge questions but with inaccuracies
- Demo and model are available on Hugging Face
- Users found some answers humorous or incorrect
- Requests for model quantization were made

**Discussion Highlights:** The discussion highlights the model's limitations and humorous inaccuracies, such as defining a dog incorrectly and providing unexpected answers to simple questions. Users also requested model quantization and shared amusing interactions with the model.

---

## 21. [Bartowski comes through again. GLM 4.7 flash GGUF](https://reddit.com/r/LocalLLaMA/comments/1qhpima/bartowski_comes_through_again_glm_47_flash_gguf/)

**Author:** u/RenewAi | **Upvotes:** 184 | **Comments:** 50 | **Date:** 2026-01-19

**Summary:** The post announces the release of GLM 4.7 Flash GGUF by Bartowski, with mixed user experiences reported in the comments.

**Key Points:**
- Bartowski released GLM 4.7 Flash GGUF on Hugging Face.
- Users report mixed results with different versions of the model.
- An Unsloth version was recently uploaded.
- Some users find the model non-functional or 'brain dead'.

**Discussion Highlights:** Users are testing various versions of GLM 4.7 Flash, with some reporting issues and others exploring new releases like the Unsloth version.

---

## 22. [Unsloth GLM 4.7-Flash GGUF](https://reddit.com/r/LocalLLaMA/comments/1qhlnsv/unsloth_glm_47flash_gguf/)

**Author:** u/Wooden-Deer-1276 | **Upvotes:** 229 | **Comments:** 44 | **Date:** 2026-01-19

**Summary:** The Reddit post discusses the release of the GLM-4.7-Flash GGUF model, with community feedback on its performance and recommendations for usage. Key points include the cautious release approach, specific quantization settings and parameters for optimal performance, ongoing issues with looping in quantized versions, and active community engagement in testing and feedback. The discussion highlights a collaborative effort to improve the model, with users sharing technical details, troubleshooting issues, and celebrating milestones like the BF16 release.

---

## 23. [GLM 4.7 Flash official support merged in llama.cpp](https://reddit.com/r/LocalLLaMA/comments/1qhitrj/glm_47_flash_official_support_merged_in_llamacpp/)

**Author:** u/ayylmaonade | **Upvotes:** 359 | **Comments:** 60 | **Date:** 2026-01-19

**Summary:** The Reddit post announces the official support for GLM 4.7 Flash in llama.cpp, highlighting its community-driven development and performance improvements.

**Key Points:**
- GLM 4.7 Flash now officially supported in llama.cpp
- Support is community-driven, not by Z.ai developers
- Performance improvements noted, with some users reporting 3x speed increase without flash-attention
- Additional versions of the model are available on Hugging Face
- Mixed feedback on flash-attention performance

**Discussion Highlights:** The discussion highlights the community effort behind the integration, performance improvements, and availability of additional model versions. Some users report better performance without flash-attention.

---

## 24. [My gpu poor comrades, GLM 4.7 Flash is your local agent](https://reddit.com/r/LocalLLaMA/comments/1qhii5v/my_gpu_poor_comrades_glm_47_flash_is_your_local/)

**Author:** u/__Maximum__ | **Upvotes:** 460 | **Comments:** 160 | **Date:** 2026-01-19

**Summary:** The author highlights GLM 4.7 Flash as a reliable local agent, outperforming other MoE models in an agentic framework. They report successful long sessions with extensive token generation and various tasks executed flawlessly, eagerly awaiting local GGUF availability.

**Key Points:**
- GLM 4.7 Flash is praised for its reliability and performance in agentic tasks
- The model handles long sessions with high token generation and context compacting
- It successfully performs tasks like cloning repos, running commands, and file editing
- Community interest in comparisons with Nemotron 30B and performance benchmarks
- GGUF versions are already available for local testing

**Discussion Highlights:** The community shows strong interest in GLM 4.7 Flash, with discussions focusing on performance comparisons, early testing results, and enthusiasm for its capabilities. Some users note its deep thinking tendencies and compare it favorably to other models like Qwen3.

---

## 25. [New in llama.cpp: Anthropic Messages API](https://reddit.com/r/LocalLLaMA/comments/1qhaq21/new_in_llamacpp_anthropic_messages_api/)

**Author:** u/paf1138 | **Upvotes:** 159 | **Comments:** 50 | **Date:** 2026-01-19

**Summary:** The Reddit post announces the introduction of the Anthropic Messages API in llama.cpp, which has been well-received by the community. Users are enthusiastic about trying it out and have shared practical tips for implementation.

**Key Points:**
- Introduction of Anthropic Messages API in llama.cpp
- Enthusiasm and positive reception from the community
- Practical implementation tips shared
- Mentions of specific hardware and context usage

**Discussion Highlights:** The discussion highlights a general positive reception of the new API, with users sharing practical advice on how to implement it. There is also mention of specific hardware and context usage, indicating a focus on practical applications.

---

## 26. [zai-org/GLM-4.7-Flash · Hugging Face](https://reddit.com/r/LocalLLaMA/comments/1qh5wdq/zaiorgglm47flash_hugging_face/)

**Author:** u/Dark_Fire_12 | **Upvotes:** 731 | **Comments:** 229 | **Date:** 2026-01-19

**Summary:** The Reddit post announces the release of the zai-org/GLM-4.7-Flash model on Hugging Face, generating significant community interest and discussion about its features and potential.

**Key Points:**
- The model is a 30B parameter model with a 3B thinking component.
- It uses MLA, which reduces KV cache memory usage, enabling longer context lengths (up to 200k).
- The community expresses excitement and anticipation for the release.
- Some users miss larger models like 70B parameters.

**Discussion Highlights:** The discussion highlights enthusiasm for the model's efficiency and potential, with users appreciating its memory optimization and long context capabilities. There is a consensus that this release is promising for broader accessibility and performance.

---

## 27. [I made a Top-K implementation that's up to 20x faster than PyTorch CPU (open source)](https://reddit.com/r/LocalLLaMA/comments/1qh0yq8/i_made_a_topk_implementation_thats_up_to_20x/)

**Author:** u/andreabarbato | **Upvotes:** 149 | **Comments:** 104 | **Date:** 2026-01-19

**Summary:** The author developed an AVX2-optimized Top-K implementation that significantly outperforms PyTorch CPU, achieving up to 20x speed improvements depending on vocabulary size. It has been integrated into llama.cpp, resulting in 63% faster prompt processing for large models.

**Key Points:**
- AVX2-optimized batched Top-K implementation beats PyTorch CPU by 4-20x
- Integrated into llama.cpp with 63% faster prompt processing on a 120B MoE model
- Uses adaptive sampling, AVX2 SIMD, and cache-optimized scanning
- GitHub repository provided with pre-built DLLs and llama.cpp implementation
- Community feedback includes requests for PR submission and explanations of performance gains

**Discussion Highlights:** The community showed strong interest, with top comments requesting a PR submission to llama.cpp, explanations of the performance improvements, and some criticism regarding the lack of reproducible benchmarks. There was also a comment about the authenticity of the post.

---

## 28. [how do you pronounce “gguf”?](https://reddit.com/r/LocalLLaMA/comments/1qglyqz/how_do_you_pronounce_gguf/)

**Author:** u/Hamfistbumhole | **Upvotes:** 109 | **Comments:** 154 | **Date:** 2026-01-18

**Summary:** The Reddit post discusses the pronunciation of 'gguf', with users offering various interpretations and humorous takes. The top comments suggest different ways to pronounce it, including letter-by-letter and playful variations. Key points include the post asking how to pronounce 'gguf', top comments with humorous and literal interpretations, and suggestions like 'jee-guff', 'giguff', and 'jee jee you eff'. The discussion highlights a mix of humorous and literal interpretations, with no clear consensus but suggestions to pronounce it letter-by-letter or using playful variations.

---

## 29. [Are most major agents really just markdown todo list processors?](https://reddit.com/r/LocalLLaMA/comments/1qgj2n9/are_most_major_agents_really_just_markdown_todo/)

**Author:** u/TheDigitalRhino | **Upvotes:** 100 | **Comments:** 37 | **Date:** 2026-01-18

**Summary:** The Reddit post discusses how major AI agents decompose tasks into smaller sub-tasks, similar to a markdown todo list, and process them sequentially. The discussion includes observations on tool usage, historical context, and analogies to human problem-solving.

**Key Points:**
- AI agents decompose tasks into smaller sub-tasks for processing.
- Tool calls and terminal commands are part of this decomposition process.
- This approach mirrors human problem-solving by breaking tasks into manageable chunks.
- Historical context from the GPT-3.5 era is provided.
- A humorous analogy compares this to simplifying complex systems into basic components.

**Discussion Highlights:** The consensus in the discussion is that task decomposition is a common and effective strategy used by AI agents. Comments highlight the use of tools, historical practices, and analogies to human cognition.

---

## 30. [4x AMD R9700 (128GB VRAM) + Threadripper 9955WX Build](https://reddit.com/r/LocalLLaMA/comments/1qgdb7f/4x_amd_r9700_128gb_vram_threadripper_9955wx_build/)

**Author:** u/NunzeCs | **Upvotes:** 348 | **Comments:** 93 | **Date:** 2026-01-18

**Summary:** The author built a high-performance system with 4x AMD R9700 GPUs (128GB VRAM) and a Threadripper 9955WX CPU, leveraging a 50% subsidy to stay within a ~10,000€ budget. The system is designed for running large language models (120B+ parameters) locally, with benchmark results provided for various models. Key points include the cost-effectiveness through subsidies, the impressive hardware setup, and the performance metrics for different models. The discussion highlights the impressive hardware and cost-effectiveness, with comments expressing curiosity about component sourcing and comparisons to similar builds.

---

## 31. [Qwen 4 might be a long way off !? Lead Dev says they are "slowing down" to focus on quality.](https://reddit.com/r/LocalLLaMA/comments/1qfv1ms/qwen_4_might_be_a_long_way_off_lead_dev_says_they/)

**Author:** u/Difficult-Cap-7527 | **Upvotes:** 451 | **Comments:** 71 | **Date:** 2026-01-17

**Summary:** The Reddit post discusses a potential slowdown in the development of Qwen 4, with the lead developer emphasizing a focus on quality over speed. The community generally supports this approach, appreciating the commitment to improvement.

**Key Points:**
- Qwen 4 development may be slowing down to prioritize quality.
- The community largely supports the focus on quality over quantity.
- Some users caution against jumping to conclusions based on limited information.
- There is appreciation for meaningful advancements rather than incremental updates.

**Discussion Highlights:** The discussion highlights a consensus that focusing on quality is beneficial for the Qwen series. Users express support for taking the necessary time to make significant improvements, though some urge caution against overinterpreting the developer's statement.

---

## 32. [128GB VRAM quad R9700 server](https://reddit.com/r/LocalLLaMA/comments/1qfscp5/128gb_vram_quad_r9700_server/)

**Author:** u/Ulterior-Motive_ | **Upvotes:** 534 | **Comments:** 116 | **Date:** 2026-01-17

**Summary:** The author upgraded their server from a dual MI100 setup to a quad R9700 setup, achieving 128GB VRAM and 128GB RAM for under the price of an RTX 6000 Blackwell. The build includes detailed hardware specifications and performance benchmarks.

**Key Points:**
- Upgraded from dual MI100 to quad R9700 GPUs for better performance and cost efficiency
- Total cost of the build is $7,035, including high-end components like 128GB RAM and a 1600W PSU
- Performance benchmarks show high token processing speeds, e.g., 6524.91 tokens per second for llama 7B Q4_0
- The build is praised in the comments for its performance and cost-effectiveness
- Some users humorously note the financial irresponsibility of such high-end builds

**Discussion Highlights:** The post received positive feedback, with users appreciating the detailed build and performance metrics. Some comments highlight the cost-effectiveness compared to other high-end GPUs, while others joke about the financial commitment required for such builds.

---

## 33. [The Search for Uncensored AI (That Isn’t Adult-Oriented)](https://reddit.com/r/LocalLLaMA/comments/1qfq9ez/the_search_for_uncensored_ai_that_isnt/)

**Author:** u/Fun-Situation-4358 | **Upvotes:** 278 | **Comments:** 216 | **Date:** 2026-01-17

**Summary:** The post discusses the challenge of finding uncensored AI models that prioritize reasoning and creativity over adult-oriented content, highlighting a gap between heavily restricted corporate AI and shallow adult-focused models.

**Key Points:**
- The author seeks an AI that is genuinely unfiltered and technically advanced, focusing on reasoning and creativity.
- Most 'uncensored' models are optimized for adult use rather than serious problem-solving.
- There is a perceived gap between heavily restricted corporate AI and shallow adult-focused models.
- Suggestions include self-hosted models, open-source projects, and lesser-known platforms.
- Decensoring techniques often reduce the intelligence of open-source models.

**Discussion Highlights:** The discussion highlights a shared frustration with the lack of AI models that balance uncensored capabilities with serious problem-solving. Users express a desire for AI that acts like an AI rather than a hall monitor, without resorting to adult-oriented content. The consensus suggests exploring open-source projects and self-hosted models, though challenges remain in maintaining intelligence while removing restrictions.

---

## 34. [China's AGI-NEXT Conference (Qwen, Kimi, Zhipu, Tencent)](https://reddit.com/r/LocalLLaMA/comments/1qfmc05/chinas_aginext_conference_qwen_kimi_zhipu_tencent/)

**Author:** u/nuclearbananana | **Upvotes:** 119 | **Comments:** 22 | **Date:** 2026-01-17

**Summary:** The Reddit post discusses China's AGI-NEXT Conference, highlighting insights on China vs US AGI development, paths to AGI, compute resources, and marketing strategies. Key points include Qwen's internal advancements, perceptions of open AI vs Google, and cultural differences in innovation.

**Key Points:**
- Qwen has internally developed Qwen3.5 and context windows in the millions.
- The next paradigm in AI is believed to come from open AI rather than Google.
- Chinese work culture is described as less willing to take risks for innovation.
- Deepseek is noted for its talent concentration but was absent from the conference.

**Discussion Highlights:** The discussion highlights Qwen's advancements and the belief that open AI is more likely to drive the next paradigm shift. There is also a consensus on the cultural differences in innovation between China and the US.

---

## 35. [Best "End of world" model that will run on 24gb VRAM](https://reddit.com/r/LocalLLaMA/comments/1qfkn3a/best_end_of_world_model_that_will_run_on_24gb_vram/)

**Author:** u/gggghhhhiiiijklmnop | **Upvotes:** 335 | **Comments:** 176 | **Date:** 2026-01-17

**Summary:** The user is seeking recommendations for the best LLM models that can run on a PC with 24GB VRAM and 64GB RAM, motivated by a desire to hoard data in anticipation of a potential 'end of the world' scenario. The discussion includes suggestions for specific models and practical advice on data storage.

**Key Points:**
- User wants to download and store models that fit within 24GB VRAM and 64GB RAM.
- Suggestions include saving the best LLM possible and running it off SSD if necessary.
- Specific model recommendations include gemma3:27b and Midnight Miku.
- Advice to download actual Wikipedia backups for offline access.
- Discussion highlights the importance of data preservation in a hypothetical end-of-world scenario.

**Discussion Highlights:** The discussion features a mix of practical advice and specific model recommendations. There is a consensus on the importance of preserving data and using models that can run efficiently on the user's hardware. The top comments emphasize flexibility in running models and the value of comprehensive data backups.

---

## 36. [KoboldCpp v1.106 finally adds MCP server support, drop-in replacement for Claude Desktop](https://reddit.com/r/LocalLLaMA/comments/1qfb0gk/koboldcpp_v1106_finally_adds_mcp_server_support/)

**Author:** u/HadesThrowaway | **Upvotes:** 101 | **Comments:** 22 | **Date:** 2026-01-17

**Summary:** KoboldCpp v1.106 introduces native MCP server support, serving as a drop-in replacement for Claude Desktop with enhanced compatibility and UI improvements. The update allows seamless integration with existing MCP configurations and supports both HTTP and STDIO transports.

**Key Points:**
- KoboldCpp v1.106 adds native MCP server support
- Designed as a drop-in replacement for Claude Desktop with full compatibility
- Supports HTTP and STDIO transports for MCP servers
- UI overhaul and tool management features included
- Community feedback highlights ease of integration and requests for similar features in other tools

**Discussion Highlights:** The community response is overwhelmingly positive, with users appreciating the seamless compatibility with existing setups and the ease of integration. There are also requests for similar MCP support in other tools like llama.cpp, indicating strong interest in broader adoption of this feature.

---

## 37. [DeepSeek Engram : A static memory unit for LLMs](https://reddit.com/r/LocalLLaMA/comments/1qf5oj0/deepseek_engram_a_static_memory_unit_for_llms/)

**Author:** u/Technical-Love-8479 | **Upvotes:** 325 | **Comments:** 47 | **Date:** 2026-01-17

**Summary:** DeepSeek AI introduced Engram, a memory unit for LLMs that separates remembering from reasoning, enabling O(1) knowledge lookup and improving performance without GPU limits.

**Key Points:**
- Engram introduces conditional memory, separating it from reasoning.
- Knowledge lookup is O(1), improving efficiency.
- Enables massive memory scaling without GPU constraints.
- Improves reasoning, math, and code performance.
- Frees attention for global reasoning rather than static knowledge.

**Discussion Highlights:** The community is excited about the separation of memory and reasoning, highlighting the efficiency gains and potential for scaling memory independently of model size. There is consensus on the significance of this development for LLM performance and context handling.

---

## 38. ["Welcome to the Local Llama. How janky's your rig?](https://reddit.com/r/LocalLLaMA/comments/1qf514i/welcome_to_the_local_llama_how_jankys_your_rig/)

**Author:** u/ForsookComparison | **Upvotes:** 105 | **Comments:** 22 | **Date:** 2026-01-16

**Summary:** The Reddit post in r/LocalLLaMA discusses users' experiences and setups for running local LLaMA models, highlighting various hardware configurations and challenges. Key points include users sharing their hardware setups and challenges, such as a 3090 without a PC and RAM limitations, discussion of unconventional cooling methods like submerging GPUs in baby oil, mentions of specific hardware like MI50 GPUs and their configurations, use of improvised materials like pallet wood for GPU support, and challenges with power consumption and motherboard limitations. The discussion highlights the creative and sometimes unconventional methods users employ to run local LLaMA models, including hardware modifications and improvised solutions to overcome limitations.

---

## 39. [Prompt Repetition Improves Non-Reasoning LLMs - a paper](https://reddit.com/r/LocalLLaMA/comments/1qeuh0z/prompt_repetition_improves_nonreasoning_llms_a/)

**Author:** u/Foreign-Beginning-49 | **Upvotes:** 108 | **Comments:** 51 | **Date:** 2026-01-16

**Summary:** The Reddit post discusses a paper showing that repeating prompts can significantly improve the performance of non-reasoning LLMs without affecting latency or output format. The technique is simple yet effective across various models and benchmarks. Key points include the improvement in performance, no impact on latency or output format, and the use of Deepseek as an open weights model. The discussion highlights surprise at the effectiveness of such a simple technique and speculation about other potential improvements.

---

## 40. [performance benchmarks (72GB VRAM) - llama.cpp server - January 2026](https://reddit.com/r/LocalLLaMA/comments/1qennp2/performance_benchmarks_72gb_vram_llamacpp_server/)

**Author:** u/jacek2023 | **Upvotes:** 114 | **Comments:** 39 | **Date:** 2026-01-16

**Summary:** The Reddit post presents performance benchmarks for various AI models run on a system with three RTX 3090 GPUs and 72GB VRAM. The author measures token generation speed for multiple models, noting that smaller models often perform better with fewer GPUs. The benchmarks are not scientific but provide a practical comparison of model speeds.

**Key Points:**
- Hardware setup includes three RTX 3090 GPUs, a Ryzen Threadripper 1920X, and DDR4 RAM.
- Performance benchmarks for 30+ models, with speeds ranging from 147.85 to 4.63 tokens/s.
- ERNIE-4.5-21B-A3B-Thinking-Q8_0 achieved the highest speed at 147.85 tokens/s.
- The author suggests manual tuning could improve performance further.
- Discussion includes suggestions for additional testing and optimization flags.

**Discussion Highlights:** The discussion highlights suggestions for further testing, such as measuring performance with a filled context of ~10k tokens. Users also discuss GPU interconnectivity and optimization flags like -DGGML_CUDA_PEER_COPY=ON for direct GPU-to-GPU data copying.

---

## 41. [I reproduced DeepSeek's mHC at 1.7B params (8xH100). The instability is 3x worse than reported (10k vs 3k), but the model didn't explode.](https://reddit.com/r/LocalLLaMA/comments/1qek917/i_reproduced_deepseeks_mhc_at_17b_params_8xh100/)

**Author:** u/poisson_labs | **Upvotes:** 178 | **Comments:** 29 | **Date:** 2026-01-16

**Summary:** The author reproduced DeepSeek's mHC at 1.7B parameters and found that the instability was 3x worse than reported, with signal amplification of 10,924x. Despite this, the model continued learning, and the issue was resolved using Manifold Hyper-Connections (mHC) with Sinkhorn projection, which maintained variance at 1.0x with no compute overhead.

**Key Points:**
- Signal amplification at 1.7B parameters was 10,924x, worse than the reported 3,000x.
- The model continued learning despite high signal amplification, possibly due to modern optimizers and gradient clipping.
- Manifold Hyper-Connections (mHC) with Sinkhorn projection resolved the instability issue with zero compute overhead.
- The author provided detailed breakdowns and loss curves in external links.
- Discussion highlights include skepticism about zero compute overhead and interest in alternative optimizers like muon.

**Discussion Highlights:** The discussion included skepticism about the claim of zero compute overhead, interest in exploring alternative optimizers like muon, and appreciation for the resourcefulness of DeepSeek's approach.

---

## 42. [Maxsun joins Sparkle in making Intel Arc B60 Pro GPUs available to regular consumers, with up to 48GB VRAM](https://reddit.com/r/LocalLLaMA/comments/1qehf0p/maxsun_joins_sparkle_in_making_intel_arc_b60_pro/)

**Author:** u/reps_up | **Upvotes:** 138 | **Comments:** 50 | **Date:** 2026-01-16

**Summary:** Maxsun and Sparkle are making Intel Arc B60 Pro GPUs available to regular consumers, featuring up to 48GB VRAM. The Reddit discussion highlights interest in higher VRAM options and inquiries about software support and availability in Europe.

**Key Points:**
- Intel Arc B60 Pro GPUs with up to 48GB VRAM are becoming available to consumers
- Users express strong interest in higher VRAM configurations (e.g., 128GB)
- Questions about software support (torch/JAX/ONNX) and comparison to RoCm
- Inquiries about purchasing options in Europe
- Limited discussion on actual usage experiences with Arc GPUs

**Discussion Highlights:** The discussion shows enthusiasm for high VRAM options and curiosity about software ecosystem support. There's a notable lack of reported usage experiences with Intel Arc GPUs in the comments, and some users are seeking purchase information for European markets.

---

## 43. [GPT-5.2 xhigh, GLM-4.7, Kimi K2 Thinking, DeepSeek v3.2 on Fresh SWE-rebench (December 2025)](https://reddit.com/r/LocalLLaMA/comments/1qefa7q/gpt52_xhigh_glm47_kimi_k2_thinking_deepseek_v32/)

**Author:** u/CuriousPlatypus1881 | **Upvotes:** 376 | **Comments:** 89 | **Date:** 2026-01-16

**Summary:** The Reddit post discusses the updated SWE-bench leaderboard results from December 2025, highlighting the performance of various AI models on GitHub PR tasks. Claude Opus 4.5 leads with a 63.3% resolved rate, followed closely by GPT-5.2 (extra high effort) at 61.5%. The post also notes the strong performance of open-source models like GLM-4.7 and GPT-OSS-120B.

**Key Points:**
- Claude Opus 4.5 leads the SWE-bench leaderboard with a 63.3% resolved rate.
- GPT-5.2 (extra high effort) follows closely at 61.5%.
- GLM-4.7 is the strongest open-source model, ranking alongside closed models like GPT-5.1-codex.
- Gemini 3 Flash Preview outperforms Gemini 3 Pro Preview despite being smaller and cheaper.
- GPT-OSS-120B shows significant performance improvement in high-effort reasoning mode.

**Discussion Highlights:** The discussion highlights excitement over the performance of open-source models like GLM-4.7 and the surprising results of Gemini Flash. There is also anticipation for future releases like DeepSeek v4.

---

## 44. [I fucking love this community](https://reddit.com/r/LocalLLaMA/comments/1qee2de/i_fucking_love_this_community/)

**Author:** u/alhinai_03 | **Upvotes:** 514 | **Comments:** 54 | **Date:** 2026-01-16

**Summary:** The author expresses gratitude to the open-source community for enabling them to run large language models on older hardware, achieving impressive performance metrics. They highlight the importance of system memory and MoE architecture for their setup.

**Key Points:**
- Gratitude towards the open-source community for their contributions
- Achieving 14-13.5 tokens per second on a 10-year-old PC with 4GB VRAM
- Importance of system memory and MoE architecture for running large models
- Community appreciation for optimization efforts
- Discussion on practicality of system RAM and MoE combo

**Discussion Highlights:** The community appreciates the author's achievement and discusses the practicality of using system RAM and MoE architecture for running large models on older hardware. There is a consensus on the effectiveness of these optimizations.

---

## 45. [New FLUX.2 [Klein] 9B is INSANELY Fast](https://reddit.com/r/LocalLLaMA/comments/1qe9xfi/new_flux2_klein_9b_is_insanely_fast/)

**Author:** u/Lopsided_Dot_4557 | **Upvotes:** 100 | **Comments:** 26 | **Date:** 2026-01-16

**Summary:** The Reddit post highlights the impressive performance of the new FLUX.2 [Klein] 9B model by Black Forest Labs, noting its sub-second inference speed on RTX 4090 hardware, 9B parameters matching larger models, and step-distillation without quality loss. Users in the comments discuss its efficiency and image quality, with some pointing out minor issues like anatomical inaccuracies. The discussion highlights a consensus on the model's efficiency and speed, with users appreciating its performance on GPUs and decent image output. Some comments point out minor issues like anatomical inaccuracies (e.g., extra fingers), but overall, the sentiment is positive about the model's capabilities and speed.

---

## 46. [Dang, M2 drives are the new DDR5 apparently.](https://reddit.com/r/LocalLLaMA/comments/1qe4so5/dang_m2_drives_are_the_new_ddr5_apparently/)

**Author:** u/Porespellar | **Upvotes:** 218 | **Comments:** 97 | **Date:** 2026-01-15

**Summary:** The Reddit post discusses the significant increase in prices of M2 drives, with users expressing frustration over the rising costs. Many commenters share their experiences of purchasing drives at lower prices in the past and note the current inflated prices. Key points include the significant price increase, user frustration, personal experiences of past purchases, uncertainty about future prices, and consideration of keeping old PCs as backups. The discussion highlights a consensus among users about the frustration and financial strain caused by the sudden increase in M2 drive prices, with many sharing personal experiences and expressing concern about the future of hardware prices.

---

## 47. [My story of underestimating /r/LocalLLaMA's thirst for VRAM](https://reddit.com/r/LocalLLaMA/comments/1qe2i88/my_story_of_underestimating_rlocalllamas_thirst/)

**Author:** u/EmPips | **Upvotes:** 1337 | **Comments:** 91 | **Date:** 2026-01-15

**Summary:** The post discusses the author's experience with underestimating the demand for VRAM in the r/LocalLLaMA community. The discussion includes hardware recommendations and market dynamics.

**Key Points:**
- Post featured on Discord and author received special flair
- Discussion includes hardware recommendations (e.g., 3090s or R9700)
- Market dynamics compared to historical events like the California gold rush
- Mixed opinions on hardware choices based on cooling and VRAM needs

**Discussion Highlights:** The discussion highlights a consensus on the importance of VRAM and cooling solutions, with some users sharing personal experiences and market insights.

---

