# r/LocalLLaMA Reading Digest

**Period:** 2026-01-23 to 2026-01-23
**Posts Summarized:** 45
**Total Posts Analyzed:** 45

---

## 1. [Llama.cpp merges in OpenAI Responses API Support](https://reddit.com/r/LocalLLaMA/comments/1qkm9zb/llamacpp_merges_in_openai_responses_api_support/)

**Author:** u/SemaMod | **Upvotes:** 122 | **Comments:** 30 | **Date:** 2026-01-23

**Summary:** The Reddit post discusses the successful integration of OpenAI Responses API Support in Llama.cpp, highlighting its effectiveness with GLM-4.7-Flash in the Codex CLI harness. Users express mixed feelings about the new API, with some appreciating its stateful interaction capabilities while others raise concerns about data security.

**Key Points:**
- Llama.cpp now supports OpenAI Responses API, enabling stateful interactions with OpenAI models.
- The integration works well with GLM-4.7-Flash in the Codex CLI harness, proving effective for exploring large codebases.
- Users are concerned about potential deprecation of the old API and data security risks associated with the stateful nature of the new API.
- The new API allows for accessing and managing previous messages, enhancing interaction capabilities.
- Some users report successful use of the API, while others seek clarification on its functionalities.

**Discussion Highlights:** The discussion highlights a mix of enthusiasm and caution. Users appreciate the new API's capabilities for stateful interactions but express concerns about data security and potential deprecation of the old API. There is a consensus on the effectiveness of the integration with GLM-4.7-Flash, though some users seek more information on its functionalities.

---

## 2. [OpenAI CFO hinting at "Outcome-Based Pricing" (aka royalties on your work)? Makes the case for local even stronger.](https://reddit.com/r/LocalLLaMA/comments/1qkiylw/openai_cfo_hinting_at_outcomebased_pricing_aka/)

**Author:** u/distalx | **Upvotes:** 211 | **Comments:** 95 | **Date:** 2026-01-23

**Summary:** The post discusses OpenAI's potential shift to outcome-based pricing for high-value enterprise deals, clarifying that it does not apply to regular users or indie developers. The author uses a solar power analogy to argue for the benefits of local AI stacks. Key points include: OpenAI's CFO mentioned outcome-based pricing for enterprise deals, not regular users; the pricing model would apply to high-value industries like pharmaceuticals; the post argues for the benefits of local AI stacks to avoid dependency on cloud APIs; top comments highlight concerns about data usage and the importance of self-hosting; the discussion emphasizes the need for transparency and fairness in AI pricing models. The discussion highlights concerns about OpenAI's potential pricing model, with many users advocating for self-hosting and local AI solutions to maintain control and avoid unexpected costs.

---

## 3. [Nvidia Introduces PersonaPlex: An Open-Source, Real-Time Conversational AI Voice](https://reddit.com/r/LocalLLaMA/comments/1qkimzg/nvidia_introduces_personaplex_an_opensource/)

**Author:** u/44th--Hokage | **Upvotes:** 158 | **Comments:** 20 | **Date:** 2026-01-22

**Summary:** Nvidia's PersonaPlex is an open-source, real-time conversational AI voice model that enables persona control through text and audio prompts. It is trained on synthetic and real conversations to produce natural, low-latency spoken interactions.

**Key Points:**
- PersonaPlex is a speech-to-speech model with persona control.
- It requires significant VRAM (96GB) for optimal performance.
- The model is described as having limited intelligence, comparable to older models like Llama 1 7B.
- Audio quality concerns were raised, with some users noting narrowband-like sound.
- The model is open-sourced with available demos and code on GitHub and HuggingFace.

**Discussion Highlights:** Users expressed concerns about the high VRAM requirements and the model's intelligence level, comparing it unfavorably to other models like Unmute. Audio quality was also criticized, with some noting a narrowband-like sound. There was curiosity about how the model would handle tool calls in future iterations.

---

## 4. [Quiet Threadripper AI Workstation - 768GB DDR5 and 160GB VRAM (RTX 5090 + 4x R9700)](https://reddit.com/r/LocalLLaMA/comments/1qkghpk/quiet_threadripper_ai_workstation_768gb_ddr5_and/)

**Author:** u/sloptimizer | **Upvotes:** 117 | **Comments:** 71 | **Date:** 2026-01-22

**Summary:** The Reddit post details a high-performance AI workstation build featuring an RTX 5090 and four R9700 GPUs, with 768GB DDR5 RAM and 160GB VRAM. The user shares performance metrics for DeepSeek-V3.1-Terminus and provides tips for optimizing the system, including cooling solutions and power management.

**Key Points:**
- The workstation includes an RTX 5090 and four R9700 GPUs, with a total of 768GB DDR5 RAM and 160GB VRAM.
- Performance metrics for DeepSeek-V3.1-Terminus show 151.76 tokens per second for prompt processing and 10.85 tokens per second for token generation.
- Key optimizations include adding RAM fans for better cooling, disabling remote management for faster boot times, and adjusting power limits for quieter operation.
- The build uses two power supplies: a 1600W unit for the main system and an 850W unit for three of the Radeon GPUs.
- The top comment highlights the impressive performance of the setup, calling it near-state-of-the-art.

**Discussion Highlights:** The discussion highlights the impressive performance of the workstation, with users expressing admiration for the setup and its capabilities. Some comments humorously inquire about the cost and the number of 'kidneys' required to afford such a build.

---

## 5. [Am I the only one who feels that, with all the AI boom, everyone is basically doing the same thing?](https://reddit.com/r/LocalLLaMA/comments/1qk8zj1/am_i_the_only_one_who_feels_that_with_all_the_ai/)

**Author:** u/Empty_Enthusiasm_167 | **Upvotes:** 340 | **Comments:** 174 | **Date:** 2026-01-22

**Summary:** The post discusses the redundancy in AI tools and applications during the AI boom, noting that many new tools are less polished versions of existing ones. The discussion highlights the enthusiasm and low barrier to entry in the field, leading to shallow implementations and repetitive projects. Key points include the redundancy of AI tools, the low barrier to entry leading to shallow implementations, and the focus on niche tools addressing specific needs. The discussion highlights a consensus that the AI field is in a hype phase, with many redundant and unoriginal projects, but also shows a focus on niche tools and applications.

