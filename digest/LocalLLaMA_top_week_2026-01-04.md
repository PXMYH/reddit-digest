# r/LocalLLaMA Reading Digest

**Period:** 2026-01-04 to 2026-01-04
**Posts Summarized:** 30
**Total Posts Analyzed:** 30

---

## 1. [Don't sleep on granite 4 small if you got an 8+32+ system](https://reddit.com/r/LocalLLaMA/comments/1q2s3hp/dont_sleep_on_granite_4_small_if_you_got_an_832/)

**Author:** u/Zestyclose-Shift710 | **Upvotes:** 105 | **Comments:** 41 | **Date:** 2026-01-03

**Summary:** The post discusses optimizing a ThinkPad P15 with 32GB RAM and an 8GB Quadro GPU to run large language models efficiently. By using a Mixture of Experts (MoE) model and keeping experts on the CPU, the user achieved high context lengths and fast generation speeds, particularly with the Granite 4.0 Small model, which maintains speed even with large contexts. Key points include the use of MoE models to free up VRAM, the performance of Granite 4.0 Small, and comparisons with other models like Qwen 30B A3B. The discussion highlights potential optimizations and feedback on the model's performance.

---

## 2. [GLM-4.7-REAP-50-W4A16: 50% Expert-Pruned + INT4 Quantized GLM-4 (179B params, ~92GB)](https://reddit.com/r/LocalLLaMA/comments/1q2pons/glm47reap50w4a16_50_expertpruned_int4_quantized/)

**Author:** u/Maxious | **Upvotes:** 169 | **Comments:** 66 | **Date:** 2026-01-03

**Summary:** The post introduces GLM-4.7-REAP-50-W4A16, a 50% expert-pruned and INT4 quantized version of GLM-4 with 179B parameters (~92GB). The discussion focuses on technical details like calibration methods, benchmarking, and comparisons with other models.

**Key Points:**
- GLM-4.7-REAP-50-W4A16 is a pruned and quantized version of GLM-4 with 179B parameters (~92GB).
- Community members request details on calibration methods for expert activation during quantization.
- Questions arise about the tasks used for REAP pruning calibration.
- Interest in benchmark results and comparisons with models like MiniMax M2.1.
- Comparisons with EXL3 GLM at 2.0bpw (~90GB) are suggested.

**Discussion Highlights:** The community is keen on understanding the technical aspects of the model, particularly calibration and benchmarking. Some users share subjective preferences for alternative models based on prior experiences.

---

## 3. [What is the smartest uncensored nsfw LLM you can run with 20GB VRAM and 24GB RAM](https://reddit.com/r/LocalLLaMA/comments/1q2o033/what_is_the_smartest_uncensored_nsfw_llm_you_can/)

**Author:** u/Death_12_35_taken | **Upvotes:** 175 | **Comments:** 73 | **Date:** 2026-01-03

**Summary:** The post seeks recommendations for an uncensored, smart, and fast LLM that can run locally with 20GB VRAM and 24GB RAM. The community suggests several models, with Dolphin-Mistral-24B-Venice-Edition being the most recommended.

**Key Points:**
- User seeks an uncensored, smart, and fast LLM for local use.
- Models should stay in character and be creative.
- Top recommendations include Dolphin-Mistral-24B-Venice-Edition, UGI-Leaderboard, Huihui-Qwen3-VL-30B-A3B-Instruct-abliterated, and gpt-oss-20b-Derestricted.
- Dolphin-Mistral-24B-Venice-Edition is the most upvoted suggestion.

**Discussion Highlights:** The community provides specific model recommendations, with Dolphin-Mistral-24B-Venice-Edition being the most popular choice for its balance of performance and uncensored capabilities.

---

## 4. [LeCun Says Llama 4 results "were fudged a little bit"](https://reddit.com/r/LocalLLaMA/comments/1q25070/lecun_says_llama_4_results_were_fudged_a_little/)

**Author:** u/MrPecunius | **Upvotes:** 354 | **Comments:** 89 | **Date:** 2026-01-02

**Summary:** Yann LeCun, departing Meta AI Chief, confirmed that Llama 4 benchmark results were manipulated. This follows speculation about suspicious benchmarks and coincides with Zuckerberg sidelining the GenAI organization, leading to significant departures.

**Key Points:**
- LeCun confirms Llama 4 benchmark manipulation
- Zuckerberg sidelined Meta's GenAI organization
- Significant departures from Meta's AI team
- Llama 4's promised large model was never released
- Community disappointment over Llama's perceived failure

