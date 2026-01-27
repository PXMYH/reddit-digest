# r/LocalLLaMA Reading Digest

**Period:** 2026-01-26 to 2026-01-26
**Posts Summarized:** 46
**Total Posts Analyzed:** 46

---

## 1. [GLM 4.7 Flash: Huge performance improvement with -kvu](https://reddit.com/r/LocalLLaMA/comments/1qnwa33/glm_47_flash_huge_performance_improvement_with_kvu/)

**Author:** u/TokenRingAI | **Upvotes:** 105 | **Comments:** 31 | **Date:** 2026-01-26

**Summary:** The post highlights a significant performance improvement in GLM 4.7 Flash when using the -kvu flag in llama.cpp, with token generation speed increasing from 17.7t/s to 100t/s on an RTX 6000. It also showcases a Zelda game created by the model.

**Key Points:**
- Using -kvu flag boosts performance from 17.7t/s to 100t/s
- Demonstrates a Zelda game created by the 30B model
- Community shows strong interest and positive feedback
- Discussion includes technical details about the -kvu flag

**Discussion Highlights:** The community is highly engaged, with users expressing interest in trying the -kvu flag themselves and praising the model's capabilities, including the creation of a Zelda game.

---

## 2. [transformers v5 final is out 🔥](https://reddit.com/r/LocalLLaMA/comments/1qnk7fq/transformers_v5_final_is_out/)

**Author:** u/unofficialmerve | **Upvotes:** 367 | **Comments:** 38 | **Date:** 2026-01-26

**Summary:** Hugging Face has released transformers v5 with significant performance improvements, especially for Mixture-of-Experts models, and a simplified API. The release includes features like dynamic weight loading and better support for quantized models.

**Key Points:**
- Performance improvements for Mixture-of-Experts (6x-11x speedups)
- Simplified API with no more slow/fast tokenizers
- Dynamic weight loading for faster performance
- Better support for quantized models and PEFT
- Migration guide and release notes available for users

**Discussion Highlights:** The community is interested in the performance improvements for Mixture-of-Experts models and how it impacts local usage on different hardware configurations like NVIDIA GPUs and AMD iGPUs.

---

## 3. [I tracked GPU prices across 25 cloud providers and the price differences are insane (V100: $0.05/hr vs $3.06/hr)](https://reddit.com/r/LocalLLaMA/comments/1qnjsvz/i_tracked_gpu_prices_across_25_cloud_providers/)

**Author:** u/sleepingpirates | **Upvotes:** 141 | **Comments:** 25 | **Date:** 2026-01-26

**Summary:** The Reddit post highlights significant price disparities for GPU rentals across 25 cloud providers, with some GPUs like the V100 showing a 61x markup between the cheapest and most expensive options. The author created a tool to track real-time pricing and compare offers.

**Key Points:**
- Price differences are substantial, e.g., V100 ranges from $0.05/hr to $3.06/hr.
- The tool tracks 783 GPU offers across 57 models from 25 providers.
- Users can filter by GPU model, VRAM, region, and pricing type.
- Discussion highlights include the need for better filtering options and concerns about availability.
- The post emphasizes the importance of cost optimization in GPU rentals.

**Discussion Highlights:** Users discussed the need for better filtering options (e.g., on-demand vs. spot pricing) and raised concerns about availability and additional costs like traffic pricing. There was general appreciation for the tool but also skepticism about the practicality of some low-priced options.

---

## 4. [I built a "hive mind" for Claude Code - 7 agents sharing memory and talking to each other](https://reddit.com/r/LocalLLaMA/comments/1qnjota/i_built_a_hive_mind_for_claude_code_7_agents/)

**Author:** u/Historical-Celery-83 | **Upvotes:** 295 | **Comments:** 38 | **Date:** 2026-01-26

**Summary:** The post describes a multi-agent system called 'hive mind' for Claude Code, where 7 specialized agents coordinate tasks, share memory, and communicate via a message bus. The system uses SQLite for persistent memory and is implemented in TypeScript. While it shows promise, debugging multiple agents can be challenging. Key points include the multi-agent system with 7 specialized agents, use of SQLite for persistent memory, implementation in TypeScript, debugging challenges, and community feedback. The discussion highlights comparisons to other multi-agent methods and suggestions for improvement.

---

## 5. [216GB VRAM on the bench. Time to see which combination is best for Local LLM](https://reddit.com/r/LocalLLaMA/comments/1qni356/216gb_vram_on_the_bench_time_to_see_which/)

**Author:** u/eso_logic | **Upvotes:** 314 | **Comments:** 93 | **Date:** 2026-01-26

**Summary:** The post discusses benchmarking secondhand Tesla GPUs for Local LLM performance, comparing their efficiency when parallelized against modern devices. The author has developed a benchmarking suite to quantitatively evaluate these GPUs. Key points include the cost-effectiveness of secondhand Tesla GPUs, concerns about cooling and noise, and potential issues with prompt processing speed. The discussion highlights skepticism about usability for real-time applications but acknowledges adequacy for specific use cases like chat applications.

---

## 6. [Minimax Is Teasing M2.2](https://reddit.com/r/LocalLLaMA/comments/1qnfegx/minimax_is_teasing_m22/)

**Author:** u/Few_Painter_5588 | **Upvotes:** 184 | **Comments:** 53 | **Date:** 2026-01-26

**Summary:** The Reddit post discusses upcoming AI model releases from Chinese labs in February, including Deepseek v4, Kimi K3, MiniMax M2.2, and a potential closed-source model from ByteDance. Users express excitement and speculate on the impact of these releases.

**Key Points:**
- Multiple Chinese AI labs are expected to release new models in February.
- MiniMax M2.2 is highly anticipated and may surpass GLM 4.7 in performance.
- ByteDance's potential closed-source model is mentioned but lacks concrete evidence.
- Users discuss the shift towards agentic MoEs and the lack of updates for 32B models.
- The community is eager for advancements in local models like MiniMax and GLM.

**Discussion Highlights:** The discussion highlights excitement for MiniMax M2.2 and its potential to become a favorite local model. Users also express curiosity about ByteDance's closed-source model and the future of agentic MoEs, while noting the lack of updates for larger models like Qwen.