---

## 6. [vLLM raising $150M confirms it: We have moved from the "Throughput Era" to the "Latency(Cold Starts)."](https://reddit.com/r/LocalLLaMA/comments/1qk68n8/vllm_raising_150m_confirms_it_we_have_moved_from/)

**Author:** u/pmv143 | **Upvotes:** 159 | **Comments:** 87 | **Date:** 2026-01-22

**Summary:** The Reddit post discusses the significant investment in vLLM, signaling a shift from the 'Throughput Era' to the 'Latency Era' in AI development. The focus is now on improving serving efficiency and latency, particularly cold starts and time-to-first-token.

**Key Points:**
- vLLM's $150M funding at an $800M valuation indicates a shift from training to serving in AI development.
- Software optimization (e.g., PagedAttention) is crucial for utilizing hardware efficiently.
- The debate between horizontal compatibility (supporting AMD/Intel) and vertical optimization (improving CUDA performance) is highlighted.
- Cold starts and latency are identified as the next major challenges in AI serving.
- The discussion includes skepticism about investment trends and comparisons to other inference engines like llama.cpp.

**Discussion Highlights:** The discussion highlights skepticism about interpreting investments as definitive trends, comparisons to other inference engines like llama.cpp, and differing opinions on the importance of cold starts in cloud environments versus local setups.

---

## 7. [Qwen have open-sourced the full family of Qwen3-TTS: VoiceDesign, CustomVoice, and Base, 5 models (0.6B &amp; 1.8B), Support for 10 languages](https://reddit.com/r/LocalLLaMA/comments/1qjul5t/qwen_have_opensourced_the_full_family_of_qwen3tts/)

**Author:** u/Nunki08 | **Upvotes:** 676 | **Comments:** 93 | **Date:** 2026-01-22

**Summary:** Qwen has open-sourced the Qwen3-TTS model family, including VoiceDesign, CustomVoice, and Base models in 0.6B and 1.8B sizes, supporting 10 languages. Resources are available on GitHub, Hugging Face, and other platforms.

**Key Points:**
- Qwen3-TTS models (0.6B & 1.8B) open-sourced
- Supports 10 languages
- Resources available on GitHub, Hugging Face, blog, paper, and demo
- Community feedback highlights English voice quality and requests for llama.cpp support
- Appreciation for open-source efforts and positive feedback on sample quality

**Discussion Highlights:** The community appreciates Qwen's open-source efforts but notes concerns about English voice quality and requests support for running models in llama.cpp. Positive feedback on sample quality and overall excitement about the release.

---

## 8. [Qwen dev on Twitter!!](https://reddit.com/r/LocalLLaMA/comments/1qjtyw8/qwen_dev_on_twitter/)

**Author:** u/Difficult-Cap-7527 | **Upvotes:** 705 | **Comments:** 60 | **Date:** 2026-01-22

**Summary:** The Reddit post discusses Qwen's TTS model announcement, with community reactions and links to the model on Hugging Face.

**Key Points:**
- Qwen's TTS model announcement
- Community reaction and discussion
- Link to the model on Hugging Face
- Thread locked due to announcements being out
- Mention of vLLM leak related to the TTS model

**Discussion Highlights:** The community is excited about the Qwen TTS model, with some users sharing links to the model on Hugging Face. There is also mention of a vLLM leak related to the TTS model, and the thread was locked as announcements are out.

---

## 9. [GLM 4.7 flash FA fix for CUDA has been merged into llama.cpp](https://reddit.com/r/LocalLLaMA/comments/1qjrsur/glm_47_flash_fa_fix_for_cuda_has_been_merged_into/)

**Author:** u/jacek2023 | **Upvotes:** 157 | **Comments:** 51 | **Date:** 2026-01-22

**Summary:** The post announces the merge of GLM 4.7 flash FA fix for CUDA into llama.cpp, with discussions highlighting performance issues and successful builds.

**Key Points:**
- GLM 4.7 flash FA fix for CUDA has been merged into llama.cpp
- Quantized cache performance issues reported
- Successful builds reported by users
- Performance issues on Pascal GPUs noted
- Ongoing bug reports and discussions

**Discussion Highlights:** Users report mixed experiences with the new fix, noting performance issues on certain hardware and successful builds with specific configurations.

---

## 10. [Fei Fei Li dropped a non-JEPA world model, and the spatial intelligence is insane](https://reddit.com/r/LocalLLaMA/comments/1qjjrmq/fei_fei_li_dropped_a_nonjepa_world_model_and_the/)

**Author:** u/coloradical5280 | **Upvotes:** 182 | **Comments:** 86 | **Date:** 2026-01-21

**Summary:** Fei-Fei Li's World Labs launched Marble, a generative world model using Neural Radiance Fields (NeRF) and Gaussian splatting, enabling fast 3D world creation with stateful, editable environments and VR support. Despite its innovative approach, the technology has faced criticism for not being open-source and for its limited scope.

**Key Points:**
- Marble uses NeRF and Gaussian splatting for fast 3D world generation
- Environments are stateful, editable, and support VR and exports to Unreal, Unity, or Blender
- Criticism includes lack of open-source availability and skepticism about it being a true 'world model'
- Mixed reactions with some users finding the environments too small and limited
- Fei-Fei Li's low-key approach has resulted in less attention for Marble

**Discussion Highlights:** The discussion highlights mixed reactions, with some users criticizing the lack of open-source availability and the limited scope of the environments. Others appreciate the technology's potential and innovative approach, despite its current rough edges.

---

## 11. [Wrote a guide for running Claude Code with GLM-4.7 Flash locally with llama.cpp](https://reddit.com/r/LocalLLaMA/comments/1qjf6ys/wrote_a_guide_for_running_claude_code_with_glm47/)

**Author:** u/tammamtech | **Upvotes:** 111 | **Comments:** 45 | **Date:** 2026-01-21