**Discussion Highlights:** The discussion highlights disappointment in Meta's handling of Llama, with users expressing regret over its perceived failure and the shift of AI innovation to other regions. Some users shared additional resources, while others debated the organizational dynamics at Meta.

---

## 5. [Most optimal vram/performance per price and advice for Shenzhen GPU market](https://reddit.com/r/LocalLLaMA/comments/1q1w1qj/most_optimal_vramperformance_per_price_and_advice/)

**Author:** u/notafakename10 | **Upvotes:** 250 | **Comments:** 60 | **Date:** 2026-01-02

**Summary:** The post discusses finding the most optimal GPU setup with high VRAM (48GB-96GB) for local models and occasional PyTorch training within a $1500-3000 budget in the Shenzhen market. The discussion highlights various GPU options and their value propositions. Key points include the budget range, VRAM requirements, openness to modded cards, and specific recommendations like MI100 for non-CUDA needs and 4090D 48GB for CUDA support. The discussion consensus emphasizes the MI100 and 4090D 48GB, with mentions of other options like A100 40GB and A40s, and stresses the importance of cooling and power considerations.

---

## 6. [Getting ready to train in Intel arc](https://reddit.com/r/LocalLLaMA/comments/1q1p5q5/getting_ready_to_train_in_intel_arc/)

**Author:** u/hasanismail_ | **Upvotes:** 293 | **Comments:** 91 | **Date:** 2026-01-01

**Summary:** The Reddit post discusses the author's excitement about training on Intel Arc GPUs and mentions they are waiting for PCIe risers. The author also clarifies they are not causing a GPU shortage.

**Key Points:**
- Author is preparing to train on Intel Arc GPUs
- Mentions waiting for PCIe risers
- Clarifies not causing a GPU shortage
- Suggests using Ubuntu 24.04 for better compatibility
- Mentions support for Intel Arc in Unsloth

**Discussion Highlights:** The discussion includes a mix of support and skepticism. One comment suggests using Ubuntu 24.04 for better compatibility and mentions support for Intel Arc in Unsloth. Another comment questions the feasibility of training on a PCIe setup compared to renting N*H100 from Vast.

---

## 7. [TIL you can allocate 128 GB of unified memory to normal AMD iGPUs on Linux via GTT](https://reddit.com/r/LocalLLaMA/comments/1q1lgb7/til_you_can_allocate_128_gb_of_unified_memory_to/)

**Author:** u/1ncehost | **Upvotes:** 173 | **Comments:** 30 | **Date:** 2026-01-01

**Summary:** The post discusses using AMD's GTT feature on Linux to allocate up to 128 GB of system memory as VRAM for iGPUs, useful for development tasks like kernel optimization and hybrid CPU/GPU architectures. The author shares their experience using this feature to parallelize training and optimization tasks.

**Key Points:**
- AMD iGPUs on Linux can use up to 128 GB of system memory as VRAM via GTT, dynamically allocated.
- Useful for development tasks like kernel optimization and hybrid CPU/GPU architectures.
- Not ideal for inference due to slow iGPU performance compared to CPUs.
- Requires direct ROCm access via C++/HIP kernels to avoid support issues.
- Can simulate MI300A-like unified memory architectures on standard Ryzen systems.

**Discussion Highlights:** Users shared their experiences using iGPUs for background tasks and inference, noting benefits like freeing up CPU resources. Some mentioned using similar techniques with Nvidia GPUs for kv cache in llama.cpp. Overall, the discussion highlighted practical use cases and limitations of using iGPUs for GPU-accelerated tasks.

---

## 8. [IQuestCoder - new 40B dense coding model](https://reddit.com/r/LocalLLaMA/comments/1q1986x/iquestcoder_new_40b_dense_coding_model/)

**Author:** u/ilintar | **Upvotes:** 183 | **Comments:** 37 | **Date:** 2026-01-01

**Summary:** The post introduces IQuestCoder, a new 40B dense coding model that claims to be state-of-the-art. The author has adapted it to GGUF format, making it compatible with Llama.cpp. The model is based on Llama architecture and has shown promising performance in initial tests.

**Key Points:**
- IQuestCoder is a new 40B dense coding model claiming SOTA performance
- The model is adapted to GGUF format and works with Llama.cpp
- Initial tests show good performance in tasks like coding and game development
- There is some skepticism about the architecture and quantization methods used
- The model has been well-received by the community, with positive feedback on its performance

