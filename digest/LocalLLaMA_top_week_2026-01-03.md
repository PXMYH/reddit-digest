# r/LocalLLaMA Reading Digest

**Period:** 2026-01-03 to 2026-01-03
**Posts Summarized:** 29
**Total Posts Analyzed:** 29

---

## 1. [GLM-4.7-REAP-50-W4A16: 50% Expert-Pruned + INT4 Quantized GLM-4 (179B params, ~92GB)](https://reddit.com/r/LocalLLaMA/comments/1q2pons/glm47reap50w4a16_50_expertpruned_int4_quantized/)

**Author:** u/Maxious | **Upvotes:** 155 | **Comments:** 65 | **Date:** 2026-01-03

**Summary:** The post introduces GLM-4.7-REAP-50-W4A16, a 50% expert-pruned and INT4 quantized version of GLM-4 with 179B parameters (~92GB). The discussion focuses on calibration details, the purpose of REAP pruning, and interest in benchmarks and comparisons with other models. Key points include the model's specifications, concerns about calibration transparency, questions about REAP pruning tasks, and interest in further benchmarks. The discussion highlights the need for calibration details and transparency, as well as community interest in understanding the pruning process and seeing performance comparisons.

---

## 2. [What is the smartest uncensored nsfw LLM you can run with 20GB VRAM and 24GB RAM](https://reddit.com/r/LocalLLaMA/comments/1q2o033/what_is_the_smartest_uncensored_nsfw_llm_you_can/)

**Author:** u/Death_12_35_taken | **Upvotes:** 140 | **Comments:** 67 | **Date:** 2026-01-03

**Summary:** The post seeks recommendations for an uncensored, smart, and fast LLM that can run locally with 20GB VRAM and 24GB RAM. Users suggest several models, with a focus on performance and creativity.

**Key Points:**
- User is looking for an uncensored, smart, and fast LLM for local use.
- Models should be creative and stay in character.
- Top recommendations include Dolphin-Mistral-24B-Venice-Edition, models from the UGI-Leaderboard, Huihui-Qwen3-VL-30B-A3B-Instruct-abliterated, and gpt-oss-20b-Derestricted.
- Performance and local running capabilities are key considerations.

**Discussion Highlights:** The discussion highlights several model recommendations, with Dolphin-Mistral-24B-Venice-Edition being the most upvoted. Users emphasize the importance of performance, creativity, and the ability to run locally with the specified hardware constraints.

---

## 3. [LeCun Says Llama 4 results "were fudged a little bit"](https://reddit.com/r/LocalLLaMA/comments/1q25070/lecun_says_llama_4_results_were_fudged_a_little/)

**Author:** u/MrPecunius | **Upvotes:** 354 | **Comments:** 89 | **Date:** 2026-01-02

**Summary:** Yann LeCun confirmed that Llama 4 benchmarks were manipulated, leading to organizational changes at Meta and the sidelining of the GenAI team. This has resulted in a lack of follow-up on promised models and significant staff departures.

**Key Points:**
- LeCun confirms Llama 4 benchmark manipulation
- Zuckerberg sidelined the GenAI organization at Meta
- Significant staff departures and lack of follow-up on Llama 4
- Community disappointment over the failure of Llama to succeed
- Shared PDF link for the complete article

**Discussion Highlights:** The discussion highlights disappointment in Meta's handling of the Llama project, with users expressing regret over the failure of a US company to succeed in open-source AI. There is also a shared PDF link for the complete article and speculation about the strategic missteps at Meta.

---

## 4. [Most optimal vram/performance per price and advice for Shenzhen GPU market](https://reddit.com/r/LocalLLaMA/comments/1q1w1qj/most_optimal_vramperformance_per_price_and_advice/)

**Author:** u/notafakename10 | **Upvotes:** 246 | **Comments:** 58 | **Date:** 2026-01-02

**Summary:** The post seeks advice on purchasing GPUs in Shenzhen with a budget of $1500-3000 USD, aiming for at least 48GB VRAM and good performance for local models and PyTorch training. The discussion highlights various GPU options and their pros and cons. Key points include the budget range, target VRAM, use case, options considered, and the importance of cooling and negotiation. The discussion suggests MI100 for best value if CUDA is not needed, and 4090D 48GB if CUDA is required. Other options like A100 and A40s are mentioned for their high VRAM and performance.

