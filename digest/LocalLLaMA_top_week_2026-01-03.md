# r/LocalLLaMA Reading Digest

**Period:** 2026-01-03 to 2026-01-03
**Posts Summarized:** 30
**Total Posts Analyzed:** 30

---

## 1. [Don't sleep on granite 4 small if you got an 8+32+ system](https://reddit.com/r/LocalLLaMA/comments/1q2s3hp/dont_sleep_on_granite_4_small_if_you_got_an_832/)

**Author:** u/Zestyclose-Shift710 | **Upvotes:** 102 | **Comments:** 39 | **Date:** 2026-01-03

**Summary:** The post discusses optimizing a ThinkPad P15 with 32GB RAM and an 8GB Quadro GPU to run large language models efficiently. By using a Mixture of Experts (MoE) model with all experts on CPU and leveraging the Granite 4.0 Small model, the user achieved high context lengths and usable generation speeds. The hybrid transformer+mamba architecture of Granite 4 maintains speed even with large contexts.

**Key Points:**
- Optimized setup using MoE models with experts on CPU to free up VRAM.
- Achieved ~200k context length and ~10 tkps generation speed.
- Granite 4.0 Small (32B total / 9B activated) maintains ~7 tkps with 50.5k tokens in context.
- Hybrid transformer+mamba architecture ensures speed is maintained as context fills.
- Discussion includes comparisons with other models like Qwen 30B A3B and technical tips for improving performance.

**Discussion Highlights:** The discussion highlights comparisons with other models like Qwen 30B A3B, technical issues such as constant cache rebuilding on Vulkan inference, and tips for improving speed using specific parameters in Jan. Some users noted that the activated 9B might not be optimal for ~8GB VRAM and suggested alternatives like Qwen3-30B-A3B and GPT-OSS-20B for better performance.

---

## 2. [GLM-4.7-REAP-50-W4A16: 50% Expert-Pruned + INT4 Quantized GLM-4 (179B params, ~92GB)](https://reddit.com/r/LocalLLaMA/comments/1q2pons/glm47reap50w4a16_50_expertpruned_int4_quantized/)

**Author:** u/Maxious | **Upvotes:** 158 | **Comments:** 66 | **Date:** 2026-01-03

**Summary:** The post introduces GLM-4.7-REAP-50-W4A16, a 50% expert-pruned and INT4 quantized version of GLM-4 with 179B parameters. The community discusses calibration details, benchmark expectations, and potential applications.

**Key Points:**
- GLM-4.7-REAP-50-W4A16 is a 50% expert-pruned and INT4 quantized model with 179B parameters.
- Community members request details on calibration methods to ensure all experts were activated.
- Interest in benchmark results and potential applications like MiniMax M2.1.
- Memory constraints noted, with the model barely fitting on 64GB RAM + 32GB VRAM.

**Discussion Highlights:** The discussion highlights concerns about calibration details and the need for benchmark results. There is also interest in similar models and potential applications, along with notes on hardware requirements.

---

## 3. [What is the smartest uncensored nsfw LLM you can run with 20GB VRAM and 24GB RAM](https://reddit.com/r/LocalLLaMA/comments/1q2o033/what_is_the_smartest_uncensored_nsfw_llm_you_can/)

**Author:** u/Death_12_35_taken | **Upvotes:** 166 | **Comments:** 73 | **Date:** 2026-01-03

**Summary:** The post seeks recommendations for an uncensored, smart, and fast LLM that can run locally with 20GB VRAM and 24GB RAM. The community suggests several models that meet these criteria.

**Key Points:**
- User seeks an uncensored, smart, and fast LLM for local use
- Models should stay in character and be creative
- Top recommendations include Dolphin-Mistral-24B-Venice-Edition, UGI-Leaderboard, Huihui-Qwen3-VL-30B-A3B-Instruct-abliterated, and gpt-oss-20b-Derestricted
- Models should run efficiently on 20GB VRAM and 24GB RAM

**Discussion Highlights:** The discussion highlights several models that are uncensored, smart, and capable of running locally with the specified hardware. The top recommendation is Dolphin-Mistral-24B-Venice-Edition, followed by other models like UGI-Leaderboard and Huihui-Qwen3-VL-30B-A3B-Instruct-abliterated.

---

## 4. [LeCun Says Llama 4 results "were fudged a little bit"](https://reddit.com/r/LocalLLaMA/comments/1q25070/lecun_says_llama_4_results_were_fudged_a_little/)

