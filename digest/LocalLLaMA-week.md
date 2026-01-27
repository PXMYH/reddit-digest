# r/LocalLLaMA Reading Digest

**Period:** 2026-01-27 to 2026-01-27
**Posts Summarized:** 48
**Total Posts Analyzed:** 49

---

## 1. [Introducing Kimi K2.5, Open-Source Visual Agentic Intelligence](https://reddit.com/r/LocalLLaMA/comments/1qo595n/introducing_kimi_k25_opensource_visual_agentic/)

**Author:** u/Kimi_Moonshot | **Upvotes:** 229 | **Comments:** 51 | **Date:** 2026-01-26

**Summary:** The post introduces Kimi K2.5, an open-source visual agentic intelligence model with state-of-the-art performance on various benchmarks, including agentic, vision, and coding tasks. It features capabilities like turning chats and media into aesthetic websites and supports agent swarms with up to 100 sub-agents. The model is available for use and download via provided links.

**Key Points:**
- Kimi K2.5 achieves global SOTA on agentic benchmarks (HLE: 50.2%, BrowseComp: 74.9%) and open-source SOTA on vision and coding benchmarks (MMMU Pro: 78.5%, VideoMMMU: 86.6%, SWE-bench Verified: 76.8%).
- Features 'Code with Taste' for creating aesthetic websites from chats, images, and videos, and supports agent swarms with up to 100 sub-agents.
- Available in chat and agent modes on kimi.com, with beta access for agent swarms and integration with Kimi Code for production-grade coding.
- Open-source weights and code are available on Hugging Face, with additional resources like API and tech blog provided.
- User discussions highlight excitement about the 100 sub-agents feature and curiosity about the model's capabilities, along with some skepticism and technical exploration.

**Discussion Highlights:** Users expressed excitement about the 100 sub-agents working in parallel, with one comment calling it 'bonkers' and another user planning to test it for coding tasks. There was also curiosity about the model's parameters (1T Activated Parameters, 32B) and some skepticism about the account's legitimacy. A user shared a quick test result of generating an SVG of a fox.

---

## 2. [Jan v3 Instruct: a 4B coding Model with +40% Aider Improvement](https://reddit.com/r/LocalLLaMA/comments/1qo3ri5/jan_v3_instruct_a_4b_coding_model_with_40_aider/)

**Author:** u/Delicious_Focus3465 | **Upvotes:** 178 | **Comments:** 30 | **Date:** 2026-01-26

**Summary:** The Jan team released Jan-v3-4B-base-instruct, a 4B-parameter model with improved math and coding performance, suitable for lightweight assistance and further fine-tuning. The model is available via Jan Desktop and Hugging Face, with future releases including Jan-Code and a 30B model family.

**Key Points:**
- Jan-v3-4B-base-instruct is a 4B-parameter model with improved math and coding capabilities.
- The model is available for download via Jan Desktop and Hugging Face.
- Future releases include Jan-Code, Jan-v3-Search-4B, and a 30B model family.
- Recommended parameters for the model are temperature: 0.7, top_p: 0.8, and top_k: 20.
- Community feedback highlights the model's performance and potential for fine-tuning.

**Discussion Highlights:** The community is excited about the release, with discussions focusing on the model's performance, potential for fine-tuning, and comparisons with other models like Qwen 4B. Some users have tested the model and provided mixed feedback on its capabilities.

---

## 3. [deepseek-ai/DeepSeek-OCR-2 · Hugging Face](https://reddit.com/r/LocalLLaMA/comments/1qo349m/deepseekaideepseekocr2_hugging_face/)

**Author:** u/Dark_Fire_12 | **Upvotes:** 243 | **Comments:** 26 | **Date:** 2026-01-26

**Summary:** The Reddit post discusses DeepSeek-OCR-2, an OCR model, with users sharing resources, comparisons, and a demo link.

**Key Points:**
- Post links to DeepSeek-OCR-2 on Hugging Face
- Top comments highlight self-thank humor and comparison with PaddleOCR-VL
- GitHub and paper links provided
- Demo link shared for testing the model

**Discussion Highlights:** The community shows engagement with the model, sharing resources and comparisons, indicating interest and practical exploration.

---

## 4. [GLM 4.7 Flash: Huge performance improvement with -kvu](https://reddit.com/r/LocalLLaMA/comments/1qnwa33/glm_47_flash_huge_performance_improvement_with_kvu/)

**Author:** u/TokenRingAI | **Upvotes:** 153 | **Comments:** 58 | **Date:** 2026-01-26

**Summary:** The Reddit post highlights a significant performance improvement in GLM 4.7 Flash when using the -kvu flag in llama.cpp, increasing token generation speed from 17.7t/s to 100t/s on an RTX 6000. The post also showcases a Zelda game created by the model. Key points include the performance boost, the Zelda game creation, and discussions about the -kvu option being automatic in newer llama.cpp versions. The discussion emphasizes the substantial performance gains and the model's capabilities.

---

## 5. [Kimi K2.5 Released !](https://reddit.com/r/LocalLLaMA/comments/1qnw3z6/kimi_k25_released/)

**Author:** u/External_Mood4719 | **Upvotes:** 124 | **Comments:** 34 | **Date:** 2026-01-26

**Summary:** The Reddit post announces the release of Kimi K2.5, a new model that may not yet be open-source. Users discuss its performance, potential release timing, and availability on platforms like Hugging Face.

**Key Points:**
- Kimi K2.5 has been released but may not be open-source yet.
- The model is in a testing phase with no official announcement on the website.
- Users report it performs close to GPT-5, making it a strong open model.
- The release timing may be influenced by the upcoming Chinese New Year.
- The model is available on Hugging Face and mentioned in Kimi Code Docs.

**Discussion Highlights:** Users are excited about the model's performance and potential open-source release. There is speculation about the timing of releases due to the upcoming holidays. Some users note the model's availability on Hugging Face and its mention in official documentation.

---

## 6. [transformers v5 final is out 🔥](https://reddit.com/r/LocalLLaMA/comments/1qnk7fq/transformers_v5_final_is_out/)

**Author:** u/unofficialmerve | **Upvotes:** 398 | **Comments:** 41 | **Date:** 2026-01-26

**Summary:** Hugging Face has released transformers v5 with significant performance improvements, especially for Mixture-of-Experts models, and a simplified API. The release includes a migration guide and encourages user feedback.

**Key Points:**
- Performance improvements for Mixture-of-Experts (6x-11x speedups)
- Simplified API with explicit backends and better performance
- Dynamic weight loading for faster operations and compatibility with quants, tp, and PEFT
- Migration guide and release notes available for user reference
- User queries about the impact on local MoE model performance

