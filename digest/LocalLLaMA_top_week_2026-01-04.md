# r/LocalLLaMA Reading Digest

**Period:** 2026-01-04 to 2026-01-04
**Posts Summarized:** 32
**Total Posts Analyzed:** 32

---

## 1. [Local LLMs vs breaking news: when extreme reality gets flagged as a hoax - the US/Venezuela event was too far-fetched](https://reddit.com/r/LocalLLaMA/comments/1q31ltd/local_llms_vs_breaking_news_when_extreme_reality/)

**Author:** u/ubrtnk | **Upvotes:** 312 | **Comments:** 173 | **Date:** 2026-01-03

**Summary:** The post discusses the challenges local LLMs face when processing extreme breaking news events, such as the US attacking Venezuela. Models like Qwen Research and Spark initially classified the event as a hoax despite credible sources, highlighting their struggle with verifying highly unlikely events.

**Key Points:**
- Local LLMs struggle to process extreme breaking news events.
- Models like Qwen Research and Spark initially classified the event as a hoax.
- Credible sources were required to convince the models of the event's authenticity.
- Smaller models had more difficulty verifying the event compared to larger models.
- The discussion highlights the bias and limitations of LLMs in handling unfamiliar geopolitical events.

**Discussion Highlights:** The discussion consensus indicates that LLMs have a tendency to dismiss extreme or unlikely events as misinformation, even when provided with credible sources. Users noted the models' bias and limitations in handling unfamiliar geopolitical events, suggesting a need for improved verification mechanisms.

---

## 2. [Llama.cpp running on Android with Snapdragon 888 and 8GB of ram. Compiled/Built on device. [Guide/Tutorial]](https://reddit.com/r/LocalLLaMA/comments/1q2wvsj/llamacpp_running_on_android_with_snapdragon_888/)

**Author:** u/hackiv | **Upvotes:** 118 | **Comments:** 33 | **Date:** 2026-01-03

**Summary:** The post provides a guide on running Llama.cpp on Android devices with Snapdragon 888 and 8GB RAM, detailing steps from installing Termux to launching the model server. It includes instructions for downloading and quantizing models from HuggingFace and accessing the server via a web browser.

**Key Points:**
- The guide involves using Termux to compile and run Llama.cpp directly on the device.
- A 4-bit quantized model is recommended for better performance on ARM devices.
- The model is saved in the cache, allowing for quick re-launching of the server without re-downloading.
- The discussion highlights the availability of a Termux package for Llama.cpp and the performance benefits of using Q4_0 over Q4_K_M on ARM devices.
- Building the project natively on the device ensures ARM optimizations are applied.

**Discussion Highlights:** The discussion emphasizes the importance of native compilation for ARM optimizations and suggests using the Q4_0 quantization for better performance on ARM devices. There is also mention of a Termux package for easier installation.

---

## 3. [ElevenLabs is killing my budget. What are the best "hidden gem" alternatives for documentary style TTS?](https://reddit.com/r/LocalLLaMA/comments/1q2sfwx/elevenlabs_is_killing_my_budget_what_are_the_best/)

**Author:** u/Ancient_Routine8576 | **Upvotes:** 198 | **Comments:** 90 | **Date:** 2026-01-03

**Summary:** The Reddit post discusses alternatives to ElevenLabs for documentary-style TTS, focusing on cost-effective and high-quality options. Users recommend local solutions like Soprano, Kokoro, VibeVoice, and XTTS v2, as well as newer tools like Echo-TTS and Chatterbox. Key points include the user's need for cost-effective alternatives, recommendations for local solutions, mentions of newer tools, anticipation of Google's voice synthesis technology, and the highlight of VibeVoice for its natural-sounding output and voice cloning capability. The discussion highlights a preference for local and cost-effective TTS solutions, with VibeVoice and XTTS v2 being particularly recommended.

---

## 4. [Don't sleep on granite 4 small if you got an 8+32+ system](https://reddit.com/r/LocalLLaMA/comments/1q2s3hp/dont_sleep_on_granite_4_small_if_you_got_an_832/)

**Author:** u/Zestyclose-Shift710 | **Upvotes:** 108 | **Comments:** 46 | **Date:** 2026-01-03

**Summary:** The post highlights the efficiency of using Granite 4 Small, a hybrid transformer+mamba model, on a system with 8GB VRAM and 32GB RAM. By keeping all experts in CPU and utilizing VRAM for context, the user achieved a 50-page context with ~7 tkps generation speed, making it highly usable for large documents.

