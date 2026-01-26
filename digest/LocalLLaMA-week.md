# r/LocalLLaMA Reading Digest

**Period:** 2026-01-26 to 2026-01-26
**Posts Summarized:** 29
**Total Posts Analyzed:** 49

---

## 1. [Minimax Is Teasing M2.2](https://reddit.com/r/LocalLLaMA/comments/1qnfegx/minimax_is_teasing_m22/)

**Author:** u/Few_Painter_5588 | **Upvotes:** 106 | **Comments:** 32 | **Date:** 2026-01-26

**Summary:** The post discusses upcoming AI model releases from Chinese labs in February, including Deepseek v4, Kimi K3, MiniMax M2.2, and a potential closed-source model from ByteDance. The community is speculating about the lack of updates on 32B models and the possibility of new models under 30B.

**Key Points:**
- Multiple AI models expected to be released in February from Chinese labs
- Models mentioned include Deepseek v4, Kimi K3, MiniMax M2.2, and ByteDance's potential closed-source model
- Community discussion highlights the lack of updates on 32B models
- Speculation about the possibility of new models under 30B
- General excitement and readiness for new releases

**Discussion Highlights:** The discussion reflects a mix of excitement and speculation, with users expressing readiness for new models and questioning the lack of updates on existing 32B models. There is also curiosity about the potential release of models under 30B.

---

## 2. [I just won an Nvidia DGX Spark GB10 at an Nvidia hackathon. What do I do with it?](https://reddit.com/r/LocalLLaMA/comments/1qn3xig/i_just_won_an_nvidia_dgx_spark_gb10_at_an_nvidia/)

**Author:** u/brandon-i | **Upvotes:** 367 | **Comments:** 116 | **Date:** 2026-01-25

**Summary:** The author won an Nvidia DGX Spark GB10 at a hackathon and seeks advice on how to utilize it, mentioning potential use for running multiple NextJS applications.

**Key Points:**
- The user is new to fine-tuning models and previously used the system for inferencing with a large model.
- The user suggests running multiple NextJS applications due to high memory usage.
- Top comments recommend exploring Nvidia's playbooks and inquire about the hackathon project.

**Discussion Highlights:** The discussion highlights suggestions for running multiple NextJS applications and recommendations to explore Nvidia's resources for guidance.

---

## 3. [I reverse-engineered Microsoft AutoGen’s reasoning loop and cut agent latency by 85% (13.4s → 1.6s). Here is the architecture.](https://reddit.com/r/LocalLLaMA/comments/1qn2n4p/i_reverseengineered_microsoft_autogens_reasoning/)

**Author:** u/New_Care3681 | **Upvotes:** 100 | **Comments:** 34 | **Date:** 2026-01-25

**Summary:** The post discusses an optimization of Microsoft AutoGen's reasoning loop using Speculative Reasoning Execution (SRE) to reduce latency by 85%, from 13.4s to 1.6s. The author implemented a module to predict tool calls during the reasoning phase, executing them asynchronously. The solution has been approved by the AutoGen core team and includes additional work on a distributed training rig for Whisper.

**Key Points:**
- Speculative Reasoning Execution (SRE) reduces latency by predicting tool calls during reasoning.
- Latency improved from 13.4s to 1.6s, an 85% reduction.
- The PR for this optimization has been approved by the AutoGen core team.
- Author also built a distributed training rig for Whisper using Ray Train and PyTorch DDP.
- Mixed reactions in comments: praise for innovation but concerns about robustness and practicality.

**Discussion Highlights:** The discussion highlights mixed reactions, with some users praising the innovation and others questioning the robustness of the regex-based approach and the practicality of the solution. Some comments also raise concerns about the approval process and the current status of AutoGen.

---

## 4. [GLM-4.7-Flash is even faster now](https://reddit.com/r/LocalLLaMA/comments/1qmvny5/glm47flash_is_even_faster_now/)

**Author:** u/jacek2023 | **Upvotes:** 243 | **Comments:** 90 | **Date:** 2026-01-25

**Summary:** The post announces that GLM-4.7-Flash has been updated to be even faster. The discussion includes appreciation, technical reactions, and humorous comments.

