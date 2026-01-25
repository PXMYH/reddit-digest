# r/LocalLLaMA Reading Digest

**Period:** 2026-01-24 to 2026-01-24
**Posts Summarized:** 43
**Total Posts Analyzed:** 43

---

## 1. [Personal experience with GLM 4.7 Flash Q6 (unsloth) + Roo Code + RTX 5090](https://reddit.com/r/LocalLLaMA/comments/1qlnruw/personal_experience_with_glm_47_flash_q6_unsloth/)

**Author:** u/Septerium | **Upvotes:** 135 | **Comments:** 70 | **Date:** 2026-01-24

**Summary:** The post discusses the author's positive experience using GLM 4.7 Flash Q6 for refactoring tasks, highlighting its reliability and precision compared to other models. The author shares the command used to optimize performance on an RTX 5090. The discussion includes feedback on the model's performance, tool call success, and comparisons with other models.

**Key Points:**
- GLM 4.7 Flash Q6 is praised for its reliability and precision in refactoring tasks.
- The model handles Roo Code well without breaking apart.
- The author shares a specific llama.cpp command for optimizing performance on an RTX 5090.
- Discussion includes feedback on tool call success and performance comparisons with other models.
- Some users report issues with timeouts and tool calls when using llama-server and Roo.

**Discussion Highlights:** The discussion highlights the model's performance in handling large amounts of tools and system prompts, with some users reporting success and others experiencing issues with timeouts and tool calls. There is a consensus that GLM 4.7 Flash Q6 is a strong contender in its category, though some users prefer other models for specific tasks.

---

## 2. [GLM-4.7-Flash-REAP on RTX 5060 Ti 16 GB - 200k context window!](https://reddit.com/r/LocalLLaMA/comments/1qlanzn/glm47flashreap_on_rtx_5060_ti_16_gb_200k_context/)

**Author:** u/bobaburger | **Upvotes:** 190 | **Comments:** 72 | **Date:** 2026-01-23

**Summary:** The post discusses the performance of the GLM-4.7-Flash-REAP model on an RTX 5060 Ti 16 GB setup, highlighting its speed and context window limitations. The author experiments with different context window sizes, noting significant performance drops at higher contexts. The discussion includes user feedback on functionality and comparisons with other setups.

**Key Points:**
- Model: unsloth/GLM-4.7-Flash-REAP-23B-A3B-UD-Q3_K_XL with specific parameters (e.g., temperature 0.7, top P 1).
- Performance metrics vary with context window size: 965.16 tok/s at 16k context, 172.02 tok/s at 100k context.
- Context window limitations lead to looping issues and performance degradation.
- User feedback highlights concerns about functionality at high token counts and comparisons with other models.
- LM Studio's new feature 'Force Model Expert Weight onto CPU' improves performance at high context windows.

**Discussion Highlights:** Users discuss the practicality of high context windows, compare performance with other setups, and question the low token generation speed. Some users report better performance with different models or configurations.

---

## 3. [Built a 100% client-side AI that plays Pokemon Red - Qwen 2.5 1.5B via WebLLM + neural network policy .   Fork/check it out! BYOR](https://reddit.com/r/LocalLLaMA/comments/1ql6cz7/built_a_100_clientside_ai_that_plays_pokemon_red/)

**Author:** u/Efficient-Proof-1824 | **Upvotes:** 246 | **Comments:** 26 | **Date:** 2026-01-23

**Summary:** The author built a client-side AI to play Pokemon Red using Qwen 2.5 1.5B via WebLLM and a neural network policy, deployed as a Svelte app on GitHub Pages. The project aims to create an agent that can beat the game by combining LLM-generated action plans with a neural network for scoring.

**Key Points:**
- Uses Qwen 2.5 1.5B via WebLLM for action plan generation
- Employs a TensorFlow.js neural network for policy learning
- Deployed as a Svelte app with live demo and GitHub repo
- Community suggests integrating larger models locally
- Potential applications include farming and training in-game

**Discussion Highlights:** The community expressed enthusiasm for the project, with suggestions to integrate larger models locally and explore additional features like audio output and in-game farming.

---

## 4. [Your post is getting popular and we just featured it on our Discord!](https://reddit.com/r/LocalLLaMA/comments/1qkyex0/your_post_is_getting_popular_and_we_just_featured/)

**Author:** u/roculus | **Upvotes:** 529 | **Comments:** 58 | **Date:** 2026-01-23

**Summary:** The Reddit post announces that a user's contribution has been featured on Discord and they have received a special flair. The community expresses annoyance at the bot's public posts, suggesting private messages would be more appropriate. Key points include the bot's announcement, the user's special flair, community annoyance, the existence of a pinned Discord thread, and suspicions of monetization. The discussion highlights a consensus that the bot's public announcements are spammy and disruptive, with a preference for private messages and skepticism about moderator intentions.

---

## 5. [The 'Infinite Context' Trap: Why 1M tokens won't solve Agentic Amnesia (and why we need a Memory OS)](https://reddit.com/r/LocalLLaMA/comments/1qkrhec/the_infinite_context_trap_why_1m_tokens_wont/)

**Author:** u/Sweet121 | **Upvotes:** 149 | **Comments:** 39 | **Date:** 2026-01-23

**Summary:** The post argues that large context windows (e.g., 1M tokens) are not a solution to AI memory issues, advocating instead for a structured Memory OS to manage memory lifecycle efficiently. The discussion highlights skepticism and alternative views on memory management in AI.

**Key Points:**
- Large context windows are inefficient for memory management.
- Memory should be structured and managed with lifecycle states (consolidate, evolve, forget).
- MemOS is proposed as a reusable layer for memory management.
- Discussion includes skepticism about the need for a Memory OS and comparisons to existing solutions like vector databases.
- Key challenge is determining relevance and salience in memory retrieval.