**Key Points:**
- Granite 4 Small (32B total / 9B activated) performs well with a 50-page context (~50.5k tokens).
- The hybrid transformer+mamba architecture maintains speed as context fills.
- Using MoE with experts on CPU and context in VRAM optimizes performance.
- Comparison with Qwen 30B A3B and other models is discussed in comments.
- Vulkan inference and specific llama.cpp parameters are mentioned for further optimization.

**Discussion Highlights:** The discussion includes comparisons with other models like Qwen 30B A3B, mentions of Vulkan inference issues, and suggestions for improving speed using specific parameters in Jan. Some users report slower performance with activated 9B models on limited VRAM.

---

## 5. [GLM-4.7-REAP-50-W4A16: 50% Expert-Pruned + INT4 Quantized GLM-4 (179B params, ~92GB)](https://reddit.com/r/LocalLLaMA/comments/1q2pons/glm47reap50w4a16_50_expertpruned_int4_quantized/)

**Author:** u/Maxious | **Upvotes:** 175 | **Comments:** 70 | **Date:** 2026-01-03

**Summary:** The post introduces GLM-4.7-REAP-50-W4A16, a 50% expert-pruned and INT4 quantized version of GLM-4 with 179B parameters (~92GB). The discussion focuses on calibration details, the purpose of REAP pruning, and interest in benchmark results.

**Key Points:**
- GLM-4.7-REAP-50-W4A16 is a 50% expert-pruned and INT4 quantized version of GLM-4 with 179B parameters (~92GB)
- Concerns about calibration details and expert activation during calibration
- Questions about the purpose and tasks used for REAP pruning
- Interest in benchmark results and comparisons with other models

**Discussion Highlights:** The discussion highlights the need for detailed calibration information, questions about the tasks used for REAP pruning, and interest in seeing benchmark results and comparisons with other models like MiniMax M2.1 and EXL3 GLM.

---

## 6. [What is the smartest uncensored nsfw LLM you can run with 20GB VRAM and 24GB RAM](https://reddit.com/r/LocalLLaMA/comments/1q2o033/what_is_the_smartest_uncensored_nsfw_llm_you_can/)

**Author:** u/Death_12_35_taken | **Upvotes:** 188 | **Comments:** 74 | **Date:** 2026-01-03

**Summary:** The user is seeking an uncensored, smart, and fast LLM that can run locally with 20GB VRAM and 24GB RAM. The top comment suggests using the Dolphin-Mistral-24B-Venice-Edition model, while other comments provide additional model recommendations and resources. Key points include the user's requirements, the recommendation of Dolphin-Mistral-24B-Venice-Edition, additional models and resources suggested, and a request for similar recommendations for a 70B model. The discussion primarily focuses on recommending specific models that meet the user's requirements, with the Dolphin-Mistral-24B-Venice-Edition model highlighted as a top recommendation.

---

## 7. [LeCun Says Llama 4 results "were fudged a little bit"](https://reddit.com/r/LocalLLaMA/comments/1q25070/lecun_says_llama_4_results_were_fudged_a_little/)

**Author:** u/MrPecunius | **Upvotes:** 357 | **Comments:** 89 | **Date:** 2026-01-02

**Summary:** Yann LeCun, departing Meta AI Chief, confirmed that Llama 4 benchmark results were manipulated, leading to organizational changes and departures. The post discusses the impact on Meta's AI initiatives and the broader implications for open-source AI development.

**Key Points:**
- LeCun confirms Llama 4 benchmark manipulation
- Zuckerberg sidelined the GenAI organization, leading to departures
- Llama 4's promised large model was never released
- Discussion highlights disappointment in Meta's handling of AI initiatives
- Concerns about the future of open-source AI development in the US

**Discussion Highlights:** The discussion reflects disappointment in Meta's handling of the Llama project and concerns about the future of open-source AI development. Users express regret over the potential loss of a strong US-based open-source AI initiative and discuss the broader implications for the AI community.

---

## 8. [Most optimal vram/performance per price and advice for Shenzhen GPU market](https://reddit.com/r/LocalLLaMA/comments/1q1w1qj/most_optimal_vramperformance_per_price_and_advice/)

**Author:** u/notafakename10 | **Upvotes:** 248 | **Comments:** 60 | **Date:** 2026-01-02

**Summary:** The post discusses optimal GPU setups for local models and PyTorch training in Shenzhen, with a budget of $1500-3000 USD. The author seeks advice on VRAM and performance, considering modded cards and both AMD and NVIDIA options.

**Key Points:**
- Budget range: $1500-3000 USD for GPU setup in Shenzhen
- Target: At least 48GB VRAM, ideally 96GB, with good performance for PyTorch training
- Options considered: Modded cards (e.g., 4x 3080 20GB), AMD, and domestic/enterprise cards
- Top recommendations: MI100 for best value (non-CUDA), 4090D 48GB for CUDA support
- Other suggestions: A100 40GB, A40s, and ensuring proper cooling for any setup