**Summary:** The Reddit post provides a guide for running Claude Code with GLM-4.7 Flash locally using llama.cpp, highlighting the motivation, installation steps, and configuration details for optimal performance. Key points include replicating Ollama features, specific commands for direct and Docker setups, recommended sampling parameters, and a multi-model setup for advanced users. The discussion highlights clarifications on the implementation timeline and suggestions for open-source alternatives like OpenCode and Harbor.

---

## 12. [8x AMD MI50 32GB at 26 t/s (tg) with MiniMax-M2.1 and 15 t/s (tg) with GLM 4.7 (vllm-gfx906)](https://reddit.com/r/LocalLLaMA/comments/1qjaxfy/8x_amd_mi50_32gb_at_26_ts_tg_with_minimaxm21_and/)

**Author:** u/ai-infos | **Upvotes:** 310 | **Comments:** 121 | **Date:** 2026-01-21

**Summary:** The post details a cost-effective local inference setup using 8x AMD MI50 GPUs, achieving high token generation speeds with MiniMax-M2.1 and GLM 4.7 models. The setup is praised for its performance and affordability, with a total VRAM of 256GB for under $1k. Key points include the performance metrics of the models, the cost and power efficiency of the setup, and the community's positive reception.

---

## 13. [VibeVoice-ASR released!](https://reddit.com/r/LocalLLaMA/comments/1qj40er/vibevoiceasr_released/)

**Author:** u/k_means_clusterfuck | **Upvotes:** 148 | **Comments:** 44 | **Date:** 2026-01-21

**Summary:** Microsoft released VibeVoice-ASR, a multilingual automatic speech recognition model. Users report high accuracy, especially in multilingual contexts, though some note challenges with polyphonic characters in names.

**Key Points:**
- VibeVoice-ASR is a multilingual ASR model released by Microsoft.
- Users report high accuracy, with one test showing 91% accuracy on Chinese audio.
- The model is large (9B parameters), raising questions about its efficiency compared to smaller models like Parakeet.
- Comparisons to Whisper highlight its performance in diarization and transcription.
- Some users emphasize the importance of backups when testing new models.

**Discussion Highlights:** The discussion highlights the model's high accuracy and multilingual capabilities, with users sharing their test results and comparisons to other ASR models like Whisper and Parakeet. Some users noted challenges with specific linguistic features, such as polyphonic characters in names.

---

## 14. [One-shot single page web development: pacman clone - GLM 4.7 vs GLM 4.7 Flash vs GLM 4.5 Air vs Gemini 3 Pro vs Gemini 3 Flash - Results available for online testing - Prompt and instructions provided for testing with other models](https://reddit.com/r/LocalLLaMA/comments/1qj13uh/oneshot_single_page_web_development_pacman_clone/)

**Author:** u/ex-arman68 | **Upvotes:** 106 | **Comments:** 48 | **Date:** 2026-01-21

**Summary:** The Reddit post compares AI models' performance in one-shot web development by creating a Pacman clone. GLM 4.7 emerged as the clear winner, outperforming Gemini models, which was unexpected. The post provides detailed results and links to test each model's output. Key points include: GLM 4.7 ranked as the best performer, followed by Minimax M2.1 and Gemini 3 Flash; Gemini 3 Pro underperformed compared to expectations; Temperature setting of 0 was found to improve results and reproducibility; The post includes links to test each model's generated Pacman game; Discussion highlights the effectiveness of this testing methodology and the surprising performance of GLM 4.7. The discussion emphasizes the usefulness of this testing approach and expresses surprise at GLM 4.7's performance over Gemini models. Some users shared additional test results and praised the methodology.

---

## 15. [GLM-4.7-Flash-GGUF bug fix - redownload for better outputs](https://reddit.com/r/LocalLLaMA/comments/1qiy0ha/glm47flashgguf_bug_fix_redownload_for_better/)

**Author:** u/etherd0t | **Upvotes:** 111 | **Comments:** 58 | **Date:** 2026-01-21

**Summary:** The post announces a bug fix for the GLM-4.7-Flash-GGUF model, which previously caused looping and poor outputs. Users are advised to re-download the model for improved performance and provided with recommended parameters for optimal use.

**Key Points:**
- Bug fix for looping and poor outputs in GLM-4.7-Flash-GGUF
- Recommended parameters: --temp 1.0 --top-p 0.95 for general use, --temp 0.7 --top-p 1.0 for tool-calling, and --min-p 0.01 for llama.cpp
- Positive user feedback on the fixed version's performance
- Performance comparison with other models like GPT-OSS-20b
- User appreciation for the update and bug fix

**Discussion Highlights:** Users express satisfaction with the bug fix, noting significant improvements in performance and usability. Some users compare the model's speed with other models and discuss potential future optimizations.

---

## 16. [Fix for GLM 4.7 Flash has been merged into llama.cpp](https://reddit.com/r/LocalLLaMA/comments/1qiwm3c/fix_for_glm_47_flash_has_been_merged_into_llamacpp/)

**Author:** u/jacek2023 | **Upvotes:** 310 | **Comments:** 86 | **Date:** 2026-01-21

**Summary:** The Reddit post announces that a fix for GLM 4.7 Flash has been merged into llama.cpp, with ongoing work on CUDA support. The community is actively discussing performance and compatibility.

**Key Points:**
- Fix for GLM 4.7 Flash merged into llama.cpp
- CUDA support in progress via GitHub pull request
- Community discussing performance metrics and compatibility
- Positive feedback on model improvements
- Discussion on CPU-only performance for users without GPUs

**Discussion Highlights:** The community is generally positive about the fix, with discussions focusing on performance metrics, compatibility with different hardware (GPU vs CPU), and ongoing development for CUDA support. Some users report significant improvements in model behavior.

---

## 17. [Knowledge distillation with Claude as the interface: trained a 0.6B model to match GPT-class performance on Text2SQL in a singe conversation](https://reddit.com/r/LocalLLaMA/comments/1qiu6jo/knowledge_distillation_with_claude_as_the/)

**Author:** u/party-horse | **Upvotes:** 168 | **Comments:** 37 | **Date:** 2026-01-21

