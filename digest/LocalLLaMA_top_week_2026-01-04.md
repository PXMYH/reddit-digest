# r/LocalLLaMA Reading Digest

**Period:** 2026-01-04 to 2026-01-04
**Posts Summarized:** 30
**Total Posts Analyzed:** 30

---

## 1. [Don't sleep on granite 4 small if you got an 8+32+ system](https://reddit.com/r/LocalLLaMA/comments/1q2s3hp/dont_sleep_on_granite_4_small_if_you_got_an_832/)

**Author:** u/Zestyclose-Shift710 | **Upvotes:** 111 | **Comments:** 44 | **Date:** 2026-01-03

**Summary:** The post highlights the performance of Granite 4 Small, a hybrid transformer+mamba model, on a system with 8GB VRAM and 32GB RAM. By using a MoE setup and keeping experts in CPU, the user achieved ~7 tkps with a 50-page context, demonstrating its efficiency compared to other models.

**Key Points:**
- Granite 4 Small (32B total / 9B activated) maintains speed (~7 tkps) even with large context (~50.5k tokens).
- The setup involves using a MoE model with experts kept in CPU, freeing up VRAM for context.
- Comparisons with Qwen 30B A3B and other models are discussed in the comments.
- Performance metrics and benchmarks are shared, including speeds on different hardware.
- The post suggests Granite 4 Small is a viable option for systems with limited VRAM.

**Discussion Highlights:** The discussion includes comparisons with other models like Qwen 30B A3B, mentions of performance issues with Vulkan inference, and benchmarks shared by users. Some users suggest optimizations for MoE models and highlight the efficiency of Granite 4 Small in specific setups.

---

## 2. [GLM-4.7-REAP-50-W4A16: 50% Expert-Pruned + INT4 Quantized GLM-4 (179B params, ~92GB)](https://reddit.com/r/LocalLLaMA/comments/1q2pons/glm47reap50w4a16_50_expertpruned_int4_quantized/)

**Author:** u/Maxious | **Upvotes:** 171 | **Comments:** 67 | **Date:** 2026-01-03

**Summary:** The post introduces GLM-4.7-REAP-50-W4A16, a 50% expert-pruned and INT4 quantized version of GLM-4 with 179B parameters (~92GB). The discussion focuses on calibration details, benchmarking, and comparisons with other models.

**Key Points:**
- GLM-4.7-REAP-50-W4A16 is a 50% expert-pruned and INT4 quantized version of GLM-4 with 179B parameters (~92GB).
- The discussion highlights the need for details on expert activation during calibration.
- REAP pruning is based on expert activation frequency during inference on a calibration set.
- Benchmarks are in progress, and comparisons with other models like MiniMax M2.1 and EXL3 are suggested.
- Subjective comparisons with previous versions (e.g., 4.6 REAP) indicate EXL3 may perform better.

**Discussion Highlights:** The discussion emphasizes the importance of calibration details for quantized models and expresses interest in benchmark results. There is also a suggestion to explore similar versions of other models like MiniMax M2.1. Subjective comparisons indicate that EXL3 may outperform previous REAP versions.

---

## 3. [What is the smartest uncensored nsfw LLM you can run with 20GB VRAM and 24GB RAM](https://reddit.com/r/LocalLLaMA/comments/1q2o033/what_is_the_smartest_uncensored_nsfw_llm_you_can/)

**Author:** u/Death_12_35_taken | **Upvotes:** 176 | **Comments:** 73 | **Date:** 2026-01-03

**Summary:** The post seeks recommendations for an uncensored, smart, and fast LLM that can run locally with 20GB VRAM and 24GB RAM. The community suggests several models, with Dolphin-Mistral-24B-Venice-Edition being the most recommended.

**Key Points:**
- User seeks an uncensored, smart, and fast LLM for local use
- Model should stay in character and be creative
- Top recommendation: Dolphin-Mistral-24B-Venice-Edition
- Other suggestions include models from UGI-Leaderboard and Huihui-Qwen3-VL-30B-A3B-Instruct-abliterated
- Community emphasizes local running efficiency and performance

**Discussion Highlights:** The discussion highlights several models that meet the user's criteria, with Dolphin-Mistral-24B-Venice-Edition being the most upvoted and recommended option. Other models like those from UGI-Leaderboard and Huihui-Qwen3-VL-30B-A3B-Instruct-abliterated are also suggested, emphasizing their suitability for local use with the specified hardware constraints.