**Discussion Highlights:** Users are interested in understanding the performance improvements, particularly for local MoE model execution, and seeking clarification on the practical implications of the updates.

---

## 7. [I tracked GPU prices across 25 cloud providers and the price differences are insane (V100: $0.05/hr vs $3.06/hr)](https://reddit.com/r/LocalLLaMA/comments/1qnjsvz/i_tracked_gpu_prices_across_25_cloud_providers/)

**Author:** u/sleepingpirates | **Upvotes:** 163 | **Comments:** 26 | **Date:** 2026-01-26

**Summary:** The Reddit post highlights significant price variations for GPU rentals across 25 cloud providers, with some GPUs showing up to a 61x price difference. The author created a tool to compare real-time pricing and shared findings for models like H100, A100, V100, and RTX 4090.

**Key Points:**
- Price differences for identical GPUs can be extreme (e.g., 61x for V100).
- VERDA consistently offers the lowest prices across multiple GPU models.
- The tool tracks 783 GPU offers from 25 providers, allowing filtering by model, VRAM, region, and pricing type.
- Discussion highlights include the need for better filtering (e.g., spot vs. on-demand) and concerns about availability.
- Some users question the practicality of cloud GPUs due to ISP limitations.

**Discussion Highlights:** Users discussed the importance of filtering options (e.g., spot vs. on-demand) and raised concerns about availability and hidden costs like traffic pricing. There was also a debate about the practicality of cloud GPUs for certain use cases.

---

## 8. [I built a "hive mind" for Claude Code - 7 agents sharing memory and talking to each other](https://reddit.com/r/LocalLLaMA/comments/1qnjota/i_built_a_hive_mind_for_claude_code_7_agents/)

**Author:** u/Historical-Celery-83 | **Upvotes:** 301 | **Comments:** 50 | **Date:** 2026-01-26

**Summary:** The author built a multi-agent system called 'hive mind' for Claude Code, consisting of 7 specialized agents that share memory and communicate via a message bus. The system uses SQLite for persistent memory and is designed to coordinate tasks intelligently, though debugging multiple agents can be challenging.

**Key Points:**
- The system includes 7 agent types with different roles and capabilities.
- It uses SQLite with FTS5 for persistent memory and a message bus for communication.
- Debugging multiple agents can lead to issues like infinite loops.
- The project is open-source and licensed under MIT.
- Discussion highlights include comparisons to other multi-agent methods and general feedback on the approach.

**Discussion Highlights:** The discussion includes comparisons to other multi-agent methods like BMAD and Microsoft's solutions, as well as general feedback on the approach and its potential benefits and challenges.

---

## 9. [216GB VRAM on the bench. Time to see which combination is best for Local LLM](https://reddit.com/r/LocalLLaMA/comments/1qni356/216gb_vram_on_the_bench_time_to_see_which/)

**Author:** u/eso_logic | **Upvotes:** 350 | **Comments:** 96 | **Date:** 2026-01-26

**Summary:** The post discusses benchmarking secondhand Tesla GPUs for Local LLM performance, comparing their efficiency against modern devices when parallelized. The author has developed a benchmarking suite to quantitatively evaluate these GPUs.

**Key Points:**
- Secondhand Tesla GPUs offer high VRAM at low cost.
- Performance of older GPUs in parallelized setups is being evaluated.
- Cooling and noise are significant concerns with older GPUs.
- Prompt processing speed is a critical factor for usability.
- Some older GPUs lack support or have limited capabilities.

**Discussion Highlights:** The discussion highlights concerns about usability, cooling, and noise levels of older GPUs. There is a consensus that while these GPUs may offer cost-effective VRAM, their performance in prompt processing and overall usability may be limited compared to modern alternatives.

---

## 10. [Minimax Is Teasing M2.2](https://reddit.com/r/LocalLLaMA/comments/1qnfegx/minimax_is_teasing_m22/)

**Author:** u/Few_Painter_5588 | **Upvotes:** 193 | **Comments:** 60 | **Date:** 2026-01-26

**Summary:** The Reddit post discusses upcoming AI model releases from Chinese labs in February, including Deepseek v4, Kimi K3, and MiniMax M2.2, with speculation about ByteDance's potential model. Users express excitement and compare these models with existing ones like GLM 4.7.

**Key Points:**
- Multiple Chinese AI labs are expected to release new models in February.
- Models mentioned include Deepseek v4, Kimi K3, MiniMax M2.2, and a potential ByteDance model.
- Users are enthusiastic about the potential improvements in these models.
- Comparisons are made with existing models like GLM 4.7 and Qwen.
- There is speculation about the future of 32B models and updates to existing ones like Qwen.

**Discussion Highlights:** Users are excited about the upcoming releases, with some expressing a preference for MiniMax models even at high quantization levels. There is also discussion about the potential impact of these new models on the AI landscape and comparisons with existing models.

---

## 11. [I just won an Nvidia DGX Spark GB10 at an Nvidia hackathon. What do I do with it?](https://reddit.com/r/LocalLLaMA/comments/1qn3xig/i_just_won_an_nvidia_dgx_spark_gb10_at_an_nvidia/)

**Author:** u/brandon-i | **Upvotes:** 494 | **Comments:** 151 | **Date:** 2026-01-25

**Summary:** The author won an Nvidia DGX Spark GB10 at a hackathon and seeks advice on how to use it, mentioning potential for running multiple NextJS applications and sharing a blog post about their project.

**Key Points:**
- Author is new to fine-tuning models
- Previously used the system for inferencing with a large model
- Potential to run multiple NextJS applications
- Shared a blog post about their hackathon project
- Top comments suggest running multiple apps, exploring Nvidia playbooks, and humorous advice to sell the hardware

**Discussion Highlights:** The discussion highlights include suggestions to run multiple NextJS applications, explore Nvidia's playbooks for guidance, and a humorous comment about selling the hardware for DDR5 memory.

---

## 12. [GLM-4.7-Flash is even faster now](https://reddit.com/r/LocalLLaMA/comments/1qmvny5/glm47flash_is_even_faster_now/)

**Author:** u/jacek2023 | **Upvotes:** 262 | **Comments:** 96 | **Date:** 2026-01-25

**Summary:** The post announces an update to GLM-4.7-Flash, highlighting its increased speed. The discussion includes reactions and additional context from the community.

**Key Points:**
- GLM-4.7-Flash has received a speed improvement
- The post was featured on Discord and the author received a special flair
- Community reactions include appreciation and humor
- An image link is provided in one of the top comments

**Discussion Highlights:** The community shows positive engagement with the update, including humor and appreciation. The post gained significant attention, as indicated by the upvotes and comments.

---

## 13. [Internet blackout and Local LLMs](https://reddit.com/r/LocalLLaMA/comments/1qmlpjp/internet_blackout_and_local_llms/)