**Summary:** The post describes a workflow for training small, task-specific models using knowledge distillation via Claude, achieving significant performance improvements on Text2SQL tasks with minimal setup overhead.

**Key Points:**
- Small models like Qwen3 0.6B perform poorly on specialized tasks like Text2SQL.
- Knowledge distillation via Claude simplifies the training process by automating data preparation, evaluation, and training.
- The fine-tuned 0.6B model achieved a 74% score compared to the base model's 36%.
- The approach was well-received, with commenters highlighting its potential for on-device agents and log analysis.
- Some discussion focused on the use of Claude and the potential for open-source alternatives.

**Discussion Highlights:** The community praised the approach for its simplicity and effectiveness, with suggestions for broader applications and debates about the necessity of using Claude over open-source tools.

---

## 18. [vLLM v0.14.0 released](https://reddit.com/r/LocalLLaMA/comments/1qim0e9/vllm_v0140_released/)

**Author:** u/jinnyjuice | **Upvotes:** 166 | **Comments:** 32 | **Date:** 2026-01-20

**Summary:** The Reddit post announces the release of vLLM v0.14.0, highlighting new features and updates. Users discuss improvements like automatic context length fitting and the deprecation of certain quantization methods.

**Key Points:**
- Automatic context length fitting to GPU memory to prevent OOM failures
- Deprecation of some quantization methods, including HQQ
- Introduction of Marlin for Turing (sm75) as a major upgrade
- User anticipation for future optimizations like sm120

**Discussion Highlights:** Users expressed excitement about the automatic context length feature and discussed the implications of deprecated quantization methods. The Marlin upgrade for Turing was noted as a significant improvement, and there was anticipation for future optimizations.

---

## 19. [Current GLM-4.7-Flash implementation confirmed to be broken in llama.cpp](https://reddit.com/r/LocalLLaMA/comments/1qih9r8/current_glm47flash_implementation_confirmed_to_be/)

**Author:** u/Sweet_Albatross9772 | **Upvotes:** 243 | **Comments:** 58 | **Date:** 2026-01-20

**Summary:** The Reddit post discusses issues with the current GLM-4.7-Flash implementation in llama.cpp, highlighting significant differences in logprobs compared to vLLM, which may explain reported problems like looping and poor performance. A potential fix is already proposed in a pull request.

**Key Points:**
- Current GLM-4.7-Flash implementation in llama.cpp is confirmed broken.
- Significant differences in logprobs compared to vLLM are noted.
- A potential fix is available in a pull request.
- Community acknowledges the issue and expects a resolution soon.
- Some users suggest waiting before downloading new models to avoid bugs.

**Discussion Highlights:** The discussion highlights a confirmed issue with the GLM-4.7-Flash implementation in llama.cpp, with users acknowledging the problem and pointing to a potential fix. The community is generally patient, recognizing that such issues are common with new model integrations and are usually resolved quickly.

---

## 20. [You have 64gb ram and 16gb VRAM; internet is permanently shut off: what 3 models are the ones you use?](https://reddit.com/r/LocalLLaMA/comments/1qids6a/you_have_64gb_ram_and_16gb_vram_internet_is/)

**Author:** u/Adventurous-Gold6413 | **Upvotes:** 538 | **Comments:** 298 | **Date:** 2026-01-20

**Summary:** The post discusses the selection of local models for use with 64GB RAM and 16GB VRAM when internet access is unavailable. Users share their preferred models and experiences.

**Key Points:**
- The post asks for recommendations on local models to use with specific hardware constraints.
- Top comments highlight models like Gemma 3 27B, GLM 4.5 Air, and GPT-OSS 120B.
- GPT-OSS 120B is praised for its performance and versatility on the given hardware.
- The community appreciates the contribution and engages in a lively discussion.
- Some users humorously suggest using books as an alternative to models.

**Discussion Highlights:** The discussion highlights a consensus around models like GPT-OSS 120B, which is noted for fitting well on the specified hardware and offering good performance across various domains. Other models like Gemma 3 27B and GLM 4.5 Air are also mentioned as strong contenders. The community shows appreciation for the post and engages in a mix of serious recommendations and light-hearted suggestions.

---

## 21. [Liquid AI released the best thinking Language Model Under 1GB](https://reddit.com/r/LocalLLaMA/comments/1qi512t/liquid_ai_released_the_best_thinking_language/)

**Author:** u/PauLabartaBajo | **Upvotes:** 228 | **Comments:** 52 | **Date:** 2026-01-20

**Summary:** Liquid AI released LFM2.5-1.2B-Thinking, a compact reasoning model optimized for on-device use, excelling in math, tool use, and instruction following. It outperforms larger models in speed and memory efficiency, though some users question its real-world applicability and licensing terms.

**Key Points:**
- LFM2.5-1.2B-Thinking is a 1.2B parameter model designed for concise reasoning and edge deployment.
- It outperforms larger models in speed and memory efficiency, despite having fewer parameters.
- The model is available on Hugging Face, LEAP, and Liquid AI Playground.
- Users raised concerns about memory requirements, performance trade-offs, and licensing.
- Some users wish for larger models with broader real-world applicability.

**Discussion Highlights:** The discussion highlights concerns about memory usage, with users noting that the benchmarked model requires at least 2GB of memory. There is also debate about the model's performance trade-offs, particularly in non-math tasks, and criticism of its non-Apache/MIT licensing.

---

## 22. [768Gb Fully Enclosed 10x GPU Mobile AI Build](https://reddit.com/r/LocalLLaMA/comments/1qi4uj2/768gb_fully_enclosed_10x_gpu_mobile_ai_build/)

**Author:** u/SweetHomeAbalama0 | **Upvotes:** 872 | **Comments:** 261 | **Date:** 2026-01-20

**Summary:** The post describes a custom-built, fully enclosed mobile AI system with 10 GPUs, designed for running large MoE models and supporting graphic design tasks. The build balances performance and cost, using a mix of GPUs and a sturdy enclosure to protect components from pets.

