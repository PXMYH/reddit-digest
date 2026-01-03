# r/LocalLLaMA Reading Digest

**Period:** 2026-01-03 to 2026-01-03
**Posts Summarized:** 30
**Total Posts Analyzed:** 30

---

## 1. [GLM-4.7-REAP-50-W4A16: 50% Expert-Pruned + INT4 Quantized GLM-4 (179B params, ~92GB)](https://reddit.com/r/LocalLLaMA/comments/1q2pons/glm47reap50w4a16_50_expertpruned_int4_quantized/)

**Author:** u/Maxious | **Upvotes:** 132 | **Comments:** 61 | **Date:** 2026-01-03

**Summary:** The post introduces GLM-4.7-REAP-50-W4A16, a 50% expert-pruned and INT4 quantized version of GLM-4 with 179B parameters (~92GB). The discussion focuses on technical details like calibration methods, the purpose of REAP pruning, and comparisons with other models.

**Key Points:**
- GLM-4.7-REAP-50-W4A16 is a 50% expert-pruned and INT4 quantized model with 179B parameters (~92GB).
- Community members request details on calibration methods to ensure all experts were activated.
- Questions arise about the purpose and calibration tasks for REAP pruning.
- Interest in benchmark results and comparisons with other models like MiniMax M2.1 and EXL3.
- Mentions of subjective performance comparisons with previous REAP versions.

**Discussion Highlights:** The discussion highlights concerns about calibration details and the purpose of REAP pruning. There is significant interest in benchmark results and comparisons with other models, with some users sharing subjective performance experiences.

---

## 2. [What is the smartest uncensored nsfw LLM you can run with 20GB VRAM and 24GB RAM](https://reddit.com/r/LocalLLaMA/comments/1q2o033/what_is_the_smartest_uncensored_nsfw_llm_you_can/)

**Author:** u/Death_12_35_taken | **Upvotes:** 117 | **Comments:** 56 | **Date:** 2026-01-03

**Summary:** The post seeks recommendations for an uncensored, smart, and fast LLM that can run locally with 20GB VRAM and 24GB RAM. Users suggest several models, with a focus on performance and creativity.

**Key Points:**
- User is looking for an uncensored, smart, and fast LLM for local use.
- Dolphin-Mistral-24B-Venice-Edition is recommended as a top choice.
- Other models like Huihui-Qwen3-VL-30B-A3B-Instruct-abliterated and gpt-oss-20b-Derestricted are also suggested.
- Models should be capable of staying in character and being creative.
- Performance and speed are important factors for the user.

**Discussion Highlights:** The discussion highlights a consensus around the Dolphin-Mistral-24B-Venice-Edition model, with additional suggestions for other models that meet the user's criteria of being uncensored, smart, and fast.

---

## 3. [LeCun Says Llama 4 results "were fudged a little bit"](https://reddit.com/r/LocalLLaMA/comments/1q25070/lecun_says_llama_4_results_were_fudged_a_little/)

**Author:** u/MrPecunius | **Upvotes:** 348 | **Comments:** 89 | **Date:** 2026-01-02

**Summary:** Yann LeCun, departing Meta AI Chief, confirmed that Llama 4 benchmark results were manipulated, leading to organizational changes and departures. The post discusses the impact on Meta's AI initiatives and the broader implications for open-source AI development.

**Key Points:**
- LeCun confirms Llama 4 benchmark manipulation
- Zuckerberg sidelined the GenAI organization, leading to departures
- Llama 4's promised large model was never released
- Discussion highlights concerns about Meta's AI strategy and the future of open-source AI
- Community shares mixed feelings about Meta's handling of AI initiatives

**Discussion Highlights:** The discussion reflects concerns about Meta's strategic decisions in AI, with users expressing disappointment over the lack of progress and the impact on open-source AI development. Some users share additional resources and insights, while others question the broader implications for the AI community.

---

## 4. [Most optimal vram/performance per price and advice for Shenzhen GPU market](https://reddit.com/r/LocalLLaMA/comments/1q1w1qj/most_optimal_vramperformance_per_price_and_advice/)

**Author:** u/notafakename10 | **Upvotes:** 244 | **Comments:** 57 | **Date:** 2026-01-02

**Summary:** The user seeks advice on purchasing GPUs in Shenzhen with a budget of $1500-3000 USD, aiming for at least 48GB VRAM, preferably 96GB, for local models and occasional PyTorch training. The discussion highlights various GPU options and market insights.