**Discussion Highlights:** The discussion reveals a mix of skepticism and agreement. Some commenters question the necessity of a Memory OS, comparing it to existing solutions like vector databases and RAG systems. Others highlight the importance of attention and salience in memory retrieval, suggesting that large context windows may exacerbate these issues.

---

## 6. [A full AI powered cooking game, where literally any ingredient is possible with infinite combinations.](https://reddit.com/r/LocalLLaMA/comments/1qkqjer/a_full_ai_powered_cooking_game_where_literally/)

**Author:** u/VirtualJamesHarrison | **Upvotes:** 104 | **Comments:** 31 | **Date:** 2026-01-23

**Summary:** The post introduces 'Infinite Kitchen', an AI-powered cooking game built with Claude Code, Gemini, and Flux, allowing infinite ingredient combinations. The game is accessible at infinite-kitchen.com/kitchen and is best experienced on a tablet or desktop.

**Key Points:**
- Game built with Claude Code, Gemini, and Flux
- Infinite ingredient combinations possible
- Best experienced on larger screens (tablet/desktop)
- Some gameplay mechanics criticized (e.g., cutting tomatoes twice, unrealistic cooking steps)
- Questions raised about live asset generation

**Discussion Highlights:** The discussion highlights both enthusiasm for the creative concept and constructive criticism about gameplay mechanics and technical limitations. Users appreciate the novelty but point out areas for improvement like screen size requirements and cooking realism.

---

## 7. [Llama.cpp merges in OpenAI Responses API Support](https://reddit.com/r/LocalLLaMA/comments/1qkm9zb/llamacpp_merges_in_openai_responses_api_support/)

**Author:** u/SemaMod | **Upvotes:** 152 | **Comments:** 40 | **Date:** 2026-01-23

**Summary:** The Reddit post discusses the successful integration of OpenAI Responses API support in llama.cpp, highlighting its effectiveness with GLM-4.7-Flash in the Codex CLI harness for exploring large codebases.

**Key Points:**
- OpenAI Responses API support has been merged into llama.cpp.
- The integration works well with GLM-4.7-Flash in the Codex CLI harness.
- The API enables stateful interactions, such as accessing and managing previous messages.
- Users are concerned about the potential deprecation of the old API.
- The new feature is effective for exploring large codebases.

**Discussion Highlights:** The discussion highlights a mix of enthusiasm for the new API's capabilities and concerns about the future of the old API. Users appreciate the functionality for managing message history and exploring codebases but are cautious about potential deprecation of existing features.

---

## 8. [OpenAI CFO hinting at "Outcome-Based Pricing" (aka royalties on your work)? Makes the case for local even stronger.](https://reddit.com/r/LocalLLaMA/comments/1qkiylw/openai_cfo_hinting_at_outcomebased_pricing_aka/)

**Author:** u/distalx | **Upvotes:** 228 | **Comments:** 98 | **Date:** 2026-01-23

**Summary:** The Reddit post discusses OpenAI's potential shift to 'Outcome-Based Pricing' for high-value enterprise deals, clarifying that it does not apply to regular users or indie developers. The author uses an analogy comparing cloud APIs to a power grid and local AI stacks to solar panels, emphasizing the benefits of local control. Key points include OpenAI's CFO mentioning 'Outcome-Based Pricing' for high-value industries like pharmaceuticals, the author initially misunderstanding the pricing model but correcting it after finding the primary source, the post highlighting the benefits of local AI stacks for avoiding potential future costs or restrictions from cloud APIs, comments reflecting concerns about fairness and the importance of self-hosting AI models, and the discussion emphasizing the value of controlling one's own AI infrastructure. The discussion highlights a consensus on the importance of self-hosting AI models to avoid potential future costs or restrictions. Users express concerns about fairness in pricing models and the benefits of local control over AI infrastructure.

---

## 9. [Nvidia Introduces PersonaPlex: An Open-Source, Real-Time Conversational AI Voice](https://reddit.com/r/LocalLLaMA/comments/1qkimzg/nvidia_introduces_personaplex_an_opensource/)

**Author:** u/44th--Hokage | **Upvotes:** 231 | **Comments:** 25 | **Date:** 2026-01-22

**Summary:** Nvidia's PersonaPlex is an open-source, real-time conversational AI voice model that enables persona control through text-based role prompts and audio-based voice conditioning. It is trained on synthetic and real conversations to produce natural, low-latency spoken interactions.

**Key Points:**
- PersonaPlex is a real-time, full-duplex speech-to-speech conversational model.
- It enables persona control through text-based role prompts and audio-based voice conditioning.
- The model is trained on a combination of synthetic and real conversations.
- It requires significant VRAM (96GB) for optimal performance.
- Discussions highlight concerns about model quality and future tool integration.

**Discussion Highlights:** The discussion includes mixed reviews on model quality, with some users noting it performs at a 'llama 1 7b level' and others highlighting high VRAM requirements. There are also questions about future tool integration and multitasking capabilities.

---

## 10. [Quiet Threadripper AI Workstation - 768GB DDR5 and 160GB VRAM (RTX 5090 + 4x R9700)](https://reddit.com/r/LocalLLaMA/comments/1qkghpk/quiet_threadripper_ai_workstation_768gb_ddr5_and/)

**Author:** u/sloptimizer | **Upvotes:** 158 | **Comments:** 90 | **Date:** 2026-01-22

**Summary:** The Reddit post details a high-performance AI workstation build featuring a Threadripper PRO 7975WX CPU, 768GB DDR5 RAM, an RTX 5090, and four R9700 GPUs. The user shares performance metrics for DeepSeek-V3.1-Terminus and discusses optimizations for cooling, power management, and GPU performance. Key points include achieving near-SOTA performance, optimizations like adding RAM fans and adjusting power limits, combining Nvidia and AMD GPUs, and the community's humorous reactions to the build's cost.

---