---

## 7. [I just won an Nvidia DGX Spark GB10 at an Nvidia hackathon. What do I do with it?](https://reddit.com/r/LocalLLaMA/comments/1qn3xig/i_just_won_an_nvidia_dgx_spark_gb10_at_an_nvidia/)

**Author:** u/brandon-i | **Upvotes:** 479 | **Comments:** 151 | **Date:** 2026-01-25

**Summary:** The author won an Nvidia DGX Spark GB10 at a hackathon and seeks advice on how to utilize it, having limited experience with fine-tuning models. They mention running a NextJS app that consumed significant memory and are open to suggestions for leveraging the new hardware. Key points include the author's background, their experience with NextJS, and community suggestions like exploring Nvidia's playbooks and running multiple NextJS apps. The discussion highlights include practical advice and humorous comments about selling the hardware.

---

## 8. [GLM-4.7-Flash is even faster now](https://reddit.com/r/LocalLLaMA/comments/1qmvny5/glm47flash_is_even_faster_now/)

**Author:** u/jacek2023 | **Upvotes:** 260 | **Comments:** 94 | **Date:** 2026-01-25

**Summary:** The Reddit post discusses the GLM-4.7-Flash model, highlighting its improved speed and popularity within the community. The discussion includes references to previous posts, AMD GPU performance, and humorous remarks about the model being 'cursed'.

**Key Points:**
- GLM-4.7-Flash model is noted for its speed
- Post is popular and featured on Discord
- References to previous posts and AMD GPU performance
- Humorous remarks about the model being 'cursed'
- Community engagement with 260 upvotes and 94 comments

**Discussion Highlights:** The discussion highlights the model's popularity and community engagement, with mentions of previous contributions and humorous remarks about the model's performance and compatibility with AMD GPUs.

---

## 9. [Internet blackout and Local LLMs](https://reddit.com/r/LocalLLaMA/comments/1qmlpjp/internet_blackout_and_local_llms/)

**Author:** u/DunderSunder | **Upvotes:** 246 | **Comments:** 74 | **Date:** 2026-01-25

**Summary:** The post discusses the severe internet blackout in Iran, highlighting the importance of local LLMs like Gemma3 and Qwen3 in circumventing censorship. Users share their experiences with limited internet access and the usefulness of local models compared to cloud-based services like ChatGPT. Key points include the severe internet blackout, the crucial role of local LLMs, the limitations of cloud-based models, the reliability of local LLMs, and suggestions for alternative methods like downloading Wikipedia. The discussion emphasizes the importance of local LLMs in situations of internet censorship and the limitations of cloud-based services.

---

## 10. [KV cache fix for GLM 4.7 Flash](https://reddit.com/r/LocalLLaMA/comments/1qmjzx1/kv_cache_fix_for_glm_47_flash/)

**Author:** u/jacek2023 | **Upvotes:** 241 | **Comments:** 69 | **Date:** 2026-01-25

**Summary:** The post discusses a fix for the KV cache in GLM 4.7 Flash, which significantly reduces VRAM usage by removing unnecessary components, allowing for longer context lengths on the same hardware setup.

**Key Points:**
- Removing 'Air' from GLM 4.7 Flash optimizes KV cache usage.
- VRAM savings allow for much longer context lengths (e.g., from 45,000 to 90,000 tokens on a 4090).
- The model is still considered somewhat quirky but functional.
- Community is actively working on further improvements, with only 5 patches remaining for full local compatibility.

**Discussion Highlights:** The community is enthusiastic about the improvements, with users reporting significant performance gains. There is a consensus that the model is progressing well, though some quirks remain. The focus is on further optimization and compatibility patches.

---

## 11. [What do you actually want from a private AI chat on your phone?](https://reddit.com/r/LocalLLaMA/comments/1qmir5d/what_do_you_actually_want_from_a_private_ai_chat/)

**Author:** u/AppDeveloperAsdf | **Upvotes:** 232 | **Comments:** 82 | **Date:** 2026-01-25

**Summary:** The post discusses the development of 'zerotap,' an Android app that allows AI to control a phone like a human, with features such as screen interaction and support for various AI models. The developer seeks user input on future features and addresses concerns about security and practicality. Key points include the app's capabilities, future feature considerations, user concerns about security and open-source requirements, and a demand for offline functionality and a user-friendly interface. The discussion highlights a consensus on the importance of open-source development, offline capabilities, and a non-buggy user interface, with users emphasizing the need for clear problem-solving purposes before app development.

---

## 12. [[Release] Qwen3-TTS: Ultra-Low Latency (97ms), Voice Cloning &amp; OpenAI-Compatible API](https://reddit.com/r/LocalLLaMA/comments/1qlzbhh/release_qwen3tts_ultralow_latency_97ms_voice/)

**Author:** u/blackstoreonline | **Upvotes:** 295 | **Comments:** 126 | **Date:** 2026-01-24

**Summary:** The post introduces Qwen3-TTS, an ultra-low latency (97ms) text-to-speech model with voice cloning and OpenAI-compatible API, offering a high-quality, open-source alternative for local speech synthesis. Key points include its ultra-low latency, natural language voice control, easy voice cloning, multilingual support, and OpenAI compatibility. The community is highly impressed with the low latency and ease of use, with many users planning to test or already hosting the model. Some technical challenges, such as GPU compatibility, were noted but are being addressed.

---

## 13. [Artificial Analysis: South Korea 🇰🇷 is now the clear #3 nation in AI — powered by the Korean National Sovereign AI Initiative there are now multiple Korean AI labs with near frontier intelligence.](https://reddit.com/r/LocalLLaMA/comments/1qltwza/artificial_analysis_south_korea_is_now_the_clear/)

**Author:** u/self-fix | **Upvotes:** 184 | **Comments:** 54 | **Date:** 2026-01-24

**Summary:** South Korea has emerged as a leading nation in AI, driven by the Korean National Sovereign AI Initiative. This government-backed competition has shortlisted top AI labs like LG, SK Telecom, and Upstage, fostering the development of advanced AI models such as K-EXAONE and Solar Open.