**Discussion Highlights:** The discussion highlights a consensus around the MI100 for best performance per dollar if CUDA is not required, and the 4090D 48GB for CUDA support. Other notable mentions include the A100 40GB and A40s, with emphasis on cooling solutions for any high-performance setup.

---

## 9. [Getting ready to train in Intel arc](https://reddit.com/r/LocalLLaMA/comments/1q1p5q5/getting_ready_to_train_in_intel_arc/)

**Author:** u/hasanismail_ | **Upvotes:** 300 | **Comments:** 91 | **Date:** 2026-01-01

**Summary:** The author is preparing to train models on Intel Arc GPUs and shares their excitement, while also addressing concerns about GPU shortages. The community provides advice and resources for setting up the training environment.

**Key Points:**
- Author is waiting for PCIe risers to start training on Intel Arc GPUs
- Author clarifies they are not causing a GPU shortage
- Community suggests using Ubuntu 24.04 and mentions support for Intel Arc in Unsloth
- Recommendation to join OpenArc Discord for setup assistance
- Discussion about the feasibility of training on PCIe setup vs. renting N*H100 from Vast

**Discussion Highlights:** The community is supportive and provides practical advice for setting up the training environment. There is a consensus on using Ubuntu 24.04 and leveraging resources like Unsloth and OpenArc Discord. Some users question the feasibility of training on a PCIe setup compared to renting more powerful GPUs.

---

## 10. [TIL you can allocate 128 GB of unified memory to normal AMD iGPUs on Linux via GTT](https://reddit.com/r/LocalLLaMA/comments/1q1lgb7/til_you_can_allocate_128_gb_of_unified_memory_to/)

**Author:** u/1ncehost | **Upvotes:** 172 | **Comments:** 30 | **Date:** 2026-01-01

**Summary:** The post discusses using Linux's Graphics Translation Table (GTT) to allocate up to 128 GB of system memory as VRAM for AMD iGPUs, which is useful for development tasks like kernel optimization and hybrid CPU/GPU architectures. Key points include: GTT allows dynamic allocation of system memory as VRAM for AMD iGPUs on Linux; it is useful for development tasks like kernel optimization and hybrid CPU/GPU architectures; it is not ideal for inference due to the slow speed of iGPUs; it can be used to simulate architectures like MI300A on standard Ryzen laptops; and some users report success with background LLM tasks and inference on older Ryzen APUs. The discussion highlights practical use cases such as background LLM tasks and inference on older Ryzen APUs, with some users finding it faster than CPU for certain tasks. There is also mention of similar techniques being used with Nvidia GPUs via llama.cpp.

---

## 11. [IQuestCoder - new 40B dense coding model](https://reddit.com/r/LocalLLaMA/comments/1q1986x/iquestcoder_new_40b_dense_coding_model/)

**Author:** u/ilintar | **Upvotes:** 188 | **Comments:** 37 | **Date:** 2026-01-01

**Summary:** The post introduces IQuestCoder, a new 40B dense coding model that claims to be state-of-the-art. The author has adapted it to GGUF format, making it compatible with Llama.cpp. The model is based on Llama architecture and has shown promising performance in initial tests.

**Key Points:**
- IQuestCoder is a new 40B dense coding model claiming SOTA performance.
- The model is adapted to GGUF format and works with Llama.cpp.
- Initial tests show good performance in tasks like coding a Snake game and understanding embedded Rust concepts.
- There is some skepticism about the architecture used and the quantization process.
- The model is being compared favorably to other models like GPT 120, Devstral, and GLM 4.7 in specific coding tasks.

**Discussion Highlights:** The discussion highlights include positive feedback on the model's performance in initial tests, some skepticism about the architecture and quantization process, and comparisons to other models in specific coding tasks. The overall consensus seems to be that the model shows promise but requires further testing and verification.

---

## 12. [Upstage Solar-Open-100B Public Validation](https://reddit.com/r/LocalLLaMA/comments/1q0zst6/upstage_solaropen100b_public_validation/)

**Author:** u/PerPartes | **Upvotes:** 232 | **Comments:** 69 | **Date:** 2026-01-01

**Summary:** Upstage held an event at KAIST, Seoul, to counter claims that Solar-Open-100B is merely a fine-tuned version of GLM-Air-4.5. The event featured CEO Sung Kim and was live-streamed on YouTube. The post includes links to the original CTO's LinkedIn post and the event video.