## 11. [Am I the only one who feels that, with all the AI boom, everyone is basically doing the same thing?](https://reddit.com/r/LocalLLaMA/comments/1qk8zj1/am_i_the_only_one_who_feels_that_with_all_the_ai/)

**Author:** u/[deleted] | **Upvotes:** 389 | **Comments:** 186 | **Date:** 2026-01-22

**Summary:** The Reddit post discusses the redundancy of AI tools and applications during the AI boom, highlighting that many new tools are less polished versions of existing ones. The discussion includes insights on the early days of AI technology and the enthusiasm driving shallow implementations. Key points include the low barrier to entry for AI development, the 'hype stage' with many self-proclaimed AI experts, and a consensus that while AI is exciting, the market is saturated with repetitive ideas. The discussion highlights the enthusiasm and low barrier to entry in AI development, leading to many similar and often redundant tools.

---

## 12. [vLLM raising $150M confirms it: We have moved from the "Throughput Era" to the "Latency(Cold Starts)."](https://reddit.com/r/LocalLLaMA/comments/1qk68n8/vllm_raising_150m_confirms_it_we_have_moved_from/)

**Author:** u/pmv143 | **Upvotes:** 167 | **Comments:** 90 | **Date:** 2026-01-22

**Summary:** The Reddit post discusses the significant investment in vLLM, signaling a shift from the 'Throughput Era' to the 'Latency Era' in AI. It highlights the growing importance of software over hardware and the need for efficient serving solutions.

**Key Points:**
- vLLM's $150M funding signals a shift from training to serving in AI.
- Software solutions are becoming more critical than hardware for efficient inference.
- The debate around vLLM's role in standardization versus optimization.
- The importance of addressing latency, particularly cold starts and time-to-first-token.
- Discussion on the role of vLLM compared to other tools like llama.cpp.

**Discussion Highlights:** The discussion highlights a debate on whether vLLM will focus on horizontal compatibility or vertical optimization. There is also a consensus on the importance of addressing latency issues in AI serving, with some users pointing out that cold starts are less of a problem in cloud environments due to data parallelism.

---

## 13. [Qwen have open-sourced the full family of Qwen3-TTS: VoiceDesign, CustomVoice, and Base, 5 models (0.6B &amp; 1.8B), Support for 10 languages](https://reddit.com/r/LocalLLaMA/comments/1qjul5t/qwen_have_opensourced_the_full_family_of_qwen3tts/)

**Author:** u/Nunki08 | **Upvotes:** 703 | **Comments:** 110 | **Date:** 2026-01-22

**Summary:** Qwen has open-sourced the Qwen3-TTS model family, including VoiceDesign, CustomVoice, and Base models in 0.6B and 1.8B sizes, supporting 10 languages. Resources are available on GitHub, Hugging Face, and other platforms.

**Key Points:**
- Open-sourcing of Qwen3-TTS model family
- Model sizes: 0.6B and 1.8B
- Support for 10 languages
- Resources available on GitHub, Hugging Face, blog, paper, and demo
- Community feedback highlights model performance and requests for additional support

**Discussion Highlights:** The community appreciates Qwen's open-sourcing efforts and provides feedback on model performance, including comments on voice quality and requests for support in running models on platforms like llama.cpp and mistral.rs.

---

## 14. [Qwen dev on Twitter!!](https://reddit.com/r/LocalLLaMA/comments/1qjtyw8/qwen_dev_on_twitter/)

**Author:** u/Difficult-Cap-7527 | **Upvotes:** 723 | **Comments:** 60 | **Date:** 2026-01-22

**Summary:** The Reddit post discusses Qwen's new TTS model announcement, with references to a vLLM leak and a link to the Hugging Face collection for Qwen3-TTS.

**Key Points:**
- Qwen's TTS model announcement
- Reference to a vLLM leak
- Link to Hugging Face collection for Qwen3-TTS
- Community discussion on the new model

**Discussion Highlights:** The community is engaged in discussing the new TTS model from Qwen, with some references to leaks and official announcements. The thread includes a link to the Hugging Face collection for further details.

---

## 15. [GLM 4.7 flash FA fix for CUDA has been merged into llama.cpp](https://reddit.com/r/LocalLLaMA/comments/1qjrsur/glm_47_flash_fa_fix_for_cuda_has_been_merged_into/)

**Author:** u/jacek2023 | **Upvotes:** 155 | **Comments:** 51 | **Date:** 2026-01-22

**Summary:** The Reddit post discusses the recent merge of GLM 4.7 flash FA fix for CUDA into llama.cpp, highlighting both successful implementations and ongoing performance issues.

**Key Points:**
- GLM 4.7 flash FA fix for CUDA has been merged into llama.cpp
- Quantized cache performance issues reported
- Successful builds reported by users
- Performance discrepancies noted on Pascal GPUs
- General feedback on model performance

**Discussion Highlights:** Users report mixed experiences with the new merge, noting successful builds but also performance issues, particularly with quantized cache and Pascal GPU performance.

---

## 16. [Fei Fei Li dropped a non-JEPA world model, and the spatial intelligence is insane](https://reddit.com/r/LocalLLaMA/comments/1qjjrmq/fei_fei_li_dropped_a_nonjepa_world_model_and_the/)

**Author:** u/coloradical5280 | **Upvotes:** 183 | **Comments:** 89 | **Date:** 2026-01-21

**Summary:** Fei-Fei Li's World Labs launched Marble, a generative world model using Neural Radiance Fields and Gaussian splatting, enabling fast, editable 3D environments with VR support. The technology is praised for its spatial intelligence but criticized for being closed-source and limited in scope.

**Key Points:**
- Marble uses Neural Radiance Fields (NeRF) and Gaussian splatting for fast 3D world generation.
- The model supports stateful, editable environments and VR integration.
- Criticisms include lack of open-source availability and skepticism about its classification as a 'world model.'
- Users note limitations in environment size and scope.
- The technology is seen as promising but early-stage.