**Key Points:**
- South Korea is now the #3 nation in AI, powered by the Korean National Sovereign AI Initiative.
- The initiative shortlists national champions, providing government funding and GPU access.
- Top Korean AI models include LG's K-EXAONE (236B) and Upstage's Solar Open (100B).
- Models vary in size and focus, with some being open weights and others proprietary.
- The initiative has narrowed down to three finalists: LG, SK Telecom, and Upstage.

**Discussion Highlights:** The discussion includes questions about the absence of Canadian AI models, skepticism about benchmarking methods, and debates about the ranking of South Korea compared to other nations like France, Canada, and Japan.

---

## 14. [I built an open-source audiobook converter using Qwen3 TTS - converts PDFs/EPUBs to high-quality audiobooks with voice cloning support](https://reddit.com/r/LocalLLaMA/comments/1qlr3wj/i_built_an_opensource_audiobook_converter_using/)

**Author:** u/TheyCallMeDozer | **Upvotes:** 135 | **Comments:** 45 | **Date:** 2026-01-24

**Summary:** The Reddit post introduces an open-source audiobook converter tool that uses Qwen3 TTS to convert various document formats (PDF, EPUB, DOCX, TXT) into high-quality audiobooks. The tool supports both pre-built voices and voice cloning, with features like smart chunking, intelligent caching, and multi-format support. The author built this tool to provide a free alternative to expensive audiobook services. Key points include the tool's ability to convert multiple document formats, offer two voice modes, and provide high-quality audio output in MP3 format. The discussion highlights include requests for audio examples, comparisons to other tools like Chatterbox and Vibevoice, and questions about GUI support and VRAM requirements.

---

## 15. [Personal experience with GLM 4.7 Flash Q6 (unsloth) + Roo Code + RTX 5090](https://reddit.com/r/LocalLLaMA/comments/1qlnruw/personal_experience_with_glm_47_flash_q6_unsloth/)

**Author:** u/Septerium | **Upvotes:** 165 | **Comments:** 92 | **Date:** 2026-01-24

**Summary:** The Reddit post discusses the user's positive experience with GLM 4.7 Flash Q6 for refactoring tasks, highlighting its reliability and precision compared to other models like GPT-OSS 120b and GLM 4.5 Air. The user shares technical details about running the model on an RTX 5090 with specific llama.cpp settings.

**Key Points:**
- GLM 4.7 Flash performs well in refactoring tasks and handles Roo Code effectively.
- The model is more reliable and precise than GPT-OSS 120b, GLM 4.5 Air, or Devstral 24b.
- Technical details include using UD-Q6_K_XL quantization and achieving 150 tok/s on an RTX 5090.
- Discussion highlights include feedback on tool calls, comparisons with other models, and technical optimizations.

**Discussion Highlights:** The discussion features feedback on the model's performance, with users noting its success in tool calls and large system prompts. Some users compare it favorably to other models, while others mention technical optimizations and the evolving state of llama.cpp.

---

## 16. [GLM-4.7-Flash-REAP on RTX 5060 Ti 16 GB - 200k context window!](https://reddit.com/r/LocalLLaMA/comments/1qlanzn/glm47flashreap_on_rtx_5060_ti_16_gb_200k_context/)

**Author:** u/bobaburger | **Upvotes:** 206 | **Comments:** 95 | **Date:** 2026-01-23

**Summary:** The post discusses the performance of the GLM-4.7-Flash-REAP model on an RTX 5060 Ti 16 GB setup, highlighting its speed and context window capabilities. The author experiments with different context window sizes and notes performance trade-offs, including issues with looping and resource usage.

**Key Points:**
- Model used: unsloth/GLM-4.7-Flash-REAP-23B-A3B-UD-Q3_K_XL
- Performance metrics provided for different context window sizes (16k, 64k, 100k, 200k)
- Issues encountered include looping with smaller context windows and resource constraints with larger windows
- Community feedback highlights potential for improvement and comparisons with other models
- Discussion emphasizes the progress towards running high-quality agents locally with large context windows

**Discussion Highlights:** The discussion highlights community interest in optimizing local model performance, with comparisons to other setups and models. There is consensus on the potential for running high-quality agents locally with large context windows, though challenges remain in balancing speed and resource usage.

---

## 17. [Built a 100% client-side AI that plays Pokemon Red - Qwen 2.5 1.5B via WebLLM + neural network policy .   Fork/check it out! BYOR](https://reddit.com/r/LocalLLaMA/comments/1ql6cz7/built_a_100_clientside_ai_that_plays_pokemon_red/)

**Author:** u/Efficient-Proof-1824 | **Upvotes:** 268 | **Comments:** 30 | **Date:** 2026-01-23

**Summary:** The post describes a client-side AI project that plays Pokemon Red using Qwen 2.5 1.5B via WebLLM and a neural network policy. The project is deployed as a Svelte app and aims to build an agent capable of beating the game.

**Key Points:**
- The project uses Qwen 2.5 1.5B via WebLLM for action plan generation.
- A TensorFlow.js neural network is used to score actions and learn from gameplay.
- The emulator is binjgb compiled to WASM, with direct RAM reading for game state.
- The project is deployed as a Svelte app on GitHub Pages.
- Community feedback highlights enthusiasm and suggestions for future improvements.

**Discussion Highlights:** The discussion is generally positive, with users expressing excitement about the project and suggesting potential enhancements, such as integrating larger models locally and adding audio output.

---

## 18. [Your post is getting popular and we just featured it on our Discord!](https://reddit.com/r/LocalLLaMA/comments/1qkyex0/your_post_is_getting_popular_and_we_just_featured/)

**Author:** u/roculus | **Upvotes:** 563 | **Comments:** 58 | **Date:** 2026-01-23

**Summary:** The Reddit post announces that a user's contribution has been featured on Discord and they have received a special flair. The community discusses the annoyance of bot spam and questions the monetization of the Discord server. Key points include the bot's announcement, community annoyance with bot spam, speculation about monetization, the existence of a pinned thread about the Discord server, and humor about the bot's behavior. The community consensus is that the bot spam is annoying and suggests private messages to the OP instead of public posts.

---