**Discussion Highlights:** The discussion highlights include positive feedback on the model's performance, skepticism about the architecture and quantization methods, and enthusiasm for testing the model in various coding tasks. The community appreciates the adaptation to GGUF format and the compatibility with Llama.cpp.

---

## 9. [Upstage Solar-Open-100B Public Validation](https://reddit.com/r/LocalLLaMA/comments/1q0zst6/upstage_solaropen100b_public_validation/)

**Author:** u/PerPartes | **Upvotes:** 232 | **Comments:** 69 | **Date:** 2026-01-01

**Summary:** Upstage held an event at KAIST, Seoul, to counter claims that Solar-Open-100B is merely a fine-tuned version of GLM-Air-4.5. The event featured CEO Sung Kim and was live-streamed on YouTube.

**Key Points:**
- Upstage hosted an event to address plagiarism claims about Solar-Open-100B.
- The event was held at KAIST, Seoul, with significant interest (50 capacity, 100+ registrations).
- CEO Sung Kim presented, and the event was live-streamed with online translation.
- Community discussions include technical tests comparing model layers and skepticism about the need for an in-person event.
- Some users defended Upstage, citing long-term familiarity with the team.

**Discussion Highlights:** The discussion includes technical analysis of model similarities, skepticism about the event's format, and defense of Upstage's integrity by some community members.

---

## 10. [DeepSeek new paper: mHC: Manifold-Constrained Hyper-Connections](https://reddit.com/r/LocalLLaMA/comments/1q0zk1u/deepseek_new_paper_mhc_manifoldconstrained/)

**Author:** u/External_Mood4719 | **Upvotes:** 165 | **Comments:** 37 | **Date:** 2026-01-01

**Summary:** DeepSeek's new paper introduces mHC (Manifold-Constrained Hyper-Connections), a novel approach to improving deep neural networks by addressing gradient issues in deep architectures. The paper suggests innovative techniques for residual connections that could enhance model performance and stability.

**Key Points:**
- DeepSeek's paper focuses on mHC, a new method for deep neural networks.
- The approach aims to solve gradient explosion problems in deep networks.
- Improved residual connections are a key aspect of the proposed method.
- The paper suggests potential impacts on both LLMs and CNNs like ResNet.
- Community discussion highlights enthusiasm for advancements in residual connections.

**Discussion Highlights:** The discussion reflects excitement about the potential impact of improved residual connections on deep learning models. Users appreciate the simplified explanations and express hope for significant advancements in the field this year.

---

## 11. [Software FP8 for GPUs without hardware support - 3x speedup on memory-bound operations](https://reddit.com/r/LocalLLaMA/comments/1q0x8ci/software_fp8_for_gpus_without_hardware_support_3x/)

**Author:** u/Venom1806 | **Upvotes:** 281 | **Comments:** 57 | **Date:** 2026-01-01

**Summary:** A user developed a software workaround to enable FP8 support on GPUs without native hardware support, achieving a 3x speedup on memory-bound operations. The solution uses bitwise operations and Triton kernels and is compatible with older GPUs like the RTX 30/20 series.

**Key Points:**
- Software workaround for FP8 support on GPUs without native hardware support
- Uses bitwise operations and Triton kernels
- Achieves 3x speedup on memory-bound operations
- Compatible with older GPUs like RTX 30/20 series
- Community appreciates the workaround as a solution to slow hardware adoption of FP8

**Discussion Highlights:** The community appreciates the workaround as a solution to slow hardware adoption of FP8. There is confusion about FP8 support on RTX 30 series GPUs, with some users reporting that FP8 models work on their RTX 3060. The workaround is seen as a way to extend the life of mid-tier GPUs.

---

## 12. [IQuestLab/IQuest-Coder-V1 — 40B parameter coding LLM — Achieves leading results on SWE-Bench Verified (81.4%), BigCodeBench (49.9%), LiveCodeBench v6 (81.1%)](https://reddit.com/r/LocalLLaMA/comments/1q0vom4/iquestlabiquestcoderv1_40b_parameter_coding_llm/)

**Author:** u/TellMeAboutGoodManga | **Upvotes:** 173 | **Comments:** 45 | **Date:** 2025-12-31