**Discussion Highlights:** The discussion reflects mixed reactions, with some users dismissing Marble due to its closed-source nature and others critiquing its current limitations, such as small environment sizes and lack of real-time rendering.

---

## 17. [Wrote a guide for running Claude Code with GLM-4.7 Flash locally with llama.cpp](https://reddit.com/r/LocalLLaMA/comments/1qjf6ys/wrote_a_guide_for_running_claude_code_with_glm47/)

**Author:** u/tammamtech | **Upvotes:** 113 | **Comments:** 45 | **Date:** 2026-01-21

**Summary:** The Reddit post provides a guide for running Claude Code with GLM-4.7 Flash locally using llama.cpp, including installation instructions and command examples for both direct and Docker setups. The discussion highlights include clarifications on the implementation timeline and inquiries about performance metrics. Key points are: Guide for running Claude Code with GLM-4.7 Flash locally using llama.cpp, Includes installation instructions and command examples for direct and Docker setups, Discussion highlights include clarifications on implementation timeline and performance inquiries. The discussion includes a clarification that the Anthropic API endpoint was implemented before Ollama, as well as questions about VRAM usage, performance metrics, and suggestions for open-source alternatives.

---

## 18. [8x AMD MI50 32GB at 26 t/s (tg) with MiniMax-M2.1 and 15 t/s (tg) with GLM 4.7 (vllm-gfx906)](https://reddit.com/r/LocalLLaMA/comments/1qjaxfy/8x_amd_mi50_32gb_at_26_ts_tg_with_minimaxm21_and/)

**Author:** u/ai-infos | **Upvotes:** 314 | **Comments:** 127 | **Date:** 2026-01-21

**Summary:** The post discusses a cost-effective local inference setup using 8x AMD MI50 GPUs, achieving high token generation speeds with MiniMax-M2.1 and GLM 4.7 models. The setup is praised for its performance and affordability.

**Key Points:**
- MiniMax-M2.1 achieves 26.8 tokens per second output and 3000 tokens per second input with a context length of 196,608.
- GLM 4.7 achieves 15.6 tokens per second output and 3000 tokens per second input with a context length of 95,000.
- The total cost for 8 GPUs is $880, providing 256GB VRAM, with power draw ranging from 280W (idle) to 1200W (inference).
- The setup is considered one of the most cost-effective solutions for fast, intelligent local inference.
- Community reactions highlight the impressive cost-to-performance ratio and usability for coding agents.

**Discussion Highlights:** The community is highly impressed with the cost-effectiveness and performance of the setup. Comments emphasize the affordability of 256GB VRAM for under $1k and the practical usability of the models for long-context tasks like coding agents.

---

## 19. [VibeVoice-ASR released!](https://reddit.com/r/LocalLLaMA/comments/1qj40er/vibevoiceasr_released/)

**Author:** u/k_means_clusterfuck | **Upvotes:** 153 | **Comments:** 46 | **Date:** 2026-01-21

**Summary:** Microsoft released VibeVoice-ASR, a multilingual automatic speech recognition model with 9B parameters. Users report good quality and performance, though concerns about its size and lack of benchmarks are noted.

**Key Points:**
- VibeVoice-ASR is a new ASR model by Microsoft
- It is multilingual and has 9B parameters
- Users report good quality despite its size
- Performance benchmarks and comparisons with other models are discussed
- Specific use cases and limitations are mentioned

**Discussion Highlights:** Users are generally positive about the model's quality and multilingual capabilities but express concerns about its size and lack of benchmarks.

---

## 20. [One-shot single page web development: pacman clone - GLM 4.7 vs GLM 4.7 Flash vs GLM 4.5 Air vs Gemini 3 Pro vs Gemini 3 Flash - Results available for online testing - Prompt and instructions provided for testing with other models](https://reddit.com/r/LocalLLaMA/comments/1qj13uh/oneshot_single_page_web_development_pacman_clone/)

**Author:** u/ex-arman68 | **Upvotes:** 110 | **Comments:** 48 | **Date:** 2026-01-21

**Summary:** The Reddit post discusses a test where various AI models were tasked with creating a Pacman clone as a single webpage. The results showed GLM 4.7 as the clear winner, followed by Minimax M2.1, Gemini 3 Flash, Gemini 3 Pro, GLM 4.7 Flash, and GLM 4.5 Air. The post provides links to the generated webpages and encourages others to test additional models. Key points include GLM 4.7's top performance, Minimax M2.1's impressive results with sound, and Gemini models' underperformance. The discussion highlighted surprise at GLM 4.7's performance and the usefulness of the testing approach.

---

## 21. [GLM-4.7-Flash-GGUF bug fix - redownload for better outputs](https://reddit.com/r/LocalLLaMA/comments/1qiy0ha/glm47flashgguf_bug_fix_redownload_for_better/)

**Author:** u/etherd0t | **Upvotes:** 110 | **Comments:** 58 | **Date:** 2026-01-21

**Summary:** A bug fix for the GLM-4.7-Flash-GGUF model has been released, improving outputs and performance. Users are advised to re-download the updated GGUF files and use recommended parameters for optimal results.

**Key Points:**
- Bug fix resolves looping and poor outputs in GLM-4.7-Flash-GGUF
- Updated GGUF files available for download
- Recommended parameters provided for general use and tool-calling
- Users report significant improvements in model performance
- Some users note slower performance compared to other models on specific hardware

**Discussion Highlights:** Users express satisfaction with the bug fix, noting improved performance and usability. Some discuss performance comparisons with other models and hardware-specific experiences.

---

## 22. [Fix for GLM 4.7 Flash has been merged into llama.cpp](https://reddit.com/r/LocalLLaMA/comments/1qiwm3c/fix_for_glm_47_flash_has_been_merged_into_llamacpp/)