**Key Points:**
- GLM-4.7-Flash has received a speed update
- The post was featured on Discord and the author received a special flair
- An image link was shared with thanks to a user for making a previous post obsolete
- Reactions include humor ('Cries in AMD GPU') and technical comments ('this model is somehow cursed')

**Discussion Highlights:** The discussion features a mix of appreciation for the update, humorous reactions, and technical commentary. The post was well-received, as indicated by the Discord feature and special flair.

---

## 5. [Internet blackout and Local LLMs](https://reddit.com/r/LocalLLaMA/comments/1qmlpjp/internet_blackout_and_local_llms/)

**Author:** u/DunderSunder | **Upvotes:** 243 | **Comments:** 72 | **Date:** 2026-01-25

**Summary:** The post discusses the severe internet blackout in Iran, highlighting the importance of local LLMs like Gemma3 and Qwen3 during censorship. It contrasts the limitations of whitelisted services like ChatGPT with the benefits of uncensored local models.

**Key Points:**
- Severe internet blackout in Iran with only a few whitelisted websites.
- Local LLMs like Gemma3 and Qwen3 are crucial for accessing uncensored information.
- Whitelisted services like ChatGPT have limitations in circumventing censorship.
- Discussion highlights the reliance on internet services and the value of local models.
- Suggestions include using Wikipedia dumps and AI modes on whitelisted sites.

**Discussion Highlights:** The discussion emphasizes the importance of local LLMs in circumventing censorship and the limitations of whitelisted services. There is a consensus on the value of having uncensored, local models for accessing information during internet blackouts.

---

## 6. [KV cache fix for GLM 4.7 Flash](https://reddit.com/r/LocalLLaMA/comments/1qmjzx1/kv_cache_fix_for_glm_47_flash/)

**Author:** u/jacek2023 | **Upvotes:** 241 | **Comments:** 68 | **Date:** 2026-01-25

**Summary:** The post discusses a fix for the KV cache in GLM 4.7 Flash, which significantly reduces VRAM usage by removing unnecessary components, allowing for longer context lengths on the same hardware setup.

**Key Points:**
- Removing 'Air' from GLM 4.7 Flash optimizes KV cache usage.
- The fix saves gigabytes of VRAM, enabling longer context lengths.
- Users report significant improvements, such as doubling context length on a 4090 GPU.
- The model is still considered somewhat quirky but functional.
- The community is actively working on further optimizations.

**Discussion Highlights:** The discussion highlights significant performance improvements and community engagement, with users reporting successful tests and ongoing optimizations. There is a consensus that the model is improving rapidly.

---

## 7. [[Release] Qwen3-TTS: Ultra-Low Latency (97ms), Voice Cloning &amp; OpenAI-Compatible API](https://reddit.com/r/LocalLLaMA/comments/1qlzbhh/release_qwen3tts_ultralow_latency_97ms_voice/)

**Author:** u/blackstoreonline | **Upvotes:** 298 | **Comments:** 117 | **Date:** 2026-01-24

**Summary:** The Reddit post introduces Qwen3-TTS, an ultra-low latency (97ms) text-to-speech model with voice cloning and OpenAI-compatible API. It supports multilingual synthesis and can be easily deployed via Docker or Python. Users in the comments highlight its impressive speed and voice cloning capabilities, though some note technical adjustments needed for specific GPUs.

**Key Points:**
- Ultra-low latency (~97ms) for streaming TTS
- Supports voice cloning with a 3-second reference clip
- OpenAI-compatible API for easy integration
- Multilingual support (10+ languages)
- Users praise its speed and voice quality, with some technical adjustments noted for GPU compatibility

**Discussion Highlights:** Users are highly impressed with the 97ms latency and voice cloning capabilities. Some technical adjustments are needed for specific GPUs, and there is a discussion about streaming support in the published code.

---

## 8. [Artificial Analysis: South Korea 🇰🇷 is now the clear #3 nation in AI — powered by the Korean National Sovereign AI Initiative there are now multiple Korean AI labs with near frontier intelligence.](https://reddit.com/r/LocalLLaMA/comments/1qltwza/artificial_analysis_south_korea_is_now_the_clear/)