---

## 4. [LeCun Says Llama 4 results "were fudged a little bit"](https://reddit.com/r/LocalLLaMA/comments/1q25070/lecun_says_llama_4_results_were_fudged_a_little/)

**Author:** u/MrPecunius | **Upvotes:** 360 | **Comments:** 89 | **Date:** 2026-01-02

**Summary:** Yann LeCun confirmed that Llama 4 benchmarks were manipulated, and Meta's GenAI organization was sidelined, leading to departures and lack of follow-up on promised models. The community expressed disappointment and shared additional resources.

**Key Points:**
- LeCun confirmed Llama 4 benchmark manipulation
- Meta's GenAI organization was sidelined by Zuckerberg
- Many employees left or are expected to leave
- No follow-up on the promised large Llama 4 model
- Community disappointment in Meta's handling of Llama

**Discussion Highlights:** The discussion highlighted disappointment in Meta's strategic decisions, with users sharing additional resources and questioning how a well-positioned organization could fail while smaller labs thrived. There was also clarification about LeCun's role in a different division (FAIR).

---

## 5. [Most optimal vram/performance per price and advice for Shenzhen GPU market](https://reddit.com/r/LocalLLaMA/comments/1q1w1qj/most_optimal_vramperformance_per_price_and_advice/)

**Author:** u/notafakename10 | **Upvotes:** 247 | **Comments:** 60 | **Date:** 2026-01-02

**Summary:** The post seeks advice on purchasing GPUs in Shenzhen with a budget of $1500-3000 USD, aiming for at least 48GB VRAM, preferably 96GB, for local models and occasional PyTorch training. The discussion highlights various GPU options and considerations. Key points include the budget range, target VRAM, considerations for modded cards, and top recommendations like MI100 for best value (non-CUDA) and 4090D 48GB for CUDA. The discussion consensus leans towards the MI100 for best performance per dollar if CUDA is not required, and the 4090D 48GB for CUDA support. Other notable mentions include the A100 40GB and A40s for high VRAM and CUDA support. Cooling and power efficiency are emphasized as important factors.

---

## 6. [Getting ready to train in Intel arc](https://reddit.com/r/LocalLLaMA/comments/1q1p5q5/getting_ready_to_train_in_intel_arc/)

**Author:** u/hasanismail_ | **Upvotes:** 297 | **Comments:** 91 | **Date:** 2026-01-01

**Summary:** The Reddit post discusses the author's excitement about training on Intel Arc GPUs and mentions they are waiting for PCIe risers to start. The author also clarifies they are not causing a GPU shortage.

**Key Points:**
- Author is preparing to train on Intel Arc GPUs
- Waiting for PCIe risers to start the training process
- Author clarifies they are not causing a GPU shortage
- Suggestions to use Ubuntu 24.04 and join OpenArc Discord for support
- Discussion about the feasibility of training on PCIe setup vs renting N*H100 from Vast

**Discussion Highlights:** The discussion includes suggestions for using Ubuntu 24.04 and joining the OpenArc Discord for support. There is also a debate about the feasibility of training on a PCIe setup compared to renting more powerful GPUs.

---

## 7. [TIL you can allocate 128 GB of unified memory to normal AMD iGPUs on Linux via GTT](https://reddit.com/r/LocalLLaMA/comments/1q1lgb7/til_you_can_allocate_128_gb_of_unified_memory_to/)

**Author:** u/1ncehost | **Upvotes:** 175 | **Comments:** 30 | **Date:** 2026-01-01

**Summary:** The post discusses using AMD iGPUs on Linux with GTT to allocate up to 128 GB of system memory as VRAM, useful for development tasks like kernel optimization and hybrid CPU/GPU architectures. Users share experiences with this feature, noting its benefits for background tasks and development.

**Key Points:**
- AMD iGPUs on Linux can use GTT to allocate up to 128 GB of system memory as VRAM.
- Useful for development tasks like kernel optimization and hybrid CPU/GPU architectures.
- Not ideal for inference due to slow performance compared to CPUs.
- Users report success with background tasks and development using this feature.
- Can simulate MI300A-like architectures for testing purposes.

**Discussion Highlights:** Users highlight the utility of GTT for background tasks and development, with some noting its effectiveness for inference on specific setups like Strix Halo. The consensus is that while not suitable for all use cases, GTT is a valuable tool for developers and those running specific workloads.