**Author:** u/DunderSunder | **Upvotes:** 253 | **Comments:** 74 | **Date:** 2026-01-25

**Summary:** The post discusses the severe internet blackout in Iran, where only a few websites like Google and ChatGPT are whitelisted. The author highlights the importance of local LLMs like Gemma3 and Qwen3 in circumventing censorship and accessing uncensored information.

**Key Points:**
- Severe internet blackout in Iran with only a few websites whitelisted
- Local LLMs like Gemma3 and Qwen3 are crucial for accessing uncensored information
- Cloud-based AI services like ChatGPT are limited in helping circumvent censorship
- Concerns about data sharing with intelligence agencies by cloud-based AI services
- Alternative solutions like downloading Wikipedia are suggested for reliable information

**Discussion Highlights:** The discussion highlights the importance of local LLMs in bypassing censorship and the limitations of cloud-based AI services. There is a consensus on the need for reliable, uncensored information sources and skepticism towards the effectiveness and privacy of cloud-based AI services.

---

## 14. [KV cache fix for GLM 4.7 Flash](https://reddit.com/r/LocalLLaMA/comments/1qmjzx1/kv_cache_fix_for_glm_47_flash/)

**Author:** u/jacek2023 | **Upvotes:** 244 | **Comments:** 70 | **Date:** 2026-01-25

**Summary:** The post discusses a fix for the KV cache in GLM 4.7 Flash, which significantly reduces VRAM usage by removing unnecessary components, allowing for longer context lengths on the same hardware setup.

**Key Points:**
- Removing 'Air' from GLM 4.7 Flash optimizes KV cache usage.
- This fix saves gigabytes of VRAM, enabling longer context lengths.
- Users report significant improvements, such as doubling context length on the same hardware.
- The model is still considered somewhat quirky but functional.
- The community is actively working on further optimizations.

**Discussion Highlights:** The community is enthusiastic about the improvements, with users reporting substantial gains in context length. There is ongoing work to further optimize the model, and the post has gained significant attention and recognition within the community.

---

## 15. [What do you actually want from a private AI chat on your phone?](https://reddit.com/r/LocalLLaMA/comments/1qmir5d/what_do_you_actually_want_from_a_private_ai_chat/)

**Author:** u/AppDeveloperAsdf | **Upvotes:** 224 | **Comments:** 82 | **Date:** 2026-01-25

**Summary:** The post discusses the development of zerotap, an Android app that allows AI to control a phone like a human. The author seeks feedback on future features and asks what would make a private AI chat useful on a daily basis.

**Key Points:**
- The app supports various AI models and can take over device control when needed.
- Future features under consideration include MCP servers, deep research, multi-modality, and on-device models.
- Users emphasize the importance of open-source software for an app with such extensive control over their devices.
- Concerns about privacy and security are prominent in the discussion.
- Suggestions for improvement include better UI, offline functionality, and clear purpose definition.

**Discussion Highlights:** The discussion highlights a strong preference for open-source solutions and concerns about privacy and security. Users suggest focusing on practical, daily-use features and improving the user interface.

---

## 16. [[Release] Qwen3-TTS: Ultra-Low Latency (97ms), Voice Cloning &amp; OpenAI-Compatible API](https://reddit.com/r/LocalLLaMA/comments/1qlzbhh/release_qwen3tts_ultralow_latency_97ms_voice/)

**Author:** u/blackstoreonline | **Upvotes:** 298 | **Comments:** 128 | **Date:** 2026-01-24

**Summary:** The post introduces Qwen3-TTS, an ultra-low latency (97ms) text-to-speech model with voice cloning and OpenAI-compatible API, offering high-quality local speech synthesis. It supports multiple languages and provides easy integration with existing applications.

**Key Points:**
- Ultra-low latency of ~97ms for streaming
- Supports natural language instructions for voice control
- Voice cloning with a 3-second reference clip
- OpenAI-compatible API for easy integration
- Multilingual support for 10+ languages

**Discussion Highlights:** Users are impressed with the low latency and voice cloning capabilities. Some technical issues were noted, such as Dockerfile compatibility with Blackwell GPUs and the lack of streaming support in the published code. Overall, the community is excited about the potential of Qwen3-TTS.

---

## 17. [Artificial Analysis: South Korea 🇰🇷 is now the clear #3 nation in AI — powered by the Korean National Sovereign AI Initiative there are now multiple Korean AI labs with near frontier intelligence.](https://reddit.com/r/LocalLLaMA/comments/1qltwza/artificial_analysis_south_korea_is_now_the_clear/)

**Author:** u/self-fix | **Upvotes:** 178 | **Comments:** 54 | **Date:** 2026-01-24

**Summary:** South Korea has emerged as a leading nation in AI, driven by the Korean National Sovereign AI Initiative. This government-backed competition has shortlisted top AI labs like LG, SK Telecom, and Upstage, fostering the development of advanced AI models such as K-EXAONE and Solar Open.

**Key Points:**
- South Korea is now the clear #3 nation in AI, powered by the Korean National Sovereign AI Initiative.
- The initiative shortlists national champions, with winners receiving government funding and GPU access.
- Top Korean AI models include LG's K-EXAONE (236B) and Upstage's Solar Open (100B).
- The discussion highlights skepticism about South Korea's ranking and interest in specific models.

**Discussion Highlights:** The discussion includes skepticism about South Korea's ranking, with comments questioning the absence of other countries like Canada and France. There is also interest in specific Korean AI models and their performance.

---

## 18. [I built an open-source audiobook converter using Qwen3 TTS - converts PDFs/EPUBs to high-quality audiobooks with voice cloning support](https://reddit.com/r/LocalLLaMA/comments/1qlr3wj/i_built_an_opensource_audiobook_converter_using/)

**Author:** u/TheyCallMeDozer | **Upvotes:** 132 | **Comments:** 45 | **Date:** 2026-01-24

**Summary:** The post introduces an open-source tool that converts various document formats (PDF, EPUB, DOCX, TXT) into high-quality audiobooks using Qwen3 TTS, featuring voice cloning and custom voice modes. The tool is designed to be user-friendly with features like smart chunking, intelligent caching, and progress tracking.

**Key Points:**
- Converts multiple document formats to audiobooks using Qwen3 TTS
- Offers custom voice modes and voice cloning capabilities
- Includes features like smart chunking, caching, and progress tracking
- Open-source and free alternative to expensive audiobook services
- Processing speed is ~4-5 minutes per chunk with high-quality output

**Discussion Highlights:** The discussion highlights requests for audio examples, comparisons with other tools like Chatterbox and Vibevoice, and inquiries about GUI support and VRAM requirements. Users also expressed interest in custom pauses and breaks in the audio output.