**Author:** u/jacek2023 | **Upvotes:** 311 | **Comments:** 86 | **Date:** 2026-01-21

**Summary:** The post announces that a fix for GLM 4.7 Flash has been merged into llama.cpp, which is significant for performance improvements. The update is well-received, with ongoing work on CUDA support.

**Key Points:**
- Fix for GLM 4.7 Flash merged into llama.cpp
- Ongoing work on CUDA support
- Performance data shared for different quantizations and GPUs
- Positive feedback on model improvements
- Discussion on CPU-only performance

**Discussion Highlights:** Users are sharing performance benchmarks and positive feedback on the model's improvements. There is ongoing discussion about CPU-only performance and the need for CUDA support.

---

## 23. [Knowledge distillation with Claude as the interface: trained a 0.6B model to match GPT-class performance on Text2SQL in a singe conversation](https://reddit.com/r/LocalLLaMA/comments/1qiu6jo/knowledge_distillation_with_claude_as_the/)

**Author:** u/party-horse | **Upvotes:** 170 | **Comments:** 37 | **Date:** 2026-01-21

**Summary:** The post describes a workflow for training small, task-specific models using knowledge distillation via Claude, achieving significant performance improvements in Text2SQL tasks with minimal setup overhead.

**Key Points:**
- Knowledge distillation via Claude simplifies the fine-tuning process for small models.
- The approach uses a large teacher model (DeepSeek-V3) to generate synthetic training data.
- The fine-tuned 0.6B model achieved a 74% score compared to the base model's 36%.
- The workflow includes task selection, data conversion, teacher evaluation, training, and packaging.
- The method is praised for its efficiency and potential for on-device inference.

**Discussion Highlights:** The discussion highlights the effectiveness of the approach, its potential for on-device inference, and suggestions for using SQL AST for validation. Some users express interest in trying the method, while others question the necessity of using Claude-specific code.

---

## 24. [Here is how to get GLM 4.7 working on llama.cpp with flash attention and correct outputs](https://reddit.com/r/LocalLLaMA/comments/1qir5eq/here_is_how_to_get_glm_47_working_on_llamacpp/)

**Author:** u/TokenRingAI | **Upvotes:** 101 | **Comments:** 49 | **Date:** 2026-01-21

**Summary:** The post discusses how to get GLM 4.7 working on llama.cpp with flash attention, highlighting performance metrics and noting potential issues with quantizations. The discussion includes updates on fixes and user experiences.

**Key Points:**
- GLM 4.7 can achieve high performance (2000+ tokens/sec prompt, 97 tokens/sec generation) on RTX 6000 Blackwell with flash attention.
- Initial setup required specific git branch and override options, but these are now unnecessary due to updates.
- Quantizations may have been made with incorrect functions, leading to nonsensical outputs.
- New GGUFs with correct settings have been released, improving model performance.
- Latest versions of llama.cpp and LM Studio support GLM 4.7 with flash attention.

**Discussion Highlights:** The discussion highlights the resolution of initial setup issues through updates to llama.cpp and GGUFs. Users report improved performance and functionality, with some noting the model's ability to handle tool calls effectively.

---

## 25. [vLLM v0.14.0 released](https://reddit.com/r/LocalLLaMA/comments/1qim0e9/vllm_v0140_released/)

**Author:** u/jinnyjuice | **Upvotes:** 168 | **Comments:** 36 | **Date:** 2026-01-20

**Summary:** The Reddit post announces the release of vLLM v0.14.0, highlighting new features and updates. Users discuss improvements like automatic context length fitting and the deprecation of certain quantization methods.

**Key Points:**
- Automatic context length fitting to GPU memory to prevent OOM failures
- Deprecation of some quantization methods, including HQQ
- Introduction of Marlin support for Turing (sm75)
- User excitement about the new features and improvements

**Discussion Highlights:** Users expressed enthusiasm for the automatic context length feature and discussed the implications of deprecated quantization methods. There was also interest in the new Marlin support for Turing.

---

## 26. [Current GLM-4.7-Flash implementation confirmed to be broken in llama.cpp](https://reddit.com/r/LocalLLaMA/comments/1qih9r8/current_glm47flash_implementation_confirmed_to_be/)

**Author:** u/Sweet_Albatross9772 | **Upvotes:** 246 | **Comments:** 60 | **Date:** 2026-01-20

**Summary:** The GLM-4.7-Flash implementation in llama.cpp is confirmed broken, with significant logprob discrepancies compared to vLLM, leading to performance issues. A potential fix is available in PR #18980.

**Key Points:**
- GLM-4.7-Flash implementation in llama.cpp is broken
- Logprob differences compared to vLLM cause looping and poor performance
- Potential fix available in PR #18980
- Community acknowledges the issue and appreciates open-source efforts
- Typical open-source development cycle: wait for fixes before using new models

**Discussion Highlights:** The community acknowledges the broken implementation and appreciates the open-source efforts to fix it. A potential fix is already proposed in PR #18980, and users suggest waiting for fixes before using new models.

---

## 27. [You have 64gb ram and 16gb VRAM; internet is permanently shut off: what 3 models are the ones you use?](https://reddit.com/r/LocalLLaMA/comments/1qids6a/you_have_64gb_ram_and_16gb_vram_internet_is/)

**Author:** u/Adventurous-Gold6413 | **Upvotes:** 541 | **Comments:** 306 | **Date:** 2026-01-20

**Summary:** The post discusses the best local models to use with 64GB RAM and 16GB VRAM when internet access is unavailable. Users recommend models like Gemma 3 27B, GLM 4.5 Air, and GPT-OSS 120B for their performance and capabilities.

**Key Points:**
- Users are discussing the best local models for offline use with specific hardware constraints.
- Gemma 3 27B, GLM 4.5 Air, and GPT-OSS 120B are highly recommended models.
- GPT-OSS 120B is praised for its versatility and performance on the given hardware.
- The post gained significant attention, as indicated by upvotes and comments.