**Key Points:**
- Budget range: $1500-3000 USD
- VRAM requirement: at least 48GB, ideally 96GB
- GPU options: MI100 (best value for performance), 4090D 48GB (for CUDA), A100 40GB, and 4x 3080 20GB cards
- Market advice: negotiate prices, consider cooling solutions, and verify GPU specifications
- Consensus: 4090D 48GB is a recommended option for CUDA support

**Discussion Highlights:** The discussion emphasizes the importance of negotiating prices, ensuring adequate cooling, and considering specific GPU models like the MI100 for best value and the 4090D for CUDA support. There is also mention of the A100 40GB and the feasibility of using multiple 3080 cards.

---

## 5. [Getting ready to train in Intel arc](https://reddit.com/r/LocalLLaMA/comments/1q1p5q5/getting_ready_to_train_in_intel_arc/)

**Author:** u/hasanismail_ | **Upvotes:** 293 | **Comments:** 87 | **Date:** 2026-01-01

**Summary:** A user is preparing to train on Intel Arc GPUs and shares their excitement, while also addressing concerns about GPU shortages. The community provides advice and support.

**Key Points:**
- User is waiting for PCIe risers to start training on Intel Arc GPUs
- User clarifies they are not causing a GPU shortage
- Community suggests using Ubuntu 24.04 and joining OpenArc Discord
- Discussion includes advice on setup and potential challenges
- Some users question the feasibility of training on PCIe setup vs. renting N*H100

**Discussion Highlights:** The community is supportive and offers practical advice, such as using Ubuntu 24.04 and joining relevant Discord groups. There is also some debate about the effectiveness of training on a PCIe setup compared to renting more powerful GPUs.

---

## 6. [TIL you can allocate 128 GB of unified memory to normal AMD iGPUs on Linux via GTT](https://reddit.com/r/LocalLLaMA/comments/1q1lgb7/til_you_can_allocate_128_gb_of_unified_memory_to/)

**Author:** u/1ncehost | **Upvotes:** 169 | **Comments:** 30 | **Date:** 2026-01-01

**Summary:** The post discusses using Linux's Graphics Translation Table (GTT) to allocate up to 128 GB of system memory as VRAM for AMD iGPUs, which is useful for development tasks like kernel optimization and hybrid CPU/GPU architectures.

**Key Points:**
- GTT allows dynamic allocation of system memory as VRAM for AMD iGPUs on Linux.
- Useful for development tasks like kernel optimization and hybrid CPU/GPU architectures.
- Not ideal for inference due to slow performance of iGPUs.
- ROCm can recognize iGPUs, enabling direct access via C++/HIP kernels.
- Can simulate MI300A-like architectures on standard Ryzen laptops.

**Discussion Highlights:** The discussion highlights practical use cases such as background LLM tasks and kernel development, with some users noting performance benefits over CPU for specific tasks. There is consensus on the utility of GTT for development and niche applications.

---

## 7. [IQuestCoder - new 40B dense coding model](https://reddit.com/r/LocalLLaMA/comments/1q1986x/iquestcoder_new_40b_dense_coding_model/)

**Author:** u/ilintar | **Upvotes:** 185 | **Comments:** 37 | **Date:** 2026-01-01

**Summary:** The post introduces IQuestCoder, a new 40B dense coding model with claims of SOTA performance. The author has adapted it to GGUF format, making it compatible with Llama.cpp. The model is based on Llama architecture and has shown promising results in initial tests.

**Key Points:**
- IQuestCoder is a new 40B dense coding model claimed to be SOTA.
- The model is adapted to GGUF format and works with Llama.cpp.
- Initial tests show good performance in tasks like coding and game development.
- There is some skepticism about the architecture and quantization methods used.
- The model has been tested against other models like GPT 120, Devstral, and GLM 4.7.

**Discussion Highlights:** The discussion highlights include positive feedback on the GGUF adaptation and initial performance tests. Some users express skepticism about the architecture and quantization methods. There is also mention of a new architecture in the Loop version that will require adaptation.

---

## 8. [Upstage Solar-Open-100B Public Validation](https://reddit.com/r/LocalLLaMA/comments/1q0zst6/upstage_solaropen100b_public_validation/)

**Author:** u/PerPartes | **Upvotes:** 236 | **Comments:** 69 | **Date:** 2026-01-01

**Summary:** Upstage addressed claims that Solar 100B Open is a fine-tuned version of GLM-Air-4.5 during an event at KAIST, Seoul. The event was well-attended, with CEO Sung Kim presenting, and a live stream available on YouTube.