---

## 5. [Getting ready to train in Intel arc](https://reddit.com/r/LocalLLaMA/comments/1q1p5q5/getting_ready_to_train_in_intel_arc/)

**Author:** u/hasanismail_ | **Upvotes:** 297 | **Comments:** 87 | **Date:** 2026-01-01

**Summary:** A user is preparing to train on Intel Arc GPUs and shares their excitement, while also addressing potential concerns about GPU shortages. The community provides feedback and suggestions.

**Key Points:**
- User is waiting for PCIe risers to start training on Intel Arc GPUs.
- User clarifies they are not causing a GPU shortage.
- Community suggests using Ubuntu 24.04 and mentions support for Intel Arc in Unsloth.
- Recommendation to join the OpenArc Discord for setup assistance.
- Discussion about the feasibility of training on PCIe setup versus renting N*H100 from Vast.

**Discussion Highlights:** The community is supportive and provides practical advice, such as using Ubuntu 24.04 and joining the OpenArc Discord. There is also a discussion about the feasibility of training on a PCIe setup compared to renting more powerful GPUs.

---

## 6. [TIL you can allocate 128 GB of unified memory to normal AMD iGPUs on Linux via GTT](https://reddit.com/r/LocalLLaMA/comments/1q1lgb7/til_you_can_allocate_128_gb_of_unified_memory_to/)

**Author:** u/1ncehost | **Upvotes:** 176 | **Comments:** 30 | **Date:** 2026-01-01

**Summary:** The post discusses how AMD iGPUs on Linux can use up to 128 GB of system memory as VRAM via Graphics Translation Table (GTT), which is useful for development and hybrid CPU/GPU architectures. The author shares their experience using this feature for kernel development while training a model on their main GPU.

**Key Points:**
- AMD iGPUs on Linux can allocate up to 128 GB of system memory as VRAM using GTT.
- This feature is dynamically allocated and useful for development and profiling.
- iGPUs are slow for inference, but useful for background tasks and kernel development.
- ROCm can recognize iGPUs, but direct access via C++/HIP kernels avoids support issues.
- This setup can simulate hybrid CPU/GPU architectures like MI300A for development purposes.

**Discussion Highlights:** The discussion highlights include users sharing their experiences with similar setups, such as using older Ryzen processors for background LLM tasks and leveraging GTT for inference on Strix Halo. There is also mention of using Nvidia GPUs with llama.cpp for kv cache to avoid speed drops.

---

## 7. [IQuestCoder - new 40B dense coding model](https://reddit.com/r/LocalLLaMA/comments/1q1986x/iquestcoder_new_40b_dense_coding_model/)

**Author:** u/ilintar | **Upvotes:** 185 | **Comments:** 37 | **Date:** 2026-01-01

**Summary:** The post introduces IQuestCoder, a new 40B dense coding model with claims of SOTA performance. The author has adapted it to GGUF format, making it compatible with Llama.cpp. The discussion includes feedback on its performance and architecture.

**Key Points:**
- IQuestCoder is a new 40B dense coding model claimed to be SOTA.
- The model is adapted to GGUF format and works with Llama.cpp.
- The Loop version requires adaptation due to its new architecture.
- Performance feedback includes success in zero-shot tasks and understanding of embedded Rust concepts.
- Comparisons with other models like GPT 120, Devstral, and GLM 4.7 are mentioned.

**Discussion Highlights:** The discussion highlights positive feedback on the model's performance, including successful zero-shot tasks and good understanding of embedded Rust concepts. There are also mentions of comparisons with other models and the need for adaptation for the Loop version due to its new architecture.

---

## 8. [Upstage Solar-Open-100B Public Validation](https://reddit.com/r/LocalLLaMA/comments/1q0zst6/upstage_solaropen100b_public_validation/)

**Author:** u/PerPartes | **Upvotes:** 228 | **Comments:** 69 | **Date:** 2026-01-01

**Summary:** Upstage hosted an event at KAIST, Seoul, to counter claims that their Solar-Open-100B model is merely a fine-tuned version of GLM-Air-4.5. The CEO presented their case, and the event was live-streamed on YouTube.