## 19. [Sweep: Open-weights 1.5B model for next-edit autocomplete](https://reddit.com/r/LocalLLaMA/comments/1qkxuv1/sweep_openweights_15b_model_for_nextedit/)

**Author:** u/Kevinlu1248 | **Upvotes:** 108 | **Comments:** 29 | **Date:** 2026-01-23

**Summary:** The post introduces Sweep, a 1.5B parameter model for next-edit autocomplete, which predicts code edits based on recent changes. It outperforms larger models in speed and accuracy and is available for local use via Hugging Face or a JetBrains plugin.

**Key Points:**
- Sweep is a 1.5B parameter model for next-edit autocomplete, available on Hugging Face and as a JetBrains plugin.
- The model uses recent edits as context, improving accuracy for tasks like variable renaming.
- Prompt format and RL training significantly improved performance, with benchmarks showing high accuracy.
- The model is designed for local use, ensuring privacy and speed.
- Community interest includes integration with various editors and mobile platforms.

**Discussion Highlights:** The discussion reflects enthusiasm for the tool, with users expressing interest in integrations for different editors and platforms. Some comments highlight concerns about leaving deterministic tasks like variable renaming to LLMs.

---

## 20. [The 'Infinite Context' Trap: Why 1M tokens won't solve Agentic Amnesia (and why we need a Memory OS)](https://reddit.com/r/LocalLLaMA/comments/1qkrhec/the_infinite_context_trap_why_1m_tokens_wont/)

**Author:** u/Sweet121 | **Upvotes:** 177 | **Comments:** 41 | **Date:** 2026-01-23

**Summary:** The post argues that large context windows (e.g., 1M tokens) are not a solution to AI memory issues, advocating instead for a structured Memory OS to manage memory lifecycle efficiently. The discussion highlights skepticism and alternative views on memory management.

**Key Points:**
- Large context windows are inefficient for memory management.
- Memory OS proposes structured memory lifecycle management (consolidate, evolve, forget).
- Critics question the necessity of a Memory OS, suggesting simpler solutions like vector DBs.
- Efficiency and relevance are key concerns in memory management.

**Discussion Highlights:** The discussion reveals skepticism about the need for a Memory OS, with some users preferring simpler solutions like vector databases or file-based storage. There is a consensus on the importance of efficient and relevant memory management, but opinions differ on the best approach.

---

## 21. [A full AI powered cooking game, where literally any ingredient is possible with infinite combinations.](https://reddit.com/r/LocalLLaMA/comments/1qkqjer/a_full_ai_powered_cooking_game_where_literally/)

**Author:** u/VirtualJamesHarrison | **Upvotes:** 118 | **Comments:** 33 | **Date:** 2026-01-23

**Summary:** The post introduces 'Infinite Kitchen', an AI-powered cooking game that allows for infinite ingredient combinations. The game is built using Claude Code for game logic, Gemini for sprites, and Flux for the overall structure. Users can try it out at the provided link. Key points include the game's construction with Claude Code, Gemini, and Flux, noted inconsistencies in game mechanics, the requirement for a larger screen, and discussions about the simplicity of the concept and curiosity about live asset generation. The discussion highlights both appreciation for the innovative concept and constructive criticism regarding game mechanics and technical implementation.

---

## 22. [Llama.cpp merges in OpenAI Responses API Support](https://reddit.com/r/LocalLLaMA/comments/1qkm9zb/llamacpp_merges_in_openai_responses_api_support/)

**Author:** u/SemaMod | **Upvotes:** 155 | **Comments:** 44 | **Date:** 2026-01-23

**Summary:** The post discusses the successful integration of OpenAI Responses API support in Llama.cpp, highlighting its effectiveness with GLM-4.7-Flash in the Codex CLI harness for exploring large codebases.

**Key Points:**
- OpenAI Responses API support has been merged into Llama.cpp.
- The integration works well with GLM-4.7-Flash in the Codex CLI harness.
- The API enables stateful interactions, such as accessing and managing previous messages.
- Users express concern about potential deprecation of the old API.
- The new feature is praised for its effectiveness in exploring large codebases.

**Discussion Highlights:** The discussion highlights a mix of enthusiasm for the new API's capabilities and concerns about the future of the old API. Users appreciate the functionality for code exploration but remain cautious about potential changes.

---

## 23. [OpenAI CFO hinting at "Outcome-Based Pricing" (aka royalties on your work)? Makes the case for local even stronger.](https://reddit.com/r/LocalLLaMA/comments/1qkiylw/openai_cfo_hinting_at_outcomebased_pricing_aka/)

**Author:** u/distalx | **Upvotes:** 234 | **Comments:** 98 | **Date:** 2026-01-23

**Summary:** The Reddit post discusses OpenAI's CFO mentioning 'Outcome-Based Pricing' for high-value enterprise deals, clarifying that it does not apply to regular users or indie developers. The post highlights the importance of local AI solutions to avoid potential future costs or restrictions. Key points include OpenAI's CFO discussing 'Outcome-Based Pricing' for high-value enterprise deals, not regular users, the concept involving OpenAI taking a cut of specific high-value wins, like pharmaceutical discoveries, the post emphasizing the benefits of local AI solutions to maintain control and avoid potential future costs, the discussion including a comparison to the Grid vs. Solar debate, highlighting the trade-offs between convenience and control, and comments reflecting skepticism and humor, with some users emphasizing the importance of self-hosting AI solutions. The discussion highlights a consensus on the importance of self-hosting AI solutions to avoid potential future costs and maintain control. Users express skepticism about OpenAI's pricing model and emphasize the benefits of local AI solutions.

---

## 24. [Nvidia Introduces PersonaPlex: An Open-Source, Real-Time Conversational AI Voice](https://reddit.com/r/LocalLLaMA/comments/1qkimzg/nvidia_introduces_personaplex_an_opensource/)

**Author:** u/44th--Hokage | **Upvotes:** 241 | **Comments:** 30 | **Date:** 2026-01-22

**Summary:** Nvidia has introduced PersonaPlex, an open-source, real-time conversational AI voice model that enables persona control through text-based role prompts and audio-based voice conditioning. It is trained on synthetic and real conversations to produce natural, low-latency spoken interactions.