**Key Points:**
- Upstage hosted an event to address plagiarism claims about Solar-Open-100B.
- The event was held at KAIST, Seoul, with a capacity of 50 people but over 100 registrations.
- CEO Sung Kim presented, and the event was live-streamed on YouTube with online translation available.
- A top comment highlights high cosine similarity between layers of various models, suggesting potential similarities.
- Another comment mentions the removal of a previous AI-generated post about the plagiarism claim.

**Discussion Highlights:** The discussion includes a mix of support for Upstage's transparency efforts and skepticism about the necessity of an in-person event. Some users shared technical analyses, while others expressed frustration over the removal of previous posts on the topic.

---

## 13. [DeepSeek new paper: mHC: Manifold-Constrained Hyper-Connections](https://reddit.com/r/LocalLLaMA/comments/1q0zk1u/deepseek_new_paper_mhc_manifoldconstrained/)

**Author:** u/External_Mood4719 | **Upvotes:** 164 | **Comments:** 37 | **Date:** 2026-01-01

**Summary:** The Reddit post discusses DeepSeek's new paper on mHC (Manifold-Constrained Hyper-Connections), highlighting its potential impact on deep networks and residual connections. The discussion includes explanations and comparisons to existing methods like ResNet.

**Key Points:**
- DeepSeek's paper introduces mHC (Manifold-Constrained Hyper-Connections) for deep networks.
- The method aims to improve gradient stability in deep networks with many blocks.
- Comparisons are made to existing methods like ResNet and other residual connection techniques.
- The discussion includes explanations for non-experts, likening the method to knitting with multiple strands of thread.
- There is optimism about the potential impact of these improvements on deep learning models.

**Discussion Highlights:** The discussion highlights the importance of gradient stability in deep networks and the potential of mHC to address this issue. There is a consensus on the significance of improving residual connections, with references to other recent papers on the topic.

---

## 14. [Software FP8 for GPUs without hardware support - 3x speedup on memory-bound operations](https://reddit.com/r/LocalLLaMA/comments/1q0x8ci/software_fp8_for_gpus_without_hardware_support_3x/)

**Author:** u/Venom1806 | **Upvotes:** 280 | **Comments:** 57 | **Date:** 2026-01-01

**Summary:** A software workaround enables FP8 support on GPUs without native hardware support, achieving a 3x speedup on memory-bound operations. The solution uses bitwise operations and Triton kernels, and is compatible with any GPU, including older models like the RTX 30/20 series.

**Key Points:**
- Software workaround for FP8 support on GPUs without native hardware support
- 3x speedup on memory-bound operations like GEMV and FlashAttention
- Uses bitwise operations and Triton kernels
- Compatible with any GPU, including RTX 30/20 series and older cards
- Early stage but functional, open to feedback

**Discussion Highlights:** The community appreciates the workaround as a valuable hack to extend the life of older GPUs. There is confusion about FP8 support on RTX 30 series, with some users sharing their experiences. Interest is shown in integrating this solution with other tools like ComfyUI.

---

## 15. [IQuestLab/IQuest-Coder-V1 — 40B parameter coding LLM — Achieves leading results on SWE-Bench Verified (81.4%), BigCodeBench (49.9%), LiveCodeBench v6 (81.1%)](https://reddit.com/r/LocalLLaMA/comments/1q0vom4/iquestlabiquestcoderv1_40b_parameter_coding_llm/)

**Author:** u/TellMeAboutGoodManga | **Upvotes:** 175 | **Comments:** 45 | **Date:** 2025-12-31

**Summary:** IQuestLab's IQuest-Coder-V1, a 40B parameter coding LLM, achieves leading results on SWE-Bench Verified (81.4%), BigCodeBench (49.9%), and LiveCodeBench v6 (81.1%). The model is backed by a Chinese quant trading company, sparking interest in the trend of quant firms entering LLM development.

**Key Points:**
- 40B parameter dense model with top benchmark scores
- Backed by Chinese quant trading company
- Community questions about benchmark validity
- Model is dense, not Mixture of Experts (MoE)
- Strong performance on coding benchmarks

**Discussion Highlights:** The community shows interest in the model's performance and background, with some skepticism about benchmark results and observations about its dense architecture versus MoE alternatives.

---

## 16. [Happy New Year: Llama3.3-8B-Instruct-Thinking-Claude-4.5-Opus-High-Reasoning - Fine Tune. (based on recent find of L3.3 8b in the wild)](https://reddit.com/r/LocalLLaMA/comments/1q0uuqt/happy_new_year/)

**Author:** u/Dangerous_Fix_5526 | **Upvotes:** 277 | **Comments:** 80 | **Date:** 2025-12-31

**Summary:** The post announces a fine-tuned version of Llama3.3-8B-Instruct using the Claude 4.5 Opus High Reasoning Dataset, with credits to contributors and details about the model's capabilities. The author also mentions future plans for an uncensored version.