---

## 19. [Personal experience with GLM 4.7 Flash Q6 (unsloth) + Roo Code + RTX 5090](https://reddit.com/r/LocalLLaMA/comments/1qlnruw/personal_experience_with_glm_47_flash_q6_unsloth/)

**Author:** u/Septerium | **Upvotes:** 167 | **Comments:** 92 | **Date:** 2026-01-24

**Summary:** The post discusses the user's positive experience with GLM 4.7 Flash for refactoring tasks, highlighting its reliability and precision compared to other models like GPT-OSS 120b and GLM 4.5 Air. The user shares technical details of their setup, including the use of an RTX 5090 and specific llama.cpp command parameters.

**Key Points:**
- GLM 4.7 Flash performs well in refactoring tasks and handles Roo Code effectively.
- The model is more reliable and precise than GPT-OSS 120b, GLM 4.5 Air, or Devstral 24b.
- User achieved 150 tok/s with 48k context size on an RTX 5090 using specific llama.cpp parameters.
- Discussion highlights include tool call success, model performance in OpenCode harness, and command optimizations.
- Some users suggest that certain llama.cpp parameters are now default and unnecessary to specify.

**Discussion Highlights:** The discussion includes questions about tool call success with the given temperature setting, positive feedback on the model's performance in the OpenCode harness, and suggestions for optimizing the llama.cpp command by removing redundant parameters.

---

## 20. [GLM-4.7-Flash-REAP on RTX 5060 Ti 16 GB - 200k context window!](https://reddit.com/r/LocalLLaMA/comments/1qlanzn/glm47flashreap_on_rtx_5060_ti_16_gb_200k_context/)

**Author:** u/bobaburger | **Upvotes:** 208 | **Comments:** 95 | **Date:** 2026-01-23

**Summary:** The post discusses the performance of the GLM-4.7-Flash-REAP model on an RTX 5060 Ti 16 GB setup, highlighting its speed and context window capabilities. The author tests different context window sizes (16k, 64k, 100k, and 200k) and notes performance trade-offs, including speed and resource usage. The discussion includes feedback on performance comparisons and the potential for local high-quality agents with large context windows.

**Key Points:**
- The model performs well with smaller context windows (16k and 64k) but faces issues with larger ones (100k and 200k).
- Speed and resource usage vary significantly with context window size, with 200k context being nearly unusable without optimizations.
- The 'Force Model Expert Weight onto CPU' feature in LM Studio improves performance for larger context windows.
- Discussion highlights include comparisons with other models and the potential for local high-quality agents.
- The post received positive engagement, with comments noting room for improvement and performance comparisons.

**Discussion Highlights:** The discussion includes comparisons with other models like Qwen 3 and feedback on the model's performance. Users highlight the potential for local high-quality agents with large context windows and note that further optimizations are possible.

---

## 21. [Built a 100% client-side AI that plays Pokemon Red - Qwen 2.5 1.5B via WebLLM + neural network policy .   Fork/check it out! BYOR](https://reddit.com/r/LocalLLaMA/comments/1ql6cz7/built_a_100_clientside_ai_that_plays_pokemon_red/)

**Author:** u/Efficient-Proof-1824 | **Upvotes:** 269 | **Comments:** 30 | **Date:** 2026-01-23

**Summary:** The author built a client-side AI using Qwen 2.5 1.5B via WebLLM and a neural network policy to play Pokemon Red. The project is deployed as a Svelte app on GitHub Pages, with the goal of creating an agent that can beat the game.

**Key Points:**
- Uses Qwen 2.5 1.5B LLM via WebLLM for action plan generation
- Employs a TensorFlow.js neural network for scoring actions
- Deployed as a Svelte app on GitHub Pages
- Community shows interest in expanding to larger models and additional features
- Potential applications include farming and training in-game

**Discussion Highlights:** The community appreciates the project, with suggestions to integrate larger models and additional features like audio output. There is enthusiasm for potential applications such as in-game farming and training.

---

## 22. [Your post is getting popular and we just featured it on our Discord!](https://reddit.com/r/LocalLLaMA/comments/1qkyex0/your_post_is_getting_popular_and_we_just_featured/)

**Author:** u/roculus | **Upvotes:** 569 | **Comments:** 57 | **Date:** 2026-01-23

**Summary:** The Reddit post announces that a user's post is popular and has been featured on Discord, with the user receiving a special flair. The community expresses annoyance at the bot's public posts, suggesting private messages instead.

**Key Points:**
- The bot announces the popularity of a user's post and its feature on Discord.
- The user receives a special flair for their contribution.
- The community finds the bot's public posts annoying and suggests private messages.
- There is a pinned thread about the Discord that has been active for months.
- Some users suspect the moderators are trying to monetize the community.

**Discussion Highlights:** The community consensus is that the bot's public posts are annoying and should be sent as private messages instead. There is also suspicion about monetization efforts by the moderators.

---

## 23. [Sweep: Open-weights 1.5B model for next-edit autocomplete](https://reddit.com/r/LocalLLaMA/comments/1qkxuv1/sweep_openweights_15b_model_for_nextedit/)

**Author:** u/Kevinlu1248 | **Upvotes:** 112 | **Comments:** 29 | **Date:** 2026-01-23

**Summary:** The post introduces Sweep, a 1.5B parameter open-source model for next-edit autocomplete in code, which outperforms larger models in speed and accuracy. It uses recent edits as context and is available via Hugging Face or a JetBrains plugin.

**Key Points:**
- Sweep is a 1.5B parameter model for next-edit autocomplete, using recent edits as context.
- The model outperforms larger models in speed and accuracy and can run locally.
- Prompt format and RL training were crucial for improving performance.
- The model is open-source and available for integration with various editors.
- Discussion highlights include enthusiasm for the tool and requests for broader editor support.

**Discussion Highlights:** The discussion shows enthusiasm for the tool, with users appreciating its availability and expressing interest in broader editor support, including Emacs, Vim, and mobile platforms.

---

## 24. [The 'Infinite Context' Trap: Why 1M tokens won't solve Agentic Amnesia (and why we need a Memory OS)](https://reddit.com/r/LocalLLaMA/comments/1qkrhec/the_infinite_context_trap_why_1m_tokens_wont/)

**Author:** u/Sweet121 | **Upvotes:** 173 | **Comments:** 41 | **Date:** 2026-01-23

**Summary:** The post argues that large context windows (e.g., 1M tokens) are inefficient for AI memory, comparing it to treating RAM as a hard drive. It proposes a 'Memory OS' (MemOS) to manage memory lifecycle (consolidate, evolve, forget) and efficiently pre-load relevant information.