---

## 8. [IQuestCoder - new 40B dense coding model](https://reddit.com/r/LocalLLaMA/comments/1q1986x/iquestcoder_new_40b_dense_coding_model/)

**Author:** u/ilintar | **Upvotes:** 185 | **Comments:** 37 | **Date:** 2026-01-01

**Summary:** The post introduces IQuestCoder, a new 40B dense coding model based on Llama architecture, which has been adapted to GGUF and is claimed to be state-of-the-art. The author has made it compatible with Llama.cpp and shared it on Hugging Face.

**Key Points:**
- IQuestCoder is a 40B dense coding model with Llama architecture.
- The model has been adapted to GGUF and works with Llama.cpp.
- Early testing shows promising results, including success in coding tasks like Snake game and embedded Rust concepts.
- There is some skepticism about the architecture and quantization methods used.
- The model is available for download and testing on Hugging Face.

**Discussion Highlights:** The discussion highlights early positive feedback on the model's performance in coding tasks, though there is some skepticism about the architecture and quantization methods. Users are actively testing the model and comparing it to other models like GPT 120, Devstral, and GLM 4.7.

---

## 9. [Upstage Solar-Open-100B Public Validation](https://reddit.com/r/LocalLLaMA/comments/1q0zst6/upstage_solaropen100b_public_validation/)

**Author:** u/PerPartes | **Upvotes:** 230 | **Comments:** 69 | **Date:** 2026-01-01

**Summary:** Upstage's official response to claims about Solar-Open-100B being a fine-tuned version of GLM-Air-4.5, including event details and a video link.

**Key Points:**
- Official counterstrike to claims about Solar 100B Open
- Event held at KAIST, Seoul with CEO presentation
- Video link provided for online translation
- Discussion includes technical tests and community reactions
- Mixed opinions on the necessity of in-person events vs. online releases

**Discussion Highlights:** The discussion includes technical tests comparing model layers, community reactions to the plagiarism claims, and mixed opinions on the format of the event versus online releases.

---

## 10. [DeepSeek new paper: mHC: Manifold-Constrained Hyper-Connections](https://reddit.com/r/LocalLLaMA/comments/1q0zk1u/deepseek_new_paper_mhc_manifoldconstrained/)

**Author:** u/External_Mood4719 | **Upvotes:** 167 | **Comments:** 37 | **Date:** 2026-01-01

**Summary:** DeepSeek's new paper introduces mHC (Manifold-Constrained Hyper-Connections), a novel approach to improving deep neural networks by addressing gradient issues in deep architectures. The paper suggests significant advancements in residual connections, potentially impacting both LLMs and CNNs like ResNet.

**Key Points:**
- mHC aims to solve gradient explosion issues in deep networks without relying solely on identity residual connections.
- The approach is applicable to both LLMs and CNNs, with potential improvements in training stability and performance.
- The paper is part of a broader trend in 2026 focusing on enhancing residual connections in neural networks.
- Community discussion highlights excitement about potential scaling trends and practical impacts of these improvements.

**Discussion Highlights:** The community shows strong interest in the practical implications of mHC, with discussions focusing on its potential to improve training stability in deep networks. There is also mention of related work on scaling trends with enhanced residual connections, indicating a growing research direction in this area.

---

## 11. [Software FP8 for GPUs without hardware support - 3x speedup on memory-bound operations](https://reddit.com/r/LocalLLaMA/comments/1q0x8ci/software_fp8_for_gpus_without_hardware_support_3x/)

**Author:** u/Venom1806 | **Upvotes:** 279 | **Comments:** 57 | **Date:** 2026-01-01

**Summary:** A software workaround enables FP8 support on GPUs without native hardware support, achieving a 3x speedup on memory-bound operations using bitwise operations and Triton kernels. It is compatible with older GPUs like the RTX 30/20 series.

**Key Points:**
- Software workaround for FP8 support on GPUs without native hardware support
- 3x speedup on memory-bound operations (GEMV, FlashAttention)
- Compatible with older GPUs like RTX 30/20 series
- Uses bitwise operations and Triton kernels
- Community interest in integrating with tools like ComfyUI

**Discussion Highlights:** The community appreciates the workaround as a solution to slow hardware adoption of FP8. There is interest in integrating it with tools like ComfyUI, and some users are surprised that FP8 is not natively supported on RTX 30 series GPUs.