**Author:** u/self-fix | **Upvotes:** 180 | **Comments:** 55 | **Date:** 2026-01-24

**Summary:** South Korea has emerged as a leading nation in AI, driven by the Korean National Sovereign AI Initiative, which incentivizes domestic AI development through government funding and GPU access. The initiative has shortlisted top AI labs like LG, SK Telecom, and Upstage, with models such as K-EXAONE and Solar Open showcasing strong performance in various AI evaluations.

**Key Points:**
- South Korea is now the clear #3 nation in AI, powered by the Korean National Sovereign AI Initiative.
- The initiative shortlists national champions, providing government funding and GPU access.
- Top Korean AI models include LG's K-EXAONE (236B) and Upstage's Solar Open (100B).
- Models vary in size and focus, with some being open weights and others proprietary.
- Discussion highlights skepticism about South Korea's ranking and interest in model performance.

**Discussion Highlights:** The discussion includes skepticism about South Korea's ranking, with comments questioning the absence of other countries like Canada and France. There is also interest in the performance and availability of Korean AI models, with some users requesting more information on specific models.

---

## 9. [Personal experience with GLM 4.7 Flash Q6 (unsloth) + Roo Code + RTX 5090](https://reddit.com/r/LocalLLaMA/comments/1qlnruw/personal_experience_with_glm_47_flash_q6_unsloth/)

**Author:** u/Septerium | **Upvotes:** 163 | **Comments:** 91 | **Date:** 2026-01-24

**Summary:** The post discusses the user's positive experience with GLM 4.7 Flash for refactoring tasks, highlighting its reliability and precision compared to other models. The user shares the command used to optimize the model's performance on an RTX 5090.

**Key Points:**
- GLM 4.7 Flash performs well in refactoring tasks and handles Roo Code effectively.
- The model is more reliable and precise than GPT-OSS 120b, GLM 4.5 Air, or Devstral 24b.
- The user used a specific llama.cpp command to optimize the model's performance on an RTX 5090.
- The discussion includes feedback on the model's performance and technical details about the command used.
- Some users note that certain command parameters are now default in the latest llama.cpp version.

**Discussion Highlights:** The discussion highlights the model's effectiveness in handling large amounts of tools and system prompts, with some users noting its superiority in specific tasks. There is also a consensus that certain command parameters are now default in the latest llama.cpp version, simplifying the setup process.

---

## 10. [GLM-4.7-Flash-REAP on RTX 5060 Ti 16 GB - 200k context window!](https://reddit.com/r/LocalLLaMA/comments/1qlanzn/glm47flashreap_on_rtx_5060_ti_16_gb_200k_context/)

**Author:** u/bobaburger | **Upvotes:** 207 | **Comments:** 86 | **Date:** 2026-01-23

**Summary:** The post discusses the performance of the GLM-4.7-Flash-REAP model on an RTX 5060 Ti 16 GB setup, highlighting its speed and context window capabilities. The author experiments with different context window sizes and notes performance trade-offs, including speed and memory usage.

**Key Points:**
- The model performs well with 16k and 64k context windows but struggles with 100k due to high resource usage.
- Enabling 'Force Model Expert Weight onto CPU' improves performance with a 100k context window.
- The model's tool calls and code generation are accurate but face issues with looping when the context window is exceeded.
- Performance metrics (pp speed and tg speed) vary significantly with different context window sizes.
- Community feedback suggests potential for further optimization and excitement about local high-quality agents.

**Discussion Highlights:** The discussion includes feedback on the post's popularity, suggestions for performance improvements, and excitement about the potential for running high-quality agents locally with large context windows.

---

## 11. [Built a 100% client-side AI that plays Pokemon Red - Qwen 2.5 1.5B via WebLLM + neural network policy .   Fork/check it out! BYOR](https://reddit.com/r/LocalLLaMA/comments/1ql6cz7/built_a_100_clientside_ai_that_plays_pokemon_red/)

**Author:** u/Efficient-Proof-1824 | **Upvotes:** 263 | **Comments:** 29 | **Date:** 2026-01-23