**Key Points:**
- PersonaPlex is a real-time, full-duplex speech-to-speech conversational model.
- It enables persona control through text-based role prompts and audio-based voice conditioning.
- The model is trained on a combination of synthetic and real conversations.
- It requires significant VRAM (96GB) for optimal performance.
- Some users have noted limitations in the model's intelligence and performance.

**Discussion Highlights:** Users have mixed reactions, with some highlighting the model's limitations in intelligence and high VRAM requirements. Others have noted issues with audio quality and questioned the model's ability to handle multitasking, such as tool calls during conversations.

---

## 25. [Quiet Threadripper AI Workstation - 768GB DDR5 and 160GB VRAM (RTX 5090 + 4x R9700)](https://reddit.com/r/LocalLLaMA/comments/1qkghpk/quiet_threadripper_ai_workstation_768gb_ddr5_and/)

**Author:** u/sloptimizer | **Upvotes:** 163 | **Comments:** 94 | **Date:** 2026-01-22

**Summary:** The Reddit post describes a high-performance AI workstation build featuring a Threadripper PRO 7975WX CPU, 768GB DDR5 RAM, an RTX 5090, and four R9700 GPUs. The system achieves impressive performance with DeepSeek-V3.1-Terminus, reaching 151.76 tokens per second in prompt processing and 10.85 tokens per second in token generation.

**Key Points:**
- The build includes a Threadripper PRO 7975WX CPU, 768GB DDR5 RAM, an RTX 5090, and four R9700 GPUs.
- Performance metrics: DeepSeek-V3.1-Terminus with context = 37279 tokens: PP = 151.76 tps, TG = 10.85 tps.
- Key optimizations: Adding RAM fans for better cooling, disabling remote management for faster boot, and adjusting power limits for cooler and quieter operation.
- The system combines Nvidia and AMD cards using llama.cpp with specific compilation flags.
- Top comments highlight the impressive performance and express admiration for the build.

**Discussion Highlights:** The discussion highlights the impressive performance of the workstation, with users expressing admiration for the build's capabilities. Some comments joke about the high cost and power of the system, while others inquire about the benefits of combining Nvidia and AMD GPUs.

---

## 26. [Am I the only one who feels that, with all the AI boom, everyone is basically doing the same thing?](https://reddit.com/r/LocalLLaMA/comments/1qk8zj1/am_i_the_only_one_who_feels_that_with_all_the_ai/)

**Author:** u/[deleted] | **Upvotes:** 400 | **Comments:** 189 | **Date:** 2026-01-22

**Summary:** The Reddit post discusses the redundancy in AI tools and applications during the AI boom, highlighting that many new tools are essentially reinventions of existing solutions. The discussion reflects a mix of enthusiasm for the technology and skepticism about the proliferation of shallow implementations. Key points include the redundancy of AI tools, the low barrier to entry leading to similar projects, and the consensus that the current phase is characterized by hype. Some developers are focusing on niche tools to address specific needs.

---

## 27. [vLLM raising $150M confirms it: We have moved from the "Throughput Era" to the "Latency(Cold Starts)."](https://reddit.com/r/LocalLLaMA/comments/1qk68n8/vllm_raising_150m_confirms_it_we_have_moved_from/)

**Author:** u/pmv143 | **Upvotes:** 168 | **Comments:** 91 | **Date:** 2026-01-22

**Summary:** The Reddit post discusses the significant investment in vLLM, signaling a shift from the 'Throughput Era' to the 'Latency Era' in AI. The focus is now on serving efficiency, latency, and throughput, with vLLM aiming to be a standard in inference software.

**Key Points:**
- vLLM's $150M funding signals a shift from training to serving in AI.
- Software optimization is crucial for utilizing hardware effectively.
- vLLM aims to standardize inference across different hardware platforms.
- The next major challenge is reducing latency, particularly cold starts.
- Community discussion highlights varying opinions on vLLM's role and the importance of latency in different contexts.

**Discussion Highlights:** The discussion includes debates on the significance of the investment, comparisons with other companies, and differing views on vLLM's role in the inference landscape. Some commenters emphasize the importance of latency in cloud environments, while others advocate for local solutions.

---

## 28. [Qwen have open-sourced the full family of Qwen3-TTS: VoiceDesign, CustomVoice, and Base, 5 models (0.6B &amp; 1.8B), Support for 10 languages](https://reddit.com/r/LocalLLaMA/comments/1qjul5t/qwen_have_opensourced_the_full_family_of_qwen3tts/)

**Author:** u/Nunki08 | **Upvotes:** 722 | **Comments:** 117 | **Date:** 2026-01-22

**Summary:** Qwen has open-sourced the Qwen3-TTS model family, including VoiceDesign, CustomVoice, and Base models in 0.6B and 1.8B sizes, supporting 10 languages. The release includes resources on GitHub, Hugging Face, and a demo space.

**Key Points:**
- Qwen3-TTS models (0.6B & 1.8B) released with support for 10 languages
- Resources available on GitHub, Hugging Face, blog, paper, and demo space
- Positive community reception with some concerns about voice quality
- Requests for compatibility with tools like llama.cpp
- Appreciation for Qwen's open-source contributions

**Discussion Highlights:** The community generally appreciates Qwen's open-source release, though some users noted concerns about the voice quality sounding like anime dubs. There were requests for compatibility with other tools like llama.cpp, and overall positive feedback for Qwen's contributions.

---

## 29. [Qwen dev on Twitter!!](https://reddit.com/r/LocalLLaMA/comments/1qjtyw8/qwen_dev_on_twitter/)

**Author:** u/Difficult-Cap-7527 | **Upvotes:** 744 | **Comments:** 60 | **Date:** 2026-01-22

**Summary:** The Reddit post discusses Qwen's TTS model announcement, which is reportedly from a vLLM leak. The community is sharing links and discussing its legitimacy.

**Key Points:**
- Qwen's TTS model announcement
- Model is from a vLLM leak
- Hugging Face link provided
- Community discussion on legitimacy

**Discussion Highlights:** The discussion highlights include a locked thread, mentions of the TTS model's source, and a shared Hugging Face link for further exploration.

---