---

## 12. [IQuestLab/IQuest-Coder-V1 — 40B parameter coding LLM — Achieves leading results on SWE-Bench Verified (81.4%), BigCodeBench (49.9%), LiveCodeBench v6 (81.1%)](https://reddit.com/r/LocalLLaMA/comments/1q0vom4/iquestlabiquestcoderv1_40b_parameter_coding_llm/)

**Author:** u/TellMeAboutGoodManga | **Upvotes:** 173 | **Comments:** 45 | **Date:** 2025-12-31

**Summary:** IQuestLab's IQuest-Coder-V1 is a 40B parameter coding LLM that achieves leading results on multiple benchmarks, including SWE-Bench Verified (81.4%), BigCodeBench (49.9%), and LiveCodeBench v6 (81.1%). The model is backed by a Chinese quant trading company, sparking interest in the community.

**Key Points:**
- IQuest-Coder-V1 achieves leading results on SWE-Bench Verified (81.4%), BigCodeBench (49.9%), and LiveCodeBench v6 (81.1%)
- The model is backed by a Chinese quant trading company, similar to DeepSeek
- The model is a dense 40B parameter model, not a Mixture of Experts (MoE)
- Community questions the authenticity of the benchmarks
- Interest in the model's performance and background

**Discussion Highlights:** The community is interested in the model's background and performance, with some questioning the authenticity of the benchmarks. There is also discussion about the model being a dense 40B parameter model rather than a Mixture of Experts (MoE).

---

## 13. [Happy New Year: Llama3.3-8B-Instruct-Thinking-Claude-4.5-Opus-High-Reasoning - Fine Tune. (based on recent find of L3.3 8b in the wild)](https://reddit.com/r/LocalLLaMA/comments/1q0uuqt/happy_new_year/)

**Author:** u/Dangerous_Fix_5526 | **Upvotes:** 277 | **Comments:** 80 | **Date:** 2025-12-31

**Summary:** The post announces a fine-tuned Llama3.3-8B model using the Claude 4.5 Opus High Reasoning dataset, with GGUF quantizations now available. The author thanks contributors and provides links to the model and dataset.

**Key Points:**
- Fine-tuned Llama3.3-8B model using Claude 4.5 Opus High Reasoning dataset
- GGUF quantizations are available
- Model aims to induce reasoning without system prompt help
- Heretic (uncensored) version also released
- Discussion includes questions about dataset size and GGUF availability

**Discussion Highlights:** The discussion highlights questions about the adequacy of the dataset size (250 rows) for inducing reasoning and interest in the GGUF version of the model.

---

## 14. [Moonshot AI Completes $500 Million Series C Financing](https://reddit.com/r/LocalLLaMA/comments/1q0i4g3/moonshot_ai_completes_500_million_series_c/)

**Author:** u/InternationalAsk1490 | **Upvotes:** 112 | **Comments:** 21 | **Date:** 2025-12-31

**Summary:** Moonshot AI has completed a $500 million Series C financing, with plans to expand GPU capacity and develop the K3 model. The company aims to achieve significant revenue growth and enhance its model's capabilities.

**Key Points:**
- Moonshot AI completed a $500 million Series C financing.
- The company's global paid user base is growing at a monthly rate of 170%.
- Funds will be used to expand GPU capacity and accelerate the development of the K3 model.
- Key priorities for 2026 include improving the K3 model's performance and achieving significant revenue growth.
- The discussion highlights positive sentiment towards Moonshot AI's progress and its Kimi models.

**Discussion Highlights:** The discussion reflects positive sentiment towards Moonshot AI's achievements and its Kimi models. Users appreciate the company's progress and are curious about the benefits of using Kimi K2 via their membership program.

---

## 15. [Solar-Open-100B is out](https://reddit.com/r/LocalLLaMA/comments/1q0bgvl/solaropen100b_is_out/)

**Author:** u/cgs019283 | **Upvotes:** 157 | **Comments:** 62 | **Date:** 2025-12-31

**Summary:** Upstage has released the Solar-Open-100B, a 102B parameter model with a commercial-friendly license. The community is excited about its potential and awaits performance benchmarks and quantized versions.