**Key Points:**
- Large context windows are inefficient for AI memory management
- Memory OS (MemOS) is proposed as a solution with lifecycle management
- MemOS includes features like Next-Scene Prediction and memory states
- Critics question if MemOS is just a wrapper around existing tools like LangChain
- Discussion highlights the need for relevance and salience in memory retrieval

**Discussion Highlights:** The discussion includes skepticism about the novelty of MemOS, with some viewing it as an overcomplication of existing RAG systems. Others agree that large context windows are not a solution and emphasize the importance of attention and salience in memory retrieval.

---

## 25. [A full AI powered cooking game, where literally any ingredient is possible with infinite combinations.](https://reddit.com/r/LocalLLaMA/comments/1qkqjer/a_full_ai_powered_cooking_game_where_literally/)

**Author:** u/VirtualJamesHarrison | **Upvotes:** 117 | **Comments:** 33 | **Date:** 2026-01-23

**Summary:** The post introduces 'Infinite Kitchen', an AI-powered cooking game built with Claude Code, Gemini, and Flux, allowing infinite ingredient combinations. Users can try it at https://infinite-kitchen.com/kitchen. The discussion highlights both praise for the concept and critiques about gameplay mechanics and technical limitations.

**Key Points:**
- Game built with Claude Code, Gemini, and Flux
- Allows infinite ingredient combinations
- Critiques about gameplay mechanics (e.g., cutting tomatoes twice, cooking chicken without preparation)
- Technical limitations (e.g., requires larger screen)
- Discussion about the simplicity of the underlying algorithm

**Discussion Highlights:** The discussion includes praise for the innovative concept and critiques about gameplay mechanics and technical limitations. Some users question the necessity of using AI for what could be a simple recipe database, while others are impressed by the live asset generation.

---

## 26. [Llama.cpp merges in OpenAI Responses API Support](https://reddit.com/r/LocalLLaMA/comments/1qkm9zb/llamacpp_merges_in_openai_responses_api_support/)

**Author:** u/SemaMod | **Upvotes:** 156 | **Comments:** 44 | **Date:** 2026-01-23

**Summary:** The post discusses the successful integration of OpenAI Responses API support in llama.cpp, highlighting its effectiveness with GLM-4.7-Flash and Codex CLI for exploring large codebases.

**Key Points:**
- OpenAI Responses API support has been merged into llama.cpp
- The integration works well with GLM-4.7-Flash and Codex CLI
- The API enables stateful interactions, such as accessing and managing previous messages
- Users appreciate the new feature but want the old API to remain functional
- Some users are still unclear about the full capabilities of the Responses API

**Discussion Highlights:** The discussion highlights a general appreciation for the new API support, with some concerns about the future of the old API. Users are exploring the new features and sharing their experiences, with a few expressing confusion about the full scope of the Responses API.

---

## 27. [OpenAI CFO hinting at "Outcome-Based Pricing" (aka royalties on your work)? Makes the case for local even stronger.](https://reddit.com/r/LocalLLaMA/comments/1qkiylw/openai_cfo_hinting_at_outcomebased_pricing_aka/)

**Author:** u/distalx | **Upvotes:** 232 | **Comments:** 98 | **Date:** 2026-01-23

**Summary:** The Reddit post discusses OpenAI's potential shift to 'Outcome-Based Pricing' for high-value enterprise deals, clarifying that it does not apply to regular users or indie developers. The author initially misunderstood the scope but corrected it after finding the primary source. Key points include: OpenAI's CFO mentioned 'Outcome-Based Pricing' for enterprise deals, not regular users; the pricing model involves sharing value created in high-value industries like pharmaceuticals; the post highlights the importance of local AI stacks to avoid dependency on cloud APIs with changing terms; top comments emphasize concerns about data usage and the benefits of self-hosting AI models; the discussion reflects a consensus on the importance of controlling AI infrastructure to avoid unexpected costs. The discussion highlights concerns about OpenAI's potential pricing changes and the benefits of self-hosting AI models. Users emphasize the importance of controlling AI infrastructure to avoid dependency on cloud APIs with changing terms.

---

## 28. [Nvidia Introduces PersonaPlex: An Open-Source, Real-Time Conversational AI Voice](https://reddit.com/r/LocalLLaMA/comments/1qkimzg/nvidia_introduces_personaplex_an_opensource/)

**Author:** u/44th--Hokage | **Upvotes:** 241 | **Comments:** 30 | **Date:** 2026-01-22

**Summary:** Nvidia has introduced PersonaPlex, an open-source, real-time conversational AI voice model that enables persona control through text-based role prompts and audio-based voice conditioning. It is trained on synthetic and real conversations to produce natural, low-latency spoken interactions.

**Key Points:**
- PersonaPlex is a real-time, full-duplex speech-to-speech conversational model.
- It enables persona control through text-based role prompts and audio-based voice conditioning.
- The model is trained on a combination of synthetic and real conversations.
- It requires significant VRAM (96GB) for optimal performance.
- Some users have noted concerns about audio quality and model performance.

**Discussion Highlights:** Users have expressed mixed reactions, with some highlighting the high VRAM requirements and others noting concerns about audio quality and model performance. There is also curiosity about how the model will handle tool calls in future iterations.

---

## 29. [Quiet Threadripper AI Workstation - 768GB DDR5 and 160GB VRAM (RTX 5090 + 4x R9700)](https://reddit.com/r/LocalLLaMA/comments/1qkghpk/quiet_threadripper_ai_workstation_768gb_ddr5_and/)

**Author:** u/sloptimizer | **Upvotes:** 164 | **Comments:** 94 | **Date:** 2026-01-22

**Summary:** The Reddit post describes a high-performance AI workstation with a Threadripper PRO 7975WX CPU, 768GB DDR5 RAM, an RTX 5090, and four R9700 GPUs. The system achieves impressive performance with DeepSeek-V3.1-Terminus, running at 151.76 tokens per second for prompt processing and 10.85 tokens per second for token generation.

**Key Points:**
- The workstation combines Nvidia and AMD GPUs using llama.cpp with specific compilation flags.
- RAM cooling is critical for performance; adding RAM fans improved performance by 30%.
- Power management tips include limiting the RTX 5090 to 400W and setting R9700 to HIGH performance level.
- The system uses dual power supplies: a 1600W for the main system and an 850W for three of the Radeons.
- The build is praised for achieving near-SOTA performance at usable speeds.

**Discussion Highlights:** The top comments highlight the impressive performance of the system, with one user noting the near-SOTA speeds achieved. Other comments express admiration and curiosity about the cost and benefits of the mixed GPU setup.

---

## 30. [Am I the only one who feels that, with all the AI boom, everyone is basically doing the same thing?](https://reddit.com/r/LocalLLaMA/comments/1qk8zj1/am_i_the_only_one_who_feels_that_with_all_the_ai/)