## 30. [GLM 4.7 flash FA fix for CUDA has been merged into llama.cpp](https://reddit.com/r/LocalLLaMA/comments/1qjrsur/glm_47_flash_fa_fix_for_cuda_has_been_merged_into/)

**Author:** u/jacek2023 | **Upvotes:** 160 | **Comments:** 51 | **Date:** 2026-01-22

**Summary:** The Reddit post announces the merge of GLM 4.7 flash FA fix for CUDA into llama.cpp, with discussions highlighting performance issues, successful builds, and mixed feedback on functionality.

**Key Points:**
- GLM 4.7 flash FA fix for CUDA has been merged into llama.cpp
- Quantized cache performance issues reported
- Successful builds and functionality confirmed by some users
- Performance discrepancies noted on Pascal GPUs
- General feedback on model performance and behavior

**Discussion Highlights:** The discussion highlights mixed experiences with the new merge, including performance issues with quantized cache and discrepancies on Pascal GPUs, alongside successful builds and general feedback on model behavior.

---

## 31. [Fei Fei Li dropped a non-JEPA world model, and the spatial intelligence is insane](https://reddit.com/r/LocalLLaMA/comments/1qjjrmq/fei_fei_li_dropped_a_nonjepa_world_model_and_the/)

**Author:** u/coloradical5280 | **Upvotes:** 189 | **Comments:** 90 | **Date:** 2026-01-21

**Summary:** Fei-Fei Li's World Labs launched Marble, a generative world model using Neural Radiance Fields and Gaussian splatting, enabling fast, stateful 3D environment creation with VR support and export capabilities. The technology allows for persistent, editable worlds and collaborative building, though it has received mixed reactions from the community.

**Key Points:**
- Marble uses Neural Radiance Fields (NeRF) and Gaussian splatting for 3D world generation.
- It supports stateful, editable environments and collaborative building.
- The model is fast, generating explorable 3D worlds in minutes.
- Community reactions are mixed, with concerns about it not being open-source and its scope.
- Some users find the environments limited in size and scope.

**Discussion Highlights:** The discussion highlights mixed reactions, with some users criticizing the lack of open-source availability and the limited scope of the generated environments. Others express skepticism about the technology's novelty and impact given the funding and hype.

---

## 32. [Wrote a guide for running Claude Code with GLM-4.7 Flash locally with llama.cpp](https://reddit.com/r/LocalLLaMA/comments/1qjf6ys/wrote_a_guide_for_running_claude_code_with_glm47/)

**Author:** u/tammamtech | **Upvotes:** 117 | **Comments:** 45 | **Date:** 2026-01-21

**Summary:** The post provides a guide for running Claude Code with GLM-4.7 Flash locally using llama.cpp, including installation instructions and command examples for both direct and Docker setups. It highlights features like model swapping and GPU memory management.

**Key Points:**
- Guide for running Claude Code with GLM-4.7 Flash using llama.cpp
- Includes installation instructions and command examples
- Features like model swapping and GPU memory management are highlighted
- Discussion includes comments on implementation details and open-source alternatives
- Mentions performance metrics like VRAM usage and tokens per second

**Discussion Highlights:** The discussion includes comments on the implementation details, performance metrics, and suggestions for open-source alternatives like OpenCode and Harbor. There is also a mention of the Anthropic API endpoint implementation timeline.

---

## 33. [8x AMD MI50 32GB at 26 t/s (tg) with MiniMax-M2.1 and 15 t/s (tg) with GLM 4.7 (vllm-gfx906)](https://reddit.com/r/LocalLLaMA/comments/1qjaxfy/8x_amd_mi50_32gb_at_26_ts_tg_with_minimaxm21_and/)

**Author:** u/ai-infos | **Upvotes:** 318 | **Comments:** 128 | **Date:** 2026-01-21

**Summary:** The post details a cost-effective local inference setup using 8x AMD MI50 GPUs, achieving high token generation speeds with MiniMax-M2.1 and GLM 4.7 models. The setup is praised for its performance and affordability.

**Key Points:**
- MiniMax-M2.1 achieves 26.8 tokens/s output and 3000 tokens/s input with a context length of 196,608.
- GLM 4.7 achieves 15.6 tokens/s output and 3000 tokens/s input with a context length of 95,000.
- The total cost for 8 GPUs is $880, providing 256GB VRAM.
- Power draw is 280W idle and 1200W during inference.
- The setup is stable for long context use cases like coding agents.

**Discussion Highlights:** The community highly praises the setup for its cost-effectiveness and performance, with many expressing interest in replicating it. Some users note the difficulty in sourcing the GPUs at the mentioned price.

---

## 34. [VibeVoice-ASR released!](https://reddit.com/r/LocalLLaMA/comments/1qj40er/vibevoiceasr_released/)

**Author:** u/k_means_clusterfuck | **Upvotes:** 153 | **Comments:** 49 | **Date:** 2026-01-21

**Summary:** Microsoft released VibeVoice-ASR, a multilingual automatic speech recognition model with 9B parameters. Users report good quality and multilingual capabilities, though some note its large size and lack of benchmarks.

**Key Points:**
- VibeVoice-ASR is a new ASR model by Microsoft
- Model size is 9B parameters, which is relatively large
- Users report good quality and multilingual support
- Accuracy around 91% in Chinese audio tests
- Lack of benchmarks and comparison with other models like Whisper

**Discussion Highlights:** Users highlight the model's good quality and multilingual capabilities but express concerns about its large size and the absence of benchmarks. Some comparisons are made with other models like Whisper and Parakeet.

---

## 35. [One-shot single page web development: pacman clone - GLM 4.7 vs GLM 4.7 Flash vs GLM 4.5 Air vs Gemini 3 Pro vs Gemini 3 Flash - Results available for online testing - Prompt and instructions provided for testing with other models](https://reddit.com/r/LocalLLaMA/comments/1qj13uh/oneshot_single_page_web_development_pacman_clone/)

**Author:** u/ex-arman68 | **Upvotes:** 113 | **Comments:** 48 | **Date:** 2026-01-21