**Key Points:**
- Solar-Open-100B is a 102B parameter model with a commercial-friendly license.
- The model was trained on 19.7 trillion tokens.
- Community is eagerly awaiting performance benchmarks and quantized versions (e.g., GGUF/AWQ).
- The model is seen as a significant milestone, with high expectations for local inference capabilities.

**Discussion Highlights:** The community is highly enthusiastic about the release, noting the rapid pace of model advancements. Key discussions include the open license, the large token count, and anticipation for performance benchmarks and quantized versions for local use.

---

## 16. [Qwen-Image-2512](https://reddit.com/r/LocalLLaMA/comments/1q094a3/qwenimage2512/)

**Author:** u/Nunki08 | **Upvotes:** 682 | **Comments:** 116 | **Date:** 2025-12-31

**Summary:** The Reddit post announces the release of Qwen-Image-2512, a new model available on multiple platforms including Hugging Face, ModelScope, and GitHub. Users have shared positive feedback and experiences, highlighting its accessibility and performance even on low-end hardware.

**Key Points:**
- Qwen-Image-2512 is available on various platforms like Hugging Face, ModelScope, and GitHub.
- The model can be tried out in Qwen Chat and has demos available on Hugging Face and ModelScope.
- Users have successfully run the model on low-end hardware without a GPU.
- Positive feedback from users, including appreciation for the model as a 'New Year's gift'.
- Creative use cases demonstrated, such as generating unique images.

**Discussion Highlights:** Users expressed gratitude for the model's release and shared their experiences running it on various hardware configurations. One user notably ran the model on a low-end Dell desktop without a GPU, showcasing its accessibility. The discussion also included creative examples of image generation using the model.

---

## 17. [Update on the Llama 3.3 8B situation](https://reddit.com/r/LocalLLaMA/comments/1q06ddc/update_on_the_llama_33_8b_situation/)

**Author:** u/FizzarolliAI | **Upvotes:** 255 | **Comments:** 22 | **Date:** 2025-12-31

**Summary:** The post discusses updates on the Llama 3.3 8B model, including benchmarks for different configurations and the author's confusion over Meta's release choices. The author provides links to both the original and context-extended versions of the model. Key points include the author uploading the model's weights, the 128k context version showing better performance, confusion over Meta's release choices, and issues with Tau-Bench results. Discussion highlights include appreciation for the author's work, a preference for the unofficial release, and humor around the author's self-deprecating remark.

---

## 18. [[In the Wild] Reverse-engineered a Snapchat Sextortion Bot: It’s running a raw Llama-7B instance with a 2048 token window.](https://reddit.com/r/LocalLLaMA/comments/1pzwlie/in_the_wild_reverseengineered_a_snapchat/)

**Author:** u/simar-dmg | **Upvotes:** 716 | **Comments:** 106 | **Date:** 2025-12-30

**Summary:** A user reverse-engineered a Snapchat sextortion bot and discovered it was running a raw Llama-7B instance with a 2048 token window. The bot was vulnerable to a persona-adoption jailbreak, revealing its configuration and malicious payload.

**Key Points:**
- The bot used a Llama-7B model with a 2048 token context window and high temperature setting.
- A 'Grandma Protocol' jailbreak forced the bot to reveal its environment variables and configuration.
- The bot was likely running on minimal hardware to reduce costs.
- The payload was a malicious link disguised to bypass Snapchat's URL filters.
- Scammers are increasingly using open-source models like Llama-7B to avoid API costs and censorship.

**Discussion Highlights:** The discussion included skepticism about the accuracy of the bot's revealed information, with some users suggesting it could be entirely hallucinated. Others questioned the feasibility of system prompts including environment variables.

---

## 19. [LLM server gear: a cautionary tale of a $1k EPYC motherboard sale gone wrong on eBay](https://reddit.com/r/LocalLLaMA/comments/1pzt1q8/llm_server_gear_a_cautionary_tale_of_a_1k_epyc/)

**Author:** u/__JockY__ | **Upvotes:** 194 | **Comments:** 81 | **Date:** 2025-12-30

**Summary:** The post discusses a seller's experience with eBay's dispute resolution process after selling a high-end EPYC motherboard. Despite providing detailed evidence and support, the seller faced challenges due to eBay's buyer-friendly policies, highlighting the risks of selling high-end gear on the platform.