**Key Points:**
- Upstage's official response to plagiarism claims about Solar-Open-100B
- Event held at KAIST, Seoul, with CEO Sung Kim presenting
- Live-stream available on YouTube with online translation
- Community discussions include technical tests and skepticism about the claims
- Mixed reactions: some users demand online release, others support the event

**Discussion Highlights:** The community is divided, with some users questioning the need for a physical event and others conducting technical tests to verify the claims. There is also support for Upstage's transparency efforts.

---

## 9. [DeepSeek new paper: mHC: Manifold-Constrained Hyper-Connections](https://reddit.com/r/LocalLLaMA/comments/1q0zk1u/deepseek_new_paper_mhc_manifoldconstrained/)

**Author:** u/External_Mood4719 | **Upvotes:** 165 | **Comments:** 37 | **Date:** 2026-01-01

**Summary:** DeepSeek's new paper introduces mHC (Manifold-Constrained Hyper-Connections), a novel approach to improving deep networks by addressing gradient issues through advanced residual connections. The Reddit discussion highlights its potential impact on LLMs and CNNs, with users expressing optimism about its implications for 2026.

**Key Points:**
- DeepSeek's paper proposes mHC to solve gradient explosion issues in deep networks.
- The method is applicable to both LLMs and CNNs like ResNet.
- Users compare it to traditional residual connections, noting its potential for better scaling.
- The community is optimistic about its impact on AI advancements in 2026.
- Additional papers on residual connections are referenced for further reading.

**Discussion Highlights:** The discussion emphasizes the importance of mHC in stabilizing deep networks, with users drawing parallels to knitting (simplifying complex processes). There is a consensus on its potential to significantly improve model performance, especially in scaling trends.

---

## 10. [Software FP8 for GPUs without hardware support - 3x speedup on memory-bound operations](https://reddit.com/r/LocalLLaMA/comments/1q0x8ci/software_fp8_for_gpus_without_hardware_support_3x/)

**Author:** u/Venom1806 | **Upvotes:** 276 | **Comments:** 57 | **Date:** 2026-01-01

**Summary:** A user developed a software-based FP8 implementation for GPUs without native support, achieving a 3x speedup on memory-bound operations. The solution is compatible with older GPUs and has garnered positive community feedback.

**Key Points:**
- Software-based FP8 implementation for GPUs without native support
- 3x speedup on memory-bound operations like GEMV and FlashAttention
- Compatible with RTX 30/20 series and older GPUs
- Positive community feedback and interest in integration with tools like ComfyUI
- Clarification that some users mistakenly believed FP8 was natively supported on RTX 30 series

**Discussion Highlights:** The community praised the innovation as a valuable workaround for extending the life of mid-tier GPUs. Some users expressed surprise about the lack of native FP8 support on RTX 30 series GPUs, while others inquired about integration possibilities with existing tools.

---

## 11. [IQuestLab/IQuest-Coder-V1 — 40B parameter coding LLM — Achieves leading results on SWE-Bench Verified (81.4%), BigCodeBench (49.9%), LiveCodeBench v6 (81.1%)](https://reddit.com/r/LocalLLaMA/comments/1q0vom4/iquestlabiquestcoderv1_40b_parameter_coding_llm/)

**Author:** u/TellMeAboutGoodManga | **Upvotes:** 171 | **Comments:** 45 | **Date:** 2025-12-31

**Summary:** IQuestLab's IQuest-Coder-V1 is a 40B parameter coding LLM that achieves leading results on multiple benchmarks, including SWE-Bench Verified (81.4%), BigCodeBench (49.9%), and LiveCodeBench v6 (81.1%). The model is backed by a Chinese quant trading company, similar to DeepSeek, and has sparked discussions about its performance and architecture.

**Key Points:**
- 40B parameter dense model with leading benchmark results
- Backed by a Chinese quant trading company
- Community skepticism about benchmark validity
- Discussion about model architecture (dense vs. MoE)
- Comparison with other models in the industry

**Discussion Highlights:** The community discussion includes skepticism about the benchmark results, observations about the model's dense architecture, and comparisons with other models. There is also interest in the background of the company and its similarities to other quant trading firms entering the LLM space.