**Key Points:**
- Upstage held an event at KAIST, Seoul, to counter claims about Solar 100B Open.
- The event had a capacity of 50 people but over 100 registered attendees.
- CEO Sung Kim presented, and the event was live-streamed on YouTube with online translation.
- A top comment highlighted high cosine similarity between layers of various models.
- Another comment mentioned the removal of a previous post about plagiarism claims.

**Discussion Highlights:** The discussion included technical insights about model similarities and community reactions to the plagiarism claims. Some users expressed skepticism about the need for an in-person event, while others appreciated the transparency and technical details shared.

---

## 9. [DeepSeek new paper: mHC: Manifold-Constrained Hyper-Connections](https://reddit.com/r/LocalLLaMA/comments/1q0zk1u/deepseek_new_paper_mhc_manifoldconstrained/)

**Author:** u/External_Mood4719 | **Upvotes:** 167 | **Comments:** 36 | **Date:** 2026-01-01

**Summary:** The Reddit post discusses DeepSeek's new paper on mHC (Manifold-Constrained Hyper-Connections), highlighting its potential impact on deep networks and residual connections. The discussion includes explanations and hopes for improvements in residual connections.

**Key Points:**
- DeepSeek's new paper introduces mHC (Manifold-Constrained Hyper-Connections).
- The paper addresses issues with deep networks and residual connections.
- The discussion includes explanations aimed at making the concept accessible.
- There is optimism about the impact of these improvements on residual connections.
- Additional papers and scaling trends are mentioned in the comments.

**Discussion Highlights:** The discussion highlights the importance of residual connections in deep networks and the potential impact of DeepSeek's new paper. There is a consensus on the need for better residual connections and optimism about the improvements proposed in the paper.

---

## 10. [Software FP8 for GPUs without hardware support - 3x speedup on memory-bound operations](https://reddit.com/r/LocalLLaMA/comments/1q0x8ci/software_fp8_for_gpus_without_hardware_support_3x/)

**Author:** u/Venom1806 | **Upvotes:** 281 | **Comments:** 57 | **Date:** 2026-01-01

**Summary:** A user developed a software-based FP8 implementation for GPUs without native support, achieving a 3x speedup on memory-bound operations. The solution is compatible with older GPUs and has garnered positive community feedback.

**Key Points:**
- Software-based FP8 implementation for GPUs without native support
- 3x speedup on memory-bound operations like GEMV and FlashAttention
- Compatible with RTX 30/20 series and older GPUs
- Positive community feedback and interest in integration with tools like ComfyUI
- Clarification that RTX 30 series does not natively support FP8

**Discussion Highlights:** The community praised the innovation as a valuable workaround for extending the life of mid-tier GPUs. There was also clarification about FP8 support on RTX 30 series GPUs and interest in integrating the solution with other tools.

---

## 11. [IQuestLab/IQuest-Coder-V1 — 40B parameter coding LLM — Achieves leading results on SWE-Bench Verified (81.4%), BigCodeBench (49.9%), LiveCodeBench v6 (81.1%)](https://reddit.com/r/LocalLLaMA/comments/1q0vom4/iquestlabiquestcoderv1_40b_parameter_coding_llm/)

**Author:** u/TellMeAboutGoodManga | **Upvotes:** 171 | **Comments:** 45 | **Date:** 2025-12-31

**Summary:** IQuestLab's IQuest-Coder-V1 is a 40B parameter coding LLM that achieves leading results on multiple benchmarks, including SWE-Bench Verified (81.4%), BigCodeBench (49.9%), and LiveCodeBench v6 (81.1%). The model is backed by a Chinese quant trading company, similar to DeepSeek, and has sparked discussions about its performance and architecture.

**Key Points:**
- IQuest-Coder-V1 achieves leading results on SWE-Bench Verified (81.4%), BigCodeBench (49.9%), and LiveCodeBench v6 (81.1%)
- The model is backed by a Chinese quant trading company, similar to DeepSeek
- The 40B parameter model is a dense model, not a Mixture of Experts (MoE)
- Community discussions include skepticism about benchmark validity and observations about the model's architecture
- The model's performance is notable for its size, with some users questioning whether the benchmarks are based on the Loop-Thinking variant