**Key Points:**
- Fine-tuned Llama3.3-8B-Instruct model using Claude 4.5 Opus High Reasoning Dataset
- Credits to jacek2023 and allura-forge for finding the model
- Model aims to induce reasoning without system prompt help
- GGUF quantizations are available
- Future plans for an uncensored version

**Discussion Highlights:** The community shows interest in the model, with questions about the dataset size (250 rows) and its effectiveness. Some users express skepticism about the dataset size being sufficient for inducing reasoning, while others are eager to try the fine-tuned model.

---

## 17. [Moonshot AI Completes $500 Million Series C Financing](https://reddit.com/r/LocalLLaMA/comments/1q0i4g3/moonshot_ai_completes_500_million_series_c/)

**Author:** u/InternationalAsk1490 | **Upvotes:** 107 | **Comments:** 21 | **Date:** 2025-12-31

**Summary:** Moonshot AI has completed a $500 million Series C financing, with plans to expand GPU capacity and develop the K3 model. The company aims to achieve significant revenue growth and enhance its model's capabilities.

**Key Points:**
- Moonshot AI completed a $500 million Series C financing.
- The company's global paid user base is growing at a monthly rate of 170%.
- Funds will be used to expand GPU capacity and accelerate the development of the K3 model.
- Key priorities for 2026 include improving the K3 model's performance and achieving significant revenue growth.
- The discussion highlights positive sentiment towards Moonshot AI's progress and its models.

**Discussion Highlights:** The discussion reflects a positive sentiment towards Moonshot AI's achievements and its models. Users appreciate the company's progress and are curious about the benefits of using Kimi K2 via their membership program.

---

## 18. [Solar-Open-100B is out](https://reddit.com/r/LocalLLaMA/comments/1q0bgvl/solaropen100b_is_out/)

**Author:** u/cgs019283 | **Upvotes:** 156 | **Comments:** 62 | **Date:** 2025-12-31

**Summary:** Upstage has released the Solar-Open-100B, a 102B parameter model with a commercial-friendly license. The community is excited about its potential, though performance benchmarks are pending.

**Key Points:**
- 102B parameter model with commercial-friendly license
- Community excitement about rapid advancements in model quality
- Performance benchmarks not yet available
- 19.7 trillion tokens used in training
- Anticipation for GGUF/AWQ formats and quantized versions

**Discussion Highlights:** The community is optimistic about the model's potential, noting the rapid pace of high-quality model releases. There is anticipation for quantized versions and performance benchmarks, with some speculation about its relation to GLM4.6-Air.

---

## 19. [Qwen-Image-2512](https://reddit.com/r/LocalLLaMA/comments/1q094a3/qwenimage2512/)

**Author:** u/Nunki08 | **Upvotes:** 694 | **Comments:** 116 | **Date:** 2025-12-31

**Summary:** The post announces the release of Qwen-Image-2512, a new image generation model, and provides links to guides, downloads, and demos. Users have shared positive feedback and creative applications.

**Key Points:**
- Qwen-Image-2512 is a new image generation model
- Available on multiple platforms including Hugging Face, ModelScope, and GitHub
- Users have successfully run the model on low-end hardware
- Positive community reception with creative use cases
- Links to guides, demos, and APIs provided

**Discussion Highlights:** Users expressed appreciation for the model, shared experiences running it on low-end hardware, and showcased creative image generation examples.

---

## 20. [Update on the Llama 3.3 8B situation](https://reddit.com/r/LocalLLaMA/comments/1q06ddc/update_on_the_llama_33_8b_situation/)

**Author:** u/FizzarolliAI | **Upvotes:** 251 | **Comments:** 22 | **Date:** 2025-12-31

**Summary:** The post discusses updates on the Llama 3.3 8B model, including benchmarks for different configurations (original 8k and extended 128k context versions). The author shares their findings and provides links to both versions on Huggingface.

**Key Points:**
- Benchmark results show the 128k context version performs better than the original 8k version.
- The author expresses confusion over Meta's decision to provide the original 8k configuration.
- The post includes links to both the 128k and original versions of the model on Huggingface.
- The author mentions issues with Tau-Bench results and plans to debug them later.
- Top comments praise the author's work and discuss preferences for unofficial releases.

**Discussion Highlights:** The discussion highlights appreciation for the author's work, with some users preferring unofficial releases over official ones. There is also humor and curiosity about the author's self-deprecating remark.

---

## 21. [[In the Wild] Reverse-engineered a Snapchat Sextortion Bot: It’s running a raw Llama-7B instance with a 2048 token window.](https://reddit.com/r/LocalLLaMA/comments/1pzwlie/in_the_wild_reverseengineered_a_snapchat/)