---

## 12. [Happy New Year: Llama3.3-8B-Instruct-Thinking-Claude-4.5-Opus-High-Reasoning - Fine Tune. (based on recent find of L3.3 8b in the wild)](https://reddit.com/r/LocalLLaMA/comments/1q0uuqt/happy_new_year/)

**Author:** u/Dangerous_Fix_5526 | **Upvotes:** 274 | **Comments:** 80 | **Date:** 2025-12-31

**Summary:** The post announces a fine-tuned version of Llama3.3-8B-Instruct, enhanced with reasoning capabilities using the Claude 4.5 Opus High Reasoning Dataset. The author credits collaborators and provides links to the model and datasets. Key points include the fine-tuning process, availability of GGUF quantizations, release of a Heretic version, and discussion about the dataset size. The discussion highlights interest in the model's capabilities and questions about the effectiveness of the fine-tuning dataset size.

---

## 13. [Moonshot AI Completes $500 Million Series C Financing](https://reddit.com/r/LocalLLaMA/comments/1q0i4g3/moonshot_ai_completes_500_million_series_c/)

**Author:** u/InternationalAsk1490 | **Upvotes:** 109 | **Comments:** 21 | **Date:** 2025-12-31

**Summary:** Moonshot AI has completed a $500 million Series C financing, with plans to expand GPU capacity and develop the K3 model. The company aims to achieve significant revenue growth and enhance its model's capabilities.

**Key Points:**
- Moonshot AI completed a $500 million Series C financing.
- The company's global paid user base is growing at a monthly rate of 170%.
- Funds will be used to expand GPU capacity and accelerate the development of the K3 model.
- Key priorities for 2026 include improving the K3 model's performance and achieving significant revenue growth.
- The discussion highlights the benefits of open-weight companies making money and the unique capabilities of the Kimi models.

**Discussion Highlights:** The discussion highlights the benefits of open-weight companies making money and the unique capabilities of the Kimi models. Users expressed confusion about the benefits of using Kimi K2 via their membership program and praised the distinctive features of the Kimi models.

---

## 14. [Solar-Open-100B is out](https://reddit.com/r/LocalLLaMA/comments/1q0bgvl/solaropen100b_is_out/)

**Author:** u/cgs019283 | **Upvotes:** 158 | **Comments:** 62 | **Date:** 2025-12-31

**Summary:** Upstage has released the Solar-Open-100B model, a 102B parameter model with a more open commercial license. The community is excited about the rapid advancements in model quality and the potential for local inference.

**Key Points:**
- Solar-Open-100B is a 102B parameter model with a commercial-friendly license.
- The model has been trained on 19.7 trillion tokens.
- Community is eagerly awaiting benchmarks and performance numbers.
- There is interest in 4-bit quantized versions for local inference.
- The rapid pace of model releases is noted as impressive.

**Discussion Highlights:** The community is generally positive about the release, highlighting the open license and the model's size. There is anticipation for performance benchmarks and quantized versions for local use. Some users are speculating about the model's potential similarities to other advanced models like GLM4.6-Air.

---

## 15. [Qwen-Image-2512](https://reddit.com/r/LocalLLaMA/comments/1q094a3/qwenimage2512/)

**Author:** u/Nunki08 | **Upvotes:** 683 | **Comments:** 116 | **Date:** 2025-12-31

**Summary:** The post announces the release of Qwen-Image-2512, a new model with various resources and demos available. It includes links to documentation, GGUF files, and interactive demos on platforms like Hugging Face and ModelScope. The community response is positive, with users sharing their experiences and creative outputs.

**Key Points:**
- Qwen-Image-2512 is a new model with extensive documentation and demo links.
- The model can be tried in Qwen Chat and is available on multiple platforms like Hugging Face and ModelScope.
- Community feedback highlights successful usage on low-end hardware and creative applications.
- Users appreciate the model as a 'new year's gift' and a 'Christmas present'.
- One user generated a creative image of a cat-octopus hybrid playing piano in a post-apocalyptic setting.

**Discussion Highlights:** The community is enthusiastic about the model's release, with users testing it on various hardware setups and sharing creative outputs. The post was featured on Discord, indicating its popularity and significance.