**Key Points:**
- eBay's dispute resolution process heavily favors buyers, even with clear evidence.
- The seller provided detailed photos and support but still faced a dispute.
- The post highlights the risks and frustrations of selling high-end gear on eBay.
- Other users shared similar experiences with eBay's buyer-friendly policies.
- The process of resolving disputes can be intentionally cumbersome and frustrating.

**Discussion Highlights:** The discussion highlights a consensus among users about the challenges and frustrations of selling on eBay, with many sharing similar experiences of buyer-inflicted damage and the platform's bias towards buyers. Users also noted the intentional complexity of the dispute resolution process.

---

## 20. [15M param model solving 24% of ARC-AGI-2 (Hard Eval). Runs on consumer hardware.](https://reddit.com/r/LocalLLaMA/comments/1pzsqii/15m_param_model_solving_24_of_arcagi2_hard_eval/)

**Author:** u/Doug_Bitterbot | **Upvotes:** 114 | **Comments:** 31 | **Date:** 2025-12-30

**Summary:** Bitterbot AI introduced TOPAS-DSPL, a 24M parameter model achieving 24% accuracy on ARC-AGI-2, significantly outperforming previous models of similar size. The model uses a dual-stream architecture to prevent compositional drift and employs test-time training for fine-tuning. The code and pipeline are open-sourced for verification.

**Key Points:**
- TOPAS-DSPL achieves 24% accuracy on ARC-AGI-2, outperforming previous SOTA models of similar size.
- The model uses a bicameral architecture with Logic and Canvas streams to prevent compositional drift.
- Test-Time Training (TTT) is used for fine-tuning on specific puzzle examples.
- The model is open-sourced, with detailed documentation for verification.
- Discussion includes comparisons with MuZero, criticisms about training on test data, and questions about scalability.

**Discussion Highlights:** The discussion includes comparisons with MuZero, criticisms about the methodology of training on test data, and questions about the model's scalability to larger parameter sizes. Some users express skepticism, while others show interest in verifying the results.

---

## 21. [Any guesses?](https://reddit.com/r/LocalLLaMA/comments/1pzhcqu/any_guesses/)

**Author:** u/Difficult-Cap-7527 | **Upvotes:** 172 | **Comments:** 36 | **Date:** 2025-12-30

**Summary:** The Reddit post discusses speculation about a new Qwen model release, with comments highlighting potential performance improvements and comparisons to GPT 5.2.

**Key Points:**
- Speculation about Qwen 6 beating GPT 5.2 on key benchmarks
- Mention of Qwen3vl-next-80b-a3b as a significant update
- References to Qwen image models (e.g., Qwen image 2512)
- Celebratory tone about Qwen's performance improvements
- Discussion of model iterations and potential future releases (e.g., Qwen3.5-235B-A10B)

**Discussion Highlights:** The discussion focuses on Qwen's competitive performance against other models, with users expressing excitement about potential advancements and sharing details about specific model versions.

---

## 22. [Running GLM-4.7 (355B MoE) in Q8 at ~5 Tokens/s on 2015 CPU-Only Hardware – Full Optimization Guide](https://reddit.com/r/LocalLLaMA/comments/1pzggbf/running_glm47_355b_moe_in_q8_at_5_tokenss_on_2015/)

**Author:** u/at0mi | **Upvotes:** 140 | **Comments:** 99 | **Date:** 2025-12-30

**Summary:** The post details a successful attempt to run the GLM-4.7 (355B MoE) model on a 2015 CPU-only system, achieving ~5 tokens/s with Q8 quantization. The author shares optimization techniques and benchmarks, highlighting the feasibility of running large models on older hardware.

**Key Points:**
- GLM-4.7 (355B MoE) runs at ~5 tokens/s on a 2015 Lenovo System x3950 X6 with 8 Xeon E7-8880 v3 CPUs.
- Optimizations include BIOS settings, NUMA node distribution, and Linux kernel tweaks.
- The setup consumes ~1300W under full load, making it power-intensive but effective for local inference.
- Discussion highlights cost and energy efficiency, with calculations showing ~60 kWh per 1 million tokens.
- Community feedback includes concerns about power draw and cost estimates for similar builds.

**Discussion Highlights:** The discussion focuses on energy efficiency, cost implications, and the trade-offs of running large models on CPU-only systems. Users share calculations on token generation costs and express interest in similar setups, though some note concerns about power consumption.

---