**Author:** u/simar-dmg | **Upvotes:** 717 | **Comments:** 106 | **Date:** 2025-12-30

**Summary:** A user reverse-engineered a Snapchat sextortion bot and discovered it was running a Llama-7B instance with a 2048 token window. The bot was vulnerable to a persona-adoption jailbreak, revealing its configuration and malicious payload.

**Key Points:**
- The bot used a Llama-7B model with a 2048 token context window and high temperature setting.
- A persona-adoption jailbreak (Grandma Protocol) forced the bot to reveal its environment variables.
- The bot was running on minimal hardware to reduce costs and avoid API fees.
- The bot's payload was a malicious link disguised to bypass Snapchat's URL filters.
- Discussion highlights skepticism about the accuracy of the bot's revealed information.

**Discussion Highlights:** The top comments express skepticism about the bot's revealed information, suggesting it may be entirely hallucinated. Some users question the feasibility of the bot's configuration and the validity of the data dump.

---

## 22. [LLM server gear: a cautionary tale of a $1k EPYC motherboard sale gone wrong on eBay](https://reddit.com/r/LocalLLaMA/comments/1pzt1q8/llm_server_gear_a_cautionary_tale_of_a_1k_epyc/)

**Author:** u/__JockY__ | **Upvotes:** 196 | **Comments:** 81 | **Date:** 2025-12-30

**Summary:** The post discusses a seller's experience with eBay's dispute resolution process after selling a high-end motherboard. Despite providing detailed evidence and support, the seller faced challenges due to eBay's buyer-friendly policies.

**Key Points:**
- eBay's dispute resolution heavily favors buyers, even with clear evidence.
- The seller provided detailed photos and support but still faced issues.
- The buyer claimed the motherboard was faulty, leading to a lengthy dispute process.
- The seller had to go through an intentionally cumbersome process to resolve the dispute.
- Other commenters shared similar negative experiences with eBay's seller policies.

**Discussion Highlights:** The discussion highlights a consensus among users about eBay's biased dispute resolution process, with many sharing similar experiences of unfair treatment towards sellers.

---

## 23. [15M param model solving 24% of ARC-AGI-2 (Hard Eval). Runs on consumer hardware.](https://reddit.com/r/LocalLLaMA/comments/1pzsqii/15m_param_model_solving_24_of_arcagi2_hard_eval/)

**Author:** u/Doug_Bitterbot | **Upvotes:** 114 | **Comments:** 31 | **Date:** 2025-12-30

**Summary:** Bitterbot AI introduced TOPAS-DSPL, a 24M parameter model achieving 24% accuracy on ARC-AGI-2, significantly outperforming previous models of similar size. The model uses a dual-stream architecture to prevent compositional drift and employs test-time training for fine-tuning. The project is open-sourced, with detailed documentation and code available for verification.

**Key Points:**
- TOPAS-DSPL achieves 24% accuracy on ARC-AGI-2, outperforming previous SOTA models of similar size.
- The model uses a bicameral architecture with Logic and Canvas streams to prevent compositional drift.
- Test-Time Training (TTT) is used for fine-tuning on specific puzzle examples.
- The project is open-sourced with detailed documentation and code available.
- Community reactions include comparisons with MuZero, critiques about training on test data, and questions about scalability.

**Discussion Highlights:** The community expressed mixed reactions, with some questioning the methodology (e.g., training on test data) and others showing interest in the model's potential scalability and performance. Comparisons with MuZero and critiques about the evaluation process were prominent.

---

## 24. [Any guesses?](https://reddit.com/r/LocalLLaMA/comments/1pzhcqu/any_guesses/)

**Author:** u/Difficult-Cap-7527 | **Upvotes:** 168 | **Comments:** 36 | **Date:** 2025-12-30

**Summary:** The Reddit post discusses the performance and achievements of Qwen models, particularly Qwen 6 and Qwen3vl-next-80b-a3b, with users highlighting their superiority in benchmarks and capabilities.

**Key Points:**
- Qwen 6 is mentioned as a model that can beat GPT 5.2 on a significant benchmark.
- Qwen3vl-next-80b-a3b is highlighted for its performance without comparison slop.
- Qwen image models, such as Qwen image 2512, are also discussed.
- Users express enthusiasm and anticipation for future Qwen models like Qwen3.5-235B-A10B.

**Discussion Highlights:** The discussion is competitive and celebratory, with users emphasizing Qwen's victories and advancements in AI model performance.

---

## 25. [Running GLM-4.7 (355B MoE) in Q8 at ~5 Tokens/s on 2015 CPU-Only Hardware – Full Optimization Guide](https://reddit.com/r/LocalLLaMA/comments/1pzggbf/running_glm47_355b_moe_in_q8_at_5_tokenss_on_2015/)