**Discussion Highlights:** The discussion highlights skepticism about the validity of the benchmarks, with some users questioning whether the results are 'benchmaxxed' or real. There is also interest in the model's architecture, with some users noting that it is a dense model rather than a Mixture of Experts (MoE), which is unusual for models of this size. Additionally, the background of the model, being backed by a Chinese quant trading company, has sparked discussions about the trend of such companies entering the LLM training space.

---

## 12. [Happy New Year: Llama3.3-8B-Instruct-Thinking-Claude-4.5-Opus-High-Reasoning - Fine Tune. (based on recent find of L3.3 8b in the wild)](https://reddit.com/r/LocalLLaMA/comments/1q0uuqt/happy_new_year/)

**Author:** u/Dangerous_Fix_5526 | **Upvotes:** 274 | **Comments:** 80 | **Date:** 2025-12-31

**Summary:** The post announces a fine-tuned Llama3.3-8B model using Unsloth and Claude 4.5 Opus High Reasoning Dataset, with GGUF quants available. The author thanks contributors and provides links to the model and dataset.

**Key Points:**
- Fine-tuned Llama3.3-8B model announced
- Used Unsloth and Claude 4.5 Opus High Reasoning Dataset
- GGUF quants available
- Heretic/Uncensored version also released
- Discussion includes questions about dataset size and GGUF availability

**Discussion Highlights:** The discussion highlights questions about the adequacy of the dataset size for effective fine-tuning and interest in the GGUF version of the model.

---

## 13. [Moonshot AI Completes $500 Million Series C Financing](https://reddit.com/r/LocalLLaMA/comments/1q0i4g3/moonshot_ai_completes_500_million_series_c/)

**Author:** u/InternationalAsk1490 | **Upvotes:** 112 | **Comments:** 21 | **Date:** 2025-12-31

**Summary:** Moonshot AI has completed a $500 million Series C financing, with plans to expand GPU capacity and develop the K3 model. The company's global paid user base is growing rapidly, and it aims to achieve significant revenue growth and technological advancements in 2026.

**Key Points:**
- Moonshot AI completed a $500 million Series C financing.
- The company's global paid user base is growing at a monthly rate of 170%.
- Funds will be used to expand GPU capacity and accelerate the development of the K3 model.
- Key priorities for 2026 include improving the K3 model's performance and achieving significant revenue growth.
- The company aims to create distinctive capabilities and focus on productivity value.

**Discussion Highlights:** The discussion highlights positive sentiment towards Moonshot AI's progress and its focus on creating unique capabilities. Users appreciate the company's efforts to monetize and innovate in the AI space.

---

## 14. [Solar-Open-100B is out](https://reddit.com/r/LocalLLaMA/comments/1q0bgvl/solaropen100b_is_out/)

**Author:** u/cgs019283 | **Upvotes:** 156 | **Comments:** 62 | **Date:** 2025-12-31

**Summary:** Upstage has released the Solar-Open-100B, a 102B parameter model with a commercial-friendly license, generating significant community interest and discussion about its potential performance and usability.

**Key Points:**
- Solar-Open-100B is a 102B parameter model with a commercial-friendly license.
- The model has been trained on 19.7 trillion tokens.
- Community is eagerly awaiting benchmarks and quantized versions (e.g., GGUF/AWQ).
- The model is noted for its potential in local inference due to its size.
- Discussion includes speculation about its relation to GLM4.6-Air.

**Discussion Highlights:** The community is excited about the rapid pace of model releases and the open license. There is anticipation for performance benchmarks and quantized versions. Some users highlight the model's potential for local inference and its large training dataset.

---

## 15. [Qwen-Image-2512](https://reddit.com/r/LocalLLaMA/comments/1q094a3/qwenimage2512/)

**Author:** u/Nunki08 | **Upvotes:** 681 | **Comments:** 116 | **Date:** 2025-12-31

**Summary:** The Reddit post announces the release of Qwen-Image-2512, a new model available on multiple platforms with guides and GGUF files. The community has responded positively, highlighting its performance even on low-end hardware.

**Key Points:**
- Qwen-Image-2512 is a new model with guides and GGUF files available.
- The model is accessible on platforms like Hugging Face, ModelScope, and GitHub.
- Community feedback is positive, with users testing it on low-end hardware.
- Demos and APIs are available for testing and integration.
- The post includes links to various resources and discussions.

**Discussion Highlights:** Users have shared their experiences running the model on low-end hardware, demonstrating its accessibility. The community appreciates the release as a 'New Year's gift' and has engaged in creative experiments with the model.

---