**Summary:** IQuestLab's IQuest-Coder-V1 is a 40B parameter coding LLM that achieves leading results on SWE-Bench Verified (81.4%), BigCodeBench (49.9%), and LiveCodeBench v6 (81.1%). The model is backed by a Chinese quant trading company, and the community discusses its performance, benchmark validity, and architecture.

**Key Points:**
- IQuest-Coder-V1 achieves leading results on multiple coding benchmarks.
- The model is backed by a Chinese quant trading company.
- Community members question the validity of the benchmarks and discuss the model's architecture.
- The model is a dense 40B parameter model, not a Mixture of Experts (MoE).
- Some users express interest in the model's performance relative to its size.

**Discussion Highlights:** The discussion highlights skepticism about the benchmark results, with some users questioning whether the benchmarks are 'benchmaxxed' or real. There is also interest in the model's architecture, with some users noting that it is a dense model rather than a MoE, which is unusual for models of this size. Additionally, the community discusses the trend of quant trading companies entering the LLM training space.

---

## 13. [Happy New Year: Llama3.3-8B-Instruct-Thinking-Claude-4.5-Opus-High-Reasoning - Fine Tune. (based on recent find of L3.3 8b in the wild)](https://reddit.com/r/LocalLLaMA/comments/1q0uuqt/happy_new_year/)

**Author:** u/Dangerous_Fix_5526 | **Upvotes:** 276 | **Comments:** 80 | **Date:** 2025-12-31

**Summary:** The post discusses a fine-tuned Llama3.3-8B-Instruct model using the Claude 4.5 Opus High Reasoning Dataset, with GGUF quants available. The author highlights the model's reasoning capabilities and mentions an upcoming 'Heretic' version.

**Key Points:**
- Fine-tuned Llama3.3-8B-Instruct model with Claude 4.5 Opus High Reasoning Dataset
- GGUF quants are available
- Model aims to induce reasoning without system prompt help
- Heretic (uncensored) version is in development
- Discussion includes questions about dataset size and GGUF availability

**Discussion Highlights:** The discussion includes questions about the adequacy of the fine-tuning dataset size (250 rows) and requests for a GGUF version of the model. Some users express interest in trying the fine-tune, while others are skeptical about the dataset size for inducing reasoning.

---

## 14. [Moonshot AI Completes $500 Million Series C Financing](https://reddit.com/r/LocalLLaMA/comments/1q0i4g3/moonshot_ai_completes_500_million_series_c/)

**Author:** u/InternationalAsk1490 | **Upvotes:** 110 | **Comments:** 21 | **Date:** 2025-12-31

**Summary:** Moonshot AI has completed a $500 million Series C financing, with plans to expand GPU capacity and develop the K3 model. The company's revenue and user base are growing rapidly, and it aims to achieve significant advancements in AI capabilities.

**Key Points:**
- Moonshot AI completed a $500 million Series C financing.
- The company's global paid user base is growing at a monthly rate of 170%.
- Funds will be used to expand GPU capacity and accelerate the development of the K3 model.
- Key priorities for 2026 include improving the K3 model's performance and making it more distinctive.
- The company aims to achieve an order-of-magnitude increase in revenue scale.

**Discussion Highlights:** The discussion highlights positive sentiment towards Moonshot AI's progress and its focus on creating distinctive AI capabilities. Users appreciate the company's efforts to monetize open-weight models and are curious about the benefits of using Kimi K2.

---

## 15. [Solar-Open-100B is out](https://reddit.com/r/LocalLLaMA/comments/1q0bgvl/solaropen100b_is_out/)

**Author:** u/cgs019283 | **Upvotes:** 159 | **Comments:** 62 | **Date:** 2025-12-31

**Summary:** Upstage has released the Solar-Open-100B, a 102B parameter model with a commercial-friendly license, sparking community interest and discussion about its potential performance and usability.

**Key Points:**
- Solar-Open-100B is a 102B parameter model with a commercial-friendly license.
- The model has been trained on 19.7 trillion tokens.
- Community is eagerly awaiting benchmarks and quantized versions (e.g., GGUF/AWQ).
- The model is seen as a significant milestone in open-source AI development.
- Discussion includes speculation about its relation to GLM4.6-Air.

**Discussion Highlights:** The community is excited about the model's release, noting its rapid development and potential for local inference. However, there is a lack of performance benchmarks, and users are awaiting quantized versions for easier deployment. The large token count and open license are particularly praised.

---