**Discussion Highlights:** The discussion highlights a consensus around GPT-OSS 120B as a top choice due to its fit for the hardware and strong performance across various domains. Other notable mentions include Gemma 3 27B and GLM 4.5 Air, with users appreciating their capabilities in an offline environment.

---

## 28. [Liquid AI released the best thinking Language Model Under 1GB](https://reddit.com/r/LocalLLaMA/comments/1qi512t/liquid_ai_released_the_best_thinking_language/)

**Author:** u/PauLabartaBajo | **Upvotes:** 230 | **Comments:** 52 | **Date:** 2026-01-20

**Summary:** Liquid AI released LFM2.5-1.2B-Thinking, a compact reasoning model that runs on-device with 900 MB of memory, excelling in math, tool use, and instruction following. It outperforms larger models in speed and efficiency, with broad ecosystem support.

**Key Points:**
- LFM2.5-1.2B-Thinking is optimized for on-device reasoning with low memory usage.
- It generates internal thinking traces for systematic problem-solving.
- The model outperforms larger models in speed and memory efficiency.
- Concerns raised about memory requirements and quantization trade-offs.
- Licensing restrictions (non-Apache/MIT) were criticized by some users.

**Discussion Highlights:** Users debated memory requirements and quantization impacts, noted performance trade-offs between 'Thinking' and 'Instruct' variants, and expressed desire for larger models. Licensing restrictions were a point of contention.

---

## 29. [768Gb Fully Enclosed 10x GPU Mobile AI Build](https://reddit.com/r/LocalLLaMA/comments/1qi4uj2/768gb_fully_enclosed_10x_gpu_mobile_ai_build/)

**Author:** u/SweetHomeAbalama0 | **Upvotes:** 884 | **Comments:** 268 | **Date:** 2026-01-20

**Summary:** The post describes a custom-built, fully enclosed 10-GPU mobile AI system designed for running large MoE models and supporting graphic design tasks. The build balances performance and cost, using a mix of GPUs and a sturdy enclosure to protect hardware from pets.

**Key Points:**
- The system features a Threadripper Pro 3995WX, 512GB DDR4, and 10 GPUs (8x 3090 + 2x 5090).
- The build prioritizes mobility, enclosure, and cost-effectiveness (~$17k).
- The enclosure was critical to protect hardware from cats and ensure sturdiness.
- The system is optimized for large MoE models, video generation, and high-detail image generation.
- Top comments highlight the system's portability and airflow concerns.

**Discussion Highlights:** The discussion focuses on the system's portability, airflow challenges, and the creative solution to enclose the hardware. Comments also joke about the system's power requirements and its suitability for the intended tasks.

---

## 30. [Over 6K novels with reasoning traces to train full book writing LLMs](https://reddit.com/r/LocalLLaMA/comments/1qi3nmd/over_6k_novels_with_reasoning_traces_to_train/)

**Author:** u/XMasterDE | **Upvotes:** 111 | **Comments:** 46 | **Date:** 2026-01-20

**Summary:** The post announces an update to the LongPage dataset, expanding it to over 6,000 novels with hierarchical planning traces to support training full-book writing LLMs. The team is also training a model on this dataset and plans to release it soon. The community shows strong interest and curiosity about the dataset and model capabilities.

**Key Points:**
- LongPage dataset updated to include over 6,000 novels with hierarchical planning traces
- Dataset aims to support training full-book writing LLMs
- Team is training a model on LongPage and plans to release it soon
- Community shows interest and requests for more details
- Inquiries about data processing and inclusion of specific works like 'Worm by Wildbow'

**Discussion Highlights:** The community is eager to see the results, with many requesting more details about how the dataset and model work. There is also interest in data processing methods and the inclusion of specific works.

---

## 31. [glm-4.7-flash has the best thinking process with clear steps, I love it](https://reddit.com/r/LocalLLaMA/comments/1qhxlgy/glm47flash_has_the_best_thinking_process_with/)

**Author:** u/uptonking | **Upvotes:** 141 | **Comments:** 34 | **Date:** 2026-01-20

**Summary:** The post discusses the user's experience with glm-4.7-flash, highlighting its structured thinking process and comparing it favorably to other models like nemotron-nano and qwen3-30b. Despite its slower speed, the user appreciates its clear reasoning steps and plans to use it more extensively.

**Key Points:**
- glm-4.7-flash has a detailed 7-step thinking process that the user finds superior for data analysis.
- The model is slower (19 tokens/s) compared to nemotron-nano (30+ tokens/s) but offers better reasoning quality.
- The user shares specific configuration settings (temperature 1.0, repeat penalty 1.1, top-p 0.95) that help stabilize the model.
- Lowering temperature can speed up the thinking process without disabling it.
- The community agrees on the model's strong reasoning capabilities, though some note occasional looping issues.

**Discussion Highlights:** The community consensus highlights appreciation for glm-4.7-flash's reasoning clarity and structure, with some users suggesting tricks like lowering temperature to improve speed. However, occasional looping issues are noted, and there is a discussion about the model's performance on different hardware configurations.

---

## 32. [It's been one year since the release of Deepseek-R1](https://reddit.com/r/LocalLLaMA/comments/1qhs2sd/its_been_one_year_since_the_release_of_deepseekr1/)

**Author:** u/Recoil42 | **Upvotes:** 301 | **Comments:** 52 | **Date:** 2026-01-19

**Summary:** The Reddit post commemorates the one-year anniversary of the release of Deepseek-R1, highlighting its significant impact on the AI community. The discussion reflects on the model's influence and the rapid pace of advancements in the field.

**Key Points:**
- Deepseek-R1 had a major impact, leading to significant changes in the AI landscape.
- The release was so impactful that it caused major shifts in other AI projects.
- The rapid pace of advancements in AI is highlighted by how much has happened in just one year.
- Deepseek-R1 is considered one of the most important releases in AI history.
- There is interest in comparing current smaller models to the performance of R1.