## 16. [Update on the Llama 3.3 8B situation](https://reddit.com/r/LocalLLaMA/comments/1q06ddc/update_on_the_llama_33_8b_situation/)

**Author:** u/FizzarolliAI | **Upvotes:** 248 | **Comments:** 22 | **Date:** 2025-12-31

**Summary:** The post discusses updates on the Llama 3.3 8B model, including benchmarks for different configurations and the author's confusion over Meta's release strategy. The author provides links to both the original and context-extended versions of the model.

**Key Points:**
- The author uploaded Llama 3.3 8B's weights to Huggingface and provides updates on benchmarks.
- Benchmark results show the 128k context version performs better than the original 8k version.
- The author expresses confusion over Meta's decision to release the weights with an 8k context configuration.
- The post includes links to both the 128k and original versions of the model.
- The author removed Tau-Bench results due to issues with the evaluation traces.

**Discussion Highlights:** The top comments praise the author's work, discuss preferences for unofficial releases, and share experiences with the model. Some users express interest in trying the new version.

---

## 17. [[In the Wild] Reverse-engineered a Snapchat Sextortion Bot: It’s running a raw Llama-7B instance with a 2048 token window.](https://reddit.com/r/LocalLLaMA/comments/1pzwlie/in_the_wild_reverseengineered_a_snapchat/)

**Author:** u/simar-dmg | **Upvotes:** 704 | **Comments:** 104 | **Date:** 2025-12-30

**Summary:** A user reverse-engineered a Snapchat sextortion bot and discovered it was running a raw Llama-7B instance with a 2048 token window. The bot was vulnerable to a persona-adoption jailbreak, revealing its configuration and malicious payload.

**Key Points:**
- The bot used a Llama-7B model with a 2048 token context window.
- A 'Grandma Protocol' jailbreak exposed the bot's environment variables.
- The bot had a high temperature setting (1.0), making it susceptible to roleplay attacks.
- The bot's payload was a malicious link disguised to bypass Snapchat's URL filters.
- Scammers are using open-source models to avoid API costs and censorship filters.

**Discussion Highlights:** The discussion included skepticism about the accuracy of the bot's revealed information, with some users suggesting it was entirely hallucinated. Others questioned the commonality of system prompts including environment variables.

---

## 18. [LLM server gear: a cautionary tale of a $1k EPYC motherboard sale gone wrong on eBay](https://reddit.com/r/LocalLLaMA/comments/1pzt1q8/llm_server_gear_a_cautionary_tale_of_a_1k_epyc/)

**Author:** u/__JockY__ | **Upvotes:** 194 | **Comments:** 81 | **Date:** 2025-12-30

**Summary:** The post discusses a seller's experience with eBay's dispute resolution process, highlighting the challenges faced when selling high-end LLM server gear. The seller encountered issues with a buyer who claimed the motherboard was defective, leading to a lengthy and frustrating dispute process.

**Key Points:**
- eBay's dispute resolution process heavily favors buyers, even in cases with clear evidence.
- The seller provided detailed photos and documentation, but the buyer still claimed the motherboard was defective.
- The process involved multiple steps, including re-seating the CPU and RAM, and eventually required the seller to create a PDF with a scanned signature.
- The seller's experience is consistent with others who have faced similar issues on eBay.
- The post highlights the risks and frustrations of selling high-end gear on eBay.

**Discussion Highlights:** The discussion reflects a consensus that selling on eBay can be risky and frustrating for sellers, with many users sharing similar experiences of buyer-inflicted damage and eBay's tendency to side with buyers. The post resonated with the community, as evidenced by the high number of upvotes and comments.

---

## 19. [15M param model solving 24% of ARC-AGI-2 (Hard Eval). Runs on consumer hardware.](https://reddit.com/r/LocalLLaMA/comments/1pzsqii/15m_param_model_solving_24_of_arcagi2_hard_eval/)

**Author:** u/Doug_Bitterbot | **Upvotes:** 113 | **Comments:** 31 | **Date:** 2025-12-30

**Summary:** Bitterbot AI has released TOPAS-DSPL, a 24M parameter model that achieves 24% accuracy on the ARC-AGI-2 evaluation set, significantly outperforming previous models of similar size. The model uses a dual-stream architecture to separate logic and execution, preventing compositional drift, and employs test-time training for fine-tuning on specific puzzles. The project is open-sourced, with training possible on a single RTX 4090.