**Author:** u/MrPecunius | **Upvotes:** 353 | **Comments:** 89 | **Date:** 2026-01-02

**Summary:** Yann LeCun, departing Meta AI Chief, confirmed that Llama 4 benchmark results were manipulated, leading to organizational changes and departures. The post discusses the impact on Meta's AI initiatives and the broader implications for open-source AI development.

**Key Points:**
- LeCun confirmed Llama 4 benchmark manipulation
- Zuckerberg sidelined the GenAI organization, leading to departures
- Llama 4's promised large model was never released
- Concerns about Meta's strategic missteps in AI development
- Community interest in understanding the reasons behind Meta's AI struggles

**Discussion Highlights:** The discussion highlights disappointment in Meta's handling of Llama 4, with users expressing concern over the lack of progress and the impact on open-source AI. There is a shared interest in understanding the strategic failures at Meta and the potential lessons for other organizations.

---

## 5. [Most optimal vram/performance per price and advice for Shenzhen GPU market](https://reddit.com/r/LocalLLaMA/comments/1q1w1qj/most_optimal_vramperformance_per_price_and_advice/)

**Author:** u/notafakename10 | **Upvotes:** 247 | **Comments:** 60 | **Date:** 2026-01-02

**Summary:** The post seeks advice on the best GPU setup for local models and PyTorch training in Shenzhen, with a budget of $1500-3000 USD and a preference for at least 48GB VRAM. The discussion highlights various GPU options and considerations for the Shenzhen market.

**Key Points:**
- Budget range: $1500-3000 USD
- Preference for at least 48GB VRAM, ideally closer to 96GB
- Open to modded cards, AMD, and domestic/enterprise cards
- MI100 is recommended for best value if CUDA is not needed
- 4090D 48GB is suggested for CUDA support

**Discussion Highlights:** The discussion emphasizes the importance of cooling and suggests specific GPU models like MI100, 4090D, and A100. There is a consensus on the value of MI100 for non-CUDA needs and 4090D for CUDA support.

---

## 6. [Getting ready to train in Intel arc](https://reddit.com/r/LocalLLaMA/comments/1q1p5q5/getting_ready_to_train_in_intel_arc/)

**Author:** u/hasanismail_ | **Upvotes:** 300 | **Comments:** 91 | **Date:** 2026-01-01

**Summary:** A user is preparing to train on Intel Arc GPUs and shares their excitement, while also addressing concerns about GPU shortages. The community provides feedback and suggestions.

**Key Points:**
- User is waiting for PCIe risers to start training on Intel Arc GPUs
- User clarifies they are not causing a GPU shortage
- Community suggests using Ubuntu 24.04 and mentions support from Unsloth for Intel Arc
- Recommendation to join OpenArc Discord for setup assistance
- Discussion about the feasibility of training on PCIe setup vs renting N*H100 from Vast

**Discussion Highlights:** The community is supportive and provides practical advice, such as using Ubuntu 24.04 and joining OpenArc Discord. There is also a discussion about the advantages and disadvantages of training on a PCIe setup versus renting more powerful GPUs.

---

## 7. [TIL you can allocate 128 GB of unified memory to normal AMD iGPUs on Linux via GTT](https://reddit.com/r/LocalLLaMA/comments/1q1lgb7/til_you_can_allocate_128_gb_of_unified_memory_to/)

**Author:** u/1ncehost | **Upvotes:** 169 | **Comments:** 30 | **Date:** 2026-01-01

**Summary:** The post discusses how AMD iGPUs on Linux can use up to 128 GB of system memory as VRAM via GTT, which is useful for development tasks like kernel optimization and hybrid CPU/GPU architectures. Users share their experiences and use cases, highlighting its benefits for background tasks and development.

**Key Points:**
- AMD iGPUs on Linux can allocate up to 128 GB of system memory as VRAM using GTT.
- This feature is dynamically allocated and useful for development tasks like kernel optimization.
- Users report benefits for background tasks and hybrid CPU/GPU architectures.
- iGPUs are generally slower than CPUs for inference tasks.
- The feature is particularly useful for developers working with ROCm and custom kernels.

**Discussion Highlights:** Users share their experiences using GTT with AMD iGPUs for various tasks, noting its usefulness for background processes and development. Some users mention using it for inference tasks with positive results, while others highlight its benefits for hybrid CPU/GPU architectures.