**Author:** u/[deleted] | **Upvotes:** 397 | **Comments:** 189 | **Date:** 2026-01-22

**Summary:** The Reddit post discusses the redundancy of AI tools and applications during the AI boom, highlighting that many new tools are less polished versions of existing ones. The discussion includes insights on the early days of AI technology and the enthusiasm driving shallow implementations. Key points include the low barrier to entry for AI development, the 'hype stage' of AI technology, and the shift from cryptocurrency to AI expertise. The discussion highlights the early days of AI technology and the enthusiasm driving shallow implementations, with a consensus that the current phase is the 'hype stage.'

---

## 31. [vLLM raising $150M confirms it: We have moved from the "Throughput Era" to the "Latency(Cold Starts)."](https://reddit.com/r/LocalLLaMA/comments/1qk68n8/vllm_raising_150m_confirms_it_we_have_moved_from/)

**Author:** u/pmv143 | **Upvotes:** 170 | **Comments:** 91 | **Date:** 2026-01-22

**Summary:** The Reddit post discusses the significant investment in vLLM, signaling a shift from the 'Throughput Era' to the 'Latency Era' in AI. It highlights the importance of software over hardware and the debate around standardization and optimization in AI inference.

**Key Points:**
- The $150M investment in vLLM signals a shift from training to serving in AI.
- Software (e.g., PagedAttention, specialized kernels) is crucial for efficient AI inference.
- vLLM aims to be the 'Linux of Inference,' but there is debate on whether it will focus on horizontal compatibility or vertical optimization.
- The next major challenge in AI is reducing latency, particularly cold starts and time-to-first-token.
- There is a discussion on whether vLLM will be the dominant inference engine or if alternatives like llama.cpp will prevail.

**Discussion Highlights:** The discussion highlights a debate on vLLM's role in the AI inference landscape, with some comparing it to Linux and others to FreeBSD or Redhat. There is also a consensus on the importance of addressing latency issues, particularly cold starts, in AI inference.

---

## 32. [Qwen have open-sourced the full family of Qwen3-TTS: VoiceDesign, CustomVoice, and Base, 5 models (0.6B &amp; 1.8B), Support for 10 languages](https://reddit.com/r/LocalLLaMA/comments/1qjul5t/qwen_have_opensourced_the_full_family_of_qwen3tts/)

**Author:** u/Nunki08 | **Upvotes:** 723 | **Comments:** 118 | **Date:** 2026-01-22

**Summary:** Qwen has open-sourced the Qwen3-TTS model family, including VoiceDesign, CustomVoice, and Base models in 0.6B and 1.8B sizes, supporting 10 languages. The models are available on GitHub, Hugging Face, and include a demo and blog post.

**Key Points:**
- Qwen3-TTS models are open-sourced with 0.6B and 1.8B parameter sizes
- Supports 10 languages and includes VoiceDesign, CustomVoice, and Base models
- Available on GitHub, Hugging Face, with a demo and blog post
- Community appreciates the open-source release for local use
- Some concerns about English voice quality and model compatibility with tools like llama.cpp

**Discussion Highlights:** The community is generally positive about the open-source release, appreciating the ability to run models locally. However, there are concerns about the English voice quality sounding like anime dubs and requests for better compatibility with tools like llama.cpp. Some users also noted the high quality of the provided samples.

---

## 33. [Qwen dev on Twitter!!](https://reddit.com/r/LocalLLaMA/comments/1qjtyw8/qwen_dev_on_twitter/)

**Author:** u/Difficult-Cap-7527 | **Upvotes:** 749 | **Comments:** 60 | **Date:** 2026-01-22

**Summary:** The Reddit post discusses Qwen's TTS model announcement, which is revealed to be from the vLLM leak. The community shares a Hugging Face link for the model.

**Key Points:**
- Qwen's TTS model is announced.
- The model is from the vLLM leak.
- A Hugging Face link is provided for the model.
- The thread is locked as announcements are out.

**Discussion Highlights:** The community is focused on the TTS model's release, its source from the vLLM leak, and sharing relevant links.

---

## 34. [GLM 4.7 flash FA fix for CUDA has been merged into llama.cpp](https://reddit.com/r/LocalLLaMA/comments/1qjrsur/glm_47_flash_fa_fix_for_cuda_has_been_merged_into/)

**Author:** u/jacek2023 | **Upvotes:** 155 | **Comments:** 51 | **Date:** 2026-01-22

**Summary:** The post announces the merge of GLM 4.7 flash FA fix for CUDA into llama.cpp, with users reporting mixed results including performance issues and successful builds.

**Key Points:**
- GLM 4.7 flash FA fix for CUDA has been merged into llama.cpp
- Quantized cache is not working well, causing high CPU usage
- Some users report successful builds and functionality
- Performance issues reported, particularly for Pascal GPUs
- Ongoing bug reports and discussions about performance optimizations

**Discussion Highlights:** Users are experiencing mixed results with the new merge, with some reporting successful builds and others facing performance issues. There is an ongoing discussion about optimizing performance, particularly for Pascal GPUs, and addressing issues with quantized cache.

---

## 35. [Fei Fei Li dropped a non-JEPA world model, and the spatial intelligence is insane](https://reddit.com/r/LocalLLaMA/comments/1qjjrmq/fei_fei_li_dropped_a_nonjepa_world_model_and_the/)

**Author:** u/coloradical5280 | **Upvotes:** 189 | **Comments:** 88 | **Date:** 2026-01-21

**Summary:** Fei-Fei Li's World Labs launched Marble, a generative world model using Neural Radiance Fields (NeRF) and Gaussian splatting, enabling fast creation of explorable 3D worlds with spatial intelligence. The technology allows for persistent, editable environments and supports VR and exports to various platforms.

**Key Points:**
- Marble is built on NeRF and Gaussian splatting, not JEPA.
- It generates explorable 3D worlds quickly and supports VR and exports.
- The technology enables persistent, editable environments.
- Some users criticize the lack of open-source availability and question its classification as a 'world model'.
- The visual quality may not impress at first glance, but the spatial intelligence is notable.

**Discussion Highlights:** The discussion highlights mixed reactions, with some users criticizing the lack of open-source availability and questioning the technology's classification as a 'world model'. Others express skepticism about the visual quality but acknowledge the spatial intelligence as a breakthrough.

---

## 36. [Wrote a guide for running Claude Code with GLM-4.7 Flash locally with llama.cpp](https://reddit.com/r/LocalLLaMA/comments/1qjf6ys/wrote_a_guide_for_running_claude_code_with_glm47/)

**Author:** u/tammamtech | **Upvotes:** 119 | **Comments:** 45 | **Date:** 2026-01-21