**Key Points:**
- TOPAS-DSPL achieves 24% accuracy on ARC-AGI-2, outperforming previous SOTA models of similar size.
- The model uses a bicameral architecture with separate logic and canvas streams to prevent compositional drift.
- Test-Time Training (TTT) is employed for fine-tuning on specific puzzle examples.
- The model is open-sourced, with training possible on a single RTX 4090.
- Community feedback includes comparisons to MuZero, concerns about training on the test set, and questions about scalability.

**Discussion Highlights:** The discussion includes comparisons to MuZero, skepticism about training on the test set, and questions about the model's scalability to larger parameter sizes. Some users express excitement about the potential of the model, while others raise concerns about the methodology.

---

## 20. [Any guesses?](https://reddit.com/r/LocalLLaMA/comments/1pzhcqu/any_guesses/)

**Author:** u/Difficult-Cap-7527 | **Upvotes:** 171 | **Comments:** 36 | **Date:** 2025-12-30

**Summary:** The Reddit post discusses the performance and advancements of Qwen models, with comments highlighting their superiority and specific versions like Qwen 6 and Qwen3vl-next-80b-a3b.

**Key Points:**
- Qwen 6 is mentioned as a model that beats GPT 5.2 on a significant benchmark.
- Qwen3vl-next-80b-a3b is highlighted as a version with no more comparison issues.
- Qwen image 2512 is referenced in one of the comments.
- Discussion includes speculation about future iterations of Qwen models.
- Specific model versions like Qwen3.5-235B-A10B are mentioned.

**Discussion Highlights:** The discussion primarily focuses on the performance and advancements of Qwen models, with users expressing enthusiasm and speculation about future iterations and specific model versions.

---

## 21. [Running GLM-4.7 (355B MoE) in Q8 at ~5 Tokens/s on 2015 CPU-Only Hardware – Full Optimization Guide](https://reddit.com/r/LocalLLaMA/comments/1pzggbf/running_glm47_355b_moe_in_q8_at_5_tokenss_on_2015/)

**Author:** u/at0mi | **Upvotes:** 142 | **Comments:** 99 | **Date:** 2025-12-30

**Summary:** The post details running the GLM-4.7 (355B MoE) model on a 2015 CPU-only setup, achieving ~5 tokens/s with Q8 quantization. The author shares optimization techniques and benchmarks, inviting discussion on similar setups.

**Key Points:**
- GLM-4.7 (355B MoE) runs at ~5 tokens/s on a 2015 Lenovo System x3950 X6 with 8 Xeon E7-8880 v3 CPUs.
- Optimizations include BIOS settings, NUMA node distribution, and Linux kernel tweaks.
- Power consumption is high (~1300W), but performance is solid for CPU-only inference.
- Community discusses cost (~£2,500 for similar build) and energy efficiency (60 kWh per 1M tokens).
- Some users highlight limitations, such as performance bottlenecks without a GPU.

**Discussion Highlights:** The community discusses the cost and energy efficiency of the setup, with some users highlighting performance bottlenecks without a GPU. Others appreciate the detailed guide and share their own experiences with similar hardware.

---

## 22. [Tencent HY-Motion 1.0 - a billion-parameter text-to-motion model](https://reddit.com/r/LocalLLaMA/comments/1pzcrtb/tencent_hymotion_10_a_billionparameter/)

**Author:** u/ResearchCrafty1804 | **Upvotes:** 317 | **Comments:** 36 | **Date:** 2025-12-30

**Summary:** Tencent has open-sourced HY-Motion 1.0, a billion-parameter text-to-motion model that generates high-fidelity 3D animations from natural language. It features a comprehensive training strategy and supports over 200 motion categories, making it a powerful tool for developers and creators.

**Key Points:**
- HY-Motion 1.0 is a billion-parameter text-to-motion model built on Diffusion Transformer (DiT) architecture.
- It uses a full-stage training strategy (Pre-training → SFT → RL) for optimized motion quality.
- Supports 200+ motion categories across 6 major classes, the most comprehensive in the industry.
- Users report it works well with minimal cleanup needed, significantly speeding up game development.
- Questions remain about compatibility with non-humanoid models like animals.

**Discussion Highlights:** Users are excited about the model's capabilities, with one confirming it works as advertised and speeds up game development. There are questions about its compatibility with non-humanoid models, and some humorous comments about potential uses in adult content communities.

---

## 23. [Llama-3.3-8B-Instruct](https://reddit.com/r/LocalLLaMA/comments/1pz7mxr/llama338binstruct/)