**Summary:** The post describes a client-side AI project that plays Pokemon Red using Qwen 2.5 1.5B via WebLLM and a neural network policy. The project is deployed as a Svelte app and aims to build an agent capable of beating the game.

**Key Points:**
- Project uses Qwen 2.5 1.5B via WebLLM for action plan generation
- Includes a TensorFlow.js neural network for scoring actions
- Deployed as a Svelte app on GitHub Pages
- Goal is to build an agent that can beat Pokemon Red
- Community feedback highlights interest in larger models and additional features

**Discussion Highlights:** The community shows enthusiasm for the project, with suggestions for integrating larger models and additional features like audio output.

---

## 12. [Your post is getting popular and we just featured it on our Discord!](https://reddit.com/r/LocalLLaMA/comments/1qkyex0/your_post_is_getting_popular_and_we_just_featured/)

**Author:** u/roculus | **Upvotes:** 555 | **Comments:** 56 | **Date:** 2026-01-23

**Summary:** The Reddit post announces that a user's post is popular and has been featured on Discord, with the user receiving a special flair. The community discusses the annoyance of bot spam and questions the monetization of the Discord server.

**Key Points:**
- The bot announces the popularity of a user's post and its feature on Discord.
- The user receives a special flair for their contribution.
- The community finds the bot spam annoying and questions the monetization of the Discord server.
- There is a pinned thread about the Discord server that has been there for 5 months.
- The community humorously suggests that the bot might announce the post's popularity on Discord.

**Discussion Highlights:** The community expresses annoyance at the bot spam and questions the monetization of the Discord server. There is a consensus that private messages would be preferable to public bot posts.

---

## 13. [A full AI powered cooking game, where literally any ingredient is possible with infinite combinations.](https://reddit.com/r/LocalLLaMA/comments/1qkqjer/a_full_ai_powered_cooking_game_where_literally/)

**Author:** u/VirtualJamesHarrison | **Upvotes:** 111 | **Comments:** 33 | **Date:** 2026-01-23

**Summary:** The post introduces 'Infinite Kitchen', an AI-powered cooking game that allows for infinite ingredient combinations. The game is built using Claude Code for game logic, Gemini for sprites, and Flux for the overall design. Users can try it out at the provided link. Key points include the game's construction with Claude Code, Gemini, and Flux, noted inconsistencies in game mechanics, the requirement for a larger screen for optimal experience, suggestions that the concept could be achieved with simpler algorithms, and curiosity about live asset generation. The discussion highlights a mix of appreciation for the innovative concept and constructive criticism regarding game mechanics and technical implementation.

---

## 14. [Llama.cpp merges in OpenAI Responses API Support](https://reddit.com/r/LocalLLaMA/comments/1qkm9zb/llamacpp_merges_in_openai_responses_api_support/)

**Author:** u/SemaMod | **Upvotes:** 156 | **Comments:** 44 | **Date:** 2026-01-23

**Summary:** The post discusses the successful integration of OpenAI Responses API support in Llama.cpp, highlighting its effectiveness with GLM-4.7-Flash in the Codex CLI harness for exploring large codebases.

**Key Points:**
- Llama.cpp now supports OpenAI Responses API, enabling stateful interactions with OpenAI models.
- The integration works well with GLM-4.7-Flash in the Codex CLI harness.
- Users appreciate the new feature but want the old API to remain functional.
- The Responses API allows accessing and managing previous messages.
- Some users are still unclear about the full implications of this update.

**Discussion Highlights:** The discussion highlights a general appreciation for the new API support, with some concerns about the future of the old API. Users are exploring the capabilities of the Responses API, which enables stateful interactions and message management. There is some confusion about the full scope of the update, but overall, the feedback is positive.

---

## 15. [OpenAI CFO hinting at "Outcome-Based Pricing" (aka royalties on your work)? Makes the case for local even stronger.](https://reddit.com/r/LocalLLaMA/comments/1qkiylw/openai_cfo_hinting_at_outcomebased_pricing_aka/)

**Author:** u/distalx | **Upvotes:** 232 | **Comments:** 98 | **Date:** 2026-01-23