**Summary:** The Reddit post provides a guide for running Claude Code with GLM-4.7 Flash locally using llama.cpp, highlighting features like model swapping and GPU memory management. The author shares commands for installation and setup, including Docker options, and discusses the benefits of using GLM-4.7 Flash for local AI model deployment. Key points include the guide for running Claude Code with GLM-4.7 Flash using llama.cpp, support for features like model swapping and GPU memory management, commands provided for installation and setup, discussion on the benefits of using GLM-4.7 Flash for local AI deployment, and community feedback including technical questions and alternative open-source options. The discussion highlights technical questions about VRAM usage and performance metrics, as well as suggestions for alternative open-source tools like OpenCode and Harbor, and mentions the Anthropic API endpoint implementation timeline.

---

## 37. [8x AMD MI50 32GB at 26 t/s (tg) with MiniMax-M2.1 and 15 t/s (tg) with GLM 4.7 (vllm-gfx906)](https://reddit.com/r/LocalLLaMA/comments/1qjaxfy/8x_amd_mi50_32gb_at_26_ts_tg_with_minimaxm21_and/)

**Author:** u/ai-infos | **Upvotes:** 315 | **Comments:** 128 | **Date:** 2026-01-21

**Summary:** The post details a cost-effective local inference setup using 8x AMD MI50 GPUs, achieving high token generation speeds with MiniMax-M2.1 and GLM 4.7 models. The setup is praised for its performance and affordability, with a total VRAM of 256GB for under $1k.

**Key Points:**
- MiniMax-M2.1 achieves 26.8 tokens per second (output) and 3000 tokens per second (input) with a context length of 196,608.
- GLM 4.7 achieves 15.6 tokens per second (output) and 3000 tokens per second (input) with a context length of 95,000.
- The setup costs $880 for 256GB VRAM and draws 280W idle / 1200W during inference.
- The goal is to create one of the most cost-effective solutions for fast, intelligent local inference.
- The community highly praises the setup for its performance and affordability.

**Discussion Highlights:** The community is highly enthusiastic about the setup, with comments highlighting its cost-effectiveness and performance. Some users express interest in replicating the setup but note that current prices for the GPUs are higher than those mentioned in the post.

---

## 38. [VibeVoice-ASR released!](https://reddit.com/r/LocalLLaMA/comments/1qj40er/vibevoiceasr_released/)

**Author:** u/k_means_clusterfuck | **Upvotes:** 152 | **Comments:** 49 | **Date:** 2026-01-21

**Summary:** Microsoft released VibeVoice-ASR, a multilingual ASR model with 9B parameters. Users report good quality but express concerns about its size and lack of benchmarks.

**Key Points:**
- VibeVoice-ASR is a new ASR model by Microsoft
- It is multilingual and has 9B parameters
- Users report good quality in tests
- Concerns about size and lack of benchmarks
- Comparisons with other models like Whisper

**Discussion Highlights:** Positive feedback on quality, but concerns about size and performance metrics compared to alternatives like Whisper.

---

## 39. [One-shot single page web development: pacman clone - GLM 4.7 vs GLM 4.7 Flash vs GLM 4.5 Air vs Gemini 3 Pro vs Gemini 3 Flash - Results available for online testing - Prompt and instructions provided for testing with other models](https://reddit.com/r/LocalLLaMA/comments/1qj13uh/oneshot_single_page_web_development_pacman_clone/)

**Author:** u/ex-arman68 | **Upvotes:** 108 | **Comments:** 48 | **Date:** 2026-01-21

**Summary:** The Reddit post discusses a comparison of various AI models in creating a Pacman clone as a single webpage. GLM 4.7 emerged as the clear winner, followed by Minimax M2.1, with Gemini models performing less impressively than expected. The post includes links to the generated webpages and encourages further testing with other models. Key points include GLM 4.7's top performance, Minimax M2.1's sound implementation, Gemini models' underperformance, the recommendation to set temperature to 0, and community surprise at GLM 4.7's performance. The discussion highlighted the testing methodology's effectiveness, unexpected performance of GLM 4.7, and limitations of LLMs in terms of token capacity and memory.

---

## 40. [GLM-4.7-Flash-GGUF bug fix - redownload for better outputs](https://reddit.com/r/LocalLLaMA/comments/1qiy0ha/glm47flashgguf_bug_fix_redownload_for_better/)

**Author:** u/etherd0t | **Upvotes:** 111 | **Comments:** 58 | **Date:** 2026-01-21

**Summary:** The post announces a bug fix for the GLM-4.7-Flash-GGUF model, which previously caused looping and poor outputs. Users are advised to re-download the model for improved performance and provided with recommended parameters for different use cases.

**Key Points:**
- Bug fix for looping and poor outputs in GLM-4.7-Flash-GGUF model
- Recommended parameters for general use-case and tool-calling
- Positive feedback from users on the fixed version
- Performance comparison with other models like GPT-OSS-20b
- Appreciation for the update and bug fix

**Discussion Highlights:** Users generally appreciate the bug fix and report improved performance. Some discuss performance comparisons with other models and express gratitude for the update.

---

## 41. [Fix for GLM 4.7 Flash has been merged into llama.cpp](https://reddit.com/r/LocalLLaMA/comments/1qiwm3c/fix_for_glm_47_flash_has_been_merged_into_llamacpp/)

**Author:** u/jacek2023 | **Upvotes:** 313 | **Comments:** 86 | **Date:** 2026-01-21

**Summary:** The post announces the integration of GLM 4.7 Flash into llama.cpp, highlighting its significance and ongoing CUDA support. Community feedback includes performance metrics and user experiences.

**Key Points:**
- GLM 4.7 Flash has been merged into llama.cpp
- CUDA support is in progress
- Performance metrics for GLM 4.7 on a 4090 GPU are provided
- Community feedback includes positive experiences and some performance concerns

**Discussion Highlights:** Users share performance data for GLM 4.7 on different hardware, discuss the quality of the model, and inquire about CPU-only performance. Overall, the community is positive about the update.

---

## 42. [Here is how to get GLM 4.7 working on llama.cpp with flash attention and correct outputs](https://reddit.com/r/LocalLLaMA/comments/1qir5eq/here_is_how_to_get_glm_47_working_on_llamacpp/)

**Author:** u/TokenRingAI | **Upvotes:** 102 | **Comments:** 49 | **Date:** 2026-01-21

**Summary:** The post discusses how to get GLM 4.7 working on llama.cpp with flash attention, highlighting high performance metrics and noting that recent updates have simplified the process.