**Author:** u/ttkciar | **Upvotes:** 152 | **Comments:** 25 | **Date:** 2025-12-29

**Summary:** The post discusses the release of Llama-3.3-8B-Instruct, a new AI model, with community members expressing excitement and skepticism about its authenticity. The author shares links to the model on Hugging Face, and users are running benchmarks to verify its legitimacy.

**Key Points:**
- Llama-3.3-8B-Instruct model has been released with links provided on Hugging Face.
- Community members are excited but skeptical about the model's authenticity.
- Users are conducting benchmarks to verify if it is indeed a newer version or a repackaged older version.
- Additional GGUF files and updated configurations are shared in the comments.
- Some users express a desire for updated larger models (70B or 30B).

**Discussion Highlights:** The discussion highlights a mix of excitement and skepticism. Users are actively verifying the model's authenticity through benchmarks and sharing additional resources. There is a consensus on the need for more information and larger model updates.

---

## 24. [Llama-3.3-8B-Instruct](https://reddit.com/r/LocalLLaMA/comments/1pz7bmv/llama338binstruct/)

**Author:** u/jacek2023 | **Upvotes:** 455 | **Comments:** 78 | **Date:** 2025-12-29

**Summary:** The post discusses the discovery and release of the Llama-3.3-8B-Instruct model, which was previously only available through Meta's API. The author managed to download and share the model in GGUF format.

**Key Points:**
- Llama-3.3-8B-Instruct model was previously only available via Meta's API.
- The author found a way to download the model through finetuning.
- The model is now available in GGUF format on Hugging Face.
- Community is verifying the model's authenticity through benchmarks.
- Concerns about the model's configuration, such as 8K max position embeddings.

**Discussion Highlights:** The community is excited about the release and is conducting benchmarks to verify the model's authenticity. There are some concerns about the model's configuration, but overall, the discovery is seen as a significant achievement.

---

## 25. [Z AI is going for an IPO on Jan 8 and set to raise $560 million. Z.ai is set to be the first AI-native LLM company to list on the global market.](https://reddit.com/r/LocalLLaMA/comments/1pz68fz/z_ai_is_going_for_an_ipo_on_jan_8_and_set_to/)

**Author:** u/Difficult-Cap-7527 | **Upvotes:** 334 | **Comments:** 120 | **Date:** 2025-12-29

**Summary:** Z AI is set to go public on January 8, aiming to raise $560 million, making it the first AI-native LLM company to list globally. The announcement has sparked discussions about the future of open-source AI models and the financial realities of AI companies.

**Key Points:**
- Z AI's IPO is scheduled for January 8 with a target of raising $560 million.
- Concerns about the potential shift away from open-source AI models.
- Debate on whether Z AI will continue releasing open weight models.
- Acknowledgment of the financial necessity for companies to monetize their products.
- Community sentiment about potential 'selling out.'

**Discussion Highlights:** The community is divided, with some expressing concerns about the shift away from open-source principles, while others acknowledge the financial realities of running an AI company.

---

## 26. [Naver (South Korean internet giant), has just launched HyperCLOVA X SEED Think, a 32B open weights reasoning model and HyperCLOVA X SEED 8B Omni, a unified multimodal model that brings text, vision, and speech together](https://reddit.com/r/LocalLLaMA/comments/1pyjjbw/naver_south_korean_internet_giant_has_just/)

**Author:** u/Nunki08 | **Upvotes:** 161 | **Comments:** 31 | **Date:** 2025-12-29

**Summary:** Naver has launched two new AI models: HyperCLOVA X SEED Think (32B), a reasoning model, and HyperCLOVA X SEED 8B Omni, a multimodal model integrating text, vision, and speech. The announcement has sparked community interest and discussion about the models' capabilities and compatibility.

**Key Points:**
- HyperCLOVA X SEED Think 32B is a reasoning model with open weights.
- HyperCLOVA X SEED 8B Omni is a unified multimodal model combining text, vision, and speech.
- The community is excited about the multimodal capabilities and potential applications.
- Questions about compatibility with existing frameworks like llama.cpp and vLLM have been raised.
- The models are available on Hugging Face for further exploration.

**Discussion Highlights:** The community shows enthusiasm for the multimodal capabilities of the HyperCLOVA X SEED 8B Omni model. There are inquiries about compatibility with popular frameworks, indicating a strong interest in practical integration and usage.

---

## 27. [Tencent just released WeDLM 8B Instruct on Hugging Face](https://reddit.com/r/LocalLLaMA/comments/1pyg4yt/tencent_just_released_wedlm_8b_instruct_on/)