**Summary:** The post discusses OpenAI's potential shift to outcome-based pricing for high-value enterprise deals, clarifying that it does not apply to regular users or indie developers. The author initially misinterpreted the scope but corrected it after finding the primary source.

**Key Points:**
- OpenAI's CFO mentioned outcome-based pricing for enterprise deals, not regular users.
- The pricing model is aimed at high-value industries like pharmaceuticals.
- The post highlights the benefits of local AI stacks over cloud APIs to avoid potential future costs.
- Users in the comments express concerns about data privacy and control.
- There is a consensus on the importance of self-hosting AI models to maintain autonomy.

**Discussion Highlights:** The discussion emphasizes the importance of self-hosting AI models to avoid potential future costs and maintain control over data and terms of use. Users generally agree that while cloud APIs are convenient, local solutions offer more autonomy and long-term cost benefits.

---

## 16. [Nvidia Introduces PersonaPlex: An Open-Source, Real-Time Conversational AI Voice](https://reddit.com/r/LocalLLaMA/comments/1qkimzg/nvidia_introduces_personaplex_an_opensource/)

**Author:** u/44th--Hokage | **Upvotes:** 239 | **Comments:** 30 | **Date:** 2026-01-22

**Summary:** Nvidia has introduced PersonaPlex, an open-source, real-time conversational AI voice model that enables persona control through text-based role prompts and audio-based voice conditioning. It is trained on synthetic and real conversations to produce natural, low-latency spoken interactions.

**Key Points:**
- PersonaPlex is a real-time, full-duplex speech-to-speech model with persona control.
- It is trained on a combination of synthetic and real conversations.
- The model requires significant VRAM (96GB) for optimal performance.
- Some users have noted concerns about audio quality and model intelligence.
- The project is open-source with available demos and code.

**Discussion Highlights:** Users have mixed reactions, with some praising the technology while others criticize its high VRAM requirements, audio quality, and perceived lack of intelligence compared to other models like Unmute.

---

## 17. [vLLM raising $150M confirms it: We have moved from the "Throughput Era" to the "Latency(Cold Starts)."](https://reddit.com/r/LocalLLaMA/comments/1qk68n8/vllm_raising_150m_confirms_it_we_have_moved_from/)

**Author:** u/pmv143 | **Upvotes:** 170 | **Comments:** 91 | **Date:** 2026-01-22

**Summary:** The Reddit post discusses the significant investment in vLLM, signaling a shift from the 'Throughput Era' to the 'Latency Era' in AI. It highlights the importance of software over hardware and the race for standardization in AI inference.

**Key Points:**
- vLLM's $150M funding signals a shift from training to serving in AI.
- Software optimization is crucial for efficient AI inference.
- Standardization and compatibility are key focus areas for vLLM.
- Latency, particularly cold starts, is the next major challenge.
- Community discussion includes debates on vLLM's role and the importance of local solutions.

**Discussion Highlights:** The discussion highlights debates on vLLM's role in the AI ecosystem, with some comparing it to Linux or FreeBSD of inference. There is also a focus on the importance of local solutions and the amortization of cold starts in cloud environments.

---

## 18. [Qwen dev on Twitter!!](https://reddit.com/r/LocalLLaMA/comments/1qjtyw8/qwen_dev_on_twitter/)

**Author:** u/Difficult-Cap-7527 | **Upvotes:** 738 | **Comments:** 60 | **Date:** 2026-01-22

**Summary:** The Reddit post discusses Qwen's TTS model announcement, with community reactions and links to the model on Hugging Face.

**Key Points:**
- Qwen's TTS model announcement
- Community reaction and discussion
- Link to the model on Hugging Face
- Thread locked due to announcements being out
- Mention of vLLM leak related to the TTS model

**Discussion Highlights:** The community is excited about the Qwen TTS model, with some users sharing links to the model on Hugging Face. There is also mention of a vLLM leak related to the TTS model, and the thread was locked as announcements are out.

---

## 19. [Fei Fei Li dropped a non-JEPA world model, and the spatial intelligence is insane](https://reddit.com/r/LocalLLaMA/comments/1qjjrmq/fei_fei_li_dropped_a_nonjepa_world_model_and_the/)