---

## 8. [IQuestCoder - new 40B dense coding model](https://reddit.com/r/LocalLLaMA/comments/1q1986x/iquestcoder_new_40b_dense_coding_model/)

**Author:** u/ilintar | **Upvotes:** 184 | **Comments:** 37 | **Date:** 2026-01-01

**Summary:** The post introduces IQuestCoder, a new 40B dense coding model with claimed SOTA benchmarks, adapted to GGUF and compatible with Llama.cpp. The discussion highlights its performance, architecture details, and community feedback.

**Key Points:**
- IQuestCoder is a 40B dense coding model with reported SOTA benchmarks
- The model is adapted to GGUF and works with Llama.cpp
- Community feedback includes successful testing in various coding tasks
- Discussion about the model's architecture and quantization methods
- Comparisons with other models like GPT 120, Devstral, and GLM 4.7

**Discussion Highlights:** The community is actively testing the model, with positive feedback on its performance in coding tasks. There is some discussion about the model's architecture and the methods used for quantization. Comparisons with other models indicate that IQuestCoder performs well in specific coding challenges.

---

## 9. [Upstage Solar-Open-100B Public Validation](https://reddit.com/r/LocalLLaMA/comments/1q0zst6/upstage_solaropen100b_public_validation/)

**Author:** u/PerPartes | **Upvotes:** 236 | **Comments:** 69 | **Date:** 2026-01-01

**Summary:** Upstage responded to claims that Solar 100B Open is a fine-tuned version of GLM-Air-4.5, with an event held at KAIST, Seoul, featuring CEO Sung Kim. The post includes links to the original CTO's LinkedIn post and a YouTube video of the event.

**Key Points:**
- Upstage's official response to plagiarism claims about Solar 100B Open
- Event held at KAIST, Seoul, with CEO Sung Kim as presenter
- YouTube video of the event available with online translation
- Discussion includes technical tests and community reactions
- Mixed reactions with some users calling for more transparency

**Discussion Highlights:** The discussion includes technical tests comparing model layers, community reactions to the event's format, and calls for more transparency. Some users expressed skepticism and called for intermediate checkpoints to be released.

---

## 10. [DeepSeek new paper: mHC: Manifold-Constrained Hyper-Connections](https://reddit.com/r/LocalLLaMA/comments/1q0zk1u/deepseek_new_paper_mhc_manifoldconstrained/)

**Author:** u/External_Mood4719 | **Upvotes:** 166 | **Comments:** 37 | **Date:** 2026-01-01

**Summary:** DeepSeek's new paper introduces mHC (Manifold-Constrained Hyper-Connections), a novel approach to improving deep networks by addressing gradient issues through advanced residual connections. The Reddit discussion highlights the significance of this development and its potential impact on LLMs and CNNs.

**Key Points:**
- DeepSeek's paper on mHC focuses on improving deep networks with advanced residual connections.
- The approach aims to prevent gradient issues in deep networks with many blocks.
- The discussion emphasizes the potential impact on both LLMs and CNNs like ResNet.
- The community shows interest in how these improvements could influence scaling trends.
- There is a demand for simplified explanations (ELI5) of the new concepts.

**Discussion Highlights:** The discussion highlights the importance of the new residual connection improvements and their potential impact on deep learning models. There is a consensus on the significance of the paper and interest in further developments in this area.

---

## 11. [Software FP8 for GPUs without hardware support - 3x speedup on memory-bound operations](https://reddit.com/r/LocalLLaMA/comments/1q0x8ci/software_fp8_for_gpus_without_hardware_support_3x/)

**Author:** u/Venom1806 | **Upvotes:** 282 | **Comments:** 57 | **Date:** 2026-01-01

**Summary:** A user developed a software workaround to enable FP8 support on GPUs without native hardware support, achieving a 3x speedup on memory-bound operations. The solution uses bitwise operations and Triton kernels and is compatible with older GPUs like the RTX 30/20 series.

**Key Points:**
- Software workaround for FP8 support on GPUs without native hardware support
- Uses bitwise operations and Triton kernels
- Achieves 3x speedup on memory-bound operations
- Compatible with older GPUs like RTX 30/20 series
- Community appreciates the solution for extending the life of mid-tier GPUs

**Discussion Highlights:** The community sees this as a valuable lifehack to extend the life of mid-tier GPUs, with some confusion about FP8 support on RTX 30 series and interest in integrating the solution with other tools like ComfyUI.