**Summary:** The Reddit post discusses a test comparing various AI models' ability to create a Pacman clone as a single webpage. GLM 4.7 emerged as the clear winner, followed by Minimax M2.1, with Gemini models performing less effectively than expected. Key points include GLM 4.7's top performance, Minimax M2.1's sound implementation, Gemini models' underperformance, the effectiveness of setting temperature to 0, and community discussions highlighting GLM 4.7's effectiveness and the usefulness of the testing methodology. The community was surprised by GLM 4.7's performance, with many praising the testing methodology and discussing the limitations of current AI models in terms of token capacity and memory.

---

## 36. [GLM-4.7-Flash-GGUF bug fix - redownload for better outputs](https://reddit.com/r/LocalLLaMA/comments/1qiy0ha/glm47flashgguf_bug_fix_redownload_for_better/)

**Author:** u/etherd0t | **Upvotes:** 112 | **Comments:** 58 | **Date:** 2026-01-21

**Summary:** The post announces a bug fix for the GLM-4.7-Flash-GGUF model, which previously caused looping and poor outputs. Users are advised to re-download the model for improved performance.

**Key Points:**
- Bug fix addresses looping and poor outputs
- Recommended parameters provided for general use and tool-calling
- Users report positive experiences with the fixed version
- Performance comparisons with other models mentioned

**Discussion Highlights:** Users express satisfaction with the bug fix, noting improved performance and usability. Some mention performance comparisons with other models.

---

## 37. [Fix for GLM 4.7 Flash has been merged into llama.cpp](https://reddit.com/r/LocalLLaMA/comments/1qiwm3c/fix_for_glm_47_flash_has_been_merged_into_llamacpp/)

**Author:** u/jacek2023 | **Upvotes:** 315 | **Comments:** 86 | **Date:** 2026-01-21

**Summary:** The post announces that a fix for GLM 4.7 Flash has been merged into llama.cpp, with ongoing work on CUDA support. The community discusses performance metrics and user experiences.

**Key Points:**
- Fix for GLM 4.7 Flash merged into llama.cpp
- CUDA support in progress
- Performance metrics shared for different quantizations and GPUs
- Community feedback on model improvements and issues
- Discussion on CPU-only performance

**Discussion Highlights:** Users share performance data for GLM 4.7, noting improvements in model intelligence and discussing prompt processing speeds. Some users inquire about CPU-only performance and the validity of existing GGUF files.

---

## 38. [Knowledge distillation with Claude as the interface: trained a 0.6B model to match GPT-class performance on Text2SQL in a singe conversation](https://reddit.com/r/LocalLLaMA/comments/1qiu6jo/knowledge_distillation_with_claude_as_the/)

**Author:** u/party-horse | **Upvotes:** 172 | **Comments:** 37 | **Date:** 2026-01-21

**Summary:** The post describes a workflow for training small, task-specific models using knowledge distillation via Claude and a teacher model (DeepSeek-V3). The approach simplifies the fine-tuning process and achieves significant performance improvements, as demonstrated by a Text2SQL task where the fine-tuned 0.6B model's accuracy improved from 36% to 74%.

**Key Points:**
- Small models often perform poorly on specialized tasks like Text2SQL.
- Knowledge distillation via Claude simplifies the fine-tuning process by automating data conversion, teacher evaluation, and training.
- The fine-tuned 0.6B model achieved a 74% accuracy on Text2SQL, a significant improvement over the base model's 36%.
- The approach was praised for its potential in training small models for on-device inference and understanding service/OS logs.
- Technical considerations include using SQL AST for validation and the flexibility to use open-source CLI tools.

**Discussion Highlights:** The discussion highlights positive feedback on the approach, with users noting its potential for training small models for local inference and understanding logs. Some technical suggestions include using SQL AST for validation and the flexibility to use open-source tools instead of Claude-specific code.

---

## 39. [vLLM v0.14.0 released](https://reddit.com/r/LocalLLaMA/comments/1qim0e9/vllm_v0140_released/)

**Author:** u/jinnyjuice | **Upvotes:** 172 | **Comments:** 36 | **Date:** 2026-01-20

**Summary:** The Reddit post announces the release of vLLM v0.14.0, highlighting new features and updates. Users discuss improvements like automatic context length fitting and the deprecation of certain quantization methods.

**Key Points:**
- Automatic context length fitting to GPU memory to prevent OOM failures
- Deprecation of some quantization methods, including HQQ
- Introduction of Marlin for Turing (sm75) as a major upgrade
- User interest in future sm120 optimizations

**Discussion Highlights:** Users expressed excitement about the automatic context length feature and discussed the implications of deprecated quantization methods. The Marlin upgrade for Turing was noted as a significant improvement, and there was anticipation for future optimizations.

---

## 40. [Current GLM-4.7-Flash implementation confirmed to be broken in llama.cpp](https://reddit.com/r/LocalLLaMA/comments/1qih9r8/current_glm47flash_implementation_confirmed_to_be/)

**Author:** u/Sweet_Albatross9772 | **Upvotes:** 240 | **Comments:** 60 | **Date:** 2026-01-20

**Summary:** The Reddit post discusses issues with the current GLM-4.7-Flash implementation in llama.cpp, highlighting significant differences in logprobs compared to vLLM, which may explain reported problems like looping and poor performance. A potential fix is already proposed in a pull request.

**Key Points:**
- Current GLM-4.7-Flash implementation in llama.cpp is confirmed broken.
- Significant differences in logprobs compared to vLLM may cause looping and poor performance.
- A potential fix is available in a pull request.
- Community acknowledges the issue and expects a resolution soon.
- Some users suggest waiting before using new models to avoid bugs.

**Discussion Highlights:** The community is aware of the issue and appreciates the open-source nature of the project. There is a consensus that the problem will be resolved shortly, with some users recommending patience before adopting new models.

---

## 41. [You have 64gb ram and 16gb VRAM; internet is permanently shut off: what 3 models are the ones you use?](https://reddit.com/r/LocalLLaMA/comments/1qids6a/you_have_64gb_ram_and_16gb_vram_internet_is/)

**Author:** u/Adventurous-Gold6413 | **Upvotes:** 554 | **Comments:** 306 | **Date:** 2026-01-20