---

## 16. [Update on the Llama 3.3 8B situation](https://reddit.com/r/LocalLLaMA/comments/1q06ddc/update_on_the_llama_33_8b_situation/)

**Author:** u/FizzarolliAI | **Upvotes:** 256 | **Comments:** 22 | **Date:** 2025-12-31

**Summary:** The post discusses updates on the Llama 3.3 8B model, including benchmarks for different configurations and the author's confusion over Meta's release strategy. The author provides links to both the original and context-extended versions of the model.

**Key Points:**
- The author released Llama 3.3 8B weights on Huggingface and provides updates on benchmarks.
- Benchmark results show the 128k context version performs better than the original 8k version.
- The author expresses confusion over Meta's decision to release the model with an 8k context configuration.
- The post includes links to both the original and context-extended versions of the model.
- The author mentions issues with Tau-Bench results and plans to debug them later.

**Discussion Highlights:** The discussion includes positive feedback on the author's work, humor, and a consensus that the model is decent but could have been better if officially released by Meta.

---

## 17. [[In the Wild] Reverse-engineered a Snapchat Sextortion Bot: It’s running a raw Llama-7B instance with a 2048 token window.](https://reddit.com/r/LocalLLaMA/comments/1pzwlie/in_the_wild_reverseengineered_a_snapchat/)

**Author:** u/simar-dmg | **Upvotes:** 710 | **Comments:** 104 | **Date:** 2025-12-30

**Summary:** A user reverse-engineered a Snapchat sextortion bot and discovered it was running a raw Llama-7B instance with a 2048 token window. The bot was vulnerable to a persona-adoption jailbreak, revealing its configuration and malicious payload.

**Key Points:**
- The bot used a Llama-7B model with a 2048 token context window and high temperature setting.
- A persona-adoption jailbreak (Grandma Protocol) forced the bot to reveal its environment variables.
- The bot was running on minimal hardware to maximize profit margins.
- The bot eventually revealed a malicious link it was programmed to hide.
- Scammers are increasingly using open-source models like Llama-7B to avoid API costs and censorship filters.

**Discussion Highlights:** The discussion highlighted skepticism about the accuracy of the bot's revealed information, with some users suggesting it could be entirely hallucinated. Others questioned the commonality of system prompts including environment variables.

---

## 18. [LLM server gear: a cautionary tale of a $1k EPYC motherboard sale gone wrong on eBay](https://reddit.com/r/LocalLLaMA/comments/1pzt1q8/llm_server_gear_a_cautionary_tale_of_a_1k_epyc/)

**Author:** u/__JockY__ | **Upvotes:** 193 | **Comments:** 81 | **Date:** 2025-12-30

**Summary:** The post discusses a seller's experience with eBay's dispute resolution process after selling a high-end EPYC motherboard. Despite providing detailed evidence and support, the seller faced challenges due to eBay's buyer-friendly policies, highlighting the risks of selling high-end gear on the platform.

**Key Points:**
- eBay's dispute resolution process heavily favors buyers, even with clear evidence from sellers.
- The seller provided high-quality photos and detailed support but still faced a dispute.
- The post highlights the risks and challenges of selling high-end server gear on eBay.
- Other users shared similar experiences, indicating a common issue with eBay's seller policies.
- The process of resolving disputes can be intentionally cumbersome and frustrating for sellers.

**Discussion Highlights:** The discussion consensus is that selling on eBay can be risky for sellers, especially for high-end items, due to the platform's buyer-friendly policies and cumbersome dispute resolution process.

---

## 19. [15M param model solving 24% of ARC-AGI-2 (Hard Eval). Runs on consumer hardware.](https://reddit.com/r/LocalLLaMA/comments/1pzsqii/15m_param_model_solving_24_of_arcagi2_hard_eval/)

**Author:** u/Doug_Bitterbot | **Upvotes:** 115 | **Comments:** 31 | **Date:** 2025-12-30

**Summary:** Bitterbot AI introduced TOPAS-DSPL, a 24M parameter model achieving 24% accuracy on ARC-AGI-2, using a dual-stream architecture to prevent compositional drift. The model is open-sourced and runs efficiently on consumer hardware like an RTX 4090.