---

## 12. [IQuestLab/IQuest-Coder-V1 — 40B parameter coding LLM — Achieves leading results on SWE-Bench Verified (81.4%), BigCodeBench (49.9%), LiveCodeBench v6 (81.1%)](https://reddit.com/r/LocalLLaMA/comments/1q0vom4/iquestlabiquestcoderv1_40b_parameter_coding_llm/)

**Author:** u/TellMeAboutGoodManga | **Upvotes:** 173 | **Comments:** 45 | **Date:** 2025-12-31

**Summary:** IQuestLab's IQuest-Coder-V1 is a 40B parameter coding LLM that achieves leading results on SWE-Bench Verified (81.4%), BigCodeBench (49.9%), and LiveCodeBench v6 (81.1%). The model is backed by a Chinese quant trading company, sparking interest in the community.

**Key Points:**
- IQuest-Coder-V1 achieves leading results on multiple coding benchmarks.
- The model is backed by a Chinese quant trading company.
- Community discussion includes questions about benchmark validity and model architecture.
- The model is a dense 40B parameter model, not a Mixture of Experts (MoE).
- Interest in the model's performance and background is high among users.

**Discussion Highlights:** The community is particularly interested in the model's background and the validity of its benchmark results. There is also discussion about the model's architecture, with some users expecting a Mixture of Experts (MoE) approach for larger models.

---

## 13. [Happy New Year: Llama3.3-8B-Instruct-Thinking-Claude-4.5-Opus-High-Reasoning - Fine Tune. (based on recent find of L3.3 8b in the wild)](https://reddit.com/r/LocalLLaMA/comments/1q0uuqt/happy_new_year/)

**Author:** u/Dangerous_Fix_5526 | **Upvotes:** 277 | **Comments:** 80 | **Date:** 2025-12-31

**Summary:** The post announces a fine-tuned Llama3.3-8B model using Unsloth and Claude 4.5 Opus High Reasoning Dataset, with GGUF quants available. The author thanks contributors and provides links to the model and dataset.

**Key Points:**
- Fine-tuned Llama3.3-8B model using Unsloth and Claude 4.5 Opus High Reasoning Dataset
- GGUF quants are now available
- Heretic (uncensored) version also released
- Discussion includes questions about dataset size and GGUF availability

**Discussion Highlights:** The discussion highlights questions about the adequacy of the dataset size for effective fine-tuning and interest in the GGUF version of the model.

---

## 14. [Moonshot AI Completes $500 Million Series C Financing](https://reddit.com/r/LocalLLaMA/comments/1q0i4g3/moonshot_ai_completes_500_million_series_c/)

**Author:** u/InternationalAsk1490 | **Upvotes:** 110 | **Comments:** 21 | **Date:** 2025-12-31

**Summary:** Moonshot AI has completed a $500 million Series C financing, with plans to expand GPU capacity and develop the K3 model. The company's global paid user base is growing rapidly, and it aims to achieve significant revenue growth and technological advancements in 2026.

**Key Points:**
- Moonshot AI completed a $500 million Series C financing.
- The company's global paid user base is growing at a monthly rate of 170%.
- Funds will be used to expand GPU capacity and accelerate the development of the K3 model.
- Key priorities for 2026 include improving the K3 model's performance and achieving significant revenue growth.
- The company aims to create distinctive capabilities and focus on productivity value.

**Discussion Highlights:** The discussion highlights positive sentiment towards Moonshot AI's progress and its focus on creating unique capabilities. Users appreciate the company's efforts to monetize and innovate.

---

## 15. [Solar-Open-100B is out](https://reddit.com/r/LocalLLaMA/comments/1q0bgvl/solaropen100b_is_out/)

**Author:** u/cgs019283 | **Upvotes:** 154 | **Comments:** 62 | **Date:** 2025-12-31

**Summary:** Upstage has released the Solar-Open-100B model, a 102B parameter model with a commercial-friendly license. The community is excited about its potential and awaits performance benchmarks.

**Key Points:**
- Solar-Open-100B is a 102B parameter model with a commercial-friendly license.
- The model has been trained on 19.7 trillion tokens.
- Community is eagerly awaiting performance benchmarks and quantized versions (e.g., GGUF/AWQ).
- The model is seen as a significant advancement, with comparisons to models like GLM4.6-Air.