**Author:** u/coloradical5280 | **Upvotes:** 191 | **Comments:** 90 | **Date:** 2026-01-21

**Summary:** Fei-Fei Li's World Labs launched Marble, a generative world model using Neural Radiance Fields and Gaussian splatting, enabling fast, editable 3D environments with VR support and export capabilities. The technology is praised for its spatial intelligence but criticized for being proprietary and limited in scope.

**Key Points:**
- Marble uses Neural Radiance Fields (NeRF) and Gaussian splatting for fast 3D world generation.
- The model supports stateful, editable environments with VR compatibility and export options.
- Criticisms include lack of open-source availability and skepticism about its classification as a 'world model.'
- Users note the environments are small and may not justify the hype.
- The technology is seen as promising but early-stage with rough edges.

**Discussion Highlights:** The discussion reflects mixed reactions, with some users dismissing Marble due to its proprietary nature and others questioning its novelty and scale. While the technology is acknowledged as innovative, criticisms focus on its closed-source model and perceived limitations in environment size and scope.

---

## 20. [GLM-4.7-Flash-GGUF bug fix - redownload for better outputs](https://reddit.com/r/LocalLLaMA/comments/1qiy0ha/glm47flashgguf_bug_fix_redownload_for_better/)

**Author:** u/etherd0t | **Upvotes:** 112 | **Comments:** 58 | **Date:** 2026-01-21

**Summary:** The post announces a bug fix for the GLM-4.7-Flash-GGUF model, with updated GGUF files available for download. Users are advised to re-download the model for improved outputs and provided with recommended parameters for different use cases.

**Key Points:**
- Bug fix for GLM-4.7-Flash-GGUF model addressing looping and poor outputs
- Updated GGUF files available for download
- Recommended parameters for general use and tool-calling provided
- Users report significant improvements in the fixed version
- Performance comparisons with other models mentioned in comments

**Discussion Highlights:** Users express satisfaction with the bug fix, noting improved performance and usability. Some discuss performance comparisons with other models like GPT-OSS-20b, and there is general appreciation for the update and the provided parameters.

---

## 21. [Fix for GLM 4.7 Flash has been merged into llama.cpp](https://reddit.com/r/LocalLLaMA/comments/1qiwm3c/fix_for_glm_47_flash_has_been_merged_into_llamacpp/)

**Author:** u/jacek2023 | **Upvotes:** 316 | **Comments:** 86 | **Date:** 2026-01-21

**Summary:** The post announces the integration of GLM 4.7 Flash into llama.cpp, highlighting its significance and ongoing CUDA support. Community feedback includes performance metrics and user experiences.

**Key Points:**
- GLM 4.7 Flash has been merged into llama.cpp
- CUDA support is in progress
- Performance metrics for different quantizations and GPUs are shared
- Community discusses CPU-only performance and model improvements

**Discussion Highlights:** Users share performance data for various quantizations and GPUs, discuss CPU-only performance, and note improvements in model behavior with reduced gibberish and repetition.

---

## 22. [Knowledge distillation with Claude as the interface: trained a 0.6B model to match GPT-class performance on Text2SQL in a singe conversation](https://reddit.com/r/LocalLLaMA/comments/1qiu6jo/knowledge_distillation_with_claude_as_the/)

**Author:** u/party-horse | **Upvotes:** 169 | **Comments:** 37 | **Date:** 2026-01-21

**Summary:** The post describes a workflow for training small, task-specific models using knowledge distillation via Claude, achieving significant performance improvements in Text2SQL tasks with minimal setup.

**Key Points:**
- Knowledge distillation via Claude simplifies fine-tuning small models for specialized tasks.
- The approach uses a large teacher model (DeepSeek-V3) to generate synthetic training data.
- Performance improved from 36% to 74% on Text2SQL tasks with minimal input data.
- The process includes task selection, data conversion, teacher evaluation, training, and packaging.
- The method is praised for its simplicity and potential for on-device inference.

**Discussion Highlights:** The discussion highlights enthusiasm for the approach, with comments noting its potential for training small models for local inference and its simplicity compared to traditional fine-tuning methods. Some users suggest improvements like using SQL AST for validation and express interest in trying the method.