**Discussion Highlights:** The discussion highlights the transformative impact of Deepseek-R1, with comments emphasizing its role in reshaping the AI landscape and the rapid pace of progress in the field. There is also curiosity about how current smaller models compare to R1 in terms of performance.

---

## 33. [Mosquito - 7.3M parameter tiny knowledge model](https://reddit.com/r/LocalLLaMA/comments/1qhqzsi/mosquito_73m_parameter_tiny_knowledge_model/)

**Author:** u/Lopsided-Repair-3638 | **Upvotes:** 116 | **Comments:** 54 | **Date:** 2026-01-19

**Summary:** The post introduces 'Mosquito,' a tiny 7.3M parameter language model that can answer general knowledge questions, though with some humorous inaccuracies. The demo and model are available on Hugging Face.

**Key Points:**
- Mosquito is a small language model with 7.3M parameters.
- It can answer general knowledge questions but with notable inaccuracies.
- The model and demo are hosted on Hugging Face.
- Users found some responses humorous or incorrect, such as defining a dog as a group of people.
- There is a request for a quantized version of the model.

**Discussion Highlights:** The discussion highlights the model's limitations and humorous inaccuracies, with users pointing out incorrect answers to simple questions like 'What is a dog?' and 'What do cats eat?' There is also a request for a quantized version of the model.

---

## 34. [Bartowski comes through again. GLM 4.7 flash GGUF](https://reddit.com/r/LocalLLaMA/comments/1qhpima/bartowski_comes_through_again_glm_47_flash_gguf/)

**Author:** u/RenewAi | **Upvotes:** 183 | **Comments:** 50 | **Date:** 2026-01-19

**Summary:** The post announces the release of the GLM 4.7 Flash GGUF model by Bartowski, with mixed user experiences reported in the comments.

**Key Points:**
- Bartowski released GLM 4.7 Flash GGUF model on Hugging Face.
- Users report mixed results with different versions of the model.
- Some users find the model non-functional or 'brain dead'.
- Unsloth also released a version of GLM 4.7 Flash GGUF.
- Community interest is high with 183 upvotes and 50 comments.

**Discussion Highlights:** Users are experimenting with different versions of the GLM 4.7 Flash model, with some reporting issues while others are trying out new releases like the one from Unsloth. The consensus is not yet clear, but there is significant community engagement.

---

## 35. [Unsloth GLM 4.7-Flash GGUF](https://reddit.com/r/LocalLLaMA/comments/1qhlnsv/unsloth_glm_47flash_gguf/)

**Author:** u/Wooden-Deer-1276 | **Upvotes:** 233 | **Comments:** 44 | **Date:** 2026-01-19

**Summary:** The Reddit post announces the release of the Unsloth GLM 4.7-Flash GGUF model, with community discussions focusing on its availability, usage recommendations, and known issues.

**Key Points:**
- The model is available on Hugging Face with various quantizations.
- Users are advised to use UD-Q4_K_XL and above for best results.
- Known issues include looping problems in quantized versions, with BF16 recommended for optimal performance.
- Community feedback emphasizes patience and thorough testing before wider release.
- Specific usage instructions are provided for LM Studio and llama.cpp environments.

**Discussion Highlights:** The community is actively engaged in testing and providing feedback on the model. Key discussions revolve around resolving technical issues like looping in quantized versions and optimizing performance settings. There is a consensus on using BF16 for best results and disabling or adjusting certain parameters in LM Studio.

---

## 36. [GLM 4.7 Flash official support merged in llama.cpp](https://reddit.com/r/LocalLLaMA/comments/1qhitrj/glm_47_flash_official_support_merged_in_llamacpp/)

**Author:** u/ayylmaonade | **Upvotes:** 365 | **Comments:** 60 | **Date:** 2026-01-19

**Summary:** The Reddit post announces the official support for GLM 4.7 Flash in llama.cpp, highlighting its community-driven development and performance improvements. Users discuss its efficiency compared to other implementations and share additional resources. Key points include: GLM 4.7 Flash now officially supported in llama.cpp, support is community-driven, performance improvements noted, additional resources and model versions shared by community members, and the post recognized with special flair for its contribution. The discussion highlights the community effort behind the implementation and shares performance insights, with some users noting that disabling flash-attention can lead to faster execution. Additional model versions and resources are also shared.

---

## 37. [My gpu poor comrades, GLM 4.7 Flash is your local agent](https://reddit.com/r/LocalLLaMA/comments/1qhii5v/my_gpu_poor_comrades_glm_47_flash_is_your_local/)

**Author:** u/__Maximum__ | **Upvotes:** 465 | **Comments:** 162 | **Date:** 2026-01-19

**Summary:** The Reddit post highlights the effectiveness of GLM 4.7 Flash as a reliable local agent for various tasks, with users praising its performance and capabilities. The discussion includes comparisons with other models and notes on its efficiency and output quality.

**Key Points:**
- GLM 4.7 Flash is praised for its reliability and performance in agentic frameworks.
- Users report successful execution of tasks like cloning repos, running commands, and editing files without errors.
- Comparisons with other models like Nemotron 30B and Qwen3 are discussed.
- The model's efficiency and speed on hardware like the 4090 are noted.
- Initial GGUF versions of the model are already available for local testing.

**Discussion Highlights:** The discussion highlights a positive consensus around GLM 4.7 Flash's capabilities, with users eager to test it locally. Comparisons with other models and notes on performance and output quality are key topics.

---

## 38. [New in llama.cpp: Anthropic Messages API](https://reddit.com/r/LocalLLaMA/comments/1qhaq21/new_in_llamacpp_anthropic_messages_api/)

**Author:** u/paf1138 | **Upvotes:** 163 | **Comments:** 51 | **Date:** 2026-01-19