**Key Points:**
- GLM 4.7 can achieve high performance (2000+ tokens/sec prompt, 97 tokens/sec generation) on RTX 6000 Blackwell
- Initial setup required specific git branch and command-line options, but these are now unnecessary due to updates
- New GGUFs have been released with correct settings to avoid nonsensical outputs
- The model performs well and is supported in the latest versions of tools like LM Studio

**Discussion Highlights:** The discussion highlights the availability of new GGUFs with correct settings, the improved performance and ease of use after recent updates, and positive feedback on the model's capabilities, including its ability to handle failed tool calls effectively.

---

## 43. [vLLM v0.14.0 released](https://reddit.com/r/LocalLLaMA/comments/1qim0e9/vllm_v0140_released/)

**Author:** u/jinnyjuice | **Upvotes:** 169 | **Comments:** 36 | **Date:** 2026-01-20

**Summary:** The Reddit post announces the release of vLLM v0.14.0, highlighting new features and updates. The discussion focuses on improvements like automatic context length fitting and the deprecation of certain quantization methods.

**Key Points:**
- Automatic context length fitting to GPU memory to prevent OOM failures
- Deprecation of some quantization methods, including HQQ
- Introduction of Marlin for Turing (sm75) as a major upgrade
- Community interest in future optimizations for sm120

**Discussion Highlights:** The community is excited about the automatic context length feature and the Marlin upgrade for Turing. There is also discussion about the deprecation of certain quantization methods and anticipation for future optimizations.

---

## 44. [Current GLM-4.7-Flash implementation confirmed to be broken in llama.cpp](https://reddit.com/r/LocalLLaMA/comments/1qih9r8/current_glm47flash_implementation_confirmed_to_be/)

**Author:** u/Sweet_Albatross9772 | **Upvotes:** 246 | **Comments:** 60 | **Date:** 2026-01-20

**Summary:** The Reddit post discusses issues with the current GLM-4.7-Flash implementation in llama.cpp, highlighting significant differences in logprobs compared to vLLM, which may explain reported problems like looping and poor performance. A potential fix is already proposed in a pull request. Key points include the confirmation of the broken implementation, differences in logprobs, availability of a fix, community acknowledgment of the issue, and suggestions to wait before adopting new models. The discussion highlights a consensus that the implementation is broken but fixable, with community members expressing confidence in the open-source process to resolve the issue quickly.

---

## 45. [You have 64gb ram and 16gb VRAM; internet is permanently shut off: what 3 models are the ones you use?](https://reddit.com/r/LocalLLaMA/comments/1qids6a/you_have_64gb_ram_and_16gb_vram_internet_is/)

**Author:** u/Adventurous-Gold6413 | **Upvotes:** 551 | **Comments:** 306 | **Date:** 2026-01-20

**Summary:** The Reddit post discusses the selection of local models for use with 64GB RAM and 16GB VRAM when internet access is unavailable. Users share their preferred models and experiences. Key points include recommendations for models like Gemma 3 27B, GLM 4.5 Air, and GPT-OSS 120B, with GPT-OSS-120B being praised for its performance and versatility. The discussion highlights a consensus around these models, emphasizing their performance and suitability for the specified hardware.

---

## 46. [Liquid AI released the best thinking Language Model Under 1GB](https://reddit.com/r/LocalLLaMA/comments/1qi512t/liquid_ai_released_the_best_thinking_language/)

**Author:** u/PauLabartaBajo | **Upvotes:** 236 | **Comments:** 53 | **Date:** 2026-01-20

**Summary:** Liquid AI released LFM2.5-1.2B-Thinking, a compact reasoning model that runs on-device with 900 MB of memory, excelling in math, tool use, and instruction following. It outperforms larger models in speed and efficiency, though some users question its memory requirements and licensing.

**Key Points:**
- LFM2.5-1.2B-Thinking is a 1.2B parameter model optimized for on-device reasoning with 900 MB memory usage.
- It generates internal thinking traces for systematic problem-solving and excels in math, tool use, and instruction following.
- The model matches or exceeds Qwen3-1.7B in performance despite having fewer parameters.
- Users raised concerns about memory requirements, performance trade-offs, and non-permissive licensing.
- Some users expressed a desire for larger models for broader real-world applications.

**Discussion Highlights:** The discussion highlights mixed reactions, with praise for the model's efficiency and capabilities but concerns about memory usage, performance comparisons with other models, and licensing restrictions. Some users also expressed a desire for larger models to better suit real-world applications.

---

## 47. [768Gb Fully Enclosed 10x GPU Mobile AI Build](https://reddit.com/r/LocalLLaMA/comments/1qi4uj2/768gb_fully_enclosed_10x_gpu_mobile_ai_build/)

**Author:** u/SweetHomeAbalama0 | **Upvotes:** 918 | **Comments:** 273 | **Date:** 2026-01-20

**Summary:** The post describes a custom-built, fully enclosed mobile AI system with 10 GPUs, designed for running large MoE models and supporting graphic design tasks. The build cost approximately $17k and features a Threadripper Pro 3995WX, 512GB DDR4, and a mix of 3090 and 5090 GPUs. The system is enclosed in a Thermaltake Core W200 case for mobility and protection.

**Key Points:**
- The system is designed for running large MoE models and supporting graphic design tasks.
- It features a Threadripper Pro 3995WX, 512GB DDR4, and a mix of 3090 and 5090 GPUs.
- The build cost approximately $17k and is enclosed in a Thermaltake Core W200 case for mobility and protection.
- The enclosure was necessary to protect the hardware from pets and to ensure mobility.
- The discussion highlights the impressive nature of the build and some humorous comments about its portability.

**Discussion Highlights:** The discussion includes humorous comments about the system's portability and its impressive specifications. Some users appreciate the build's capabilities, while others joke about its size and power requirements.

---

## 48. [Over 6K novels with reasoning traces to train full book writing LLMs](https://reddit.com/r/LocalLLaMA/comments/1qi3nmd/over_6k_novels_with_reasoning_traces_to_train/)

**Author:** u/XMasterDE | **Upvotes:** 110 | **Comments:** 46 | **Date:** 2026-01-20

**Summary:** The post announces an update to the LongPage dataset, expanding it to over 6,000 novels with hierarchical reasoning traces for training full-book writing LLMs. The team is also training a model on this dataset and plans to release it soon.

**Key Points:**
- LongPage dataset now includes over 6,000 novels with hierarchical planning traces.
- The dataset supports training full-book writing LLMs.
- Early model checkpoints are being tested internally, with plans for public release.
- The community shows interest in the dataset's potential for fiction writing and other languages.
- Requests for more details on the dataset's structure and processing code.

**Discussion Highlights:** The discussion reflects enthusiasm for the dataset's potential in fiction writing and storytelling. Users are eager for more details on how the dataset works and whether it includes specific works. There is also interest in extending the dataset to other languages.

---