## 23. [Tencent HY-Motion 1.0 - a billion-parameter text-to-motion model](https://reddit.com/r/LocalLLaMA/comments/1pzcrtb/tencent_hymotion_10_a_billionparameter/)

**Author:** u/ResearchCrafty1804 | **Upvotes:** 319 | **Comments:** 36 | **Date:** 2025-12-30

**Summary:** Tencent has open-sourced HY-Motion 1.0, a billion-parameter text-to-motion model that generates high-fidelity 3D animations from natural language. It features a comprehensive training strategy and supports over 200 motion categories, making it a powerful tool for developers and creators.

**Key Points:**
- HY-Motion 1.0 is a billion-parameter text-to-motion model based on Diffusion Transformer (DiT) architecture.
- It uses a full-stage training strategy (Pre-training → SFT → RL) for optimized motion quality.
- Supports 200+ motion categories across 6 major classes, the most comprehensive in the industry.
- Users report it works well with minimal cleanup needed, significantly speeding up game development.
- Questions remain about its compatibility with non-humanoid models like animals.

**Discussion Highlights:** Users are excited about the model's capabilities, with one confirming it works as advertised and is beneficial for game development. There are inquiries about its applicability to non-humanoid models and its potential use in other communities.

---

## 24. [Llama-3.3-8B-Instruct](https://reddit.com/r/LocalLLaMA/comments/1pz7mxr/llama338binstruct/)

**Author:** u/ttkciar | **Upvotes:** 153 | **Comments:** 25 | **Date:** 2025-12-29

**Summary:** The post discusses the release of Llama-3.3-8B-Instruct, a potentially new model, with links to Hugging Face repositories. The community expresses excitement and skepticism, with ongoing benchmark tests to verify its authenticity.

**Key Points:**
- Llama-3.3-8B-Instruct model release with Hugging Face links
- Community excitement and skepticism about the model's authenticity
- Ongoing sanity check benchmarks to verify the model
- Discussion about updated rope config for full context length
- Desire for updated 70B or new 30B models

**Discussion Highlights:** The community is engaged in verifying the model's authenticity through benchmarks. There is a mix of excitement and skepticism, with some users providing additional resources and configurations. The consensus leans towards cautious optimism pending further verification.

---

## 25. [Llama-3.3-8B-Instruct](https://reddit.com/r/LocalLLaMA/comments/1pz7bmv/llama338binstruct/)

**Author:** u/jacek2023 | **Upvotes:** 463 | **Comments:** 78 | **Date:** 2025-12-29

**Summary:** The post discusses the discovery and release of the Llama-3.3-8B-Instruct model, which was obtained through a finetuning API after overcoming several technical challenges. The model is significant as it was previously only available behind Meta's API.

**Key Points:**
- Discovery of Llama-3.3-8B-Instruct model via finetuning API
- Model was previously only available behind Meta's API
- Community is verifying the model's authenticity and performance
- Technical details like position embeddings are being discussed
- Enthusiastic reactions from the community

**Discussion Highlights:** The community is actively verifying the model's authenticity and performance, with some users running benchmarks and evaluations. There is enthusiasm about the discovery, though some technical details like position embeddings are being questioned.

---

## 26. [Z AI is going for an IPO on Jan 8 and set to raise $560 million. Z.ai is set to be the first AI-native LLM company to list on the global market.](https://reddit.com/r/LocalLLaMA/comments/1pz68fz/z_ai_is_going_for_an_ipo_on_jan_8_and_set_to/)

**Author:** u/Difficult-Cap-7527 | **Upvotes:** 343 | **Comments:** 120 | **Date:** 2025-12-29

**Summary:** Z AI is set to go public on January 8, aiming to raise $560 million, marking a significant milestone as the first AI-native LLM company to list globally. The announcement has sparked a debate about the future of open-source AI models and the necessity for companies to monetize their products.

**Key Points:**
- Z AI's IPO is scheduled for January 8, with a target of raising $560 million.
- Concerns about the future of open-source AI models.
- Debate on whether Z AI will continue releasing open weight models.
- The necessity for companies to monetize their products eventually.
- Mixed reactions from the community, with some expressing disappointment at the potential shift away from open-source.

**Discussion Highlights:** The community is divided, with some users expressing skepticism about the future of open-source AI, while others argue that monetization is a natural progression for companies.

---