**Key Points:**
- The system features a Threadripper Pro 3995WX, 512GB DDR4, and 10 GPUs (8x 3090 + 2x 5090).
- It is designed for large MoE models, video generation, and high-detail image generation.
- The enclosure ensures mobility and protection from pets, addressing a key challenge.
- The total cost was around $17k, balancing performance and budget constraints.
- The post received significant engagement, with comments highlighting its uniqueness and practicality.

**Discussion Highlights:** The discussion highlights the system's impressive capabilities and the creative solution to the enclosure problem. Comments also joke about its portability and power requirements, emphasizing its uniqueness in the community.

---

## 23. [Over 6K novels with reasoning traces to train full book writing LLMs](https://reddit.com/r/LocalLLaMA/comments/1qi3nmd/over_6k_novels_with_reasoning_traces_to_train/)

**Author:** u/XMasterDE | **Upvotes:** 110 | **Comments:** 46 | **Date:** 2026-01-20

**Summary:** The post announces an update to the LongPage dataset, expanding it to over 6,000 novels with hierarchical reasoning traces for training full-book writing LLMs. The team is also training a model on this dataset and plans to release it soon.

**Key Points:**
- LongPage dataset updated to include over 6,000 novels with reasoning traces.
- The dataset supports training full-book writing LLMs with hierarchical planning traces.
- A full-book writing model is being trained and will be released once quality standards are met.
- The post includes links to the dataset and the team's social media/website.
- Top comments express interest in the project and request more details about the dataset and model.

**Discussion Highlights:** The discussion highlights enthusiasm for the project, with users expressing interest in the potential of the dataset and model for fiction writing. Some users request more details about the dataset structure and model functionality, while others inquire about the inclusion of specific works and the possibility of multilingual datasets.

---

## 24. [glm-4.7-flash has the best thinking process with clear steps, I love it](https://reddit.com/r/LocalLLaMA/comments/1qhxlgy/glm47flash_has_the_best_thinking_process_with/)

**Author:** u/uptonking | **Upvotes:** 140 | **Comments:** 34 | **Date:** 2026-01-20

**Summary:** The Reddit post discusses the user's experience with the glm-4.7-flash model, highlighting its structured thinking process and comparing it favorably to other models like nemotron-nano and qwen3-30b. The user appreciates the model's clear reasoning steps but notes its slow performance and occasional looping issues.

**Key Points:**
- glm-4.7-flash has a detailed and structured thinking process with clear steps.
- The model's thinking duration is longer compared to other models, but the quality of reasoning is preferred.
- The user faces performance issues with slow token generation and occasional looping.
- Adjusting parameters like temperature and repeat penalty helps improve performance.
- The community generally appreciates the model's reasoning process but acknowledges its performance limitations.

**Discussion Highlights:** The discussion highlights a consensus on the model's superior reasoning process but also acknowledges its performance issues. Users share tips on parameter adjustments to improve performance and express overall satisfaction with the model's reasoning capabilities.

---

## 25. [It's been one year since the release of Deepseek-R1](https://reddit.com/r/LocalLLaMA/comments/1qhs2sd/its_been_one_year_since_the_release_of_deepseekr1/)

**Author:** u/Recoil42 | **Upvotes:** 295 | **Comments:** 51 | **Date:** 2026-01-19

**Summary:** The Reddit post commemorates the one-year anniversary of the release of Deepseek-R1, highlighting its significant impact on the AI community. The discussion reflects on the rapid advancements and changes in the field over the past year.

**Key Points:**
- Deepseek-R1 had a major impact, leading to significant changes in the AI landscape.
- The release was so impactful that it reportedly caused major disruptions, including the disbanding of a flagship AI training team.
- The rapid pace of advancements in AI is noted, with the past year feeling like several years due to the volume of changes.
- Deepseek-R1 is considered one of the most important releases, second only to the original Llama model.
- There is curiosity about the progress of smaller models and their performance relative to R1.

**Discussion Highlights:** The discussion highlights the transformative impact of Deepseek-R1, with users noting its disruptive effects on the AI community and the rapid pace of advancements. There is also interest in measuring the progress of smaller models compared to R1.

---

## 26. [Mosquito - 7.3M parameter tiny knowledge model](https://reddit.com/r/LocalLLaMA/comments/1qhqzsi/mosquito_73m_parameter_tiny_knowledge_model/)

**Author:** u/Lopsided-Repair-3638 | **Upvotes:** 115 | **Comments:** 53 | **Date:** 2026-01-19

**Summary:** The Reddit post introduces 'Mosquito,' a tiny knowledge model with 7.3M parameters that can answer general knowledge questions, though with some humorous inaccuracies. The demo and model are available on Hugging Face. Key points include the model's capabilities and notable inaccuracies, such as defining a dog incorrectly. Users have requested a quantized version of the model and highlighted its limitations with humorous examples, while also expressing interest in improvements like quantization.

---

## 27. [Bartowski comes through again. GLM 4.7 flash GGUF](https://reddit.com/r/LocalLLaMA/comments/1qhpima/bartowski_comes_through_again_glm_47_flash_gguf/)

**Author:** u/RenewAi | **Upvotes:** 183 | **Comments:** 50 | **Date:** 2026-01-19

**Summary:** The post announces the release of GLM 4.7 Flash GGUF by Bartowski, with a link to the Hugging Face repository. Users in the comments discuss their experiences and challenges with the model, including issues with performance and alternative versions.

**Key Points:**
- Bartowski released GLM 4.7 Flash GGUF on Hugging Face.
- Users report mixed results with the model, with some finding it non-functional.
- Alternative versions like Unsloth's 16-bit copy are mentioned.
- The model is available for download and testing.
- Discussion includes troubleshooting and comparisons with other versions.

**Discussion Highlights:** The discussion highlights mixed user experiences, with some reporting issues with the model's performance. There is mention of alternative versions and ongoing troubleshooting efforts.

---

## 28. [Unsloth GLM 4.7-Flash GGUF](https://reddit.com/r/LocalLLaMA/comments/1qhlnsv/unsloth_glm_47flash_gguf/)

**Author:** u/Wooden-Deer-1276 | **Upvotes:** 230 | **Comments:** 44 | **Date:** 2026-01-19