**Summary:** The Reddit post discusses the best local models to use with 64GB RAM and 16GB VRAM when internet access is unavailable. The community highlights several models, with a focus on performance and versatility. Top comments suggest models like Gemma 3 27B, GLM 4.5 Air, and GPT-OSS 120B. GPT-OSS 120B is praised for its performance and versatility on the specified hardware. The discussion highlights a consensus around GPT-OSS 120B as a top choice due to its performance and fit for the given hardware. Other models like Gemma 3 27B and GLM 4.5 Air are also recommended. The community shows appreciation for the post and active participation in the discussion.

---

## 42. [Liquid AI released the best thinking Language Model Under 1GB](https://reddit.com/r/LocalLLaMA/comments/1qi512t/liquid_ai_released_the_best_thinking_language/)

**Author:** u/PauLabartaBajo | **Upvotes:** 234 | **Comments:** 53 | **Date:** 2026-01-20

**Summary:** Liquid AI released LFM2.5-1.2B-Thinking, a compact reasoning model that runs on-device with 900 MB of memory, excelling in math, tool use, and instruction following. It outperforms larger models in speed and efficiency, with broad ecosystem support.

**Key Points:**
- LFM2.5-1.2B-Thinking is optimized for on-device reasoning with low memory usage.
- It generates internal thinking traces for systematic problem-solving.
- The model matches or exceeds Qwen3-1.7B in benchmarks despite fewer parameters.
- Concerns raised about memory requirements and quantization for edge deployment.
- Criticism over non-Apache/MIT licensing and desire for larger models.

**Discussion Highlights:** The discussion highlights concerns about memory requirements and quantization for edge deployment, with some users questioning the practicality of the model's size. There is also criticism regarding the licensing model and a desire for larger, more capable models for real-world applications.

---

## 43. [768Gb Fully Enclosed 10x GPU Mobile AI Build](https://reddit.com/r/LocalLLaMA/comments/1qi4uj2/768gb_fully_enclosed_10x_gpu_mobile_ai_build/)

**Author:** u/SweetHomeAbalama0 | **Upvotes:** 917 | **Comments:** 273 | **Date:** 2026-01-20

**Summary:** The post describes a custom-built, high-performance AI system designed for running large MoE models and supporting graphic design tasks. The system features a Threadripper Pro 3995WX, 512GB DDR4, 10 GPUs (8x 3090 + 2x 5090), and is enclosed in a Thermaltake Core W200 case for mobility and protection. The total cost was approximately $17k, balancing performance and budget constraints.

**Key Points:**
- The system is designed for large MoE models and graphic design tasks.
- It features a Threadripper Pro 3995WX, 512GB DDR4, and 10 GPUs (8x 3090 + 2x 5090).
- The enclosure (Thermaltake Core W200) ensures mobility and protection from pets.
- The total cost was around $17k, balancing performance and budget.
- The post received significant engagement with 917 upvotes and 273 comments.

**Discussion Highlights:** The discussion highlights include humorous comments about the system's portability and power requirements, as well as appreciation for the innovative enclosure solution. The top comments reflect a mix of admiration for the build and playful remarks about its practicality.

---

## 44. [Over 6K novels with reasoning traces to train full book writing LLMs](https://reddit.com/r/LocalLLaMA/comments/1qi3nmd/over_6k_novels_with_reasoning_traces_to_train/)

**Author:** u/XMasterDE | **Upvotes:** 111 | **Comments:** 46 | **Date:** 2026-01-20

**Summary:** The post announces an update to the LongPage dataset, expanding it to over 6,000 novels with hierarchical planning traces for training full-book writing LLMs. The team is also developing a full-book writing model, with plans to release it once quality standards are met.

**Key Points:**
- LongPage dataset expanded to 6K+ novels with hierarchical planning traces
- Dataset supports training full-book writing LLMs
- Team is developing a full-book writing model for future release
- Community shows strong interest and requests for more details
- Inquiries about dataset content and code availability for other languages

**Discussion Highlights:** The community is eager to see the results, with requests for more details on how the dataset works and whether it includes specific works like 'Worm by Wildbow.' There is also interest in accessing the code for data processing to create datasets in other languages.

---

## 45. [glm-4.7-flash has the best thinking process with clear steps, I love it](https://reddit.com/r/LocalLLaMA/comments/1qhxlgy/glm47flash_has_the_best_thinking_process_with/)

**Author:** u/uptonking | **Upvotes:** 142 | **Comments:** 34 | **Date:** 2026-01-20

**Summary:** The Reddit post discusses the user's experience with the glm-4.7-flash model, highlighting its structured thinking process and comparing it favorably to other models like nemotron-nano and qwen3-30b. The user appreciates the model's clear reasoning steps but notes its slow performance and occasional looping issues. Key points include the model's detailed thinking process, slower performance compared to nemotron-nano, user appreciation for its logical reasoning, occasional looping issues, and suggestions to adjust parameters for better performance. The discussion highlights a consensus on the model's superior reasoning process, with concerns about its speed and occasional looping issues, and suggestions to adjust parameters to improve performance.

---

## 46. [It's been one year since the release of Deepseek-R1](https://reddit.com/r/LocalLLaMA/comments/1qhs2sd/its_been_one_year_since_the_release_of_deepseekr1/)

**Author:** u/Recoil42 | **Upvotes:** 310 | **Comments:** 52 | **Date:** 2026-01-19

**Summary:** The Reddit post commemorates the one-year anniversary of the Deepseek-R1 release, highlighting its significant impact on the AI community, including its influence on major players like Meta and the rapid pace of advancements in the field.

**Key Points:**
- Deepseek-R1 had a major impact, reportedly causing Meta to disband its flagship AI training team and reassess its strategy.
- The release is considered one of the most significant in AI history, second only to the original Llama release.
- The rapid pace of AI advancements is noted, with the past year feeling much longer due to the volume of changes.
- Deepseek-R1 forced other models to expose reasoning output and slashed prices, reshaping the AI landscape.
- There is curiosity about how current smaller models compare to R1 in performance and size.

**Discussion Highlights:** The discussion highlights the transformative impact of Deepseek-R1 on the AI industry, with users emphasizing its role in reshaping strategies, pricing, and transparency in AI development. The consensus is that Deepseek-R1 was a pivotal release that accelerated progress and competition in the field.

---