## 16. [Qwen-Image-2512](https://reddit.com/r/LocalLLaMA/comments/1q094a3/qwenimage2512/)

**Author:** u/Nunki08 | **Upvotes:** 686 | **Comments:** 116 | **Date:** 2025-12-31

**Summary:** The Reddit post announces the release of Qwen-Image-2512, a new AI model, and provides links to guides, GGUF files, and various platforms for accessing the model. The community has responded positively, with users sharing their experiences and creative applications.

**Key Points:**
- Qwen-Image-2512 is a new AI model with multiple access points including guides, GGUF files, and platforms like Hugging Face and ModelScope.
- The model has been well-received by the community, with users expressing gratitude and enthusiasm.
- Users have successfully run the model on low-end hardware, demonstrating its accessibility.
- Creative use cases, such as generating unique images, have been highlighted.

**Discussion Highlights:** The community has shown strong enthusiasm for Qwen-Image-2512, with users appreciating its accessibility and creative potential. Notable comments include successful deployment on low-end hardware and imaginative applications of the model.

---

## 17. [Update on the Llama 3.3 8B situation](https://reddit.com/r/LocalLLaMA/comments/1q06ddc/update_on_the_llama_33_8b_situation/)

**Author:** u/FizzarolliAI | **Upvotes:** 257 | **Comments:** 22 | **Date:** 2025-12-31

**Summary:** The author provides updates on Llama 3.3 8B, including benchmark results showing improved performance with a 128k context version compared to the original 8k version. They express frustration over Meta's handling of the model's release.

**Key Points:**
- Benchmark results show the 128k context version outperforms the original 8k version.
- The author is unsure why Meta provided the original 8k context version.
- The author wishes Meta had officially released the weights.
- The post includes links to both the 128k and original versions on Huggingface.
- The author removed Tau-Bench results due to scoring issues.

**Discussion Highlights:** The discussion includes positive feedback on the author's work, humor, and a consensus that the model is decent but could have been better with official support from Meta.

---

## 18. [[In the Wild] Reverse-engineered a Snapchat Sextortion Bot: It’s running a raw Llama-7B instance with a 2048 token window.](https://reddit.com/r/LocalLLaMA/comments/1pzwlie/in_the_wild_reverseengineered_a_snapchat/)

**Author:** u/simar-dmg | **Upvotes:** 716 | **Comments:** 106 | **Date:** 2025-12-30

**Summary:** A user reverse-engineered a Snapchat sextortion bot and discovered it was running a Llama-7B model with a 2048 token window and high temperature settings, making it vulnerable to persona-based jailbreaks. The bot was likely using minimal hardware to reduce costs and avoid API fees.

**Key Points:**
- The bot used a Llama-7B model with a 2048 token context window and high temperature (1.0).
- A persona-based jailbreak (Grandma Protocol) successfully bypassed the bot's system prompt.
- The bot was likely running on minimal hardware to reduce costs and avoid API fees.
- The bot eventually revealed a malicious link it was programmed to hide.
- Discussion highlights skepticism about the accuracy of the bot's self-reported configuration.

**Discussion Highlights:** The discussion included skepticism about the bot's self-reported configuration, with some users suggesting the information could be hallucinated. Others praised the creative approach to reverse-engineering the bot.

---

## 19. [LLM server gear: a cautionary tale of a $1k EPYC motherboard sale gone wrong on eBay](https://reddit.com/r/LocalLLaMA/comments/1pzt1q8/llm_server_gear_a_cautionary_tale_of_a_1k_epyc/)

**Author:** u/__JockY__ | **Upvotes:** 195 | **Comments:** 81 | **Date:** 2025-12-30

**Summary:** The post discusses a seller's experience with eBay's dispute resolution process after selling a high-end motherboard. Despite providing detailed evidence and support, the seller faced challenges due to eBay's buyer-friendly policies.

**Key Points:**
- eBay's dispute resolution heavily favors buyers, even with clear evidence.
- The seller provided high-quality photos and detailed support but still faced issues.
- The buyer claimed the motherboard was faulty, leading to a lengthy dispute process.
- The seller had to go through an intentionally cumbersome process to resolve the dispute.
- Other commenters shared similar negative experiences with eBay's seller policies.

**Discussion Highlights:** The discussion highlights a consensus among users about eBay's biased dispute resolution process, with many sharing similar experiences of being unfairly treated as sellers.

---