---

## 23. [Current GLM-4.7-Flash implementation confirmed to be broken in llama.cpp](https://reddit.com/r/LocalLLaMA/comments/1qih9r8/current_glm47flash_implementation_confirmed_to_be/)

**Author:** u/Sweet_Albatross9772 | **Upvotes:** 245 | **Comments:** 60 | **Date:** 2026-01-20

**Summary:** The Reddit post discusses issues with the current GLM-4.7-Flash implementation in llama.cpp, highlighting significant differences in logprobs compared to vLLM, which may explain reported problems like looping and poor performance. A potential fix is already proposed in a pull request.

**Key Points:**
- Current GLM-4.7-Flash implementation in llama.cpp is confirmed broken.
- Significant differences in logprobs compared to vLLM may explain reported issues.
- A potential fix is proposed in a pull request by Piotr.
- Community acknowledges the issue and expects a quick resolution.
- Some users suggest waiting before downloading new models to avoid bugs.

**Discussion Highlights:** The discussion highlights a confirmed issue with the GLM-4.7-Flash implementation in llama.cpp, with significant differences in logprobs compared to vLLM. The community is optimistic about a quick fix, as a potential solution is already proposed in a pull request. Users generally acknowledge that such issues are common with new model releases and suggest waiting for bugs to be resolved before downloading.

---

## 24. [Liquid AI released the best thinking Language Model Under 1GB](https://reddit.com/r/LocalLLaMA/comments/1qi512t/liquid_ai_released_the_best_thinking_language/)

**Author:** u/PauLabartaBajo | **Upvotes:** 229 | **Comments:** 53 | **Date:** 2026-01-20

**Summary:** Liquid AI released LFM2.5-1.2B-Thinking, a reasoning model that runs on-device with 900 MB of memory, excelling in math, tool use, and instruction following. It outperforms larger models in speed and memory efficiency, with broad ecosystem support.

**Key Points:**
- LFM2.5-1.2B-Thinking is optimized for concise reasoning and runs on-device with 900 MB memory.
- It outperforms larger models in speed and memory efficiency, especially in math and tool use.
- The model is available across multiple platforms, including Hugging Face and Liquid AI Playground.
- Discussion highlights concerns about memory requirements, performance trade-offs, and licensing.
- Some users express a desire for larger models for real-world applications.

**Discussion Highlights:** The discussion includes concerns about memory requirements for edge deployment, comparisons with other models showing mixed performance results, and criticism of the non-Apache/MIT licensing. Some users appreciate the model's capabilities but wish for larger versions.

---

## 25. [768Gb Fully Enclosed 10x GPU Mobile AI Build](https://reddit.com/r/LocalLLaMA/comments/1qi4uj2/768gb_fully_enclosed_10x_gpu_mobile_ai_build/)

**Author:** u/SweetHomeAbalama0 | **Upvotes:** 908 | **Comments:** 271 | **Date:** 2026-01-20

**Summary:** The post describes a custom-built, high-performance AI system designed for running large MoE models and supporting graphic design tasks. The system features a Threadripper Pro 3995WX, 512GB DDR4, 10 GPUs (8x 3090 + 2x 5090), and dual PSUs, all enclosed in a Thermaltake Core W200 case for mobility and protection. The build cost approximately $17k and balances performance with budget constraints.

**Key Points:**
- The system is designed for large MoE models and graphic design tasks.
- It features a Threadripper Pro 3995WX, 512GB DDR4, and 10 GPUs (8x 3090 + 2x 5090).
- The build is enclosed in a Thermaltake Core W200 case for mobility and protection.
- The total cost was approximately $17k, balancing performance and budget.
- The post highlights the challenges of enclosure and mobility, especially in a household with pets.

**Discussion Highlights:** The discussion includes humorous comments about the system's portability and power requirements, as well as appreciation for the build's capabilities and aesthetics. Some users expressed curiosity about the physical arrangement of the GPUs.

---

## 26. [Over 6K novels with reasoning traces to train full book writing LLMs](https://reddit.com/r/LocalLLaMA/comments/1qi3nmd/over_6k_novels_with_reasoning_traces_to_train/)