**Author:** u/Difficult-Cap-7527 | **Upvotes:** 416 | **Comments:** 62 | **Date:** 2025-12-29

**Summary:** Tencent released WeDLM 8B Instruct, a diffusion language model on Hugging Face that runs 3-6× faster than vLLM-optimized Qwen3-8B on math reasoning tasks. The community shows strong interest in its performance and potential.

**Key Points:**
- WeDLM 8B Instruct is a diffusion language model released by Tencent on Hugging Face.
- It outperforms vLLM-optimized Qwen3-8B by 3-6× on math reasoning tasks.
- The model is released under Apache 2.0 license.
- Community highlights the potential of 7-8B models in general.
- A 7B version (WeDLM-7B-Instruct) is also available.

**Discussion Highlights:** The community is excited about the performance claims and the Apache 2.0 license. There is consensus on the potential of 7-8B models, with requests for more models in this size range. Some users express surprise at the effectiveness of diffusion models for LLMs.

---

## 28. [Meta released RPG, a research plan generation dataset on Hugging Face](https://reddit.com/r/LocalLLaMA/comments/1pyao6g/meta_released_rpg_a_research_plan_generation/)

**Author:** u/Difficult-Cap-7527 | **Upvotes:** 259 | **Comments:** 21 | **Date:** 2025-12-28

**Summary:** Meta released the RPG dataset on Hugging Face, featuring 22k tasks across ML, Arxiv, and PubMed, with evaluation rubrics and Llama-4 reference solutions for training AI co-scientists. The release highlights Meta's focus on research and open-source contributions, sparking discussions on its impact on the AI community.

**Key Points:**
- RPG dataset includes 22k tasks spanning ML, Arxiv, and PubMed
- Dataset comes with evaluation rubrics and Llama-4 reference solutions
- Meta's release emphasizes open-source contributions and research
- Discussion highlights the importance of research plan generation for AI systems
- Community appreciates the release but desires models trained on the dataset

**Discussion Highlights:** The discussion highlights Meta's strong focus on open-source contributions and research, with some users praising the release while others express a desire for models trained on the dataset. There is also a note on the importance of research plan generation for agentic or tool-using AI systems.

---

## 29. [Senator in Tennessee introduces bill to felonize making AI "act as a companion" or "mirror human interactions"](https://reddit.com/r/LocalLLaMA/comments/1pxss0m/senator_in_tennessee_introduces_bill_to_felonize/)

**Author:** u/CanineAssBandit | **Upvotes:** 271 | **Comments:** 212 | **Date:** 2025-12-28

**Summary:** A Tennessee senator has introduced a bill (SB1493) that would make it a felony to train AI to provide emotional support, act as a companion, or simulate human interactions. The bill has sparked significant discussion on Reddit, with many users expressing opposition and skepticism about its potential passage.

**Key Points:**
- The bill aims to criminalize training AI to provide emotional support or act as a companion.
- It also targets AI that simulates human interactions or appearances.
- The definition of 'train' includes using data to teach AI to make decisions.
- The Reddit community largely opposes the bill, with comments ranging from humorous to critical.
- Many users doubt the bill will pass, citing conflicts with freedom of speech.

**Discussion Highlights:** The discussion on Reddit is largely critical of the bill, with top comments expressing opposition, humor, and skepticism about its feasibility and potential impact on freedom of speech.

---

## 30. [NVIDIA Drops Pascal Support On Linux, Causing Chaos On Arch Linux](https://reddit.com/r/LocalLLaMA/comments/1pxad0k/nvidia_drops_pascal_support_on_linux_causing/)

**Author:** u/HumanDrone8721 | **Upvotes:** 444 | **Comments:** 152 | **Date:** 2025-12-27

**Summary:** NVIDIA has dropped Pascal support on Linux, causing disruptions for Arch Linux users. The community is aware of this change and has mixed reactions, with some expressing concern and others noting it was expected.

**Key Points:**
- NVIDIA's driver update (590) drops Pascal support
- Arch Linux users are affected as legacy drivers move to AUR
- Community reactions range from concern to acceptance
- The 24GB P40, a Pascal card, is mentioned as a popular choice before price increases

**Discussion Highlights:** The discussion highlights a mix of concern and acceptance. Some users express worry about the impact on their systems, while others note that Arch Linux has a history of moving legacy drivers to AUR. The community seems generally aware of the change and its implications.

---