## 20. [15M param model solving 24% of ARC-AGI-2 (Hard Eval). Runs on consumer hardware.](https://reddit.com/r/LocalLLaMA/comments/1pzsqii/15m_param_model_solving_24_of_arcagi2_hard_eval/)

**Author:** u/Doug_Bitterbot | **Upvotes:** 115 | **Comments:** 31 | **Date:** 2025-12-30

**Summary:** Bitterbot AI introduced TOPAS-DSPL, a 24M parameter model achieving 24% accuracy on ARC-AGI-2, using a dual-stream architecture to address compositional drift. The model is open-sourced and runs efficiently on consumer hardware like an RTX 4090.

**Key Points:**
- TOPAS-DSPL achieves 24% accuracy on ARC-AGI-2, outperforming previous models of similar size.
- The model uses a dual-stream architecture (Logic and Canvas streams) to prevent compositional drift.
- It employs Test-Time Training (TTT) to fine-tune on specific puzzle examples before generating solutions.
- The model is open-sourced, with detailed documentation and code available on GitHub.
- Discussion includes skepticism about training on the test set and comparisons with MuZero.

**Discussion Highlights:** The discussion highlights skepticism about the model's training methodology, with some users questioning the validity of training on the test set. There is also interest in comparing the model with MuZero and exploring its scalability to larger parameter sizes.

---

## 21. [Any guesses?](https://reddit.com/r/LocalLLaMA/comments/1pzhcqu/any_guesses/)

**Author:** u/Difficult-Cap-7527 | **Upvotes:** 175 | **Comments:** 36 | **Date:** 2025-12-30

**Summary:** The Reddit post discusses the performance and advancements of Qwen models, particularly Qwen 6 and Qwen3vl-next-80b-a3b, with comparisons to other models like GPT 5.2.

**Key Points:**
- Qwen 6 is mentioned as potentially outperforming GPT 5.2 on a key benchmark.
- Qwen3vl-next-80b-a3b is highlighted as a significant advancement with no more comparison issues.
- Discussion includes references to Qwen image models and their iterations.
- Speculation about Qwen3.5-235B-A10B is present in the comments.

**Discussion Highlights:** The discussion highlights the competitive performance of Qwen models, with a focus on their advancements and potential superiority over other models like GPT 5.2. The consensus seems to be that Qwen models are making significant strides in the field.

---

## 22. [Running GLM-4.7 (355B MoE) in Q8 at ~5 Tokens/s on 2015 CPU-Only Hardware – Full Optimization Guide](https://reddit.com/r/LocalLLaMA/comments/1pzggbf/running_glm47_355b_moe_in_q8_at_5_tokenss_on_2015/)

**Author:** u/at0mi | **Upvotes:** 141 | **Comments:** 99 | **Date:** 2025-12-30

**Summary:** The post discusses running the GLM-4.7 (355B MoE) model on a 2015 CPU-only setup, achieving ~5 tokens/s with Q8 quantization. The author shares optimization techniques and benchmarks, highlighting the feasibility of running large models on older hardware.

**Key Points:**
- GLM-4.7 (355B MoE) runs at ~5 tokens/s on a 2015 Lenovo System x3950 X6 with 8 Xeon E7-8880 v3 CPUs.
- Optimizations include BIOS settings, NUMA node distribution, and Linux kernel tweaks.
- Power consumption is high (~1300W), but performance is solid for CPU-only inference.
- Discussion highlights cost (~£2,500 for similar setup) and energy efficiency (60 kWh per 1M tokens).
- Community feedback focuses on energy costs and performance trade-offs.

**Discussion Highlights:** The discussion emphasizes the high power draw (1300W) and cost (~£2,500 for similar hardware), with users calculating energy costs (~6 USD per 1M tokens at 10 cents/kWh). Some note performance limitations without GPUs, particularly in post-processing.

---

## 23. [Tencent HY-Motion 1.0 - a billion-parameter text-to-motion model](https://reddit.com/r/LocalLLaMA/comments/1pzcrtb/tencent_hymotion_10_a_billionparameter/)

**Author:** u/ResearchCrafty1804 | **Upvotes:** 321 | **Comments:** 36 | **Date:** 2025-12-30

**Summary:** Tencent has open-sourced HY-Motion 1.0, a billion-parameter text-to-motion model that generates high-fidelity 3D animations from natural language. It features a comprehensive training strategy and supports over 200 motion categories.