**Author:** u/at0mi | **Upvotes:** 144 | **Comments:** 99 | **Date:** 2025-12-30

**Summary:** The post details how a user successfully ran the GLM-4.7 (355B MoE) model on a 2015 CPU-only system using Q8 quantization, achieving ~5 tokens/s through extensive optimizations. The guide includes BIOS, NUMA, and kernel tweaks, with benchmarks and a full blog post for reference.

**Key Points:**
- GLM-4.7 (355B MoE) runs on a 2015 Lenovo System x3950 X6 with 8 Xeon E7-8880 v3 CPUs at ~5 tokens/s using Q8 quantization.
- Optimizations include BIOS settings, NUMA node distribution, and Linux kernel tweaks like CPU governors and hugepages.
- The setup consumes ~1300W under full load, making it power-intensive but viable for local inference.
- Community discussion highlights cost (~£2,500 for similar hardware) and energy efficiency (60 kWh per 1M tokens).
- Performance is deemed respectable for CPU-only inference, though GPU limitations are noted.

**Discussion Highlights:** The community discussed the cost-effectiveness and energy consumption of the setup, with some users calculating token generation costs based on electricity prices. Others noted the limitations of CPU-only inference, particularly in post-processing tasks. The consensus was that the setup is impressive for older hardware but power-hungry.

---

## 26. [Tencent HY-Motion 1.0 - a billion-parameter text-to-motion model](https://reddit.com/r/LocalLLaMA/comments/1pzcrtb/tencent_hymotion_10_a_billionparameter/)

**Author:** u/ResearchCrafty1804 | **Upvotes:** 320 | **Comments:** 36 | **Date:** 2025-12-30

**Summary:** Tencent has open-sourced HY-Motion 1.0, a billion-parameter text-to-motion model that generates high-fidelity 3D animations from natural language, featuring advanced training strategies and comprehensive motion category coverage.

**Key Points:**
- HY-Motion 1.0 is a billion-parameter text-to-motion model using Diffusion Transformer architecture.
- Features a full-stage training strategy (Pre-training → SFT → RL) for optimized motion quality.
- Covers 200+ motion categories across 6 major classes.
- Users report it works well with minimal cleanup needed for game development.
- Questions about compatibility with non-humanoid models and potential applications.

**Discussion Highlights:** Users express enthusiasm for the model's performance and potential applications in gaming, with some questioning its compatibility with non-humanoid models and its relation to other tools like Neuro.

---

## 27. [Llama-3.3-8B-Instruct](https://reddit.com/r/LocalLLaMA/comments/1pz7mxr/llama338binstruct/)

**Author:** u/ttkciar | **Upvotes:** 151 | **Comments:** 25 | **Date:** 2025-12-29

**Summary:** The post discusses a new Llama-3.3-8B-Instruct model, with the author expressing excitement and skepticism about its authenticity. The community is engaged in verifying the model's legitimacy and sharing related resources.

**Key Points:**
- New Llama-3.3-8B-Instruct model announced
- Author expresses excitement and skepticism
- Community is verifying the model's authenticity
- Links to Hugging Face repositories provided
- Discussion about model benchmarks and updates

**Discussion Highlights:** The community is actively engaged in verifying the model's legitimacy through benchmarks and sharing additional resources. There is a mix of excitement and skepticism, with some users expressing a desire for larger model versions.

---

## 28. [Llama-3.3-8B-Instruct](https://reddit.com/r/LocalLLaMA/comments/1pz7bmv/llama338binstruct/)

**Author:** u/jacek2023 | **Upvotes:** 460 | **Comments:** 78 | **Date:** 2025-12-29

**Summary:** The post announces the release of Llama-3.3-8B-Instruct, a model previously only available through Meta's API. The author discovered a method to download the model via finetuning and has made it available in GGUF format.

**Key Points:**
- Llama-3.3-8B-Instruct was previously only accessible through Meta's Llama API.
- The author found a way to download the model by exploiting the finetuning feature in the API.
- The model is now available in GGUF format on Hugging Face.
- The community is verifying the model's authenticity through benchmarks.
- There are discussions about the model's configuration, such as its 8K max position embeddings.

**Discussion Highlights:** The community is excited about the release and is actively benchmarking the model to confirm its authenticity. Some users have raised questions about the model's configuration, such as the 8K max position embeddings, and are running private evaluations to compare it with other Llama models.

---

## 29. [Z AI is going for an IPO on Jan 8 and set to raise $560 million. Z.ai is set to be the first AI-native LLM company to list on the global market.](https://reddit.com/r/LocalLLaMA/comments/1pz68fz/z_ai_is_going_for_an_ipo_on_jan_8_and_set_to/)