**Key Points:**
- TOPAS-DSPL achieves 24% accuracy on ARC-AGI-2, outperforming previous models in its size class.
- The model uses a bicameral architecture with Logic and Canvas streams to prevent compositional drift.
- It employs Test-Time Training (TTT) to fine-tune on specific puzzle examples before generating solutions.
- The model is open-sourced, with code and detailed documentation available.
- Discussion highlights include comparisons with MuZero, concerns about training on the test set, and questions about scalability.

**Discussion Highlights:** The discussion includes skepticism about the model's training methodology, comparisons with other approaches like MuZero, and interest in its potential scalability to larger parameter sizes.

---

## 20. [Any guesses?](https://reddit.com/r/LocalLLaMA/comments/1pzhcqu/any_guesses/)

**Author:** u/Difficult-Cap-7527 | **Upvotes:** 173 | **Comments:** 36 | **Date:** 2025-12-30

**Summary:** The Reddit post discusses potential advancements in AI models, specifically focusing on Qwen models and their performance compared to other models like GPT 5.2. The comments highlight various iterations and improvements in Qwen models.

**Key Points:**
- Qwen 6 is mentioned as potentially outperforming GPT 5.2 on a significant benchmark.
- Qwen3vl-next-80b-a3b is highlighted as a significant improvement with no more comparison issues.
- Qwen image 2512 is referenced, suggesting advancements in image processing capabilities.
- Discussion includes speculation about future iterations like Qwen3.5-235B-A10B.
- The community shows enthusiasm and anticipation for these advancements.

**Discussion Highlights:** The discussion is centered around the potential capabilities and improvements of Qwen models, with a focus on their performance benchmarks and future iterations. The community appears optimistic and engaged in speculating about the advancements.

---

## 21. [Running GLM-4.7 (355B MoE) in Q8 at ~5 Tokens/s on 2015 CPU-Only Hardware – Full Optimization Guide](https://reddit.com/r/LocalLLaMA/comments/1pzggbf/running_glm47_355b_moe_in_q8_at_5_tokenss_on_2015/)

**Author:** u/at0mi | **Upvotes:** 143 | **Comments:** 99 | **Date:** 2025-12-30

**Summary:** The post describes running the GLM-4.7 (355B MoE) model on a 2015 CPU-only setup, achieving ~5 tokens/s with Q8 quantization. The author shares optimization techniques and benchmarks, highlighting the feasibility of running large models on older hardware.

**Key Points:**
- GLM-4.7 (355B MoE) runs at ~5 tokens/s on a 2015 Lenovo System x3950 X6 with eight Xeon E7-8880 v3 CPUs.
- Optimizations include BIOS settings, NUMA node distribution, and Linux kernel tweaks.
- The setup consumes ~1300W under full load, making it power-intensive but viable for local runs.
- Discussion highlights cost (~£2,500 for similar hardware) and energy efficiency (60 kWh per 1M tokens).
- Community feedback includes concerns about power draw and performance limitations without a GPU.

**Discussion Highlights:** The community discussed the cost and energy efficiency of the setup, with some users calculating the energy cost per token and others noting the limitations of CPU-only setups for certain tasks.

---

## 22. [Tencent HY-Motion 1.0 - a billion-parameter text-to-motion model](https://reddit.com/r/LocalLLaMA/comments/1pzcrtb/tencent_hymotion_10_a_billionparameter/)

**Author:** u/ResearchCrafty1804 | **Upvotes:** 315 | **Comments:** 36 | **Date:** 2025-12-30

**Summary:** Tencent has open-sourced HY-Motion 1.0, a billion-parameter text-to-motion model that generates high-fidelity 3D animations from natural language. It features advanced training strategies and covers 200+ motion categories, making it a powerful tool for developers and creators.

**Key Points:**
- Billion-parameter Diffusion Transformer (DiT) architecture with flow matching for high-quality motion generation.
- Full-stage training strategy (Pre-training → SFT → RL) to optimize motion quality and semantic accuracy.
- Supports 200+ motion categories across 6 major classes, offering comprehensive coverage.
- Positive user feedback highlights its effectiveness and potential for game development.
- Questions raised about compatibility with non-humanoid models and potential applications.