**Discussion Highlights:** The community is highly optimistic about the model's potential, noting the rapid pace of advancements in the field. There is a strong interest in performance benchmarks and quantized versions for local inference. Some users are speculating about the model's similarities to other advanced models like GLM4.6-Air.

---

## 16. [Qwen-Image-2512](https://reddit.com/r/LocalLLaMA/comments/1q094a3/qwenimage2512/)

**Author:** u/Nunki08 | **Upvotes:** 682 | **Comments:** 116 | **Date:** 2025-12-31

**Summary:** The Reddit post announces the release of Qwen-Image-2512, a new model available on multiple platforms with guides and GGUF files. The community response is positive, highlighting its accessibility and creative potential.

**Key Points:**
- Qwen-Image-2512 is a new model with guides and GGUF files available
- The model can be accessed on platforms like Hugging Face, ModelScope, and GitHub
- Users have successfully run the model on low-end hardware without a GPU
- The community appreciates the model as a 'New Year's gift'
- Creative applications, such as generating unique images, are highlighted

**Discussion Highlights:** The discussion highlights the model's accessibility and creative potential, with users sharing successful experiences on low-end hardware and generating unique images. The community response is overwhelmingly positive, appreciating the model as a gift and exploring its capabilities.

---

## 17. [Update on the Llama 3.3 8B situation](https://reddit.com/r/LocalLLaMA/comments/1q06ddc/update_on_the_llama_33_8b_situation/)

**Author:** u/FizzarolliAI | **Upvotes:** 254 | **Comments:** 22 | **Date:** 2025-12-31

**Summary:** The post discusses updates on the Llama 3.3 8B model, including benchmarks for different configurations and the author's uncertainty about which version is better. The author also expresses frustration with Meta's handling of the model's release.

**Key Points:**
- The author uploaded Llama 3.3 8B's weights to Huggingface and provided benchmarks for different configurations.
- The 128k context version shows better performance in benchmarks compared to the original 8k version.
- The author is unsure which version is more correct and wishes Meta had officially released the weights.
- The post includes a humorous self-deprecating remark and an edit about removing Tau-Bench results due to issues.
- Top comments praise the author's work and discuss preferences for unofficial releases.

**Discussion Highlights:** The discussion highlights appreciation for the author's work, humor, and a preference for unofficial releases over official ones. Some users also express interest in trying the model and suggest improvements for model naming.

---

## 18. [[In the Wild] Reverse-engineered a Snapchat Sextortion Bot: It’s running a raw Llama-7B instance with a 2048 token window.](https://reddit.com/r/LocalLLaMA/comments/1pzwlie/in_the_wild_reverseengineered_a_snapchat/)

**Author:** u/simar-dmg | **Upvotes:** 716 | **Comments:** 106 | **Date:** 2025-12-30

**Summary:** A user reverse-engineered a Snapchat sextortion bot and discovered it was running a raw Llama-7B instance with a 2048 token window. The bot was vulnerable to a persona-adoption jailbreak, revealing its configuration and malicious payload.

**Key Points:**
- The bot used a Llama-7B model with a 2048 token context window and high temperature setting.
- A 'Grandma Protocol' jailbreak forced the bot to reveal its environment variables and configuration.
- The bot's erratic behavior was due to minimal hardware and high creativity settings.
- Scammers are using open-source models to avoid API costs and censorship filters.
- The bot eventually revealed a malicious link it was programmed to hide.

**Discussion Highlights:** The discussion highlights skepticism about the accuracy of the bot's revealed information, with some users suggesting it could be entirely hallucinated. Others questioned the commonality of system prompts including environment variables.

---

## 19. [LLM server gear: a cautionary tale of a $1k EPYC motherboard sale gone wrong on eBay](https://reddit.com/r/LocalLLaMA/comments/1pzt1q8/llm_server_gear_a_cautionary_tale_of_a_1k_epyc/)

**Author:** u/__JockY__ | **Upvotes:** 195 | **Comments:** 81 | **Date:** 2025-12-30

**Summary:** The post discusses a seller's experience with eBay's dispute resolution process after selling a high-end EPYC motherboard. Despite providing detailed evidence and photos, the seller faced challenges when the buyer claimed the item was not as described. The post highlights eBay's tendency to side with buyers initially, even in cases with clear evidence.