**Summary:** The Reddit post discusses the release of the GLM-4.7-Flash GGUF model, with users sharing feedback on its performance and recommendations for optimal usage. Key points include advising to take time to ensure the model works properly before release, recommending specific quantization settings and parameters for better performance, reporting issues with looping in quantized versions with BF16 suggested for best results, the community actively working on fixes and improvements, and the release of a BF16 version of the model. The discussion highlights the community's engagement in troubleshooting and optimizing the model, focusing on resolving looping issues and recommending specific settings for better performance.

---

## 29. [GLM 4.7 Flash official support merged in llama.cpp](https://reddit.com/r/LocalLLaMA/comments/1qhitrj/glm_47_flash_official_support_merged_in_llamacpp/)

**Author:** u/ayylmaonade | **Upvotes:** 365 | **Comments:** 60 | **Date:** 2026-01-19

**Summary:** The post announces the official support for GLM 4.7 Flash in llama.cpp, highlighting its community-driven development and performance improvements. Users discuss its speed and share additional resources.

**Key Points:**
- GLM 4.7 Flash now officially supported in llama.cpp
- Support is community-driven, not by Z.ai developers
- Performance improvements noted, with some users reporting faster speeds without flash-attention
- Additional resources and model versions shared by users
- Post recognized and featured in the community Discord

**Discussion Highlights:** The discussion highlights the community effort behind the integration and shares performance insights, with some users noting that disabling flash-attention can improve speed. Additional model versions and resources are also shared.

---

## 30. [My gpu poor comrades, GLM 4.7 Flash is your local agent](https://reddit.com/r/LocalLLaMA/comments/1qhii5v/my_gpu_poor_comrades_glm_47_flash_is_your_local/)

**Author:** u/__Maximum__ | **Upvotes:** 459 | **Comments:** 162 | **Date:** 2026-01-19

**Summary:** The Reddit post highlights GLM 4.7 Flash as a reliable local agent, outperforming other MoE models in an agentic framework with successful tool calling and task execution. Users are eager for its local availability via GGUFs.

**Key Points:**
- GLM 4.7 Flash is praised for its reliability and performance in agentic tasks
- It successfully handles complex tasks like cloning repos and running commands
- Users anticipate local use via GGUFs
- Comparisons with Nemotron 30B and Qwen3 are discussed
- Performance benchmarks suggest it is competitive with larger models like SEED OSS 36B

**Discussion Highlights:** The discussion highlights enthusiasm for GLM 4.7 Flash's performance, with users comparing it favorably to other models and noting its efficiency. Some users have already started testing it locally, reporting decent speed and deep reasoning capabilities.

---

## 31. [New in llama.cpp: Anthropic Messages API](https://reddit.com/r/LocalLLaMA/comments/1qhaq21/new_in_llamacpp_anthropic_messages_api/)

**Author:** u/paf1138 | **Upvotes:** 164 | **Comments:** 51 | **Date:** 2026-01-19

**Summary:** The Reddit post announces the introduction of the Anthropic Messages API in llama.cpp, which has been well-received by the community. Users are enthusiastic about trying it out and have shared practical tips for implementation.

**Key Points:**
- Introduction of Anthropic Messages API in llama.cpp
- Enthusiasm and positive reception from the community
- Practical implementation tips shared in comments
- Mentions of specific hardware and context usage

**Discussion Highlights:** The discussion highlights a positive consensus around the new feature, with users sharing practical advice on how to implement and use the API effectively. There is also mention of specific hardware and context usage, indicating a focus on practical applications.

---

## 32. [zai-org/GLM-4.7-Flash · Hugging Face](https://reddit.com/r/LocalLLaMA/comments/1qh5wdq/zaiorgglm47flash_hugging_face/)

**Author:** u/Dark_Fire_12 | **Upvotes:** 734 | **Comments:** 231 | **Date:** 2026-01-19

**Summary:** The Reddit post discusses the release of the zai-org/GLM-4.7-Flash model on Hugging Face, highlighting its technical features and community excitement.

**Key Points:**
- The model uses MLA, reducing KV cache memory usage
- 30B parameter model with potential for 200k context
- Community anticipation and positive reception
- Mention of a 3B 'thinking model' in the codebase

**Discussion Highlights:** The community is excited about the release, particularly noting the model's efficiency with MLA and its potential for long context lengths. There is also nostalgia for larger models (70B) and interest in the technical details of the 3B 'thinking model'.

---

## 33. [I made a Top-K implementation that's up to 20x faster than PyTorch CPU (open source)](https://reddit.com/r/LocalLLaMA/comments/1qh0yq8/i_made_a_topk_implementation_thats_up_to_20x/)

**Author:** u/andreabarbato | **Upvotes:** 150 | **Comments:** 103 | **Date:** 2026-01-19

**Summary:** The author optimized Top-K selection for LLM sampling, achieving 4-20x speed improvements over PyTorch CPU using AVX2 and cache optimizations. The implementation is integrated into llama.cpp, showing significant performance gains.

**Key Points:**
- AVX2-optimized batched Top-K outperforms PyTorch CPU by 4-20x depending on vocab size.
- Integrated into llama.cpp, resulting in 63% faster prompt processing on a 120B MoE model.
- Uses adaptive sampling, AVX2 SIMD, and cache-optimized scanning with fast paths for sorted/constant inputs.
- GitHub repository provided for the implementation.
- Community feedback includes requests for PRs and explanations of the speed improvements.

**Discussion Highlights:** The community showed strong interest, with requests for PRs and explanations of the speed improvements. Some users criticized the lack of reproducible benchmarks and raised concerns about the authenticity of the post.

---

## 34. [how do you pronounce “gguf”?](https://reddit.com/r/LocalLLaMA/comments/1qglyqz/how_do_you_pronounce_gguf/)

**Author:** u/Hamfistbumhole | **Upvotes:** 106 | **Comments:** 154 | **Date:** 2026-01-18

**Summary:** The Reddit post discusses the pronunciation of the term 'gguf' and presents several options for how it might be pronounced. Users share their interpretations and humorous takes in the comments.