**Discussion Highlights:** Users praised the model's performance and ease of integration, with one noting it as a 'massive speed boost' for game development. Some inquiries focused on its applicability to non-humanoid models and potential use cases in other communities.

---

## 23. [Llama-3.3-8B-Instruct](https://reddit.com/r/LocalLLaMA/comments/1pz7mxr/llama338binstruct/)

**Author:** u/ttkciar | **Upvotes:** 154 | **Comments:** 25 | **Date:** 2025-12-29

**Summary:** The Reddit post discusses the release of the Llama-3.3-8B-Instruct model, with the author expressing excitement and skepticism about its authenticity. The community is engaged in verifying the model's legitimacy and sharing related resources.

**Key Points:**
- Llama-3.3-8B-Instruct model has been released with links to Hugging Face repositories.
- The community is verifying if the model is genuinely a newer version or a repackaged older version.
- Multiple GGUF versions and updated configurations are being shared.
- There is excitement and skepticism about the model's authenticity and backstory.
- Some users express a desire for updated larger models (e.g., 70B or new 30B).

**Discussion Highlights:** The discussion highlights a mix of excitement and skepticism regarding the Llama-3.3-8B-Instruct model. Key points include community efforts to verify the model's authenticity, sharing of related resources and configurations, and expressions of interest in larger model updates.

---

## 24. [Llama-3.3-8B-Instruct](https://reddit.com/r/LocalLLaMA/comments/1pz7bmv/llama338binstruct/)

**Author:** u/jacek2023 | **Upvotes:** 463 | **Comments:** 78 | **Date:** 2025-12-29

**Summary:** The post announces the release of Llama-3.3-8B-Instruct, a previously API-exclusive model from Meta, now available in GGUF format after the author discovered a method to download it via finetuning. The community is excited and conducting benchmarks to verify its authenticity.

**Key Points:**
- Llama-3.3-8B-Instruct was previously only available via Meta's API.
- The author found a way to download the model through finetuning and released it in GGUF format.
- The community is conducting benchmarks to verify the model's authenticity and performance.
- There are discussions about the model's configuration, such as the 8K max position embeddings.

**Discussion Highlights:** The community is excited about the release, with ongoing benchmarks to verify the model's authenticity. Some users are running private evaluations to compare it with other Llama models, and there are discussions about the model's configuration details.

---

## 25. [Z AI is going for an IPO on Jan 8 and set to raise $560 million. Z.ai is set to be the first AI-native LLM company to list on the global market.](https://reddit.com/r/LocalLLaMA/comments/1pz68fz/z_ai_is_going_for_an_ipo_on_jan_8_and_set_to/)

**Author:** u/Difficult-Cap-7527 | **Upvotes:** 337 | **Comments:** 120 | **Date:** 2025-12-29

**Summary:** Z AI is set to go public on January 8, aiming to raise $560 million, marking it as the first AI-native LLM company to list globally. The announcement has sparked discussions about the future of open-source AI models and the company's potential shift in focus.

**Key Points:**
- Z AI's IPO is scheduled for January 8 with a target of $560 million.
- Concerns about the future of open-source AI models post-IPO.
- Debate on whether Z AI will continue releasing open weight models.
- Mixed reactions from the community, with some expressing concerns about commercialization.
- Acknowledgment that companies need to monetize eventually.

**Discussion Highlights:** The discussion highlights a divide in the community regarding the implications of Z AI's IPO. While some users express concerns about the potential end of open-source contributions, others argue that monetization is a natural progression for companies. There is also speculation about the company's future model releases and subscription services.

---

## 26. [Naver (South Korean internet giant), has just launched HyperCLOVA X SEED Think, a 32B open weights reasoning model and HyperCLOVA X SEED 8B Omni, a unified multimodal model that brings text, vision, and speech together](https://reddit.com/r/LocalLLaMA/comments/1pyjjbw/naver_south_korean_internet_giant_has_just/)

**Author:** u/Nunki08 | **Upvotes:** 161 | **Comments:** 31 | **Date:** 2025-12-29

**Summary:** Naver has launched two new AI models: HyperCLOVA X SEED Think 32B (a reasoning model) and HyperCLOVA X SEED 8B Omni (a multimodal model combining text, vision, and speech). The announcement has generated interest in the AI community, with users discussing its capabilities and compatibility.