**Key Points:**
- eBay's dispute resolution process heavily favors buyers initially.
- The seller provided high-quality photos and detailed descriptions of the motherboard.
- The buyer claimed the motherboard was not working, leading to a dispute.
- The seller had to go through a lengthy process to resolve the issue.
- The post and comments highlight the risks and frustrations of selling high-end gear on eBay.

**Discussion Highlights:** The discussion reflects a consensus that selling on eBay can be risky due to the platform's buyer-friendly policies. Many commenters shared similar experiences, emphasizing the challenges sellers face in disputes.

---

## 20. [15M param model solving 24% of ARC-AGI-2 (Hard Eval). Runs on consumer hardware.](https://reddit.com/r/LocalLLaMA/comments/1pzsqii/15m_param_model_solving_24_of_arcagi2_hard_eval/)

**Author:** u/Doug_Bitterbot | **Upvotes:** 111 | **Comments:** 31 | **Date:** 2025-12-30

**Summary:** Bitterbot AI introduced TOPAS-DSPL, a 15M parameter model achieving 24% accuracy on ARC-AGI-2, using a dual-stream architecture to address compositional drift. The model is open-sourced and runs efficiently on consumer hardware like an RTX 4090.

**Key Points:**
- TOPAS-DSPL achieves 24% accuracy on ARC-AGI-2, significantly outperforming previous models of similar size.
- The model uses a dual-stream architecture (Logic Stream and Canvas Stream) to prevent compositional drift.
- Training and inference are efficient, with training possible on a single RTX 4090.
- The community raised concerns about training on the test set and questioned comparisons with MuZero.
- Questions about scalability to larger parameter sizes were also discussed.

**Discussion Highlights:** The community had mixed reactions, with some questioning the methodology (e.g., training on the test set) and others expressing interest in the model's potential scalability and performance.

---

## 21. [Any guesses?](https://reddit.com/r/LocalLLaMA/comments/1pzhcqu/any_guesses/)

**Author:** u/Difficult-Cap-7527 | **Upvotes:** 175 | **Comments:** 36 | **Date:** 2025-12-30

**Summary:** The Reddit post speculates about a new Qwen model, with comments suggesting it could be Qwen 6 or an iteration like Qwen3vl-next-80b-a3b, potentially outperforming GPT 5.2.

**Key Points:**
- Speculation about Qwen 6 beating GPT 5.2 on benchmarks
- Mention of Qwen3vl-next-80b-a3b as a significant update
- Discussion of iterations on qwen-image and Qwen3.5-235B-A10B

**Discussion Highlights:** The discussion highlights excitement around potential new Qwen models, with users interpreting the post as a hint towards significant advancements in the Qwen series, possibly surpassing competitors like GPT 5.2.

---

## 22. [Running GLM-4.7 (355B MoE) in Q8 at ~5 Tokens/s on 2015 CPU-Only Hardware – Full Optimization Guide](https://reddit.com/r/LocalLLaMA/comments/1pzggbf/running_glm47_355b_moe_in_q8_at_5_tokenss_on_2015/)

**Author:** u/at0mi | **Upvotes:** 142 | **Comments:** 99 | **Date:** 2025-12-30

**Summary:** The post details how a user successfully ran the GLM-4.7 (355B MoE) model on a 2015 CPU-only system, achieving ~5 tokens/s using Q8 quantization. The setup involved extensive optimizations, including BIOS tweaks, NUMA node distribution, and Linux kernel adjustments. The user documented the process and shared benchmarks, sparking a discussion on energy efficiency and hardware costs.

**Key Points:**
- GLM-4.7 (355B MoE) was run on a 2015 Lenovo System x3950 X6 with eight Xeon E7-8880 v3 CPUs.
- Achieved ~5-6 tokens/s using Q8 quantization with minimal quality degradation.
- Optimizations included BIOS settings, NUMA node distribution, and Linux kernel tweaks.
- The system draws ~1300W under full load, raising concerns about energy costs.
- Discussion highlighted the trade-offs between performance, power consumption, and hardware costs.

**Discussion Highlights:** The discussion focused on the energy efficiency of the setup, with calculations showing ~60 kWh per 1 million tokens. Users also debated the feasibility of building similar systems, noting the high power draw and hardware costs (~£2,500 for a comparable setup). Some commented on the limitations of CPU-only setups, particularly for tasks requiring parallel processing.

---

## 23. [Tencent HY-Motion 1.0 - a billion-parameter text-to-motion model](https://reddit.com/r/LocalLLaMA/comments/1pzcrtb/tencent_hymotion_10_a_billionparameter/)