**Key Points:**
- The post asks about the pronunciation of 'gguf' with options like 'jee-guff', 'giguff', or 'jee jee you eff'.
- Top comments suggest pronouncing each letter, similar to how '.PNG' is pronounced.
- Other interpretations include 'gee gee you eff', 'guh-GUFF', and 'gê-guf'.
- A humorous comment suggests that 'gguf' is not pronounced but downloaded silently.

**Discussion Highlights:** The discussion highlights a variety of interpretations for pronouncing 'gguf', with no clear consensus. The top comment humorously suggests that 'gguf' is not pronounced but downloaded silently, reflecting a playful tone in the discussion.

---

## 35. [Are most major agents really just markdown todo list processors?](https://reddit.com/r/LocalLLaMA/comments/1qgj2n9/are_most_major_agents_really_just_markdown_todo/)

**Author:** u/TheDigitalRhino | **Upvotes:** 105 | **Comments:** 37 | **Date:** 2026-01-18

**Summary:** The Reddit post discusses how major agents decompose tasks into todo lists and process them sequentially, with users sharing similar observations and examples.

**Key Points:**
- Major agents decompose tasks into todo lists and process them one by one.
- Users confirm this approach with examples and additional context.
- The method has been effective since earlier models like GPT-3.5.
- Breaking down complex tasks into smaller ones is a common human approach as well.

**Discussion Highlights:** The discussion highlights a consensus that major agents use a todo list approach for task decomposition, with users providing examples and additional insights into the effectiveness and history of this method.

---

## 36. [4x AMD R9700 (128GB VRAM) + Threadripper 9955WX Build](https://reddit.com/r/LocalLLaMA/comments/1qgdb7f/4x_amd_r9700_128gb_vram_threadripper_9955wx_build/)

**Author:** u/NunzeCs | **Upvotes:** 345 | **Comments:** 94 | **Date:** 2026-01-18

**Summary:** The author built a high-end system with 4x AMD R9700 GPUs (128GB VRAM) and a Threadripper 9955WX CPU, leveraging a 50% subsidy to stay within a ~10,000€ budget. The system is designed for running large AI models locally, with benchmark results provided for various models.

**Key Points:**
- The build was motivated by a 50% subsidy for digitalization investments, allowing a high-end setup within budget.
- The system features 4x AMD R9700 GPUs (128GB VRAM) and a Threadripper 9955WX CPU, optimized for large AI models.
- Benchmark results show performance metrics for models ranging from 8B to 230B parameters.
- The discussion highlights include admiration for the build and curiosity about the components' sourcing and cost.

**Discussion Highlights:** The discussion features admiration for the build, with comments like 'HE HAS RAM GET HIM...' and 'G O D D A A A A A Y U U U U M...' reflecting excitement. There is also curiosity about the sourcing of components and the author's job.

---

## 37. [Qwen 4 might be a long way off !? Lead Dev says they are "slowing down" to focus on quality.](https://reddit.com/r/LocalLLaMA/comments/1qfv1ms/qwen_4_might_be_a_long_way_off_lead_dev_says_they/)

**Author:** u/Difficult-Cap-7527 | **Upvotes:** 456 | **Comments:** 71 | **Date:** 2026-01-17

**Summary:** The Reddit post discusses the potential delay in Qwen 4 development, as the lead developer mentions slowing down to focus on quality. The community generally appreciates this focus on quality over quantity.

**Key Points:**
- Qwen 4 development may be delayed to focus on quality
- Community appreciates the focus on quality over quantity
- Some users caution against jumping to conclusions based on limited information
- General consensus that incremental improvements aren't meaningful for advancement
- Post gained popularity and was featured on Discord

**Discussion Highlights:** The discussion highlights a positive reception to the focus on quality, with many users expressing appreciation for taking the necessary time to improve the Qwen series. Some users also advise caution against spreading rumors based on limited information.

---

## 38. [128GB VRAM quad R9700 server](https://reddit.com/r/LocalLLaMA/comments/1qfscp5/128gb_vram_quad_r9700_server/)

**Author:** u/Ulterior-Motive_ | **Upvotes:** 532 | **Comments:** 117 | **Date:** 2026-01-17

**Summary:** The author upgraded from MI100s to four R9700 GPUs, building a 128GB VRAM server for under $7,035, showcasing impressive performance benchmarks and cost efficiency compared to alternatives like the RTX 6000 Blackwell. Key points include the upgrade rationale, detailed hardware specifications, performance benchmarks, and positive community feedback. The community praised the build, with comments highlighting its appeal and the author's financial irresponsibility joke, indicating strong interest and approval.

---

## 39. [The Search for Uncensored AI (That Isn’t Adult-Oriented)](https://reddit.com/r/LocalLLaMA/comments/1qfq9ez/the_search_for_uncensored_ai_that_isnt/)

**Author:** u/Fun-Situation-4358 | **Upvotes:** 277 | **Comments:** 216 | **Date:** 2026-01-17

**Summary:** The post discusses the challenge of finding uncensored AI models that prioritize reasoning and creativity over adult-oriented content, highlighting a gap in the market between heavily restricted corporate AI and shallow adult-focused models.

**Key Points:**
- The author seeks an AI that is genuinely unfiltered and technically advanced, focusing on reasoning and creativity.
- Many models marketed as 'uncensored' are optimized for adult use rather than intelligence or depth.
- There is a perceived gap between heavily restricted corporate AI and shallow adult-focused models.
- Techniques used to decensor open-source models often reduce their intelligence.
- The Uncensored General Intelligence Leaderboard is suggested as a resource.

**Discussion Highlights:** The discussion highlights a shared frustration with the lack of AI models that balance uncensored capabilities with serious problem-solving and creativity. Many users agree that most uncensored models are either too restricted or too focused on adult content, leaving a gap for models that prioritize reasoning and technical depth.

---

## 40. [China's AGI-NEXT Conference (Qwen, Kimi, Zhipu, Tencent)](https://reddit.com/r/LocalLLaMA/comments/1qfmc05/chinas_aginext_conference_qwen_kimi_zhipu_tencent/)

**Author:** u/nuclearbananana | **Upvotes:** 119 | **Comments:** 22 | **Date:** 2026-01-17