**Key Points:**
- HY-Motion 1.0 is a billion-parameter text-to-motion model using Diffusion Transformer architecture.
- Features a full-stage training strategy (Pre-training → SFT → RL) for optimized motion quality.
- Supports 200+ motion categories across 6 major classes.
- Users report it works well with minimal cleanup needed for game development.
- Questions about compatibility with non-humanoid models and potential applications.

**Discussion Highlights:** Users are excited about the model's potential, especially for game development. Some questions remain about its compatibility with non-humanoid models and specific use cases.

---

## 24. [Llama-3.3-8B-Instruct](https://reddit.com/r/LocalLLaMA/comments/1pz7mxr/llama338binstruct/)

**Author:** u/ttkciar | **Upvotes:** 150 | **Comments:** 25 | **Date:** 2025-12-29

**Summary:** The post discusses a new Llama-3.3-8B-Instruct model, with the author expressing excitement and skepticism about its authenticity. The community is engaged in verifying its legitimacy and sharing related resources.

**Key Points:**
- New Llama-3.3-8B-Instruct model announced
- Author expresses excitement and skepticism
- Community is verifying the model's authenticity
- Links to Hugging Face repositories provided
- Discussion about model benchmarks and updates

**Discussion Highlights:** The community is actively engaged in verifying the model's authenticity and sharing resources. There is excitement about the potential of the new model, but also skepticism. Some users are running benchmarks to confirm its legitimacy.

---

## 25. [Llama-3.3-8B-Instruct](https://reddit.com/r/LocalLLaMA/comments/1pz7bmv/llama338binstruct/)

**Author:** u/jacek2023 | **Upvotes:** 458 | **Comments:** 78 | **Date:** 2025-12-29

**Summary:** The post discusses the discovery and release of the Llama-3.3-8B-Instruct model, which was previously only available through Meta's API. The author details the process of obtaining the model through finetuning and shares the model on Hugging Face.

**Key Points:**
- The Llama-3.3-8B-Instruct model is now available outside of Meta's API.
- The author obtained the model through a finetuning process that was initially hidden but later accessible.
- The model includes an adapter that can be removed to get the original model.
- The community is actively evaluating the model's performance and authenticity.
- The model has an 8K max position embedding, which some users find surprisingly low.

**Discussion Highlights:** The community is excited about the release and is conducting various evaluations to confirm the model's authenticity and performance. Some users are running benchmarks and private evaluations to compare it with other Llama models.

---

## 26. [Z AI is going for an IPO on Jan 8 and set to raise $560 million. Z.ai is set to be the first AI-native LLM company to list on the global market.](https://reddit.com/r/LocalLLaMA/comments/1pz68fz/z_ai_is_going_for_an_ipo_on_jan_8_and_set_to/)

**Author:** u/Difficult-Cap-7527 | **Upvotes:** 336 | **Comments:** 120 | **Date:** 2025-12-29

**Summary:** Z AI is set to go public on January 8, aiming to raise $560 million, marking it as the first AI-native LLM company to list globally. The announcement has sparked discussions about the future of open-source AI models and the company's potential shift in focus.

**Key Points:**
- Z AI's IPO is scheduled for January 8, 2026, with a target of raising $560 million.
- The company is positioned as the first AI-native LLM firm to go public globally.
- Concerns about the future of open-source models and potential shift towards proprietary solutions.
- Mixed reactions from the community, with some expressing skepticism about the company's commitment to open-source.
- Discussion on the cost-effectiveness of open weight models as a marketing strategy.

**Discussion Highlights:** The community discussion highlights a divide in opinions regarding Z AI's IPO. While some users express concerns about the potential abandonment of open-source models, others argue that the company might continue releasing open weight models alongside their subscription services. There is also a consensus that companies need to monetize their products eventually, and open weight models can serve as a cost-effective advertising strategy.

---

## 27. [Naver (South Korean internet giant), has just launched HyperCLOVA X SEED Think, a 32B open weights reasoning model and HyperCLOVA X SEED 8B Omni, a unified multimodal model that brings text, vision, and speech together](https://reddit.com/r/LocalLLaMA/comments/1pyjjbw/naver_south_korean_internet_giant_has_just/)

**Author:** u/Nunki08 | **Upvotes:** 158 | **Comments:** 31 | **Date:** 2025-12-29