**Summary:** The Reddit post announces the introduction of the Anthropic Messages API in llama.cpp, which has been well-received by the community. Users are enthusiastic about trying it out and have shared practical tips for implementation.

**Key Points:**
- Introduction of Anthropic Messages API in llama.cpp
- Positive reception and enthusiasm from users
- Practical tips for implementation shared in comments
- Mention of specific hardware and context usage

**Discussion Highlights:** The discussion highlights a positive consensus around the new feature, with users sharing practical tips for implementation and expressing excitement about trying it out on various hardware configurations.

---

## 39. [zai-org/GLM-4.7-Flash · Hugging Face](https://reddit.com/r/LocalLLaMA/comments/1qh5wdq/zaiorgglm47flash_hugging_face/)

**Author:** u/Dark_Fire_12 | **Upvotes:** 736 | **Comments:** 230 | **Date:** 2026-01-19

**Summary:** The post announces the release of GLM-4.7-Flash model, generating significant interest and discussion in the r/LocalLLaMA community.

**Key Points:**
- The model uses MLA, reducing KV cache memory usage
- Supports full 200k context, making it accessible to more users
- Community excitement about 30B models and anticipation for larger models
- Special recognition given to the poster for their contribution
- Technical details about the model's architecture are being discussed

**Discussion Highlights:** The community shows strong enthusiasm for the new model release, particularly noting its memory efficiency and context length capabilities. There's anticipation for larger models and appreciation for the technical advancements demonstrated in this release.

---

## 40. [I made a Top-K implementation that's up to 20x faster than PyTorch CPU (open source)](https://reddit.com/r/LocalLLaMA/comments/1qh0yq8/i_made_a_topk_implementation_thats_up_to_20x/)

**Author:** u/andreabarbato | **Upvotes:** 149 | **Comments:** 103 | **Date:** 2026-01-19

**Summary:** The author developed an AVX2-optimized batched Top-K implementation that significantly outperforms PyTorch CPU, achieving up to 20x speed improvements depending on vocabulary size. It has been integrated into llama.cpp, resulting in 63% faster prompt processing for a 120B MoE model.

**Key Points:**
- AVX2-optimized batched Top-K implementation beats PyTorch CPU by 4-20x depending on vocab size.
- Integrated into llama.cpp, achieving 63% faster prompt processing (81→142 tokens/sec) on a 120B MoE model.
- Uses adaptive sampling, AVX2 SIMD, and cache-optimized scanning with fast paths for sorted/constant inputs.
- GitHub repository provided with pre-built DLLs and llama.cpp implementation for Windows.
- Community feedback includes requests for PR submission to llama.cpp and explanations for the performance gains.

**Discussion Highlights:** The community showed strong interest, with requests for a PR submission to llama.cpp and explanations for the performance improvements. Some users raised concerns about the lack of reproducible benchmarks and the authenticity of the post.

---

## 41. [how do you pronounce “gguf”?](https://reddit.com/r/LocalLLaMA/comments/1qglyqz/how_do_you_pronounce_gguf/)

**Author:** u/Hamfistbumhole | **Upvotes:** 110 | **Comments:** 155 | **Date:** 2026-01-18

**Summary:** The Reddit post discusses the pronunciation of 'gguf', with users debating various interpretations such as 'jee-guff', 'giguff', or 'jee jee you eff'. The top comments suggest pronouncing each letter individually or not pronouncing it at all. Key points include the debate over pronunciation, suggestions like 'jee-guff' and 'giguff', and humorous comments about downloading it silently. The discussion highlights a lack of consensus, with top comments leaning towards pronouncing each letter individually or not pronouncing it at all.

---

## 42. [Are most major agents really just markdown todo list processors?](https://reddit.com/r/LocalLLaMA/comments/1qgj2n9/are_most_major_agents_really_just_markdown_todo/)

**Author:** u/TheDigitalRhino | **Upvotes:** 102 | **Comments:** 37 | **Date:** 2026-01-18

**Summary:** The Reddit post discusses how major LLM agents decompose tasks into todo lists and process them sequentially. The discussion highlights that this approach is common and effective, with some users noting its similarity to human problem-solving methods. Key points include: Major LLM agents decompose tasks into todo lists and process them one by one; this approach includes tool calls and the ability to run terminal commands; breaking down complex tasks into smaller ones is akin to human problem-solving; this method has been effective since GPT-3.5; some users humorously compare this to simplifying complex systems into manageable parts. The discussion generally agrees that decomposing tasks into smaller, manageable parts is a common and effective approach used by major LLM agents.

---

## 43. [4x AMD R9700 (128GB VRAM) + Threadripper 9955WX Build](https://reddit.com/r/LocalLLaMA/comments/1qgdb7f/4x_amd_r9700_128gb_vram_threadripper_9955wx_build/)

**Author:** u/NunzeCs | **Upvotes:** 345 | **Comments:** 101 | **Date:** 2026-01-18

**Summary:** The author built a high-performance system with 4x AMD R9700 GPUs (128GB VRAM) and a Threadripper 9955WX CPU, leveraging a 50% subsidy to stay within a ~10,000€ budget. The system is designed for running large AI models (120B+ parameters) locally, with benchmark results provided for various models.

**Key Points:**
- The build was motivated by a 50% subsidy for digitalization investments, allowing a high-end setup within budget.
- The system features 4x AMD R9700 GPUs (128GB VRAM total) and a Threadripper 9955WX CPU, optimized for large AI models.
- Benchmark results show performance metrics for models ranging from 8B to 230B parameters.
- The community praised the build, with comments highlighting its power and cost.
- The author emphasized data privacy as a key reason for running models locally.

**Discussion Highlights:** The community reacted positively, with comments praising the build's power and cost-effectiveness. Some users asked about the sourcing of components and the author's job, while others noted similarities to their own setups.

---