## 27. [Naver (South Korean internet giant), has just launched HyperCLOVA X SEED Think, a 32B open weights reasoning model and HyperCLOVA X SEED 8B Omni, a unified multimodal model that brings text, vision, and speech together](https://reddit.com/r/LocalLLaMA/comments/1pyjjbw/naver_south_korean_internet_giant_has_just/)

**Author:** u/Nunki08 | **Upvotes:** 162 | **Comments:** 31 | **Date:** 2025-12-29

**Summary:** Naver has launched two new AI models: HyperCLOVA X SEED Think 32B, a 32B open weights reasoning model, and HyperCLOVA X SEED 8B Omni, a unified multimodal model combining text, vision, and speech. The announcement has generated significant interest in the AI community.

**Key Points:**
- HyperCLOVA X SEED Think 32B is a 32B open weights reasoning model.
- HyperCLOVA X SEED 8B Omni is a multimodal model integrating text, vision, and speech.
- The community is interested in the models' capabilities and compatibility with existing tools like llama.cpp and vLLM.
- The announcement aligns with expectations of new AI models from Korea.
- There is enthusiasm for the multimodal capabilities of the Omni model.

**Discussion Highlights:** The community discussion highlights excitement about the multimodal capabilities of the Omni model and questions about compatibility with existing AI tools. Some users also noted that this release aligns with expectations of new models from Korea.

---

## 28. [Tencent just released WeDLM 8B Instruct on Hugging Face](https://reddit.com/r/LocalLLaMA/comments/1pyg4yt/tencent_just_released_wedlm_8b_instruct_on/)

**Author:** u/Difficult-Cap-7527 | **Upvotes:** 420 | **Comments:** 62 | **Date:** 2025-12-29

**Summary:** Tencent released WeDLM 8B Instruct on Hugging Face, a diffusion language model that runs 3-6× faster than vLLM-optimized Qwen3-8B on math reasoning tasks. The community response highlights its impressive performance and potential in the 7-8B model space.

**Key Points:**
- WeDLM 8B Instruct is a diffusion language model with significant speed improvements over Qwen3-8B.
- The model is released under an Apache 2.0 license.
- Community interest is high, with discussions on its potential and performance.
- A 7B version of the model is also available.

**Discussion Highlights:** The community is excited about the model's performance and potential, with many users expressing interest in its capabilities and the broader implications for the 7-8B model space.

---

## 29. [Meta released RPG, a research plan generation dataset on Hugging Face](https://reddit.com/r/LocalLLaMA/comments/1pyao6g/meta_released_rpg_a_research_plan_generation/)

**Author:** u/Difficult-Cap-7527 | **Upvotes:** 263 | **Comments:** 21 | **Date:** 2025-12-28

**Summary:** Meta released the RPG dataset on Hugging Face, featuring 22k tasks across ML, Arxiv, and PubMed, with evaluation rubrics and Llama-4 reference solutions for training AI co-scientists.

**Key Points:**
- RPG dataset includes 22k tasks spanning ML, Arxiv, and PubMed
- Dataset comes with evaluation rubrics and Llama-4 reference solutions
- Meta's open-source contributions are highlighted as significant
- Research plan generation is seen as crucial for agentic or tool-using AI systems
- Community appreciates the release but desires models trained on such datasets

**Discussion Highlights:** The community praises Meta's open-source efforts and emphasizes the importance of research plan generation for AI systems, though some express a desire for models trained on such datasets.

---

## 30. [Senator in Tennessee introduces bill to felonize making AI "act as a companion" or "mirror human interactions"](https://reddit.com/r/LocalLLaMA/comments/1pxss0m/senator_in_tennessee_introduces_bill_to_felonize/)

**Author:** u/CanineAssBandit | **Upvotes:** 278 | **Comments:** 212 | **Date:** 2025-12-28

**Summary:** A Tennessee senator has introduced a bill (SB1493) that aims to felonize training AI to provide emotional support, act as a companion, or simulate human interactions. The bill defines 'train' broadly and has sparked significant discussion on Reddit. Key points include the bill targeting AI trained to provide emotional support or act as companions, provisions against AI simulating human interactions or appearing sentient, and a broad definition of 'train' encompassing data usage and model development. The post encourages contacting representatives to oppose the bill, and top comments express skepticism, humor, and concerns about lobbying. The discussion highlights skepticism about the bill's feasibility and potential impact, with some users expressing humor and others raising concerns about lobbying and freedom of speech.

---