**Key Points:**
- HyperCLOVA X SEED Think 32B is a 32B open weights reasoning model.
- HyperCLOVA X SEED 8B Omni is a unified multimodal model supporting text, vision, and speech.
- Users are curious about compatibility with existing frameworks like llama.cpp and vLLM.
- The community shows enthusiasm for multimodal capabilities.
- The models are part of a broader release of AI advancements from South Korea.

**Discussion Highlights:** The discussion highlights enthusiasm for the multimodal capabilities of the 8B Omni model, with users expressing interest in audio-to-audio features and compatibility with existing AI frameworks. Some users also noted the broader trend of AI advancements emerging from South Korea.

---

## 27. [Tencent just released WeDLM 8B Instruct on Hugging Face](https://reddit.com/r/LocalLLaMA/comments/1pyg4yt/tencent_just_released_wedlm_8b_instruct_on/)

**Author:** u/Difficult-Cap-7527 | **Upvotes:** 420 | **Comments:** 62 | **Date:** 2025-12-29

**Summary:** Tencent released WeDLM 8B Instruct on Hugging Face, a diffusion language model that runs 3-6× faster than vLLM-optimized Qwen3-8B on math reasoning tasks. The release has generated significant interest and discussion in the community.

**Key Points:**
- WeDLM 8B Instruct is a diffusion language model released by Tencent on Hugging Face.
- It outperforms vLLM-optimized Qwen3-8B by 3-6× on math reasoning tasks.
- The model is released under the Apache 2.0 license.
- There is also a 7B version available.
- The community shows strong interest in smaller models (7-8B) and their potential.

**Discussion Highlights:** The community is excited about the performance claims and the potential of smaller models. There is consensus on the promising nature of 7-8B models and interest in further developments in this space.

---

## 28. [Meta released RPG, a research plan generation dataset on Hugging Face](https://reddit.com/r/LocalLLaMA/comments/1pyao6g/meta_released_rpg_a_research_plan_generation/)

**Author:** u/Difficult-Cap-7527 | **Upvotes:** 260 | **Comments:** 21 | **Date:** 2025-12-28

**Summary:** Meta released the RPG dataset on Hugging Face, featuring 22k tasks across ML, Arxiv, and PubMed, with evaluation rubrics and Llama-4 reference solutions for training AI co-scientists. The community discussion highlights Meta's strong research and open-source contributions, with some concerns about the future of open frontier models.

**Key Points:**
- RPG dataset includes 22k tasks with evaluation rubrics and Llama-4 reference solutions
- Dataset spans ML, Arxiv, and PubMed domains
- Community praises Meta's research and open-source contributions
- Discussion on the future of open frontier models
- Research plan generation seen as important for agentic systems

**Discussion Highlights:** The community appreciates Meta's contributions, with a notable comment highlighting Meta's dominance in research and open-source. There is also discussion on the importance of research plan generation for AI systems and concerns about the future of open models.

---

## 29. [Senator in Tennessee introduces bill to felonize making AI "act as a companion" or "mirror human interactions"](https://reddit.com/r/LocalLLaMA/comments/1pxss0m/senator_in_tennessee_introduces_bill_to_felonize/)

**Author:** u/CanineAssBandit | **Upvotes:** 275 | **Comments:** 212 | **Date:** 2025-12-28

**Summary:** A Tennessee senator has introduced a bill (SB1493) that would make it a felony to train AI to provide emotional support, act as a companion, or simulate human interactions. The bill has sparked significant discussion and opposition online.

**Key Points:**
- The bill aims to criminalize training AI to provide emotional support or act as a companion.
- It also targets AI that simulates human appearance, voice, or mannerisms.
- The bill defines 'training' broadly, including the development of large language models.
- Online reactions range from opposition to skepticism about the bill's chances of passing.
- Some commenters suggest the bill stems from unique personal circumstances of the sponsoring senator.

**Discussion Highlights:** The discussion highlights strong opposition to the bill, with many users expressing skepticism about its feasibility and potential impact on freedom of speech. Some commenters joke about the implications, while others suggest alternative legislative priorities.

---