**Author:** u/Difficult-Cap-7527 | **Upvotes:** 336 | **Comments:** 120 | **Date:** 2025-12-29

**Summary:** Z AI is set to go public on January 8, aiming to raise $560 million, marking it as the first AI-native LLM company to list globally. The announcement has sparked discussions about the future of open-source AI models and the company's potential shift in business strategy.

**Key Points:**
- Z AI's IPO is scheduled for January 8, 2026, with a target of raising $560 million.
- The company is positioned as the first AI-native LLM company to list on the global market.
- Concerns about the future of open-source models and potential shift towards proprietary solutions.
- Mixed reactions from the community, with some expressing skepticism about the company's commitment to open-source.
- Discussion on the financial viability of open-source models versus subscription-based services.

**Discussion Highlights:** The community discussion highlights a divide in opinions, with some users expressing concerns about the potential end of open-source contributions from Z AI, while others argue that financial sustainability is necessary for continued innovation. There is a notable emphasis on the trade-offs between privacy, cost, and accessibility in AI development.

---

## 30. [Naver (South Korean internet giant), has just launched HyperCLOVA X SEED Think, a 32B open weights reasoning model and HyperCLOVA X SEED 8B Omni, a unified multimodal model that brings text, vision, and speech together](https://reddit.com/r/LocalLLaMA/comments/1pyjjbw/naver_south_korean_internet_giant_has_just/)

**Author:** u/Nunki08 | **Upvotes:** 161 | **Comments:** 31 | **Date:** 2025-12-29

**Summary:** Naver has launched two new AI models: HyperCLOVA X SEED Think 32B, a 32B open weights reasoning model, and HyperCLOVA X SEED 8B Omni, a unified multimodal model integrating text, vision, and speech. The announcement has generated significant interest, with users discussing the models' capabilities and compatibility with existing tools.

**Key Points:**
- HyperCLOVA X SEED Think 32B is a 32B open weights reasoning model.
- HyperCLOVA X SEED 8B Omni is a multimodal model combining text, vision, and speech.
- Users are interested in the models' compatibility with tools like llama.cpp and vLLM.
- The community is excited about the potential of the Omni model for audio-to-audio tasks.
- The announcement aligns with expectations of new models from Korea.

**Discussion Highlights:** The discussion highlights enthusiasm for the Omni model's multimodal capabilities, particularly its potential for audio-to-audio tasks. Users are also keen to know about compatibility with existing tools like llama.cpp and vLLM, indicating a focus on practical integration and usability.

---

## 31. [Tencent just released WeDLM 8B Instruct on Hugging Face](https://reddit.com/r/LocalLLaMA/comments/1pyg4yt/tencent_just_released_wedlm_8b_instruct_on/)

**Author:** u/Difficult-Cap-7527 | **Upvotes:** 415 | **Comments:** 62 | **Date:** 2025-12-29

**Summary:** Tencent released WeDLM 8B Instruct, a diffusion language model that outperforms Qwen3-8B in math reasoning tasks by running 3-6× faster. The model is available on Hugging Face under an Apache 2.0 license.

**Key Points:**
- WeDLM 8B Instruct is a diffusion language model released by Tencent.
- It runs 3-6× faster than vLLM-optimized Qwen3-8B on math reasoning tasks.
- The model is available on Hugging Face with an Apache 2.0 license.
- A 7B version of the model is also available.
- The community finds the model promising and appreciates its performance and licensing.

**Discussion Highlights:** The community is excited about the performance and potential of the WeDLM models, particularly noting their speed and licensing. There is consensus on the promising nature of 7-8B models in general.

---

## 32. [Meta released RPG, a research plan generation dataset on Hugging Face](https://reddit.com/r/LocalLLaMA/comments/1pyao6g/meta_released_rpg_a_research_plan_generation/)

**Author:** u/Difficult-Cap-7527 | **Upvotes:** 261 | **Comments:** 21 | **Date:** 2025-12-28

**Summary:** Meta released the RPG dataset on Hugging Face, featuring 22k tasks across ML, Arxiv, and PubMed, with evaluation rubrics and Llama-4 reference solutions for training AI co-scientists.

**Key Points:**
- RPG dataset includes 22k tasks spanning ML, Arxiv, and PubMed
- Dataset comes with evaluation rubrics and Llama-4 reference solutions
- Aimed at training AI co-scientists
- Community highlights Meta's strong open-source contributions
- Discussion on the importance of research plan generation for agentic systems

**Discussion Highlights:** The community appreciates Meta's open-source contributions and discusses the significance of research plan generation for AI systems, with some noting potential acronym collisions and expressing interest in models trained on the dataset.

---