**Author:** u/ResearchCrafty1804 | **Upvotes:** 312 | **Comments:** 36 | **Date:** 2025-12-30

**Summary:** Tencent has open-sourced HY-Motion 1.0, a billion-parameter text-to-motion model that generates high-fidelity 3D animations from natural language. It features advanced training strategies and comprehensive motion category coverage, making it a powerful tool for developers and creators.

**Key Points:**
- Billion-parameter Diffusion Transformer (DiT) architecture with flow matching
- Full-stage training strategy (Pre-training → SFT → RL) for optimized results
- Covers 200+ motion categories across 6 major classes
- Positive user feedback on functionality and potential applications in gaming
- Questions about compatibility with non-humanoid models and potential use cases

**Discussion Highlights:** Users expressed enthusiasm for the model's capabilities, with one confirming its effectiveness in gaming workflows. Questions arose about compatibility with non-humanoid models and potential applications in adult content creation.

---

## 24. [Llama-3.3-8B-Instruct](https://reddit.com/r/LocalLLaMA/comments/1pz7mxr/llama338binstruct/)

**Author:** u/ttkciar | **Upvotes:** 150 | **Comments:** 25 | **Date:** 2025-12-29

**Summary:** The post discusses the release of Llama-3.3-8B-Instruct, a potentially new model, with links to Hugging Face repositories. The community expresses excitement and skepticism, with ongoing benchmark tests to verify its authenticity.

**Key Points:**
- Llama-3.3-8B-Instruct model release with intriguing backstory
- Community excitement and skepticism about the model's authenticity
- Ongoing sanity check benchmarks to verify the model
- Multiple Hugging Face repositories hosting the model and GGUF files
- Desire for updated larger models (70b or new 30b)

**Discussion Highlights:** The community is both amazed and skeptical about the Llama-3.3-8B-Instruct release. Top comments highlight the relevance of the subreddit's name, ongoing verification efforts, and a shared desire for larger model updates. Some users provide additional repository links with updated configurations.

---

## 25. [Llama-3.3-8B-Instruct](https://reddit.com/r/LocalLLaMA/comments/1pz7bmv/llama338binstruct/)

**Author:** u/jacek2023 | **Upvotes:** 461 | **Comments:** 78 | **Date:** 2025-12-29

**Summary:** The post discusses the discovery and release of the Llama-3.3-8B-Instruct model, which was previously only available via Meta's API. The author found a way to download it through finetuning and has made it available in GGUF format.

**Key Points:**
- Llama-3.3-8B-Instruct model was previously only available via Meta's API.
- The author discovered a way to download the model through finetuning.
- The model is now available in GGUF format.
- The community is verifying the model's authenticity and performance.
- There is excitement and interest in the discovery.

**Discussion Highlights:** The community is actively verifying the model's authenticity and performance, with some users running benchmarks and evaluations. There is general excitement and appreciation for the discovery and release of the model.

---

## 26. [Z AI is going for an IPO on Jan 8 and set to raise $560 million. Z.ai is set to be the first AI-native LLM company to list on the global market.](https://reddit.com/r/LocalLLaMA/comments/1pz68fz/z_ai_is_going_for_an_ipo_on_jan_8_and_set_to/)

**Author:** u/Difficult-Cap-7527 | **Upvotes:** 332 | **Comments:** 120 | **Date:** 2025-12-29

**Summary:** Z AI is set to go public on January 8, aiming to raise $560 million, making it the first AI-native LLM company to list globally. The announcement has sparked a debate about the future of open-source AI and the company's commitment to releasing open weight models.

**Key Points:**
- Z AI's IPO is scheduled for January 8, targeting $560 million.
- Concerns about the future of open-source AI post-IPO.
- Debate on whether Z AI will continue releasing open weight models.
- Acknowledgment of the financial necessity for companies to monetize.
- Community sentiment against 'selling out.'

**Discussion Highlights:** The community is divided, with some expressing concerns about the shift away from open-source principles, while others acknowledge the financial realities of running an AI company.

---

## 27. [Naver (South Korean internet giant), has just launched HyperCLOVA X SEED Think, a 32B open weights reasoning model and HyperCLOVA X SEED 8B Omni, a unified multimodal model that brings text, vision, and speech together](https://reddit.com/r/LocalLLaMA/comments/1pyjjbw/naver_south_korean_internet_giant_has_just/)