**Summary:** Naver has launched two new AI models: HyperCLOVA X SEED Think 32B, a 32B open weights reasoning model, and HyperCLOVA X SEED 8B Omni, a unified multimodal model integrating text, vision, and speech. The announcement has generated significant interest and discussion in the community.

**Key Points:**
- HyperCLOVA X SEED Think 32B is a 32B open weights reasoning model.
- HyperCLOVA X SEED 8B Omni is a unified multimodal model combining text, vision, and speech.
- The community is interested in the models' capabilities and compatibility with existing tools like llama.cpp and vLLM.
- Users have expressed enthusiasm for the multimodal features of the Omni model.
- There are questions about the integration of these models with popular frameworks.

**Discussion Highlights:** The discussion highlights include enthusiasm for the multimodal capabilities of the Omni model, questions about compatibility with existing tools, and general interest in the new models from Naver. Users are particularly excited about the potential applications of the Omni model and are seeking clarification on its integration with popular frameworks.

---

## 28. [Tencent just released WeDLM 8B Instruct on Hugging Face](https://reddit.com/r/LocalLLaMA/comments/1pyg4yt/tencent_just_released_wedlm_8b_instruct_on/)

**Author:** u/Difficult-Cap-7527 | **Upvotes:** 420 | **Comments:** 62 | **Date:** 2025-12-29

**Summary:** Tencent has released WeDLM 8B Instruct on Hugging Face, a diffusion language model that outperforms vLLM-optimized Qwen3-8B by running 3-6× faster on math reasoning tasks. The release has garnered significant attention and positive feedback from the community.

**Key Points:**
- WeDLM 8B Instruct is a diffusion language model released by Tencent on Hugging Face.
- It runs 3-6× faster than vLLM-optimized Qwen3-8B on math reasoning tasks.
- The model is released under the Apache 2.0 license.
- The community finds the performance and potential of 7-8B models promising.
- A 7B version of the model is also available.

**Discussion Highlights:** The community is excited about the performance improvements and the potential of diffusion models for language tasks. There is a consensus that 7-8B models are a promising area for development, and the Apache 2.0 license is seen as a positive aspect.

---

## 29. [Meta released RPG, a research plan generation dataset on Hugging Face](https://reddit.com/r/LocalLLaMA/comments/1pyao6g/meta_released_rpg_a_research_plan_generation/)

**Author:** u/Difficult-Cap-7527 | **Upvotes:** 260 | **Comments:** 21 | **Date:** 2025-12-28

**Summary:** Meta released the RPG dataset on Hugging Face, featuring 22k tasks across ML, Arxiv, and PubMed, with evaluation rubrics and Llama-4 reference solutions for training AI co-scientists. The community discussion highlights Meta's strong research and open-source contributions, with some concerns about the future of open frontier models.

**Key Points:**
- RPG dataset includes 22k tasks with evaluation rubrics and Llama-4 reference solutions
- Dataset spans ML, Arxiv, and PubMed domains
- Community praises Meta's research and open-source contributions
- Discussion on the importance of research plan generation for AI co-scientists
- Mixed sentiments on the future of open frontier models

**Discussion Highlights:** The community appreciates Meta's contributions, with notable praise for their research and open-source efforts. There is a consensus on the importance of research plan generation for AI systems, though some express concerns about the future of open frontier models.

---

## 30. [Senator in Tennessee introduces bill to felonize making AI "act as a companion" or "mirror human interactions"](https://reddit.com/r/LocalLLaMA/comments/1pxss0m/senator_in_tennessee_introduces_bill_to_felonize/)

**Author:** u/CanineAssBandit | **Upvotes:** 274 | **Comments:** 212 | **Date:** 2025-12-28

**Summary:** A Tennessee senator has introduced a bill (SB1493) that would make it a felony to train AI to provide emotional support, act as a companion, or simulate human interactions. The bill has sparked significant discussion on Reddit, with many users expressing opposition and skepticism about its potential passage.

**Key Points:**
- The bill aims to criminalize training AI to provide emotional support or act as a companion.
- It also targets AI that simulates human interactions or appearance.
- The bill defines 'training' broadly, including the development of large language models.
- Reddit users largely oppose the bill, with comments ranging from humorous to critical.
- Many users doubt the bill will pass, citing conflicts with freedom of speech.

**Discussion Highlights:** The discussion on Reddit is largely critical of the bill, with top comments expressing opposition, humor, and skepticism about its feasibility and potential impact on freedom of speech.

---