**Summary:** The Reddit post discusses China's AGI-NEXT Conference, highlighting insights on China vs US AGI development, paths to AGI, compute, and marketing. It mentions internal advancements like Qwen3.5 and large context windows, and notes the absence of Deepseek despite their talent concentration.

**Key Points:**
- Qwen has internally developed Qwen3.5 and context windows in the millions.
- The next paradigm in AI is believed to likely come from OpenAI rather than Google.
- Chinese work culture is described as less willing to take risks for innovation.
- Deepseek, despite having strong talent, was notably absent from the conference.

**Discussion Highlights:** The discussion highlights advancements in Chinese AI models like Qwen3.5 and the belief that OpenAI may lead the next AI paradigm. There is also a note on the risk-averse culture in Chinese AI development and the absence of Deepseek from the conference.

---

## 41. [Best "End of world" model that will run on 24gb VRAM](https://reddit.com/r/LocalLLaMA/comments/1qfkn3a/best_end_of_world_model_that_will_run_on_24gb_vram/)

**Author:** u/gggghhhhiiiijklmnop | **Upvotes:** 346 | **Comments:** 180 | **Date:** 2026-01-17

**Summary:** The user is seeking recommendations for the best LLM models that can run on a PC with 24GB VRAM and 64GB RAM, motivated by a desire to hoard data in an 'end of world' scenario. The discussion highlights various suggestions, including prioritizing the best available models and considering practical solutions like running models off SSD.

**Key Points:**
- User wants to download and store models that fit within 24GB VRAM and 64GB RAM.
- Suggestions include saving the best LLM available and running it off SSD if necessary.
- Specific model recommendations include gemma3:27b and Midnight Miku.
- Advice to download actual Wikipedia backups for offline access.
- Discussion emphasizes practicality and preparedness in an 'end of world' scenario.

**Discussion Highlights:** The discussion consensus leans towards prioritizing the best available models and practical solutions for running them, even if it means using alternative storage methods like SSDs. There is also a focus on ensuring access to essential data like Wikipedia backups.

---

## 42. [KoboldCpp v1.106 finally adds MCP server support, drop-in replacement for Claude Desktop](https://reddit.com/r/LocalLLaMA/comments/1qfb0gk/koboldcpp_v1106_finally_adds_mcp_server_support/)

**Author:** u/HadesThrowaway | **Upvotes:** 104 | **Comments:** 22 | **Date:** 2026-01-17

**Summary:** KoboldCpp v1.106 introduces native MCP server support, offering a drop-in replacement for Claude Desktop with compatibility for existing configurations and support for both HTTP and STDIO transports. The update includes a UI overhaul and allows third-party clients to use the MCP bridge. The community response is positive, highlighting the ease of integration and compatibility.

**Key Points:**
- KoboldCpp v1.106 adds native MCP server support
- Designed as a drop-in replacement for Claude Desktop
- Supports both HTTP and STDIO transports
- Community appreciates the compatibility and ease of use
- Requests for similar features in other tools like llama.cpp

**Discussion Highlights:** The community response is overwhelmingly positive, with users praising the compatibility with existing Claude Desktop configurations and the ease of integration. There is also interest in seeing similar MCP support in other tools like llama.cpp.

---

## 43. [DeepSeek Engram : A static memory unit for LLMs](https://reddit.com/r/LocalLLaMA/comments/1qf5oj0/deepseek_engram_a_static_memory_unit_for_llms/)

**Author:** u/Technical-Love-8479 | **Upvotes:** 321 | **Comments:** 48 | **Date:** 2026-01-17

**Summary:** DeepSeek AI introduced Engram, a memory unit for LLMs that separates remembering from reasoning, enabling O(1) knowledge lookup and improving performance without GPU limits.

**Key Points:**
- Engram introduces conditional memory, separating it from reasoning.
- Knowledge lookup is O(1), improving efficiency.
- Enables massive memory scaling without GPU constraints.
- Improves reasoning, math, and code performance.
- Frees attention for global reasoning rather than static knowledge.

**Discussion Highlights:** The community highlights the significance of separating memory from reasoning, the efficiency of O(1) lookup, and the potential for scaling memory independently of model size.

---

## 44. ["Welcome to the Local Llama. How janky's your rig?](https://reddit.com/r/LocalLLaMA/comments/1qf514i/welcome_to_the_local_llama_how_jankys_your_rig/)

**Author:** u/ForsookComparison | **Upvotes:** 104 | **Comments:** 22 | **Date:** 2026-01-16

**Summary:** The Reddit post in r/LocalLLaMA discusses various unconventional and humorous setups for running GPUs, highlighting the creative and sometimes janky solutions users employ to manage their hardware.

**Key Points:**
- Users share unconventional methods for setting up GPUs, such as using pallet wood for support.
- Discussion includes humorous remarks about hardware limitations and sacrifices.
- Mentions of specific hardware like MI50 GPUs and their cooling solutions.
- Comments reflect a community that enjoys sharing and laughing about their unique setups.

**Discussion Highlights:** The discussion highlights a lighthearted and supportive community where users share their creative and sometimes humorous solutions to hardware challenges, with a focus on unconventional setups and the trials of managing powerful GPUs.

---

## 45. [Prompt Repetition Improves Non-Reasoning LLMs - a paper](https://reddit.com/r/LocalLLaMA/comments/1qeuh0z/prompt_repetition_improves_nonreasoning_llms_a/)

**Author:** u/Foreign-Beginning-49 | **Upvotes:** 112 | **Comments:** 51 | **Date:** 2026-01-16

**Summary:** The Reddit post discusses a paper showing that repeating prompts can significantly improve the performance of non-reasoning LLMs without affecting latency or output format. The technique is simple yet effective, as demonstrated by benchmark scores. Key points include: Prompt repetition improves non-reasoning LLM performance, no impact on latency or output format, simple yet effective technique with notable benchmark gains, Deepseek is highlighted as an open weights model tested, and discussion highlights potential for other undiscovered simple tricks. The discussion emphasizes the simplicity and effectiveness of the technique, with users expressing surprise at its impact. There is speculation about other potential undiscovered tricks and the current limitations in understanding LLMs.

---