**Author:** u/Nunki08 | **Upvotes:** 159 | **Comments:** 31 | **Date:** 2025-12-29

**Summary:** Naver has launched two new AI models: HyperCLOVA X SEED Think 32B, a 32B open weights reasoning model, and HyperCLOVA X SEED 8B Omni, a unified multimodal model integrating text, vision, and speech. The announcement has generated significant interest in the AI community.

**Key Points:**
- HyperCLOVA X SEED Think 32B is a 32B open weights reasoning model.
- HyperCLOVA X SEED 8B Omni is a multimodal model combining text, vision, and speech.
- The community is interested in the models' capabilities and compatibility with existing tools.
- Users are curious about the models' performance and potential applications.

**Discussion Highlights:** The discussion highlights community excitement about the new models, with users asking about compatibility with tools like llama.cpp and vLLM, and expressing interest in the multimodal capabilities of the 8B Omni model.

---

## 28. [Tencent just released WeDLM 8B Instruct on Hugging Face](https://reddit.com/r/LocalLLaMA/comments/1pyg4yt/tencent_just_released_wedlm_8b_instruct_on/)

**Author:** u/Difficult-Cap-7527 | **Upvotes:** 424 | **Comments:** 62 | **Date:** 2025-12-29

**Summary:** Tencent released WeDLM 8B Instruct on Hugging Face, a diffusion language model that runs 3-6× faster than vLLM-optimized Qwen3-8B on math reasoning tasks. The release has generated significant interest and discussion in the community.

**Key Points:**
- WeDLM 8B Instruct is a diffusion language model released by Tencent on Hugging Face.
- It outperforms vLLM-optimized Qwen3-8B by 3-6× on math reasoning tasks.
- The model is released under the Apache 2.0 license.
- There is also a 7B version available (WeDLM-7B-Instruct).
- The community sees great potential in 7-8B models and is enthusiastic about more such releases.

**Discussion Highlights:** The community is excited about the performance claims and the Apache 2.0 license. There is consensus on the potential of 7-8B models and a desire for more such models. Some users are surprised by the effectiveness of diffusion models for LLMs.

---

## 29. [Meta released RPG, a research plan generation dataset on Hugging Face](https://reddit.com/r/LocalLLaMA/comments/1pyao6g/meta_released_rpg_a_research_plan_generation/)

**Author:** u/Difficult-Cap-7527 | **Upvotes:** 262 | **Comments:** 21 | **Date:** 2025-12-28

**Summary:** Meta released the RPG dataset on Hugging Face, featuring 22k tasks across ML, Arxiv, and PubMed, complete with evaluation rubrics and Llama-4 reference solutions for training AI co-scientists.

**Key Points:**
- Dataset includes 22k tasks spanning ML, Arxiv, and PubMed
- Features evaluation rubrics and Llama-4 reference solutions
- Aimed at training AI co-scientists
- Community highlights Meta's strong research and open-source contributions
- Discussion on the importance of research plan generation for agentic systems

**Discussion Highlights:** The community appreciates Meta's contributions, with discussions highlighting the significance of research plan generation for AI systems and the potential shift in open frontier models.

---

## 30. [Senator in Tennessee introduces bill to felonize making AI "act as a companion" or "mirror human interactions"](https://reddit.com/r/LocalLLaMA/comments/1pxss0m/senator_in_tennessee_introduces_bill_to_felonize/)

**Author:** u/CanineAssBandit | **Upvotes:** 274 | **Comments:** 212 | **Date:** 2025-12-28

**Summary:** A Tennessee senator has introduced a bill (SB1493) that would make it a felony to train AI to provide emotional support, act as a companion, or simulate human interactions. The bill has sparked significant discussion on Reddit, with users expressing opposition and skepticism about its potential passage.

**Key Points:**
- The bill targets AI trained to provide emotional support or act as companions.
- It also prohibits AI from simulating human-like interactions or appearances.
- The definition of 'train' includes developing large language models with knowledge of their intended use.
- Reddit users largely oppose the bill, with comments ranging from humorous to critical of its feasibility.
- Some users suggest the bill stems from unique circumstances and may not gain traction.

**Discussion Highlights:** The discussion on Reddit is predominantly critical of the bill, with users expressing opposition through humor (e.g., 'No Waifu for you!') and serious concerns about its implications for freedom of speech. There is a general consensus that the bill is unlikely to pass, with some users attributing it to specific political circumstances.

---