**Author:** u/XMasterDE | **Upvotes:** 115 | **Comments:** 46 | **Date:** 2026-01-20

**Summary:** The post announces an update to the LongPage dataset, expanding it to over 6,000 novels with hierarchical reasoning traces for training full-book writing LLMs. The team is also training a model on this dataset and plans to release it soon.

**Key Points:**
- LongPage dataset updated to include over 6,000 novels with reasoning traces
- Dataset supports training full-book writing LLMs with hierarchical planning traces
- Team is training a model on LongPage and plans to release it soon
- Dataset and model details available on Hugging Face and other platforms
- Community interest in understanding the dataset structure and potential applications

**Discussion Highlights:** The discussion shows enthusiasm for the project, with users expressing interest in the dataset's structure, potential applications, and requests for more details on data processing and multilingual support.

---

## 27. [glm-4.7-flash has the best thinking process with clear steps, I love it](https://reddit.com/r/LocalLLaMA/comments/1qhxlgy/glm47flash_has_the_best_thinking_process_with/)

**Author:** u/uptonking | **Upvotes:** 138 | **Comments:** 34 | **Date:** 2026-01-20

**Summary:** The Reddit post discusses the user's experience with the glm-4.7-flash model, highlighting its structured thinking process and comparing it favorably to other models like nemotron-nano and qwen3-30b. The user appreciates the model's clear reasoning steps but notes its slower performance and occasional looping issues. Key points include the model's detailed thinking process, longer thinking duration, specific configuration settings for performance improvement, occasional looping issues, and user consensus on its strong reasoning capabilities. The discussion highlights a consensus on the model's strong reasoning process, with users appreciating its structured approach but noting concerns about speed and occasional looping issues.

---

## 28. [It's been one year since the release of Deepseek-R1](https://reddit.com/r/LocalLLaMA/comments/1qhs2sd/its_been_one_year_since_the_release_of_deepseekr1/)

**Author:** u/Recoil42 | **Upvotes:** 305 | **Comments:** 52 | **Date:** 2026-01-19

**Summary:** The Reddit post commemorates the one-year anniversary of the Deepseek-R1 model release, highlighting its significant impact on the AI community. The discussion emphasizes the model's disruptive influence, including its role in reshaping AI development and forcing major industry changes.

**Key Points:**
- Deepseek-R1's release had a massive impact, leading to significant changes in the AI industry.
- The model's influence was so profound that it disrupted major AI projects and teams.
- The release accelerated progress and innovation in AI, making the past year feel much longer due to rapid developments.
- Deepseek-R1's release is considered one of the most important in AI history, second only to the original Llama model.
- The model's release led to reduced prices and increased transparency in AI reasoning outputs.

**Discussion Highlights:** The discussion highlights the model's disruptive impact, with users noting its role in forcing industry changes, accelerating progress, and setting new standards for AI development. The consensus is that Deepseek-R1 was a pivotal release that significantly influenced the AI landscape.

---

## 29. [Mosquito - 7.3M parameter tiny knowledge model](https://reddit.com/r/LocalLLaMA/comments/1qhqzsi/mosquito_73m_parameter_tiny_knowledge_model/)

**Author:** u/Lopsided-Repair-3638 | **Upvotes:** 121 | **Comments:** 54 | **Date:** 2026-01-19

**Summary:** The post introduces 'Mosquito', a tiny 7.3M parameter language model that can answer general knowledge questions, though with some humorous inaccuracies. Users shared mixed reactions, highlighting both its surprising capabilities and obvious limitations.

**Key Points:**
- Mosquito is a 7.3M parameter model designed for general knowledge questions
- The model demonstrates surprising capabilities despite its small size
- Users noted humorous inaccuracies, such as defining a dog incorrectly
- There were requests for model quantization to improve performance
- The model's responses were sometimes nonsensical or incorrect

**Discussion Highlights:** The discussion was marked by a mix of amusement and criticism, with users pointing out both the model's unexpected successes and its glaring errors. There was a consensus that while the model is impressive for its size, it still has significant limitations and inaccuracies.

---

